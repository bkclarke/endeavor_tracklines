from qgis.core import QgsVectorLayer, QgsProject

# Function to export layer as KML
def export_layer_as_kml(layer, output_path):
    kml_options = QgsVectorFileWriter.SaveVectorOptions()
    kml_options.driverName = "KML"
    kml_options.fileEncoding = "UTF-8"
    kml_options.layerName = layer.name()
    kml_options.actionOnExistingFile = QgsVectorFileWriter.CreateOrOverwriteFile
    kml_options.layerOptions = ["FORMAT=KML"]
    QgsVectorFileWriter.writeAsVectorFormatV2(layer, output_path, QgsProject.instance().transformContext(), kml_options)

# List of layers to export
layers_to_export = QgsProject.instance().mapLayers().values()

# Output folder for KML files
output_folder = "C:/Users/bonny/github/endeavor_tracklines/kml_files"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Export layers to KML
for layer in layers_to_export:
    output_file = os.path.join(output_folder, f"{layer.name()}.kml")
    export_layer_as_kml(layer, output_file)

print("Export completed successfully.")