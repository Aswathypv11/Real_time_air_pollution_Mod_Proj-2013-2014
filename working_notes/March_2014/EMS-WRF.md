EMS WRF OF COIMBATORE REGION USING 4 DOMAINS :-  
Five simple steps required for the execution of EMS (Environmental modeling system) WRF.

Step 1: Create a computational domain with the Domain Wizard(DW) GUI
                 After the successful installation of EMS follow these steps, 

a) Start the DW by executing the command "dwiz" in terminal .
b) DW window should appear and gives you an opportunity to select from creating a new domain or  modifying existing domain. Current run directory also shown in this window.
c) Select "Create new Domain" and then "Continue" button.
d) "Name your domain challenge window" should appear and give name to your Domain. Name of domain should be in lower case characters without any spaces. Example : cbrwrf. This will create a new directory cbrwrf underneath wrfems/runs/cbrwrf.
e) Click on "Continue" button to move on to the "Horizontal Editor" window.
f) The Horizontal Editor window allows you to define a model domain by drawing a bounding
box on a map . You can edit the “Centerpoint Lon = 77.03 “and “Centerpoint Lat =11.03 “in Projection Options  to get our exact region of interest( Coimbatore).
g) On the right side of window, in Domain menu map section allows to change the “Scale = 12.5%” and “Center = Over 180 degrees longitude ” . In Projection Options (degrees) change the “Type = Lambert Conformal”. You can change the grid points in X & Y directions and resolution of geographic data in Grid options.
h) Click on “Update Map” , this will create a primary domain of our region.
i) Nested domain configuration can be achieved by selecting “Nests” menu. Here you can create new nested domains or edit/delete existing ones .
j) To create a new sub-domain, simply click on the “New” button to bring up the “New Nest” configuration window. Here Nest properties section allows you to edit the parent ID, Grid spacing ratio to parent, Geographic data resolution and Nest coordinates defines the coordinates of particular domain.
k) Created 4 domains to stimulate Coimbatore region with 1KM resolution.
l) Click on “Next” button to run the Localization in Run Preprocessors window. Localization serves to extract the terrestrial data over the area covered by the domain(s) from the large global files at the resolution(s) that you specified during your domain creation .
m) Click on “Localize Domain”.
n) After successful execution geogrid created 4 output files such as geo.em.d01.nc , geo.em.d02.nc , geo.em.d03.nc , geo.em.d04.nc. These files will reside in wrfems/runs/cbrwrf/static.
o) Click on “Next “ button and select each domain to visualize the outputs by clicking on “view in  panoply”. You should get a dataset window and double click on any dataset to display.
p) Click “ Exit ” when work done.
 

Step 2 : Prepare to run a simulation

a) A new domain “cbrwrf” was created and placed in a directory wrfems/runs/cbrwrf. From this directory you will run your simulation.
b) The EMS default configuration should be sufficient for running simulations . But sometimes it will change so there are two configuration files that you can review just to make sure everything is correct.
c)In the “conf/ems_run/run_ncpus.conf” configuration file, make sure that the number of CPUs is 
correctly specified for your computer. Check the following parameters :
 		REAL_NODECPUS = local:3
		WRFM_NODECPUS = local:3 
Where 3 represents the number of processors on your system. 
d) The other file that you might want to examine is “conf/ems_run/run_physics.conf”, which 
contains all the model physics settings for your simulation. If your grid spacing is less than 8 KM then change the parameter CU_PHYSICS = 1,0 to  CU_PHYSICS = 0,0 or  CU_PHYSICS = 5,0



Step 3 : Processing your Initialization data

a)This step assumes that you have an internet connection so you can access the initialization data 
sets . If you have good bandwidth, try running the following command in domain (Directory :wrfems/runs/cbrwrf): 
       		% ems_prep --dset gfs --length 24 
If you have limited bandwidth, then try running: 
		% ems_prep --dset gfsptiles --length 24 
Running either command causes the ems_prep routine to download and process the 
first 24 hours of forecast files from the most recent Global Forecast System (GFS) operational 
model run. These files will serve to provide your initial and boundary condition data for a 24 hour 
simulation (“--length 24”) .
b)For nested domains try the following command 
		% ems_prep –dset gfsptiles –domains 2,3,4 (for 3 nested domains)
Or 		% ems_prep –dset gfsptiles –domains 4  (this will automatically activate 2,3 domains too)
c) Domain 1 is the parent of all domains and is always included by default.
d) Check wrfems/runs/cbrwrf/wpsprd , all the WRF intermediate files are located here.



Step 4 : Running your Simulation 

a) Change your directory to wrfems/runs/cbrwrf , and run the following command
		% ems_run
b) For nested domains , run the command 
		% ems_run –domains 2,3,4
c) Output files will reside in wrfems/runs/cbrwrf/wrfprd 



Step 5 : Processing the model output files 

a) After successful simulation you will get the WRF output files .These data should be in netCDF format can be viewed using ncview command. So try the command
		% ncview <netCDF file>

Ex:  		% ncview wrfbdy_d01

