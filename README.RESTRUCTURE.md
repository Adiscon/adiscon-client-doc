# Restructure Playbook

This guide describes the incremental workflow for restructuring the Adiscon documentation set. Follow it whenever you reorganize, consolidate, or retarget existing content.

## 1. Triage each page first

1. **Inventory candidate pages.** Start with a short list of files that feel related (e.g., duplicate tutorials or overlapping feature guides).
2. **Decide shared vs. product-specific ownership.**
   - Keep material in a product directory (such as `winsyslog/` or `rsyslog/`) when it depends on product-only features, UI, or versioning.
   - Promote content into `source/shared/` only when it is vendor-neutral, reused verbatim by multiple products, or documents infrastructure that applies across the suite.
   - When in doubt, leave the file in its current product tree and log a follow-up question rather than moving it prematurely.
3. **Document the queue.** Track every file you did **not** tackle (or that exceeds this PR’s scope) in a follow-up list so the next pass can pick it up.

## 2. Keep pull requests intentionally small

- **Touch at most five files per restructuring PR.** Bundling smaller batches keeps reviews quick and minimizes merge conflicts.
- **Split the backlog into sequential PRs.** When the triage list is longer than five files, move the extra items into follow-up tickets or tasks and reference them in the summary of the current PR.
- **Call out dependency ordering.** Note when a future PR must wait for the current change set (for example, if a shared include will be renamed later).

## 3. Verification commands and hygiene checklist

Run the relevant Sphinx builds before requesting review:

- `make html-<product>` – build only the product(s) touched in this PR (e.g., `make html-winsyslog`).
- `make all-html` – optional but recommended after a series of restructure PRs to ensure cross-project integrity.

Use this checklist while reviewing your diff:

- **Toctrees:** Confirm each moved or renamed document still appears in an appropriate toctree. Update parent `index.rst` files as needed.
- **Includes:** Adjust any `.. include::` directives so they reference the new path, and prune unused includes that are now empty.
- **Supporting labels:** Synchronize anchors and references in `source/shared/supporting-labels.rst` to keep labels unique, documented, and free of orphans.

## 4. Reusable AI prompt

Use (and adapt) the following prompt whenever you ask an AI assistant to help with restructure work. It enforces the incremental workflow above and keeps label hygiene in sync with `source/shared/supporting-labels.rst`.

```text
You are helping restructure the Adiscon documentation repository. Follow this incremental workflow:

1. Triage the provided files. For each one, decide whether it belongs in a product-specific directory (e.g., winsyslog/, rsyslog/) or in source/shared/.
2. Limit the change set to five files or fewer. If more files need work, describe them and queue them as follow-up tasks instead of editing them now.
3. After drafting changes, verify:
   - Each affected toctree still lists the right documents.
   - All include directives point to the correct paths.
   - Labels remain unique and are documented in source/shared/supporting-labels.rst.
4. List the commands to run for validation (make html-<product> for touched products, plus make all-html when a full sweep is required).
5. Summarize outstanding follow-up tasks so the next PR can continue the restructure.
```
