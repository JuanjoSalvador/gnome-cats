.PHONY: install run \

install:
	flatpak-builder build-dir com.jotadevs.GnomeCats.json --force-clean

run:
	flatpak-builder --run build-dir com.jotadevs.GnomeCats.json runner.sh
