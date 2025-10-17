import processing

# Input with actual layer name
point_layer_path = "C:/Users/bonny/github/endeavor_tracklines/points/EN711_EN736_points.gpkg|layername=EN711_EN736_points"

# Output: geopackage file + explicit layer name
output_line_layer_path = "C:/Users/bonny/github/endeavor_tracklines/lines/ENEN711_EN736_lines.gpkg"

processing.run("qgis:pointstopath", {
    'INPUT': point_layer_path,
    'ORDER_FIELD': 'fid',
    'GROUP_FIELD': 'EN711',
    'DATE_FORMAT': '',
    'OUTPUT': output_line_layer_path
})

# Load output
line_layer = QgsVectorLayer(output_line_layer_path, "line_layer", "ogr")
if not line_layer.isValid():
    print("Line layer failed to load!")
else:
    QgsProject.instance().addMapLayer(line_layer)