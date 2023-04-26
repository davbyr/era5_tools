# era5_tools

This is a small Python package for automating and simplifying the downloading of ERA5 data using CDSAPI.
The functions currently in the package will download data in monthly blocks, saving to file.
You also have the option of passing simple analysis functions to the package, which will be
automatically applied to each file once downloaded.

An example script of how to use `download_multiple_months()` is in the `/scripts` directory.

## Installation

1. Clone this repository.
2. Create a new Python environment using conda. Install pip into this environment.
3. Activate environment.
4. `cd` into the top repository directory.
5. Enter `pip install -e .`

Once installed, import this into your script using `import era5_tools`.

## Basic Overview

The most useful function is `era5_tools.download_multiple_months()`:

```
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
    ```
