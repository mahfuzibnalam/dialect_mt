import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "Avant Garde"


regions = ['Dhaka', 'Barisal', 'Jessore', 'Khulna', 'Kushtia']
df = pd.DataFrame([regions,[3+(i/2) for i in range(6)]]).transpose()
df.columns = ['region','quantity']

df = pd.read_csv("maps/Bangladesh/region_NLLB.csv", delimiter='\t')
regions = list(df['region'])
print(regions)

texts = [f'{x:.3f}' for x in list(df['quantity']) if x]
df['text'] = texts
print(df)

#Download a geojson of the region geometries
gdf = gpd.read_file(filename=r'maps/Bangladesh/bangladesh.geojson')
gdf = gdf.dissolve(by='NAME_2') #The geojson is too detailed, dissolve boundaries by NAME_2 attribute
gdf = gdf.reset_index()

# print(gdf.NAME_2[~gdf.NAME_2.isin(regions)])

gdf = pd.merge(left=gdf, right=df, how='left', left_on='NAME_2', right_on='region')

gdf.text = gdf.text.replace(np.nan,"")
ax = gdf.plot(
    column="quantity",
    legend=False,
    figsize=(5, 6),
    cmap='Greens',
    missing_kwds={'color': 'lightgrey'})

gdf.apply(lambda x: ax.annotate(text=x['text'], fontsize=9, xy=x.geometry.centroid.coords[0], ha='center'), axis=1)
ax.set_axis_off()
plt.savefig('NLLB_Bangladesh.pdf', format="pdf", bbox_inches="tight")
plt.show()