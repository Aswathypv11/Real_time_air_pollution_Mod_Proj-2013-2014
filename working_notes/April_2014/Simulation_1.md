#### EMS wRF modelling over Coimbatore region by modifying some physical parameters


1.*cd home/hoopoe/wrfems/wrfems/runs/cbe_h1* 
...Modify parameters in cbe_h1/conf/ems_run/run_physics.conf_
''Parameters are CUMULUS , MICROPHYSICS , PLANETARY BOUNDARY LAYER ,  SURFACE LAYER, LAND SURFACE PHYSICS Schemes
		
		CU_PHYSICS = 1,5,5,5 ( Kain-Fritsch (1), grell-3D(5))
    MP_PHYSICS = 2,2,2,2 (Lin)
		BL-PBL-PHYSICS = 2,2,2,2 (MYJ)
		SF_SFCLAY_PHYSICS = 4 (QNSE)
		SF_SURFACE_PHYSICS = 2,2,2,2 (Noah)

''Simulation time is 1 hour 38 minutes 45 seconds

''Namelist.wps :

&share
 wrf_core                   = 'ARW'
 max_dom                    = 4
 start_date                 = '2014-03-01_00:00:00', '2014-03-01_00:00:00', '2014-03-01_00:00:00', '2014-03-01_00:00:00'
 end_date                   = '2014-03-01_06:00:00', '2014-03-01_00:00:00', '2014-03-01_00:00:00', '2014-03-01_00:00:00'
 interval_seconds           = 21600
 io_form_geogrid            = 2
 opt_output_from_geogrid_path = '/home/hoopoe/wrfems/wrfems/runs/cbe_h1/static/'
 debug_level                = 0
/

&geogrid
 parent_id                  = 1, 1, 2, 3
 parent_grid_ratio          = 1, 3, 3, 3
 i_parent_start             = 1, 27, 16, 26
 j_parent_start             = 1, 6, 6, 20
 e_we                       = 90, 76, 109, 175
 e_sn                       = 85, 67, 88, 148
 geog_data_res              = '10m', '5m', '30s', '30s'
 dx                         = 27000
 dy                         = 27000
 map_proj                   = 'lambert'
 ref_lat                    = 18.363
 ref_lon                    = 78.925
 truelat1                   = 18.363
 truelat2                   = 18.363
 stand_lon                  = 78.925
 ref_x                      = 45
 ref_y                      = 42.5
 geog_data_path             = '/home/hoopoe/wrfems/wrfems/data/geog'
 opt_geogrid_tbl_path       = '/home/hoopoe/wrfems/wrfems/runs/cbe_h1/static/'
/

&ungrib
 out_format                 = 'WPS'
 prefix                     = 'FILE'
/

&metgrid
 fg_name                    = FNL
 io_form_metgrid            = 2
 opt_output_from_metgrid_path = '/home/hoopoe/wrfems/wrfems/runs/cbe_h1/wpsprd'
 opt_metgrid_tbl_path       = '/home/hoopoe/wrfems/wrfems/runs/cbe_h1'
 process_only_bdy           =  
/

&mod_levs
 press_pa                   = 201300, 200100, 100000, 95000, 90000, 85000, 80000, 75000, 70000, 65000, 60000, 55000, 50000, 45000, 40000, 35000, 30000, 25000, 20000, 15000, 10000, 5000, 1000
/

&domain_wizard
 grib_data_path             = 'null'
 grib_vtable                = 'Vtable.GFS'
 dwiz_center_over_gmt       = false
 dwiz_desc                  = cbe_h1
 dwiz_gridpt_dist_km        = 27.0
 dwiz_latlon_linecolor      = -8355712
 dwiz_latlon_space_in_deg   = 10
 dwiz_map_horiz_scrollbar_pos = 0
 dwiz_map_scale_pct         = 12.5
 dwiz_map_vert_scrollbar_pos = 0
 dwiz_mpi_command           = 
 dwiz_name                  = cbe_h1
 dwiz_show_political        = true
 dwiz_user_rect_x1          = 330
 dwiz_user_rect_x2          = 558
 dwiz_user_rect_y1          = 305
 dwiz_user_rect_y2          = 501
 dwiz_modis                 = false
/

''Namelist.real :

