import os.path, glob
from qgis.core import QgsVectorLayer

layers=[]

for file in glob.glob('C:/users/bonny/downloads/EN259_EN587/*'):
    uri = "file:///" + file + "?type=csv&xField=lon&yField=lat&spatialIndex=no&subsetIndex=no&watchFile=no&crs=epsg:4326"
    vlayer = QgsVectorLayer(uri, os.path.basename(file), "delimitedtext")
    layers.append(vlayer)
    
QgsProject.instance().addMapLayers(layers)
