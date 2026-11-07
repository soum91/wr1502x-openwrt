# TL-WR1502X OpenWrt bring-up

Experimental OpenWrt-derived bring-up work for the **TP-Link TL-WR1502X V1.0 US**.

> **Warning: this is not a flashable release.** The current build is an untested pair of Realtek kernel/rootfs components, not an OEM-signed TP-Link update. Do not upload it through the stock updater or write it to flash before serial recovery and the exact unit's flash layout are verified.

## Current state

- Built a Realtek cs6c kernel component from TP-Link's matching GPL Linux 4.4 source.
- Built an OpenWrt 21.02.7 generic MIPS little-endian rootfs wrapped as r6cr.
- Neither component has been boot-tested on the router.
- LAN/WAN port mapping, DHCP, and both Wi-Fi radios are unverified; the current rootfs has no WR1502X-specific Wi-Fi configuration.
- A 3.3 V USB-TTL UART log, active-slot/MTD verification, full flash backup, and confirmed recovery procedure are still required before any flash attempt.

The existing stock kernel and Realtek proprietary drivers are retained in this prototype. This is not a mainline OpenWrt device target.

## Device details

- Model: TP-Link TL-WR1502X
- Hardware: V1.0 US
- Stock firmware reported by Tether: 1.1.1 Build 20250808 rel.68172
