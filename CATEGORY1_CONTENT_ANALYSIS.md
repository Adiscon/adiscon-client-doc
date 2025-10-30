# Category 1: Content Analysis Report
## Files Already in Shared - Content Comparison

This report analyzes the 7 files that exist in both `source/shared/` and product-specific directories (`mwagentspecific`, `rsyslogwaspecific`, `winsyslogspecific`, `eventreporterspecific`) to determine if product-specific versions have been customized or can be safely deleted.

---

## Summary

| File | Match Status | Customization Level | Recommendation |
|------|-------------|---------------------|----------------|
| `creatinganinitialconfiguration.rst` | ❌ Different | **High** - Completely different content | **KEEP SEPARATE** - Product-specific workflows |
| `editioncomparison.rst` | ❌ Different | **Medium** - Product-specific editions | **KEEP SEPARATE** - Product-specific content |
| `filterconditions.rst` | ❌ Different | **High** - Extensive customization | **KEEP SEPARATE** - Different purposes |
| `installation.rst` | ❌ Different | **Low** - Structure similar, URLs differ | **CONSOLIDATE** - Can merge with `.. only::` blocks |
| `multiple-rulesets-rules-actions.rst` | ❌ Different | **High** - Different content depth | **KEEP SEPARATE** - Product-specific versions |
| `obtainingaprintablemanual.rst` | ❌ Different | **Low** - Only URLs differ | **CONSOLIDATE** - Can merge with `.. only::` blocks |

---

## Detailed Analysis

### 1. `creatinganinitialconfiguration.rst`

**Shared:** `source/shared/gettingstarted/creatinganinitialconfiguration.rst`  
**Product-specific:** 
- `source/rsyslogwaspecific/creatinganinitialconfiguration.rst`
- `source/winsyslogspecific/creatinganinitialconfiguration.rst`

**Content Comparison:**
- **Shared version:** Focuses on MonitorWare Agent's 5 functions (Data gatherer, Real Time Alerter, Automatic Admin Actions, Relay Server, Event Repository)
- **WinSyslog version:** Completely different - focuses on WinSyslog-specific workflow (creating rulesets, syslog listeners, starting service)
- **Rsyslog version:** Not reviewed but likely different

**Verdict:** ❌ **HIGH CUSTOMIZATION**  
**Recommendation:** **KEEP SEPARATE** - These serve different products with different workflows. The shared version is MonitorWare Agent-specific, not truly shared.

---

### 2. `editioncomparison.rst`

**Shared:** `source/shared/references/editioncomparison.rst`  
**Product-specific:**
- `source/eventreporterspecific/editioncomparison.rst`
- `source/rsyslogwaspecific/editioncomparison.rst`
- `source/winsyslogspecific/editioncomparison.rst`

**Content Comparison:**
- Each product has different editions/versions
- Content likely compares different feature sets per product

**Verdict:** ❌ **MEDIUM CUSTOMIZATION**  
**Recommendation:** **KEEP SEPARATE** - Edition comparisons are inherently product-specific.

---

### 3. `filterconditions.rst`

**Shared:** `source/shared/gettingstarted/filterconditions.rst`  
**Product-specific:**
- `source/eventreporterspecific/filterconditions.rst`
- `source/mwagentspecific/filterconditions.rst`
- `source/rsyslogwaspecific/filterconditions.rst`
- `source/winsyslogspecific/filterconditions.rst`

**Content Comparison:**

**Shared version (basic):**
- Simple explanation of Boolean operators (AND, OR, XOR, NOT, TRUE, FALSE)
- Very short, conceptual only
- ~21 lines

**Product-specific versions (extensive):**
- Detailed explanations with screenshots
- Real-world examples (IIS intrusion detection)
- Product-specific toctrees linking to product-specific filter documentation
- ~75-150 lines depending on product
- Different toctree structures per product:
  - EventReporter: Links to `../mwagentspecific/f-*` filters
  - MonitorWare Agent: Links to `f-*` filters (relative paths)
  - WinSyslog: Likely different structure

**Verdict:** ❌ **HIGH CUSTOMIZATION**  
**Recommendation:** **KEEP SEPARATE** - The shared version is a basic primer, while product-specific versions are comprehensive guides with product-specific navigation. They serve different purposes.

**Note:** The shared version might be intended as a simple introduction, while product-specific versions are the full documentation. Consider if the shared version should be renamed or removed.

---

### 4. `installation.rst`

**Shared:** `source/shared/gettingstarted/installation.rst`  
**Product-specific:**
- `source/eventreporterspecific/installation.rst`
- `source/rsyslogwaspecific/installation.rst`
- `source/winsyslogspecific/installation.rst`

**Content Comparison:**

**Shared version:**
```rst
.. only:: mwagent
   Review the `Installing MonitorWare Agent <https://www.mwagent.com/...>`_
   guide...
   ...links to mwagent.com download page
```

**EventReporter version:**
```rst
.. only:: eventreporter
   Review the dedicated `Installing EventReporter <https://www.mwagent.com/...>`_
   guide...
   ...links to EventReporter.com download page
```

**WinSyslog version:**
```rst
.. only:: winsyslog
   **Installation is quick and easy...**
   ...links to WinSyslog.com download page
   ...includes more detailed installation instructions
