# Changelog

## [gpl-extract] - 2026-11-08

## Verified changes since project start

- Document candidate build provenance and limits ([`0f83fa1c`](https://github.com/soum91/wr1502x-openwrt/commit/0f83fa1c39687181ee62c6603dca277f4a08be68); `artifacts/2026-11-07/PROVENANCE.md`)
- Add candidate validation workflow ([`d0570858`](https://github.com/soum91/wr1502x-openwrt/commit/d05708586e629c6647bb2836da9fa394093af48f); `.github/workflows/validate-candidate.yml`)
- Add experimental bring-up build materials ([`320ff072`](https://github.com/soum91/wr1502x-openwrt/commit/320ff0720fd736e33cdb3a37bfc0e633ae1f579c); `artifacts/2026-11-07/900-rtl8192cd-sta-assoc-reply.patch`)
- Add experimental bring-up build materials ([`a7f193ee`](https://github.com/soum91/wr1502x-openwrt/commit/a7f193ee73c5e142fa687fdf1022dbb5dba057c6); `artifacts/2026-11-07/openwrt-21.02.diffconfig`)
- Add experimental bring-up build materials ([`fdb205c0`](https://github.com/soum91/wr1502x-openwrt/commit/fdb205c01238bda550e228de5b09b38c42473ff7); `artifacts/2026-11-07/feeds.conf`)
- Add experimental bring-up build materials ([`3dcf24c6`](https://github.com/soum91/wr1502x-openwrt/commit/3dcf24c6a7491eef3c8ee638b85ff7402de9cd9d); `artifacts/2026-11-07/SHA256SUMS.txt`)
- Add experimental bring-up build materials ([`0e97747a`](https://github.com/soum91/wr1502x-openwrt/commit/0e97747a617f141707a795da116dd90a42ce6504); `artifacts/2026-11-07/README.txt`)
- Add experimental bring-up build materials ([`e960852b`](https://github.com/soum91/wr1502x-openwrt/commit/e960852b0a5503f47082f7563c68b7a25d2bd9b1); `artifacts/2026-11-07/PORTING_STATUS.md`)
- Add detailed porting status ([`c0e82f1b`](https://github.com/soum91/wr1502x-openwrt/commit/c0e82f1b984fa56144234747346650fb091f94bb); `docs/PORTING_STATUS.md`)
- Document WR1502X OpenWrt bring-up status ([`1152cca1`](https://github.com/soum91/wr1502x-openwrt/commit/1152cca116de73808bc4a67b00fd0906a64a130d); `README.md`)

[Inspect exact code changes](https://github.com/soum91/wr1502x-openwrt/commits/gpl-extract)

## Unreleased

- Added initial WR1502X V1.0 US OpenWrt bring-up status and experimental artifact packaging.
- Built untested Realtek cs6c kernel and r6cr OpenWrt rootfs components from matching vendor GPL kernel plus generic OpenWrt userspace.
- No flash-ready/signed firmware release; hardware boot, network, wireless, and recovery validation remain open.
