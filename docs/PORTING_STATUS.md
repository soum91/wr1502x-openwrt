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

## Outstanding validation

1. Capture UART boot output from this exact router and verify bootargs, active bank, and MTD table.
2. Make a complete flash backup and prove a recovery procedure before any write.
3. Verify Ethernet port mapping, LAN DHCP, WAN behavior, and management access.
4. Add board-specific radio initialization/configuration and test 2.4 GHz and 5 GHz, calibration, and switch behavior.
5. Verify USB and rollback behavior.

A USB-C Ethernet adapter does not provide serial console access. Use only a 3.3 V USB-TTL adapter for UART; do not use RS-232 voltage levels. No flashing directions are published until recovery and partition geometry are verified.