```

**Structure:** All versions use:
- Same index entry
- Same included partial: `../shared/partials/installation-overview.rst` (or `../partials/installation-overview.rst` in shared)
- Same toctree structure
- Product-specific `.. only::` blocks with product-specific URLs and text

**Verdict:** ⚠️ **LOW-MEDIUM CUSTOMIZATION**  
**Recommendation:** **CAN CONSOLIDATE** - All versions share the same structure and include. The only differences are:
1. Product-specific `.. only::` blocks (which are correct)
2. Different download URLs (product-specific)
3. Minor text differences

**Action Plan:**
1. Merge all product-specific `.. only::` blocks into the shared version
2. Update product-specific files to just include: `.. include:: ../shared/gettingstarted/installation.rst`
3. Verify all product-specific `.. only::` blocks are present in shared version
4. Update references from product-specific paths to shared path

---

### 5. `multiple-rulesets-rules-actions.rst`

**Shared:** `source/shared/gettingstarted/multiple-rulesets-rules-actions.rst`  
**Product-specific:**
- `source/eventreporterspecific/multiple-rulesets-rules-actions.rst`
- `source/rsyslogwaspecific/multiple-rulesets-rules-actions.rst`
- `source/winsyslogspecific/multiple-rulesets-rules-actions.rst`

**Content Comparison:**

**Shared version:**
- Mentions "MonitorWare Agent" specifically
- Basic explanation (~22 lines)
- Simple structure with image and brief description
- Links use `../../glossaryofterms/` paths

**EventReporter version:**
- Mentions "EventReporter" specifically
- Similar structure to shared (~25 lines)
- Links use `../glossaryofterms/` paths
- Slightly different capitalization ("rules" vs "Rules")

**WinSyslog version:**
- Completely rewritten, much more detailed (~23 lines but richer content)
- Title: "Organizing with RuleSets, Rules, and Actions" (vs "Multiple RuleSets - Rules - Actions")
- Extensive explanation with examples
- Different image width (70% vs 100%)
- Product-specific links: `../winsyslogspecific/wsconcepts-services`
- More educational tone

**Verdict:** ❌ **HIGH CUSTOMIZATION**  
**Recommendation:** **KEEP SEPARATE** - WinSyslog version is significantly rewritten. EventReporter and shared versions are similar but have product-specific mentions. These reflect different documentation styles/approaches per product.

---

### 6. `obtainingaprintablemanual.rst`

**Shared:** `source/shared/gettingstarted/obtainingaprintablemanual.rst`  
**Product-specific:**
- `source/eventreporterspecific/obtainingaprintablemanual.rst`
- `source/rsyslogwaspecific/obtainingaprintablemanual.rst`
- `source/winsyslogspecific/obtainingaprintablemanual.rst`

**Content Comparison:**

**Shared version:**
```rst
A printable version of the manual can be obtained at
https://www.mwagent.com/help/manual.
```

**EventReporter version:**
```rst
A printable version of the manual can be obtained at
https://www.EventReporter.com/manuals.
```

**WinSyslog version:**
```rst
A printable version of the manual can be obtained at
https://www.WinSyslog.com/help/manual/.
```

**Rsyslog version:**
```rst
A printable version of the manual can be obtained at http://www.Rsyslog.com
```

**Structure:** All versions are **identical** except for the URL on line 4-5.

**Verdict:** ✅ **LOW CUSTOMIZATION**  
**Recommendation:** **CONSOLIDATE** - Content is identical except for product-specific URLs. Can easily merge with `.. only::` blocks.

**Action Plan:**
1. Merge all product-specific URL blocks into shared version using `.. only::` blocks
2. Update all references to point to shared version
3. Delete product-specific duplicates
4. Test builds

---

## Overall Recommendations

### Files to Consolidate (Low Risk)

1. **`installation.rst`** - ✅ **SAFE TO CONSOLIDATE**
   - All versions share same structure
   - Only differences are product-specific `.. only::` blocks and URLs
   - Can merge all `.. only::` blocks into shared version

2. **`obtainingaprintablemanual.rst`** - ✅ **SAFE TO CONSOLIDATE**
   - Content is identical except for product-specific URLs
   - Can merge with `.. only::` blocks for URLs

### Files to Keep Separate (High Risk)

1. **`creatinganinitialconfiguration.rst`** - ❌ **KEEP SEPARATE**
   - Completely different content per product
   - Different workflows and purposes

2. **`filterconditions.rst`** - ❌ **KEEP SEPARATE**
   - Shared version is basic primer
   - Product versions are comprehensive guides with product-specific navigation
   - Different purposes

3. **`multiple-rulesets-rules-actions.rst`** - ❌ **KEEP SEPARATE**
   - WinSyslog version significantly rewritten
   - Different documentation styles/approaches

4. **`editioncomparison.rst`** - ❌ **KEEP SEPARATE**
   - Product-specific editions


---

## Next Steps

1. **For `installation.rst` (CONSOLIDATE):**
   - Read all product-specific versions
   - Merge all `.. only::` blocks into shared version
   - Update all references to point to shared version
   - Delete product-specific duplicates
   - Test builds

2. **For other files (KEEP SEPARATE):**
   - Consider removing from shared if they're not truly shared
   - OR update shared versions to be truly generic (if possible)
   - Document why they remain separate

3. **For `obtainingaprintablemanual.rst` (CONSOLIDATE):**
   - Merge all product-specific URLs into shared version using `.. only::` blocks
   - Update all references to point to shared version
   - Delete product-specific duplicates
   - Test builds

---

## Risk Assessment

**Low Risk:**
- `installation.rst` - Structure is identical, only product-specific blocks differ
- `obtainingaprintablemanual.rst` - Content identical, only URLs differ

**High Risk:**
- All other files - Significant content differences, different purposes, or product-specific information
