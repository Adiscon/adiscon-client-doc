# Agent Anti-Patterns

This file records repeated documentation review findings that future agents
should actively avoid. Read it before documentation work, especially when
touching sales, licensing, versioning, FAQ, or support-policy pages.

When review feedback identifies a repeated mistake, add a short rule here so
the same issue does not return in later cleanup passes.

## Licensing And Version Wording

- Do not expose "License V2" as a user-facing concept. Use "licensing",
  "license file", or a specific user task such as "apply the license file".
- Do not describe version 26 as a "major" in user documentation. Prefer
  "version 26 and later" for current-version pages.
- Do not lead with signed or encrypted implementation details for license
  files. Users usually need to know that `license.alic` is the license file and
  how to apply it.
- Do not repeat older-version licensing details across normal licensing pages.
  Keep the older-version entitlement note in an FAQ-style answer: current
  licenses can cover older versions, but users may need to request a free
  license key from Adiscon for older product versions.
