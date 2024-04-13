# Kartdata brukt

## Kommuner og fylker

Nedlastet fra kartverket:
* `Basisdata_0000_Norge_25833_Fylker_GeoJSON.geojson`
* `Basisdata_0000_Norge_25833_Kommuner_GeoJSON.geojson`

Kjør `python data-preprocess.py` for å generere filer.

## Kart over hele Norge

Nedlastet fra [Natural Earth](https://www.naturalearthdata.com/):
* `ne_10m_admin_0_countries_lakes.zip`

Prosess:
```shell
cat output.geojson | jq '.features[] | select(.properties["ADMIN"] == "Norway") | .geometry' > norway.geojson
OGR_ENABLE_PARTIAL_REPROJECTION=TRUE ogr2ogr -f "GeoJSON" -skipfailures -t_srs EPSG:32633 output.geojson ne_10m_admin_0_countries_lakes.shp 
```