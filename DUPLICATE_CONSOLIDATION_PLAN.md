# Duplicate Articles Consolidation Plan

## Executive Summary

This document outlines a plan to consolidate duplicate articles found across the documentation repository. The analysis identified **49 duplicate filenames** across the codebase, categorized into three groups:

1. **19 files already in shared** - Need reference updates
2. **27 candidates for moving to shared** - Need content comparison and consolidation
3. **3 product-specific files** - Need manual review to determine if consolidation is possible

---

## Category 1: Files Already in Shared (Update References)

These files exist in `source/shared/` but are also duplicated in product-specific directories. **Action: Update all references to point to shared versions, then delete product-specific duplicates.**

### Priority 1: Reference Files (High Priority)

| File | Shared Location | Product-Specific Locations | Impact |
|------|----------------|---------------------------|--------|
| `cpumemorymonitor.rst` | `source/shared/references/cpumemorymonitor.rst` | `source/producttour/cpumemorymonitor.rst` | Low - appears to be tour vs reference |
| `databasemonitor.rst` | `source/shared/references/databasemonitor.rst` | `source/mwagentspecific/databasemonitor.rst`, `source/producttour/databasemonitor.rst` | Medium |
| `diskspacemonitor.rst` | `source/shared/references/diskspacemonitor.rst` | `source/mwagentspecific/diskspacemonitor.rst`, `source/producttour/diskspacemonitor.rst` | Medium |
| `filemonitor.rst` | `source/shared/references/filemonitor.rst` | `source/mwagentspecific/filemonitor.rst`, `source/producttour/filemonitor.rst` | Medium |
| `ftpprobe.rst` | `source/shared/references/ftpprobe.rst` | `source/mwagentspecific/ftpprobe.rst`, `source/producttour/ftpprobe.rst` | Medium |
| `httpprobe.rst` | `source/shared/references/httpprobe.rst` | `source/mwagentspecific/httpprobe.rst`, `source/producttour/httpprobe.rst` | Medium |
| `imapprobe.rst` | `source/shared/references/imapprobe.rst` | `source/mwagentspecific/imapprobe.rst`, `source/producttour/imapprobe.rst` | Medium |
| `nntpprobe.rst` | `source/shared/references/nntpprobe.rst` | `source/mwagentspecific/nntpprobe.rst`, `source/producttour/nntpprobe.rst` | Medium |
| `pingprobe.rst` | `source/shared/references/pingprobe.rst` | `source/mwagentspecific/pingprobe.rst`, `source/producttour/pingprobe.rst` | Medium |
| `pop3probe.rst` | `source/shared/references/pop3probe.rst` | `source/mwagentspecific/pop3probe.rst`, `source/producttour/pop3probe.rst` | Medium |
| `portprobe.rst` | `source/shared/references/portprobe.rst` | `source/mwagentspecific/portprobe.rst`, `source/producttour/portprobe.rst` | Medium |
| `smtpprobe.rst` | `source/shared/references/smtpprobe.rst` | `source/mwagentspecific/smtpprobe.rst`, `source/producttour/smtpprobe.rst` | Medium |

**Note:** The `producttour/` versions appear to be shorter overview/teaser files that link to the detailed references. These should be kept as they serve a different purpose (quick tour vs detailed reference).

### Priority 2: Getting Started Files (High Priority)

| File | Shared Location | Product-Specific Locations | Impact |
|------|----------------|---------------------------|--------|
| `creatinganinitialconfiguration.rst` | `source/shared/gettingstarted/creatinganinitialconfiguration.rst` | `source/rsyslogwaspecific/creatinganinitialconfiguration.rst`, `source/winsyslogspecific/creatinganinitialconfiguration.rst` | High |
| `filterconditions.rst` | `source/shared/gettingstarted/filterconditions.rst` | `source/eventreporterspecific/filterconditions.rst`, `source/mwagentspecific/filterconditions.rst`, `source/rsyslogwaspecific/filterconditions.rst`, `source/winsyslogspecific/filterconditions.rst` | High |
| `installation.rst` | `source/shared/gettingstarted/installation.rst` | `source/eventreporterspecific/installation.rst`, `source/rsyslogwaspecific/installation.rst`, `source/winsyslogspecific/installation.rst` | High |
| `multiple-rulesets-rules-actions.rst` | `source/shared/gettingstarted/multiple-rulesets-rules-actions.rst` | `source/eventreporterspecific/multiple-rulesets-rules-actions.rst`, `source/rsyslogwaspecific/multiple-rulesets-rules-actions.rst`, `source/winsyslogspecific/multiple-rulesets-rules-actions.rst` | High |
| `obtainingaprintablemanual.rst` | `source/shared/gettingstarted/obtainingaprintablemanual.rst` | `source/eventreporterspecific/obtainingaprintablemanual.rst`, `source/rsyslogwaspecific/obtainingaprintablemanual.rst`, `source/winsyslogspecific/obtainingaprintablemanual.rst` | Medium |

