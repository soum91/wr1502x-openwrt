TL-WR1502X V1.0 (US) OpenWrt bring-up, REV3 (2026-11-07)
NOT FLASHABLE. NOT BOOT-TESTED. Hardware model/revision: TL-WR1502X(US) Ver 1.0 only.

Components
  wr1502x-openwrt-kernel-cr6c.bin   vendor Linux 4.4.176 built from TP-Link's GPL
                                    header cr6c, load 0x80A00000, burn 0x00900000
  wr1502x-openwrt-rootfs-r6cr.bin   OpenWrt 21.02.7 mipsel_24kc userspace (rev2 contents)
                                    header r6cr, start 0x000F0000, burn 0x00E00000

Kernel provenance
  Source: GPL_TL-WR1502Xv1.tar.gz from TP-Link (sha256 9efe1123e8f92a00398c7170691daff59355abf06cfe145de58900b74947d4a3)
  Built by .github/workflows/kernel-build.yml in soum91/wr1502x-openwrt (release kernel-build)
  Toolchain: Realtek MSDK-6.4.1 (gcc 6.4.1) shipped in the GPL
  Board config: boards/rtl8197F/config.linux-4.4.SPINAND_RTL8197F_VG_8832BR_8367R_KERN44_GW
  Only change from stock config: CONFIG_OVERLAY_FS=y
  Cmdline (stock): console=ttyS0,38400 root=/dev/mtdblock3
  Packaged by the SDK's own rtkload + cvimg (linux-ro). Verified: header length, 16-bit
  checksum = 0, embedded kernel decompresses, "Linux version 4.4.176 ... MSDK-6.4.1",
  overlayfs present.

Where the addresses come from (GPL, not guesses)
  Kernel partition table (rtknflash_partition.c): boot 0x0, setting 0x500000,
  linux 0x800000, rootfs 0xE00000 (mtdblock3).
  Board config: CONFIG_RTL_LINUX_IMAGE_OFFSET=0x900000, CONFIG_RTL_ROOT_IMAGE_OFFSET=0xE00000.
  SPI NAND bootcode configs scan kernel 0x800000..0x900000 and rootfs 0xE00000..0x1000000.
  SDK mkimg: "cvimg root squashfs.o root.bin F0000 $ROOTFS_OFFSET".
  Kernel ends at 0xAE7812 and rootfs at 0x1141012, both inside their partitions.

Changes vs rev1/rev2
  - Kernel replaced: rebuilt from GPL instead of ChatGPT's build. Rev1 kernel had burn
    address 0x300000 (inside the boot partition, at the bootinfo offset used by the
    dual-image code path), no root=, and console 115200.
  - Rootfs burn address 0xD00000 -> 0xE00000 (stock). Rootfs contents unchanged from rev2.

Known risks / unverified
  - The GPL is the June 2024 drop; the unit runs 1.1.1 (2025-08-08). The bootloader on the
    unit was not built from this tree and its layout is NOT confirmed. TP-Link's
    product config lists partition-manager sizes (40 MB bank, 1 MB uboot, 10 MB kernel,
    30 MB rootfs) that do not line up with the Realtek offsets. Get a UART log first.
  - Overlayfs now exists, but there is no rootfs_data partition, so mount_root falls back to a
    RAM overlay: writable, NOT persistent. Persistence needs a partition split.
  - OpenWrt userspace on a vendor 4.4 kernel: no kmods, vendor Ethernet/switch/Wi-Fi drivers
    built in, eth0 port mapping unknown. LAN DHCP/RA disabled; use static 192.168.1.2.
  - Sysupgrade and the LuCI flash page are disabled.
  - Never use the TP-Link web updater for these images. Stock updates are signed/encrypted.

Before any write to flash
  1. UART at 38400 8N1, capture full stock boot log (bootloader + /proc/mtd).
  2. Full flash backup through the bootloader or stock shell.
  3. Confirm offsets above against the log; confirm a recovery path (bootloader TFTP).