&time_control
 start_year                 = 2014, 2014, 2014, 2014
 start_month                = 03, 03, 03, 03
 start_day                  = 01, 01, 01, 01
 start_hour                 = 00, 00, 00, 00
 start_minute               = 00, 00, 00, 00
 start_second               = 00, 00, 00, 00
 end_year                   = 2014, 2014, 2014, 2014
 end_month                  = 03, 03, 03, 03
 end_day                    = 01, 01, 01, 01
 end_hour                   = 06, 06, 06, 06
 end_minute                 = 00, 00, 00, 00
 end_second                 = 00, 00, 00, 00
 interval_seconds           = 21600
 input_from_file            = T, T, T, T
 history_interval           = 60, 60, 60, 60
 history_outname            = "wrfout_d<domain>_<date>"
 frames_per_outfile         = 1, 1, 1, 1
 io_form_history            = 2
 io_form_input              = 2
 io_form_restart            = 2
 io_form_boundary           = 2
 io_form_auxinput2          = 2
 restart                    = F
 restart_interval           = 720
 auxhist1_outname           = "auxhist1_d<domain>_<date>"
 auxhist1_interval          = 0, 0, 0, 0
 frames_per_auxhist1        = 1, 1, 1, 1
 io_form_auxhist1           = 2
 auxhist2_outname           = "auxhist2_d<domain>_<date>"
 auxhist2_interval          = 0, 0, 0, 0
 output_diagnostics         = 0
 auxhist3_outname           = "wrfxtrm_d<domain>_<date>"
 auxhist3_interval          = 0, 0, 0, 0
 frames_per_auxhist2        = 1, 1, 1, 1
 io_form_auxhist2           = 2
 auxinput4_inname           = "wrflowinp_d<domain>"
 auxinput4_interval         = 360, 360, 360, 360
 io_form_auxinput4          = 2
 fine_input_stream          = 0, 2, 2, 2
 adjust_output_times        = T
 reset_simulation_start     = F
 cycling                    = F
 diag_print                 = 0
 debug_level                = 0
/

&domains
 time_step                  = 162
 time_step_fract_num        = 0
 time_step_fract_den        = 10
 time_step_dfi              = 60
 max_dom                    = 4
 s_we                       = 1, 1, 1, 1
 e_we                       = 90, 76, 109, 175
 s_sn                       = 1, 1, 1, 1
 e_sn                       = 85, 67, 88, 148
 s_vert                     = 1, 1, 1, 1
 e_vert                     = 45, 45, 45, 45
 dx                         = 27000.0000, 9000.0000, 3000.0000, 1000.0000
 dy                         = 27000.0000, 9000.0000, 3000.0000, 1000.0000
 grid_id                    = 1, 2, 3, 4
 parent_id                  = 1, 1, 2, 3
 i_parent_start             = 1, 27, 16, 26
 j_parent_start             = 1, 6, 6, 20
 parent_grid_ratio          = 1, 3, 3, 3
 parent_time_step_ratio     = 1, 3, 3, 3
 feedback                   = 0
 smooth_option              = 0
 grid_allowed               = T, T, T, T
 max_dz                     = 1000.
 numtiles                   = 1
 nproc_x                    = -1
 nproc_y                    = -1
 num_metgrid_soil_levels    = 4
 num_metgrid_levels         = 27
 interp_type                = 2
 extrap_type                = 2
 t_extrap_type              = 2
 use_levels_below_ground    = T
 use_surface                = T
 lagrange_order             = 1
 zap_close_levels           = 500
 lowest_lev_from_sfc        = F
 force_sfc_in_vinterp       = 1
 sfcp_to_sfcp               = F
 smooth_cg_topo             = F
 use_tavg_for_tsk           = F
 aggregate_lu               = F
 rh2qv_wrt_liquid           = T
 rh2qv_method               = 1
 p_top_requested            = 5000
 vert_refine_fact           = 1
 use_adaptive_time_step     = F
/

&dfi_control
 dfi_opt                    = 0
/

