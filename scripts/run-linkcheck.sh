#!/usr/bin/env bash
# Wrapper for Sphinx linkcheck that allows broken links to surface as warnings
# instead of failing the CI job outright. The script preserves the build exit
# code for unexpected errors while tolerating missing/out-of-service external
# resources.

set -o pipefail

LOG_DIR="${LINKCHECK_LOG_DIR:-build/linkcheck}"
TARGET="${LINKCHECK_TARGET:-linkcheck}"
LOG_FILE="$LOG_DIR/${TARGET}.log"

mkdir -p "$LOG_DIR"

echo "Running Sphinx linkcheck (soft-fail for broken external URLs)..."

# Ensure we do not inherit fatal-warning behaviour from the Makefile default.
export SPHINXOPTS="${SPHINXOPTS_OVERRIDE:---keep-going}"

# Run linkcheck, capturing output for later inspection.
make "$TARGET" 2>&1 | tee "$LOG_FILE"
status=${PIPESTATUS[0]}

if [[ $status -eq 0 ]]; then
  echo "Linkcheck completed without fatal issues."
  exit 0
fi

shopt -s nullglob
reports=()

if [[ -f "$LOG_DIR/output.txt" ]]; then
  reports+=("$LOG_DIR/output.txt")
fi

while IFS= read -r -d '' report; do
  reports+=("$report")
done < <(find "$LOG_DIR" -mindepth 1 -maxdepth 2 -type f -name 'output.txt' -print0 2>/dev/null)

if (( ${#reports[@]} == 0 )); then
  echo "::error::Linkcheck did not emit any reports; failing the build."
  exit "$status"
fi

broken_count=0
disallowed_line=""

for report in "${reports[@]}"; do
  while IFS= read -r line; do
    [[ -z "$line" ]] && continue
    if [[ "$line" =~ \[([[:alnum:]_-]+)\] ]]; then
      status_token="${BASH_REMATCH[1]}"
      case "$status_token" in
        broken)
          ((broken_count++))
          ;;
        redirected|ignored|timeout|unchecked|working)
          ;;
        *)
          disallowed_line="$line"
          break 2
          ;;
      esac
    fi
  done < "$report"
done

if [[ -n "$disallowed_line" ]]; then
  echo "::error::Linkcheck encountered a fatal issue: $disallowed_line"
  exit "$status"
fi

if (( broken_count > 0 )); then
  echo "::warning::Linkcheck reported $broken_count unreachable link(s). See $LOG_DIR for details."
  exit 0
fi

echo "::error::Linkcheck failed without reporting broken links. See $LOG_FILE for details."
exit "$status"
