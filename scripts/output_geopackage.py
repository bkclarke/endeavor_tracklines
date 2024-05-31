# Import necessary QGIS modules
from qgis.core import QgsVectorLayer, QgsVectorFileWriter

layers = QgsProject.instance().mapLayers().values()

for layer in layers:
    point_layer_name = layer.name()
    print(point_layer_name)

    # Define the path to the GeoPackage file
    output_gpkg = "C:/Users/bonny/github/endeavor_tracklines/ %s.gpkg" % point_layer_name

    print(output_gpkg)

    # Define the name of the layer to export
    layer_name = point_layer_name

    # Check if the layer is valid
    if not layer.isValid():
        print("Layer loading failed!")
        exit()

    # Export the layer to GeoPackage
    options = QgsVectorFileWriter.SaveVectorOptions()
    options.actionOnExistingFile = QgsVectorFileWriter.CreateOrOverwriteLayer
    QgsVectorFileWriter.writeAsVectorFormat(layer, output_gpkg, options)

    print("Layer exported to GeoPackage successfully.")