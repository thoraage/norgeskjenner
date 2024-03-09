import json
import os

with open("Basisdata_0000_Norge_25833_Kommuner_GeoJSON.geojson", "r") as f:
    data = json.load(f)

os.mkdir("municipalities")
municipality_feats = data["Kommune"]["features"]
for index, feat in enumerate(municipality_feats):
    name = feat["properties"]["kommunenavn"]
    print(index, name)
    with open(f"municipalities/{index}.json", "w") as f:
        json.dump({"name": name, "geometry": feat["geometry"]}, f)
