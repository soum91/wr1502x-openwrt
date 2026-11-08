#
# TL-WR1502X bring-up build: sysupgrade is deliberately disabled.
# The flash layout (dual bank, SPI NAND with Realtek BBT remap) is not
# verified, and the stock OpenWrt ramips logic must never run here.
#

PART_NAME=firmware

platform_check_image() {
	echo "Sysupgrade is disabled on the TL-WR1502X bring-up build."
	return 1
}

platform_do_upgrade() {
	echo "Sysupgrade is disabled on the TL-WR1502X bring-up build."
	exit 1
}
