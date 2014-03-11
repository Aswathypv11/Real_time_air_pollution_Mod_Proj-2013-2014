**WIND_POWER_FORECASTING_MAP_FOR_COIMBATORE_REGION_OF_TAMIL_NADU**

* Problem statement

In Tamil Nadu, electricity is significantly relying of wind power based renewable energy source. If much wind is there, there will be minimal power cuts and vice versa. Especially second tier urban area like Coimbatore, this dependence is much visible and so one of the simple predicator of long power cuts is lack of adequate wind power in nearby wind park area for example. On the other hand operators of wind mills or power transmission sector if they know much early about the forecast of wind power in their area, they have much advantages in preparing for storing the surplus energy source or find alternatives in the situation of low wind power.

Predicting the wind power is problem of multi domain variables especially of meteorological predictions and engineering variables from the specific wind turbine used to generate the energy using wind power. One of the solution is to use the existing empirical observation data from similar wind mills or park to see how the variable are changing in the wind speed or meteorological domain of our area of interest (AOI).

* Computations

Wind power is third power of the wind speed. Based on this equation wind power can be calculated

w = 1/2 r A v3 where w is power, r is air density, A is the rotor area, and v is the wind speed.

r = (1.325 x P) / T where T is the temperature in Fahrenheit + 459.69 and P is the pressure in inches of Mercury adjusted for elevation

Based on //www.iowaenergycenter.org/wind-energy-manual/wind-and-wind-power/wind-speed-and-power/#sthash.4UBSpEQx.dpuf

* Algorithm

    Collect Numerical weather prediction (NWP) data of AOI. Mostly in the form of netCDF.
    Convert netCDF into geotiff for the wind speed variable band. While conversion made it into array object and execute the wind power calculation equations in the array.
    Convert the wind power calculated array into geotiff and visualize it in webGIS and implement query interface for common public user and operator user.
    Make a vector of urban locality and nearby wind park with points of wind turbine.
    Based on the use case query,
        if a common public is querying how much energy would be nearby wind park is producing, calculate a vector polygon of (wind park area) calculation using the geotiff (array) of wind power from number of wind turbine in the park.
        If a operator is asking for a specific turbine energy production, calculate point vector calculation using the the geotiff (array) of wind power
    Iterate the steps 1 to 4 for daily dynamic mapping of the wind power or based on the time frame availability of NWP data.

* After review presentation

the points raised by Rajan sir and fellow participants are

    Use the wind prediction map for establishing wind mills, so done site suitability analysis.
    the problem addresses already established wind mills, there were few GIS components involved as a solution, even though a visualization part is involved it is minimal use here, how the user going to be interested in dynamic entity of weather.

So the problem is restated as Wind power forecasting map: a lightweight, event detection subscribable web application, based on work of 

http://earth.nullschool.net/about.html
https://github.com/cambecc/air