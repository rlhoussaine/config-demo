import xarray as xr
import numpy as np
import pandas as pd

# Créer des dimensions
time = pd.date_range("2023-01-01", periods=10, freq="D")
lat = np.linspace(-90, 90, 180)
lon = np.linspace(-180, 180, 360)

# Créer des données fictives
data = 20 + 10 * np.sin(np.radians(lat[:, np.newaxis])) * np.cos(np.radians(lon[np.newaxis, :]))
data = data[np.newaxis, :, :] * np.random.rand(len(time), 1, 1)

# Créer un DataArray
temperature = xr.DataArray(
    data,
    coords=[time, lat, lon],
    dims=["time", "lat", "lon"],
    name="temperature",
    attrs={"units": "degrees Celsius"}
)

# Créer un Dataset
dataset = xr.Dataset({"temperature": temperature})

# Enregistrer le Dataset dans un fichier NetCDF
dataset.to_netcdf("temperature_data.nc")

print("Fichier NetCDF créé avec succès !")
