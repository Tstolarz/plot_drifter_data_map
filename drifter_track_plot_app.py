import xarray as xr
import pandas as pd
import folium
from folium.plugins import TimestampedGeoJson
import sys
import os

# Load the drifter data from a NetCDF file
def load_drifter_data(netcdf_file):
    # Open the dataset
    ds = xr.open_dataset(netcdf_file)
    # Extract latitude, longitude, and time
    lats = ds['lat'].values
    lons = ds['lon'].values
    times = pd.to_datetime(ds['time'].values)
    return lons, lats, times

# Extract the drifter name from the file name
def get_drifter_name(file_path):
    file_name = os.path.basename(file_path)
    drifter_name = file_name.split("_")[0]
    output_dir = os.path.dirname(file_path)
    return drifter_name, output_dir

# Create the Folium map with a time slider
# Create the Folium map with a time slider
def create_interactive_map(datasets, drifter_names):
    # Create a base map centered around the first lat/lon of the first dataset
    m = folium.Map(location=[datasets[0][1][0], datasets[0][0][0]], zoom_start=10, tiles="OpenStreetMap")
    
    colors = ['blue', 'red', 'green', 'orange', 'purple']  # Add more colors as needed
    
    for i, (lons, lats, times) in enumerate(datasets):
        # Create a dataframe for easier manipulation
        df = pd.DataFrame({
            'Longitude': lons,
            'Latitude': lats,
            'Time': times
        })
        
        # Generate GeoJSON features for each point in time
        features = []
        for _, row in df.iterrows():
            feature = {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [row['Longitude'], row['Latitude']],
                },
                'properties': {
                    'time': row['Time'].isoformat(),
                    'style': {'color': colors[i % len(colors)],
                              'fillColor': colors[i % len(colors)],
                              'fillOpacity': 0.7,
                              'radius': 6
                    },
                    'icon': 'circle',
                    'popup': f'Drifter: {drifter_names[i]}<br>Time: {row["Time"]}<br>Lat: {row["Latitude"]}<br>Lon: {row["Longitude"]}',
                }
            }
            features.append(feature)
        
        # Create a separate TimestampedGeoJson object for each drifter
        timestamped_geojson = TimestampedGeoJson(
            {'type': 'FeatureCollection', 'features': features},
            period='PT1H',
            add_last_point=True,
            auto_play=False,
            loop=False,
            max_speed=1,
            loop_button=True,
            date_options='YYYY-MM-DD HH:mm:ss',
            time_slider_drag_update=True
        )
        
        # Add the TimestampedGeoJson to the map
        timestamped_geojson.add_to(m)
        # Create output dir
        output_dir = os.path.join(nc_dir, f'{drifter_names[i]}_drifter_tracks')
        # Save the map to an HTML file
        m.save(f"{output_dir}.html")
    return m


if __name__ == "__main__":
    # Get the list of NetCDF files from command line arguments
    netcdf_files = sys.argv[1:]
    
    # Load the drifter data for each file
    datasets = []
    drifter_names = []
    for file in netcdf_files:
        lons, lats, times = load_drifter_data(file)
        datasets.append((lons, lats, times))
        drifter_name, nc_dir = get_drifter_name(file)
        drifter_names.append(drifter_name)
    
    # Create the interactive map
    m = create_interactive_map(datasets, drifter_names)
    
    # Create output dir
    nc_dir = os.path.join(nc_dir, 'drifter_tracks')
    # Save the map to an HTML file
    m.save(f"{nc_dir}.html")