import os
from qgis.core import QgsVectorLayer, QgsProject

# Function to import layers from GeoPackage
def import_layers_from_geopackage(geopackage_path):
    layer = QgsVectorLayer(geopackage_path, os.path.basename(geopackage_path), "ogr")
    if not layer.isValid():
        print(f"Error loading layer from {geopackage_path}")
        return
    QgsProject.instance().addMapLayer(layer)

# Directory containing GeoPackage files
directory = "C:/Users/bonny/github/endeavor_tracklines/points/individual_cruises"

# List all files in the directory
geopackage_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.gpkg')]

# Import layers from each GeoPackage file
for geopackage_file in geopackage_files:
    import_layers_from_geopackage(geopackage_file)

print("Import completed successfully.")