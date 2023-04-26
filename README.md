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

