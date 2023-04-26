import cdsapi
import os
import subprocess
import numpy as np
from . import _utils

def download_month(era5_varname, dp_output,
                   year, month, lon_bnds = None, lat_bnds = None,
                   verbose = True, 
                   era5_server = 'reanalysis-era5-single-levels'):
    """
    Download global ERA5 data for a single month and year on an hourly frequency.

    Args:
        era5_varname (str)   : Variable name to download from ERA5.
        dp_output (str)      : Output directory
        year (int)           : Download year
        month (int)          : Download month
        lon_bnds (tuple)     : Longitude bounds of download (default global)
        lat_bnds (tuple)     : Latitude bounds of download (default global)
        verbose (bool)       : If true, print stuff
        era5_server (str)    : Name of era5 download server

    Returns:
        Saves downloaded file to dp_output. Filename is automatic.
        Returns new filename.
    """
    c = cdsapi.Client()
    
    # Make output filename
    fp_out = f'{era5_varname}_y{year}m{month:02d}.nc' 
    fp_out = os.path.join(dp_output, fp_out)
    
    if verbose:
        print("=========================================================")
        print("Downloading y{year}m{month:02d}".format(year=year, month=month))
        print(f'Output filename: {fp_out}')
        
    param_dict = _utils.make_cds_dict(era5_varname, year, month)
    
    if lat_bnds is not None and lon_bnds is not None:
        raise NotImplemented()

    c.retrieve(
        era5_server,
        param_dict,
        fp_out) 
    
    return fp_out