### Priority 3: Reference Files (Medium Priority)

| File | Shared Location | Product-Specific Locations | Impact |
|------|----------------|---------------------------|--------|
| `editioncomparison.rst` | `source/shared/references/editioncomparison.rst` | `source/eventreporterspecific/editioncomparison.rst`, `source/rsyslogwaspecific/editioncomparison.rst`, `source/winsyslogspecific/editioncomparison.rst` | Medium |

---

## Category 2: Candidates for Moving to Shared

These files exist in multiple product-specific directories but **not** in shared. **Action: Compare content, create unified shared version if content is similar, update references, delete duplicates.**

### Group A: Documentation Structure Files

| File | Locations | Notes |
|------|-----------|-------|
| `actions.rst` | `source/eventreporterspecific/actions.rst`, `source/mwagentspecific/actions.rst`, `source/rsyslogwaspecific/actions.rst`, `source/winsyslogspecific/actions.rst` | Likely identical structure/navigation |
| `articles.rst` | `source/eventreporterspecific/articles.rst`, `source/mwagentspecific/articles.rst`, `source/rsyslogwaspecific/articles.rst`, `source/winsyslogspecific/articles.rst` | Likely identical structure/navigation |
| `components.rst` | `source/eventreporterspecific/components.rst`, `source/rsyslogwaspecific/components.rst`, `source/winsyslogspecific/components.rst` | Need content comparison |
| `references.rst` | `source/eventreporterspecific/references.rst`, `source/rsyslogwaspecific/references.rst`, `source/winsyslogspecific/references.rst` | Need content comparison |
| `services.rst` | `source/eventreporterspecific/services.rst`, `source/mwagentspecific/services.rst`, `source/rsyslogwaspecific/services.rst`, `source/winsyslogspecific/services.rst` | Need content comparison |

### Group B: Getting Help and Support

| File | Locations | Notes |
|------|-----------|-------|
| `gettinghelp.rst` | `source/eventreporterspecific/gettinghelp.rst`, `source/gettinghelp.rst`, `source/rsyslogwaspecific/gettinghelp.rst`, `source/winsyslogspecific/gettinghelp.rst` | **Product-specific URLs/product names** - May need `.. only::` blocks or parameterized version |

### Group B: Product Features and Concepts

| File | Locations | Notes |
|------|-----------|-------|
| `features.rst` | `source/eventreporterspecific/features.rst`, `source/introduction/features.rst`, `source/rsyslogwaspecific/features.rst`, `source/winsyslogspecific/features.rst` | Likely product-specific content |
| `introduction.rst` | `source/eventreporterspecific/introduction.rst`, `source/rsyslogwaspecific/introduction.rst`, `source/winsyslogspecific/introduction.rst` | Likely product-specific content |
| `producttour.rst` | `source/eventreporterspecific/producttour.rst`, `source/winsyslogspecific/producttour.rst` | Need content comparison |
| `pt-otherfeatures.rst` | `source/eventreporterspecific/pt-otherfeatures.rst`, `source/winsyslogspecific/pt-otherfeatures.rst` | Need content comparison |
| `pt-powerfulleventprocessing.rst` | `source/eventreporterspecific/pt-powerfulleventprocessing.rst`, `source/winsyslogspecific/pt-powerfulleventprocessing.rst` | Need content comparison |
| `pt-setpsupport.rst` | `source/eventreporterspecific/pt-setpsupport.rst`, `source/winsyslogspecific/pt-setpsupport.rst` | Need content comparison |
| `pt-syslogsupport.rst` | `source/eventreporterspecific/pt-syslogsupport.rst`, `source/winsyslogspecific/pt-syslogsupport.rst` | Need content comparison |

### Group C: Configuration Options

| File | Locations | Notes |
|------|-----------|-------|
| `general-options.rst` | `source/mwagentspecific/general-options.rst`, `source/winsyslogspecific/general-options.rst` | Need content comparison - may have product-specific differences |
| `generaloptions.rst` | `source/mwagentspecific/generaloptions.rst`, `source/winsyslogspecific/generaloptions.rst` | **Note:** Hyphenated vs non-hyphenated - check if these are different files |
| `a-forwardsyslogoptions.rst` | `source/mwagentspecific/a-forwardsyslogoptions.rst`, `source/rsyslogwaspecific/a-forwardsyslogoptions.rst`, `source/winsyslogspecific/a-forwardsyslogoptions.rst` | Action reference - likely similar |

