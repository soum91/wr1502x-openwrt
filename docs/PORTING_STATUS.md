# TL-WR1502X V1 OpenWrt bring-up status

Updated: 2026-11-07

## Target

- TP-Link TL-WR1502X V1.0 US
- Stock version reported in Tether: 1.1.1 Build 20250808 rel.68172
- Matching TP-Link GPL source includes the vendor Linux 4.4 kernel and proprietary radio drivers.

## Prototype

- Built a Realtek `cs6c` kernel component from the matching vendor kernel tree. It links for MIPS32r2, uses serial console 115200 8N1, and carries burn address `0x00300000`.
- Built a generic OpenWrt 21.02.7 MIPS little-endian root filesystem, wrapped in a Realtek `r6cr` component with burn address `0x00D00000`.
- Kernel and rootfs fit the observed partition sizes, but the dual-bank map is community-derived and has not been confirmed on this physical unit.
- Neither component has been boot-tested. This is not a TP-Link-signed updater image and not yet a usable router firmware.

## Kernel gaps found in the rev1 kernel (2026-11-07)

- No overlayfs: OpenWrt cannot get a writable root. Rootfs rev2 works around this with a RAM-backed /etc (non-persistent). Real fix: rebuild with `CONFIG_OVERLAY_FS=y` plus a `rootfs_data` partition.
- No `root=` in the built-in cmdline and no IKCONFIG; the root device depends on the Realtek flash map in the vendor tree.
- Stock 1.1.1 updater image is signed and encrypted, so stock addresses must come from the GPL tree or a UART log.

## Flash layout per TP-Link GPL (GPL_TL-WR1502Xv1.tar.gz, sha256 9efe1123...d4a3)

The rev1/rev2 component burn addresses (kernel 0x00300000, rootfs 0x00D00000) do NOT match anything in the GPL. Do not write them anywhere, including via bootloader TFTP, which writes to the header burn address.

- SDK model built by the GPL: `SPINAND_RTL8197F_VG_8832BR_8367R_KERN44_GW` (rtl8197/.config).
- Kernel board config: `CONFIG_RTL_LINUX_IMAGE_OFFSET=0x900000`, `CONFIG_RTL_ROOT_IMAGE_OFFSET=0xE00000`, `CONFIG_RTL_FLASH_SIZE=0x5000000`, `CONFIG_CMDLINE="console=ttyS0,38400 root=/dev/mtdblock3"`, `# CONFIG_OVERLAY_FS is not set`.
- SPI NAND partitions (drivers/mtd/nand/rtkn_nand/rtknflash_partition.c, cmdline parts disabled): boot 0x0 (5 MB), setting 0x500000 (3 MB), linux 0x800000 (to 0xE00000), rootfs 0xE00000 (to flash size). root=/dev/mtdblock3 is the rootfs partition.
- Every SPI NAND bootcode config: kernel scanned 0x800000 to 0x900000 and rootfs 0xE00000 to 0x1000000, 0x20000 steps.
- Alternate Barrier Breaker path (rtknflash_openwrt.c, only if CONFIG_WRT_BARRIER_BREAKER, which is not set in any product config found): same boot/setting/linux/rootfs offsets, 40 MB banks, and the bootinfo (active bank) block at 0x300000. The rev1 kernel burn address is exactly that bootinfo offset.
- TP-Link product layer (Iplatform/build/product_configs/wr1502xv1/iplatform.config): `CONFIG_PACKAGE_NM_FLASH_SIZE=0x2800000`, `NM_UBOOT_FLASH_SIZE=0x100000`, `NM_KERNEL_FLASH_SIZE=0xa00000`, `NM_ROOTFS_FLASH_SIZE=0x1e00000`. These partition-manager sizes do not line up with the Realtek offsets above, so the on-device layout still has to be confirmed from a UART log (`/proc/mtd`, bootloader output).
- Stock serial console is 38400 8N1, not 115200.

## Outstanding validation

1. Capture UART boot output from this exact router and verify bootargs, active bank, and MTD table.
2. Make a complete flash backup and prove a recovery procedure before any write.
3. Verify Ethernet port mapping, LAN DHCP, WAN behavior, and management access.
4. Add board-specific radio initialization/configuration and test 2.4 GHz and 5 GHz, calibration, and switch behavior.
5. Verify USB and rollback behavior.

A USB-C Ethernet adapter does not provide serial console access. Use only a 3.3 V USB-TTL adapter for UART; do not use RS-232 voltage levels. No flashing directions are published until recovery and partition geometry are verified.
