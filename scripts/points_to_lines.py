from qgis.core import QgsProject, QgsVectorLayer, QgsFeature, QgsField, QgsGeometry, QgsFeatureRequest
from qgis.PyQt.QtCore import QVariant

layers = QgsProject.instance().mapLayers().values()

for layer in layers:
    # Define the name of the existing point layer
    point_layer_name = layer.name()
    line_layer_name = point_layer_name[0:10]

    # Find the existing point layer by name
    point_layer = QgsProject.instance().mapLayersByName(point_layer_name)[0]

    # Check if the layer is valid
    if not layer.isValid():
        print("Layer loading failed!")
        exit()

    # Create a memory layer to store the lines
    crs = layer.crs()
    line_layer = QgsVectorLayer("LineString?crs=" + crs.toWkt(), line_layer_name , "memory")
    provider = line_layer.dataProvider()
    fields = layer.fields()
    provider.addAttributes(fields.toList())
    line_layer.updateFields()

    # Create an empty list to store the features for the line layer
    lines = []

    # Iterate through each feature in the point layer
    for point_feature in layer.getFeatures():
        # Extract the geometry of the point feature
        point_geom = point_feature.geometry()
        
        # Append the point geometry to the list of lines
        lines.append(point_geom.asPoint())
        
    # Create a new line feature using the points
    line_geom = QgsGeometry.fromPolylineXY(lines)
    line_feature = QgsFeature()
    line_feature.setGeometry(line_geom)
    line_feature.setAttributes(point_feature.attributes())

    # Add the new line feature to the memory layer
    provider.addFeatures([line_feature])
    line_layer.updateExtents()

    # Add the memory layer to the map
    QgsProject.instance().addMapLayer(line_layer)

    print("Points converted to lines successfully!")