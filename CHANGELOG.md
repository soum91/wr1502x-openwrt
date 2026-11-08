# Changelog

## Unreleased

### Rootfs rev2 (2026-11-07), artifacts/2026-11-07-rev2

Target: TP-Link TL-WR1502X V1.0 US. Still NOT flashable, not boot-tested.

- Kernel component unchanged (sha256 49ade965...d67a2).
- Added `lib/preinit/80_ram_etc_fallback`: the vendor 4.4.176 kernel has no overlayfs, so mount_root cannot build a writable overlay. /etc now goes on its own tmpfs when it is not writable. Config, root password and dropbear keys work per boot; nothing persists and nothing is written to flash.
- Replaced the ramips/mt7621 `lib/upgrade/platform.sh` (accepted any image) with one that always refuses sysupgrade.
- Removed the LuCI "Backup / Flash Firmware" page.
- Removed leftover `lib/preinit/07_mt7621_bringup_dsa_master`.
- DHCP and RA disabled on lan (`option ignore 1`) until the eth0 port mapping is known.
- Rootfs rewrapped as r6cr (start 0x000F0000, burn 0x00D00000) with `tools/cvimg.py`; the tool reproduces the original rev1 rootfs component byte for byte. Same size as rev1 (0x341002).
- Added `.github/workflows/gpl-extract.yml`: pulls TP-Link's GPL_TL-WR1502Xv1.tar.gz on a runner and publishes the 4.4 kernel tree(s), kernel configs and flash layout hints as release `gpl-extract`.

### Findings

- Stock 1.1.1 updater image (`fw-type:Cloud`) is signed and its payload is encrypted (entropy ~7.95 bits/byte throughout). It cannot be used to cross-check addresses, and the stock web updater is not a route for any custom image.
- Vendor kernel: no IKCONFIG, built-in cmdline is only `console=ttyS0,115200` (no `root=`), no overlayfs.
- `artifacts/2026-11-07/openwrt-21.02.diffconfig` header still refers to "MR1500X" / `DEVICE_adslr_g7`; it was carried over from another build and needs checking.
- `validate-candidate.yml` expects `artifacts/2026-11-07/wr1502x-openwrt-bringup-candidate.zip`, which is not in the repo, so that workflow fails as committed.

### Rev1 (2026-11-07)

- Added initial WR1502X V1.0 US OpenWrt bring-up status and experimental artifact packaging.
- Built untested Realtek cs6c kernel and r6cr OpenWrt rootfs components from matching vendor GPL kernel plus generic OpenWrt userspace.
- No flash-ready/signed firmware release; hardware boot, network, wireless, and recovery validation remain open.
