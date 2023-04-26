import cdsapi
import os
import subprocess
import numpy as np
from . import _utils

def download_month(era5_varname, dp_output,
                   year, month, 
                   era5_server = 'reanalysis-era5-single-levels'):
    """
    Download global ERA5 data for a single month and year on an hourly frequency.

    Args:
        era5_varname (str)   : Variable name to download from ERA5.
        dp_output (str)      : Output directory
        year (int)           : Download year
        month (int)          : Download month
        era5_server (str)    : Name of era5 download server

    Returns:
        Saves downloaded file to dp_output. Filename is automatic.
        Returns new filename.
    """
    # Check inputs
    if type(month) is not str:
        month = f'{month:02d}'
    if type(year) is not str:
        year = f'{year}'
    
    # Make output filename
    fp_out = f'{era5_varname}_y{year}m{month}.nc' 
    fp_out = os.path.join(dp_output, fp_out)
    
    # Print status update and filename
    print("=========================================================")
    print("Downloading y{year}m{month}".format(year=year, month=month))
    print(f'Output filename: {fp_out}')
        
    # Make parameter dict and pass to cdsapi client
    param_dict = _utils.make_cds_dict(era5_varname, year, month)
    c = cdsapi.Client()
    c.retrieve(era5_server, param_dict, fp_out) 
    
    return fp_out

def download_multiple_months(era5_varname, dp_output,
                             year_start, year_end, 
                             month = None,
                             apply_func = None,
                             func_name = 'analysis',
                             delete_after_func = False,
                             era5_server = 'reanalysis-era5-single-levels'):
    """
    Download global ERA5 data for a multiple months and years on an hourly frequency.
    Data is downloaded and saved into monthly files.
    
    There is an additional option of applying a functions to the resulting monthly data
    using the apply_func argument. For example, if you want to resample from hourly
    to daily data. Must take a single argument as input ( filename ) and output a 
    single xarray dataset. When passed, this function will be applied and the r
    esulting dataset will be saved to a new file with suffic func_name. 

    Args:
        era5_varname (str)   : Variable name to download from ERA5.
        dp_output (str)      : Output directory
        year_start (int)     : Start year for download.
        year_end (int)       : End year for download (same as start for one year)
        month (int)          : Download month. Default all months.
        apply_func (function): A function to apply to the data downloaded at
                               each monthly iteration. Default None.
        func_name (str)      : Modifier for output file. Dataset that is output by
                               apply_func() will be saved to a file with this suffix.
                               Default 'analysis'.
        delete_after_func (bool) : If true, delete the hourly downloaded file after
                                   apply_func is applied.
        era5_server (str)    : Name of era5 download server

    Returns:
        Saves downloaded file to dp_output. Filename is automatic.
        Returns new filename.
    """
    
    # Make list inputs for year and months
    year_list = np.arange(year_start, year_end+1, dtype=int)
    if month is None:
        month = np.arange(1,13, dtype=int)
        
    month = [f'{yy:02d}' for yy in month]
    year_list = [f'{yy}' for yy in year_list]

    # Make parameter dict and pass to cdsapi client
    c = cdsapi.Client()
    
    # Loop over years and months
    for yy in year_list:
        for mm in month:
            
            # Download single month for this loop iteration
            print(era5_varname, dp_output, yy, mm, era5_server)
            fp_ii = download_month(era5_varname, dp_output, yy, mm,
                                   era5_server)
            
            # Apply function if one was provided
            if apply_func is not None:
                apply_out = apply_func( fp_ii )
                fp_ii_func = f'{fp_ii[:-3]}_{func_name}.nc' 
                apply_out.to_netcdf(fp_ii_func)
                
            # Delete original downloaded file if specified
            if delete_after_func:
                os.remove(fp_ii)
    
    return