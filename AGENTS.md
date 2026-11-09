# Project instructions

- Preserve the WR1502X V1.0 US hardware target and clearly identify every image's exact model/revision.
- Never call a component bundle flashable until boot, LAN/WAN, radios, and the unit-specific recovery route are validated.
- Never instruct use of the TP-Link web updater for unsigned/custom images.
- Every release must include a root `CHANGELOG.md` with concrete changes and a visible installed/build version where applicable.
- Record SHA-256 hashes for distributed binaries and include source/build provenance.
- Keep known risks and unverified hardware assumptions in the README and release notes.


## Universal diagnostic copy and export contract

Applies to Codex, Claude and all future diagnostic/debug/log reporting UI:

- Never ship a silent clipboard-only Copy button. After writing a report to the platform clipboard, immediately verify the full written text where APIs permit and display success or actionable failure. Do not present success on an unverified write.
- Every report must also offer an independent native Share action and Save as plain `.txt` file. On iOS, use the system share sheet and native Files picker (`fileExporter` or `UIDocumentPickerViewController`), not a custom file-path prompt. Allow selection of the complete report.
- Export the full diagnostics, including actual installed app/build, OS/device, and actionable failure/return codes. Redact credentials, access tokens, passwords and other secrets. Do not upload reports without consent.
- Test on a signed real device: Copy, paste into another app, Share and Save to Files, including error paths. If physical verification is unavailable, say so explicitly; a passing build is not evidence of clipboard success.
- Prefer one reusable diagnostic export component per application. Ensure future releases and newly created repositories retain this rule in both AGENTS.md and CLAUDE.md.
