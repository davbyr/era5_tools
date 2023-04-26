## era5_tools

This is a small Python package for automating and simplifying the downloading of ERA5 data using CDSAPI.
The functions currently in the package will download data in monthly blocks, saving to file.
You also have the option of passing simple analysis functions to the package, which will be
automatically applied to each file once downloaded.

An example script of how to use `download_multiple_months()` is in the `/scripts` directory.

### Installation

1. Clone this repository.
2. Create a new Python environment using conda. Install pip into this environment.
3. Activate environment.
4. `cd` into the top repository directory.
5. Enter `pip install -e .`

Make sure you have set up the use of CDSAPI on your machine.

Once installed, import this into your script using `import era5_tools`.

### Basic Overview

The most useful function is `era5_tools.download_multiple_months()` (more info in function docstring). Examples:

**Download data into monthly files over multiple years (2000 and 2001)**

```
import era5_tools
output_directory = './data'
era5_tools.download_multiple_months('2m_temperature', output_directory, 2000, 2001)
```

**Download data into monthly files for just January and February**
```
era5_tools.download_multiple_months('2m_temperature', output_directory, 2000, 2001, month=[1,2])
```

**Download data for a single year (all months) and apply a simple resampling function:**
```
def resample_func( fp ):

  # Open dataset and resample to daily means
  ds = xr.open_dataset(fp).resample(time='1D').mean(dim='time')
  
  return ds
  
era5_tools.download_multiple_months('2m_temperature', output_directory, 2000, 2001, month=[1,2],
                                    apply_func = resample_func, func_name = '1Dmean', delete_after_func = True)
```

This function will resample each downloaded monthly file to daily means. The original downloaded hourly file will be deleted.

