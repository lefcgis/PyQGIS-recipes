#Importar KMZ
processing.run("kmltools:importkml", {'Input':'C:\\Users\\OLIMPO\\Downloads\\Caracterización - Hector (Facilidad).kmz','PointOutputLayer':'ogr:dbname=\'C:/Users/OLIMPO/Downloads/runtusapa2.gpkg\' table="puntos2" (geom)','LineOutputLayer':'TEMPORARY_OUTPUT','PolygonOutputLayer':'TEMPORARY_OUTPUT'})
