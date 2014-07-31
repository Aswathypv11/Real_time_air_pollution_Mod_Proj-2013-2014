""EMS -WRF Simulation over Coimbatore 

Simulation 1:

""cd home/hoopoe/wrfems/wrfems/runs/cbe_h1

""Modify parameters in cbe_h1/conf/ems_run/run_physics.conf

""Parameters are CUMULUS , MICROPHYSICS , PLANETARY BOUNDARY LAYER ,  SURFACE LAYER, LAND SURFACE PHYSICS Schemes
		
		CU_PHYSICS = 1,5,5,5 ( Kain-Fritsch(1), grell-3D(5))
    MP_PHYSICS = 2,2,2,2 (Lin)
		BL-PBL-PHYSICS = 2,2,2,2 (MYJ)
		SF_SFCLAY_PHYSICS = 4 (QNSE)
		SF_SURFACE_PHYSICS = 2,2,2,2 (Noah)

""Load fnl files in grib folder

""run 
ems_prep –dset fnl –date 20140301 –local –analysis –cycle 00 –domians 2,3,4 –length 24

""finally run 
ems_run –domains 2,3,4
"" Simulation time is 1 hour 38 minutes 45 seconds

Simulation 2:

	CU_PHYSICS = 1,1,1,1   ( Kain-Fritsch(1))
	MP_PHYSICS = 2,2,2,2   (Lin)
	BL-PBL-PHYSICS = 2,2,2,2 (MYJ)
	SF_SFCLAY_PHYSICS = 4  (QNSE)
	SF_SURFACE_PHYSICS = 2,2,2,2 (Noah)
	
"" 	
Simulation time is 1 hour 38 minutes 47 seconds
Simulation 3:
	
	CU_PHYSICS = 1,1,1,1   ( Kain-Fritsch (1))
     	MP_PHYSICS = 2,2,2,2   (Lin)
	BL-PBL-PHYSICS = 7,7,7,7 (ACM2)
	SF_SFCLAY_PHYSICS = 7 (Pleim)
	SF_SURFACE_PHYSICS = 7,7,7,7 (Pleim)
""simulation time is 1 hour  42 minute 57 seconds.

SIMULATION 4:


	CU_PHYSICS = 1,1,1,1   ( Kain-Fritsch (1))
     	MP_PHYSICS = 2,2,2,2   (Lin)
	BL-PBL-PHYSICS =1,1,1,1  (YSU)
	SF_SFCLAY_PHYSICS = 11 (MM5)
	SF_SURFACE_PHYSICS = 2,2,2,2 (Noah)

Simulation time is 1 hour 48 minutes 38 seconds
