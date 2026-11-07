# TL-WR1502X V1 OpenWrt bring-up status

Updated: 2026-11-07

## Device

- TP-Link TL-WR1502X V1.0 US
- Stock version reported in Tether: 1.1.1 Build 20250808 rel.68172
- Hardware platform from the matching vendor GPL source: RTL8197F family
- Matching GPL source includes the vendor Linux 4.4 kernel and proprietary radio drivers.

## Prototype built

A paired experimental component bundle is at `build-output/wr1502x-openwrt-bringup-candidate.zip`.

- Kernel: rebuilt from TP-Link's product GPL tree with the observed 128 MiB dual-bank flash geometry and a serial console. It packages as Realtek `cs6c` with burn address `0x00300000`.
- Root filesystem: OpenWrt 21.02.7 generic MIPS little-endian userspace, packaged as Realtek `r6cr` with burn address `0x00D00000`.
- The OpenWrt root filesystem is approximately 3.4 MB and fits the observed rootfs partition size.
- Kernel links successfully for MIPS32r2. Vendor build emits two section-mismatch warnings. No physical boot test has occurred.

This is not a signed TP-Link updater image and is not accepted as a verified stock-web-update file. The candidate has not been confirmed bootable or flashable. Do not write it to flash based only on the community-derived partition map.

## Known missing validation

- Capture UART boot output on this exact unit and verify bootargs, active slot, and `/proc/mtd`.
- Identify/verify U-Boot TFTP or other recovery mode before a write; no confirmed recovery procedure exists yet.
- Make a complete flash backup first.
- Validate Ethernet port mapping and DHCP/LAN behavior.
- Port board-specific OpenWrt wireless configuration and verify both radios, calibration, switch, and USB behavior.

The USB-C Ethernet adapter is useful for a wired host connection, but it does not provide serial console access. A 3.3V USB-TTL adapter is required to gather boot data and improve recovery options. The candidate bundle intentionally contains no blind-flash directions.
