.PHONY: install run \

install:
	flatpak-builder build-dir com.jotadevs.GnomeCats.json --force-clean

debug:
	flatpak-builder build-dir com.jotadevs.GnomeCats.json

run:
	flatpak-builder --run build-dir com.jotadevs.GnomeCats.json runner.sh
