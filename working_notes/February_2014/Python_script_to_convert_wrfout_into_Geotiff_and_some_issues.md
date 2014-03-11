**Python_script_to_convert_wrfout_into_Geotiff_and_some_issues**

I want to visualize WRF output in GIS platform so that I would have an extra hand in interactive visualization and spatial analysis out of it. I used below python script (modified from http://lists.osgeo.org/pipermail/gdal-dev/2013-November/037602.html and http://geoexamples.blogspot.in/2013/09/reading-wrf-netcdf-files-with-gdal.html) to convert netcdf into Geotiff format. How ever the given scripts in those links are throwing error while convert eWRF netcdf output, saying there are multiple bands in specific variables say for example U10. I slightly changed those code to collect one band out of 24 band in U10 (In some variables the band number goes around 650, like P) and converted into geotiff without error and can visualise it in GIS. Below script is modified version.

```
from osgeo import gdal
from osgeo import osr
import numpy
import numpy.ma as ma
datafile = 'wrfout_d01_2008-04-28_00:00:00'
proj_out = osr.SpatialReference()
proj_out.SetMercator(0.0, 115.02, 0.98931892612652, 0.0, 0.0)
ds_in = gdal.Open(datafile)
subdatasets = ds_in.GetSubDatasets()
variables = []
for subdataset in subdatasets:
     variables.append(subdataset[1].split(" ")[1])
ds_lon = gdal.Open('NETCDF:"wrfout_d01_2008-04-28_00:00:00":XLONG')
ds_lat = gdal.Open('NETCDF:"wrfout_d01_2008-04-28_00:00:00":XLAT')
longs = ds_lon.GetRasterBand(1).ReadAsArray()
lats = ds_lat.GetRasterBand(1).ReadAsArray()
ds_lon = None
ds_lat = None
proj_gcp = osr.SpatialReference()
proj_gcp.ImportFromEPSG(4326)
transf = osr.CoordinateTransformation(proj_gcp, proj_out)
ul = transf.TransformPoint(float(longs[0][0]), float(lats[0][0]))
lr = transf.TransformPoint(float(longs[len(longs)-1][len(longs[0])-1]),
float(lats[len(longs)-1][len(longs[0])-1]))
ur = transf.TransformPoint(float(longs[0][len(longs[0])-1]),
float(lats[0][len(longs[0])-1]))
ll = transf.TransformPoint(float(longs[len(longs)-1][0]),
float(lats[len(longs)-1][0]))
gt0 = ul[0]
gt1 = (ur[0] - gt0) / len(longs[0])
gt2 = (lr[0] - gt0 - gt1*len(longs[0])) / len(longs)
gt3 = ul[1]
gt5 = (ll[1] - gt3) / len(longs)
gt4 = (lr[1] - gt3 - gt5*len(longs) ) / len(longs[0])
gt = (gt0,gt1,gt2,gt3,gt4,gt5)
ds_u10 = gdal.Open('NETCDF:"'+datafile+'":U10')
i=23
num_bands = ds_u10.RasterCount
x_size = ds_u10.RasterXSize
y_size = ds_u10.RasterYSize
ds_p_b = ds_u10.GetRasterBand(num_bands - i).ReadAsArray()
driver = gdal.GetDriverByName( 'GTiff' )
ds_out = driver.Create( 'u10.tiff', x_size, y_size, 1, gdal.GDT_Float32 )
ds_out.SetGeoTransform( gt )
ds_out.SetProjection(proj_out.ExportToWkt())
ds_out.GetRasterBand(1).WriteArray( ds_p_b )
```