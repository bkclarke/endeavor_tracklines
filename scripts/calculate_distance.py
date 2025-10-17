from geopy import distance

coord1 = (48.800,-68.600)
coord2 = (48.700,-62.633)

print(distance.geodesic(coord1, coord2, ellipsoid='WGS-84').miles)