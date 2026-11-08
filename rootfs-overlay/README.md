# Rootfs overlay (rev2)

Files changed or added on top of the OpenWrt 21.02.7 mipsel_24kc rootfs for the TL-WR1502X V1.0 US bring-up. Applied in rootfs rev2 (see CHANGELOG.md).

`lib/preinit/80_ram_etc_fallback` puts /etc on tmpfs when it is not writable after mount_root, because the vendor kernel lacks overlayfs. Changes do not survive a reboot.

`lib/upgrade/platform.sh` refuses all sysupgrade images. The flash layout is unverified.

Not in this folder but also applied in rev2: removal of `lib/preinit/07_mt7621_bringup_dsa_master`, removal of the `admin/system/flash` entry from `usr/share/luci/menu.d/luci-mod-system.json`, and `option ignore 1` on `config dhcp lan` in `etc/config/dhcp`.

Repack: `mksquashfs <root> rootfs.sqfs -comp xz -b 262144 -noappend -all-root -no-xattrs`, then `python3 tools/cvimg.py rootfs.sqfs wr1502x-openwrt-rootfs-r6cr.bin r6cr 000f0000 00d00000`.