### Group D: Monitors and Services

| File | Locations | Notes |
|------|-----------|-------|
| `eventlogmonitorv2.rst` | `source/mwagentspecific/eventlogmonitorv2.rst`, `source/producttour/eventlogmonitorv2.rst` | Tour vs reference - keep both? |
| `heartbeat.rst` | `source/mwagentspecific/heartbeat.rst`, `source/producttour/heartbeat.rst` | Tour vs reference - keep both? |
| `serialportmonitor.rst` | `source/mwagentspecific/serialportmonitor.rst`, `source/producttour/serialportmonitor.rst` | Tour vs reference - keep both? |
| `setpserver.rst` | `source/mwagentspecific/setpserver.rst`, `source/producttour/setpserver.rst` | Tour vs reference - keep both? |
| `snmptrapreceiver.rst` | `source/mwagentspecific/snmptrapreceiver.rst`, `source/producttour/snmptrapreceiver.rst` | Tour vs reference - keep both? |
| `syslogserver.rst` | `source/mwagentspecific/syslogserver.rst`, `source/producttour/syslogserver.rst` | Tour vs reference - keep both? |

### Group E: Other Files

| File | Locations | Notes |
|------|-----------|-------|
| `commonuses.rst` | `source/commonuses.rst`, `source/rsyslogwaspecific/commonuses.rst` | Need content comparison |
| `eventreporter.rst` | `source/eventreporterspecific/eventreporter.rst`, `source/glossaryofterms/eventreporter.rst` | Likely different purposes (overview vs glossary) |
| `glossaryofterms.rst` | `source/rsyslogwaspecific/glossaryofterms.rst`, `source/winsyslogspecific/glossaryofterms.rst` | Need content comparison |
| `stepbystepguides.rst` | `source/eventreporterspecific/stepbystepguides.rst`, `source/stepbystepguides.rst`, `source/winsyslogspecific/stepbystepguides.rst` | Need content comparison |
| `systemrequirements.rst` | `source/eventreporterspecific/systemrequirements.rst`, `source/rsyslogwaspecific/systemrequirements.rst`, `source/winsyslogspecific/systemrequirements.rst` | May have product-specific requirements |

---

## Category 3: Product-Specific Files (Manual Review Needed)

These files exist in FAQ directories and may have product-specific content that cannot be easily consolidated.

| File | Locations | Notes |
|------|-----------|-------|
| `faq.rst` | `source/eventreporterspecific/faq.rst`, `source/mwagentspecific/faq.rst`, `source/rsyslogwaspecific/faq.rst`, `source/winsyslogspecific/faq.rst` | FAQ index files - likely product-specific questions |
| `log-rotation-file-handle-cleanup.rst` | `source/eventreporterspecific/faq/log-rotation-file-handle-cleanup.rst`, `source/mwagentspecific/faq/log-rotation-file-handle-cleanup.rst`, `source/winsyslogspecific/faq/log-rotation-file-handle-cleanup.rst` | **Already reviewed** - Different product versions/contexts, may be consolidatable with version-specific sections |
| `start-program-action-troubleshooting.rst` | `source/eventreporterspecific/faq/start-program-action-troubleshooting.rst`, `source/mwagentspecific/faq/start-program-action-troubleshooting.rst`, `source/rsyslogwaspecific/faq/start-program-action-troubleshooting.rst`, `source/winsyslogspecific/faq/start-program-action-troubleshooting.rst` | Need content comparison - may be consolidatable |

---

## Implementation Plan

### Phase 1: High-Priority Reference Updates (Category 1, Priority 1 & 2)

**Goal:** Update references to files already in shared, then remove duplicates.

1. **For each file in Priority 1 & 2:**
   - Find all references using: `grep -r "filename" source/ --include="*.rst"`
   - Update references from product-specific paths to shared paths
   - Use `.. only::` blocks for product-specific builds if needed (per AGENTS.md Rule 4)
   - Verify build with `make all-html SPHINXOPTS="-W"`
   - Delete product-specific duplicate files

2. **Special handling for `producttour/` files:**
   - Keep `producttour/` versions as they serve as teaser/overview files
   - Ensure they properly link to shared reference versions
   - Verify no broken references

