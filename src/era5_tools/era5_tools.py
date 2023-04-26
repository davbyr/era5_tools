import cdsapi
import os
import subprocess
import numpy as np

def download_month(era5_varname, dp_output,
                   year, month, lon_bnds = None, lat_bnds = None,
                   verbose = True, 
                   era5_server = 'reanalysis-era5-single-levels'):
    """
    Download global ERA5 data for a single month and year on an hourly frequency.

    Args:
        era5_varname (str)   : Variable name to download from ERA5.
        output_varname (str) : Variable name to use in filename
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
        
    param_dict = {
            'product_type': 'reanalysis',
            'variable': era5_varname,
            'year': str(year),
            'month': "{month:02d}".format(month=month),
            'day': [
                    '01', '02', '03',
                    '04', '05', '06',
                    '07', '08', '09',
                    '10', '11', '12',
                    '13', '14', '15',
                    '16', '17', '18',
                    '19', '20', '21',
                    '22', '23', '24',
                    '25', '26', '27',
                    '28', '29', '30',
                    '31',
                ],
            'time': [
                '00:00', '01:00', '02:00',
                '03:00', '04:00', '05:00',
                '06:00', '07:00', '08:00',
                '09:00', '10:00', '11:00',
                '12:00', '13:00', '14:00',
                '15:00', '16:00', '17:00',
                '18:00', '19:00', '20:00',
                '21:00', '22:00', '23:00',
            ],
            'format': 'netcdf',
        }
    
    if lat_bnds is not None and lon_bnds is not None:
        raise NotImplemented()

    c.retrieve(
        era5_server,
        param_dict,
        fp_out) 
    
    return fp_out