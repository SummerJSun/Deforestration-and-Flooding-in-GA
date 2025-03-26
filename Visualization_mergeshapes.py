import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import tempfile, os, shutil
from arcgis.gis import GIS


ga_counties = gpd.read_file("./Georgia_Counties/Georgia_Counties.shp")
combined_nlcd = pd.read_csv ("./Processed/Combined_NLCD.csv")


merged_gdf = ga_counties.merge(combined_nlcd,left_on = "NAMELSAD10", right_on = "County", how = "inner")
merged_gdf["Year"] = pd.to_datetime(merged_gdf["Year"], format="%Y")


# out_dir = tempfile.mkdtemp()
# out_shp = os.path.join(out_dir, "ga_landcover.shp")
# merged_gdf.to_file(out_shp)

# shp_zip = os.path.join(out_dir, "ga_landcover.zip")
# shutil.make_archive(os.path.splitext(shp_zip)[0], 'zip', out_dir)

# print(gdf['ShapeSTAre'].head())

# gis = GIS("https://www.arcgis.com", "production_sci4ga", "2i24U:EPWa2S7-c")

# item_properties = {
#     "title": "Georgia Land Cover (Time-enabled)",
#     "tags": "Georgia, land cover, counties",
#     "type": "Shapefile",
#     "description": "County-level land cover data over time"
# }

# shapefile_item = gis.content.add(item_properties, data=shp_zip)
# published_layer = shapefile_item.publish()

# print(published_layer.url)