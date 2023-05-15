import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "Avant Garde"


regions = ['Trentino-Alto Adige/Südtirol', "Valle d'Aosta/Vallée d'Aoste", 'Veneto', 'Lombardia', 'Emilia-Romagna', 'Toscana', 'Friuli-Venezia Giulia', 'Liguria', 'Piemonte', 'Marche', 'Lazio', 'Umbria', 'Abruzzo', 'Sardegna', 'Puglia', 'Molise', 'Basilicata', 'Calabria', 'Sicilia', 'Campania']
print(len(regions))
df = pd.DataFrame([regions,[10+(i/2) for i in range(20)]]).transpose()
df.columns = ['region','quantity']

df = pd.read_csv("maps/Italy/region_NLLB.csv", delimiter='\t')
regions = list(df['region'])
print(regions)

texts = [f'{x:.3f}' for x in list(df['quantity']) if x]
df['text'] = texts
print(df)

#Download a geojson of the region geometries
gdf = gpd.read_file(filename=r'maps/Italy/limits_IT_municipalities.geojson')
gdf = gdf.dissolve(by='reg_name') #The geojson is too detailed, dissolve boundaries by reg_name attribute
gdf = gdf.reset_index()

#print(gdf.reg_name[~gdf.reg_name.isin(regions)])

gdf = pd.merge(left=gdf, right=df, how='left', left_on='reg_name', right_on='region')

ax = gdf.plot(
    column="quantity",
    legend=False,
    figsize=(5, 6),
    cmap='Greens',
    missing_kwds={'color': 'lightgrey'})

gdf.apply(lambda x: ax.annotate(text=x['text'], fontsize=9, xy=x.geometry.centroid.coords[0], ha='center'), axis=1)
ax.set_axis_off()
#gdf.plot()
plt.savefig('NLLB_Italy.pdf', format="pdf", bbox_inches="tight")
plt.show()