.PHONY: install run \

install:
	flatpak-builder build com.jotadevs.GnomeCats.json --force-clean

debug:
	flatpak-builder build com.jotadevs.GnomeCats.json

run:
	flatpak-builder --run build com.jotadevs.GnomeCats.json /app/share/gnome-cats/__main__.py