&physics
 cu_physics                 = 1, 1, 1, 1
 cudt                       = 5, 5, 5, 5
 kfeta_trigger              = 1
 cugd_avedx                 = 1
 ishallow                   = 0
 mp_physics                 = 2, 2, 2, 2
 mp_zero_out                = 0
 mp_zero_out_thresh         = 1.e-8
 mp_tend_lim                = 10.
 no_mp_heating              = 0
 do_radar_ref               = 1
 shcu_physics               = 0, 0, 0, 0
 bl_pbl_physics             = 1, 1, 1, 1
 bldt                       = 0, 0, 0, 0
 topo_wind                  = 0, 0, 0, 0
 mfshconv                   = 0
 sf_sfclay_physics          = 11, 11, 11, 11
 isfflx                     = 1
 isftcflx                   = 0
 sf_surface_physics         = 2, 2, 2, 2
 num_land_cat               = 24
 num_soil_cat               = 16
 num_soil_layers            = 4
 surface_input_source       = 1
 rdmaxalb                   = T
 rdlai2d                    = F
 tmn_update                 = 0
 sf_urban_physics           = 0, 0, 0, 0
 ra_lw_physics              = 1, 1, 1, 1
 ra_sw_physics              = 1, 1, 1, 1
 radt                       = 6, 6, 6, 6
 ra_call_offset             = 0
 swrad_scat                 = 1
 slope_rad                  = 0, 0, 0, 0
 topo_shading               = 0, 0, 0, 0
 icloud                     = 1
 co2tf                      = 1
 sst_skin                   = 1
 sst_update                 = 0
 seaice_threshold           = 271
 fractional_seaice          = 0
 prec_acc_dt                = 0, 0., 0., 0.
 bucket_mm                  = -1
 bucket_j                   = -1
 windturbines_spec          = "none"
 td_turbgridid              = -1
/

&noah_mp
/

&dynamics
 non_hydrostatic            = T, T, T, T
 gwd_opt                    = 0
 rk_ord                     = 3
 h_mom_adv_order            = 5, 5, 5, 5
 h_sca_adv_order            = 5, 5, 5, 5
 v_mom_adv_order            = 3, 3, 3, 3
 v_sca_adv_order            = 3, 3, 3, 3
 moist_adv_opt              = 1, 1, 1, 1
 moist_adv_dfi_opt          = 0
 scalar_adv_opt             = 1, 1, 1, 1
 momentum_adv_opt           = 1, 1, 1, 1
 chem_adv_opt               = 1, 1, 1, 1
 tke_adv_opt                = 1, 1, 1, 1
 diff_opt                   = 1
 km_opt                     = 4
 km_opt_dfi                 = 1
 w_damping                  = 1
 diff_6th_opt               = 2, 2, 2, 2
 diff_6th_factor            = 0.12, 0.12, 0.12, 0.12
 damp_opt                   = 0
 zdamp                      = 5000., 5000., 5000., 5000.
 dampcoef                   = 0.2, 0.2, 0.2, 0.2
 khdif                      = 0, 0, 0, 0
 kvdif                      = 0, 0, 0, 0
 time_step_sound            = 0, 0, 0, 0
 do_avgflx_em               = 0, 0, 0, 0
 do_avgflx_cugd             = 0, 0, 0, 0
 smdiv                      = 0.1, 0.1, 0.1, 0.1
 emdiv                      = 0.01, 0.01, 0.01, 0.01
 epssm                      = 0.1, 0.1, 0.1, 0.1
 top_lid                    = F, F, F, F
 mix_isotropic              = 0, 0, 0, 0
 mix_upper_bound            = 0.1, 0.1, 0.1, 0.1
 rotated_pole               = F
 tke_upper_bound            = 1000., 1000., 1000., 1000.
 sfs_opt                    = 0, 0, 0, 0
 m_opt                      = 0, 0, 0, 0
 iso_temp                   = 0.
 tracer_opt                 = 0, 0, 0, 0
 tracer_adv_opt             = 0, 0, 0, 0
/

&scm
 scm_force                  = 0
 scm_force_dx               = 4000.
 num_force_layers           = 8
 scm_lu_index               = 2
 scm_isltyp                 = 4
 scm_vegfra                 = 0.5
 scm_canwat                 = 0.0
 scm_lat                    = 37.600
 scm_lon                    = -96.700
 scm_th_adv                 = .true.
 scm_wind_adv               = .true.
 scm_qv_adv                 = .true.
 scm_vert_adv               = .true.
/

&fdda
 grid_fdda                  = 0
/

&tc
 insert_bogus_storm         = F
 remove_storm               = F
 num_storm                  = 1
 latc_loc                   = -999.
 lonc_loc                   = -999.
 vmax_meters_per_second     = -999.
 rmax                       = -999.
 vmax_ratio                 = -999.
/

&fire
/

&bdy_control
 spec_bdy_width             = 5
 spec_zone                  = 1
 relax_zone                 = 4
 spec_exp                   = 0
 specified                  = T, F, F, F
 nested                     = F, T, T, T
/

&grib2
/

&namelist_quilt
 nio_tasks_per_group        = 0
 nio_groups                 = 1
/
