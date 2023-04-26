import os
import subprocess
import numpy as np

def make_cds_dict(era5_varname, year, month=None, day=None, time=None,
                  product_type = 'reanalysis', form='netcdf'):
    
    """
    Download global ERA5 data for a single month and year on an hourly frequency.

    Args:
        era5_varname (str)   : Variable name to download from ERA5.
        year (int)           : Download year
        month (str or list)  : Download month(s). Default all
        day (str or list)    : Download day(s). Default all
        time (str or list)   : Download time(s). Default all hours.
        product_type (str)   : ERA5 product type. Default 'reanalysis'.
        form (str)           :

    Returns:
        Saves downloaded file to dp_output. Filename is automatic.
        Returns new filename.
    """
    
    # Create empty param dict. We will add key-items one by one
    param_dict = dict()
    param_dict['product_type'] = product_type
    param_dict['variable'] = era5_varname
    param_dict['format'] = form
    param_dict['year'] = year

    # If day is not provided, do all days
    if day is None:
        param_dict['day'] = [
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
            ]
    else:
        param_dict['day'] = day

    # If time is not provided, do all hours
    if time is None:
        param_dict['time'] = [
            '00:00', '01:00', '02:00',
            '03:00', '04:00', '05:00',
            '06:00', '07:00', '08:00',
            '09:00', '10:00', '11:00',
            '12:00', '13:00', '14:00',
            '15:00', '16:00', '17:00',
            '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00',
        ]
    else:
        param_dict['time'] = time

    # If month is not provided, do all month
    if month is None:
        param_dict['month'] = [
            '01', '02', '03', '04', '05',
            '06', '07', '08', '09', '10',
            '11', '12']
    else:
        param_dict['month'] = month

    return param_dict