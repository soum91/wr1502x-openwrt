# Candidate artifact provenance

Target: TP-Link TL-WR1502X V1.0 US
Candidate: experimental Realtek kernel/rootfs component bundle
Source context: TP-Link GPL SDK 3.6.0 family, Linux 4.4; OpenWrt 21.02.7 generic MIPS little-endian userspace.
Current limitations: candidate was not boot-tested; partition map and recovery path are unverified; LAN/WAN and Wi-Fi operation are unverified.
Important: repository does not contain the full GPL SDK or OpenWrt source checkout, so GitHub Actions cannot perform a fresh source compilation. The workflow only verifies and packages the existing candidate ZIP as an Actions artifact. Do not call it flashable or use the TP-Link stock web updater.
