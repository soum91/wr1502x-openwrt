TP-Link TL-WR1502X V1.0 US - OpenWrt bring-up candidate

STATUS: EXPERIMENTAL COMPONENTS ONLY. NOT A STOCK WEB-UPDATER IMAGE.
Do not upload these files through TP-Link's normal firmware update page.
Do not write either component to flash until the exact unit's UART boot log,
active slot/partition map, and recovery method are verified.

Hardware identity used: TL-WR1502X V1.0 US; stock firmware 1.1.1 Build
20250808 rel.68172.

Files:
- wr1502x-openwrt-kernel-cs6c.bin: Realtek cvimg kernel component, based on
  TP-Link GPL Linux 4.4 tree; built-in console 115200 8N1; kernel payload
  header burn address 0x00300000.
- wr1502x-openwrt-rootfs-r6cr.bin: Realtek cvimg root filesystem component
  wrapping an OpenWrt 21.02.7 MIPS little-endian generic userspace; header
  burn address 0x00D00000.

These are two separate components, not a signed TP-Link cloud/update image.
The normal web updater's signature/format requirements have not been met.
The U-Boot/TFTP recovery route is not verified on this hardware revision, so
no flashing command is provided.

Known gaps:
- Not boot-tested on the router.
- No verified mapping for LAN/WAN ports in OpenWrt.
- No OpenWrt radio configuration; Wi-Fi operation is not provided by this
  prototype even though the vendor kernel source contains proprietary radio
  drivers.
- No successful UART recovery test or complete per-device flash backup.
- The runtime dual-bank layout came from community reverse engineering and
  still needs confirmation on this exact device.

Next required validation: connect a 3.3V USB-TTL adapter (not RS-232), capture
serial boot output at 115200 8N1, identify active slot and MTD partitions,
back up flash, and verify a recovery procedure before any write. Preserve the
stock firmware and do not use the USB-C Ethernet adapter as a serial adapter.

Build context: generated from TP-Link's WR1502X V1 GPL SDK plus an OpenWrt
21.02.7 MIPS userspace. This keeps the vendor kernel/driver base; it is not a
mainline OpenWrt device port.

----------------------------------------------------------------------
REVISION 2 (2026-11-07): rootfs fixes. Kernel component is UNCHANGED.
----------------------------------------------------------------------

Rootfs changes:
- Added /lib/preinit/80_ram_etc_fallback. The vendor 4.4 kernel has no
  overlayfs, so mount_root cannot build a writable overlay and the stock
  rootfs would stay fully read-only. If /etc is not writable after
  mount_root, /etc is copied onto its own tmpfs and moved into place.
  Config, root password and dropbear host keys now work, but NOTHING
  persists across reboots, and nothing is written to flash.
- Sysupgrade disabled: platform_check_image now always fails. The old
  file was the ramips/mt7621 platform.sh, which accepted any image.
- LuCI "Backup / Flash Firmware" page removed.
- Removed leftover lib/preinit/07_mt7621_bringup_dsa_master.
- DHCP and IPv6 RA disabled on lan ("option ignore 1"). The OpenWrt eth0
  port mapping is unknown; if eth0 is the WAN-side jack the router would
  otherwise serve DHCP onto the upstream network. To reach it, set your
  laptop to a static 192.168.1.2/24 and browse or ssh to 192.168.1.1.
  Root password is empty until set (per boot).

Still open (needs a kernel rebuild from the TP-Link GPL tree):
- CONFIG_OVERLAY_FS=y and a defined rootfs_data partition for persistent
  config.
- Kernel has no IKCONFIG and no root= in its built-in cmdline; root device
  depends on the Realtek flash map, unverified.
- Kernel start address 0x80A00000 and burn addresses not yet compared
  against stock firmware 1.1.1 components.
- /lib/modules is empty; kmod-* packages from opkg are for 5.4 and will
  not load on this 4.4 kernel.

All the original warnings above still apply. Do not flash without a UART
log, a full flash backup and a verified recovery path.
