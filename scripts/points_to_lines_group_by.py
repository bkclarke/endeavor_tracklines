import processing

# Replace 'point_layer_path' with the path to your point layer
point_layer_path = "C:/Users/bonny/github/endeavor_tracklines/points/EN674_EN693_points.gpkg"

# Replace 'output_line_layer_path' with the desired path for the output line layer
output_line_layer_path = "C:/Users/bonny/github/endeavor_tracklines/lines/EN674_EN693_points.gpkg"

# Run the Points to Path algorithm
processing.run("qgis:pointstopath", {
    'INPUT': point_layer_path,
    'ORDER_FIELD': '',
    'GROUP_FIELD': 'cruise',
    'DATE_FORMAT': '',
    'OUTPUT': output_line_layer_path
})

# Load the output line layer
line_layer = QgsVectorLayer(output_line_layer_path, "line_layer", "ogr")

# Check if the layer loaded successfully
if not line_layer.isValid():
    print("Line layer failed to load!")
else:
    # Add the line layer to the map
    QgsProject.instance().addMapLayer(line_layer)