**Estimated Files to Update:** ~15-20 files  
**Estimated References to Fix:** ~50-100 references

### Phase 2: Content Comparison and Consolidation (Category 2)

**Goal:** Compare duplicate files, create shared versions where appropriate.

1. **For each candidate file:**
   - Compare content of all duplicate versions
   - Determine if content is:
     - **Identical** → Move to shared, update references, delete duplicates
     - **Similar but product-specific** → Create shared version with `.. only::` blocks for product-specific sections
     - **Different products** → Keep separate but document why

2. **Priority order:**
   - Group A (Documentation Structure) - High priority
   - Group C (Configuration Options) - Medium priority  
   - Group B (Getting Help) - Medium priority (may need product-specific handling)
   - Group D (Monitors) - Low priority (tour vs reference distinction)
   - Group E (Other) - Low priority

**Estimated Files to Process:** ~27 files  
**Estimated Time:** Content comparison required for each

### Phase 3: Product-Specific Review (Category 3)

**Goal:** Review FAQ and product-specific files for consolidation opportunities.

1. Review each FAQ file:
   - Compare content across products
   - Determine if consolidation is possible with version/product-specific sections
   - Document findings

2. For `log-rotation-file-handle-cleanup.rst`:
   - **Already analyzed:** Files cover different products/versions
   - **Possible approach:** Create shared version with product-specific sections using `.. only::` blocks
   - **Alternative:** Keep separate if consolidation reduces clarity

**Estimated Files to Process:** ~3 files

---

## Reference Update Patterns

### Pattern 1: Update :doc: references

**Before:**
```rst
:doc:`Filter Conditions <../winsyslogspecific/filterconditions>`
```

**After:**
```rst
:doc:`Filter Conditions <../shared/gettingstarted/filterconditions>`
```

### Pattern 2: Update toctree entries

**Before:**
```rst
.. toctree::
   ../winsyslogspecific/filterconditions
```

**After:**
```rst
.. toctree::
   ../shared/gettingstarted/filterconditions
```

### Pattern 3: Cross-manual references (use .. only:: blocks)

**Before:**
```rst
:doc:`General Options <../mwagentspecific/generaloptions>`
```

**After (if consolidating):**
```rst
.. only:: mwagent
   :doc:`General Options <../shared/references/generaloptions>`

.. only:: winsyslog
   :doc:`General Options <../shared/references/generaloptions>`
```

---

## Risk Assessment

### Low Risk
- Updating references to files already in shared (Category 1)
- Files with identical content across products

### Medium Risk
- Files with product-specific differences (need careful `.. only::` usage)
- Tour vs reference distinction (need to verify purpose)

### High Risk
- Files with significant product-specific content (may not be consolidatable)
- FAQ files (may lose context if consolidated)

---

## Validation Steps

After each phase:

1. **Build validation:**
   ```bash
   make all-html SPHINXOPTS="-W"
   ```

2. **Reference validation:**
   ```bash
   grep -r "old-path" source/ --include="*.rst"
   # Should return zero results after updates
   ```

3. **English spelling validation:**
   ```bash
   make spelling
   ```

4. **RST validation:**
   ```bash
   make validate-rst
   ```

---

## Estimated Impact

- **Files to delete:** ~40-50 duplicate files
- **References to update:** ~100-200 references
- **Files to create/update in shared:** ~10-15 new shared files
- **Build improvements:** Faster builds, less duplication to maintain

---

## Notes and Considerations

1. **`producttour/` vs `shared/references/` distinction:**
   - `producttour/` files appear to be short overview/teaser files
   - `shared/references/` files are detailed reference documentation
   - These may serve different purposes and both should be kept

2. **Product-specific URLs and names:**
   - Files like `gettinghelp.rst` contain product-specific URLs
   - May need `.. only::` blocks or separate shared versions per product
   - Consider using Sphinx substitutions or includes for product names

3. **Case sensitivity:**
   - `general-options.rst` vs `generaloptions.rst` - verify these are different files
   - Be careful with file name casing per AGENTS.md rules

4. **Cross-manual references:**
   - Per AGENTS.md Rule 4, cross-manual links MUST be guarded with `.. only::` blocks
   - This becomes critical when consolidating to shared

5. **Index files:**
   - Multiple `index.rst` files exist - these are typically directory-specific and should remain separate

---

## Next Steps

1. **Review this plan** and provide feedback
2. **Approve priorities** - determine which categories to tackle first
3. **Begin Phase 1** - Start with high-priority reference updates
4. **Iterate** - Update plan based on findings during implementation
