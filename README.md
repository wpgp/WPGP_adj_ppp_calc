# adj_ppp_calc

Module to adjust WorldPop Population rasters (available at ftp://ftp.worldpop.org.uk/GIS/Population/Global_2000_2020/) according to user-define rates

Developed by: David Kerr; WorldPop (University of Southampton) 
Email: david.kerr@soton.ac.uk

Calculation formula:
adj_ppp = (ppp_raster * user-defined-rate)/worldpop_country_total_population

Currently the script requires the user to use a population raster downloaded from the above link as input. Future iterations will include the functionality to download the raster in the class.

***Note - This script is written to run on a Linux machine with GDAL installed. As it calls the gdal_calc.py module, this may not work on other machines. In these cases, if GDAL is installed, the gdal_calc.py (calc_adj() function) command will need to point to the GDAL/OSGEO installation.


Class can be instantiated and calculation done as follows:

>> AdjPPPCalc(iso, in_raster, year, out_raster, adj_rate)

iso:            str -> 3 character alpha country code (see WorldPop raster name)

in_raster:      str -> path to input population raster

year:           int/str -> 4 digit year of input population raster (2000-2020)

out_raster:     str -> path to output adjusted raster

n:              float -> rate at which to adjust raster

