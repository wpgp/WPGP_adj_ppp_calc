"""Module to adjust WorldPop Population rasters (available at ftp://ftp.worldpop.org.uk/GIS/Population/Global_2000_2020/) according to user-define rates

Developed by: David Kerr; WorldPop (University of Southampton) 
Email: david.kerr@soton.ac.uk

Calculation formula:
adj_ppp = (ppp_raster * user-defined-rate)/worldpop_country_total_population

Currently the script requires the user to use a population raster downloaded from the above link as input. Future iterations will include the functionality to download the raster in the class.

***Note - This script is written to run on a Linux machine with GDAL installed. As it calls the gdal_calc.py module, this may not work on other machines. In these cases, if GDAL is installed, the gdal_calc.py (calc_adj() function) command will need to point to the GDAL/OSGEO installation.

"""

import os
import subprocess
import sys
from total_population_dict import total_pop_dict


class AdjPPPCalc:
    """Class to adjust WorldPop population grid data to user-defined rate"""

    def __init__(self, iso, in_raster, year, out_raster, n):
        """
        iso:            str -> 3 character alpha country code (see WorldPop raster name)
        in_raster:      str -> path to input population raster
        year:           int/str -> 4 digit year of input population raster (2000-2020)
        out_raster:     str -> path to output adjusted raster
        n:              float -> rate at which to adjust raster
        """
        self.iso = iso.upper()
        self.in_raster = in_raster
        self.year = year
        self.year_cut = int(str(self.year)[-2:])
        self.out_raster = out_raster
        self.n = float(n)
        try:
            self.total_pop = total_pop_dict[self.iso][self.year_cut]
        except KeyError:
            print('{0} ISO code does not exist. Please check your ISO code'.format(iso))
            sys.exit(1)
        self.calc_adj()

    
    def calc_adj(self):
        """Function to calculate adjusted rate based on user-define rate"""
        equation = '(A * {0})/{1}'.format(self.n, self.total_pop)
        gdal_command = 'gdal_calc.py -A {0} --outfile={1} --calc="{2}" --NoDataValue=-99999 --co COMPRESS=LZW --co PREDICTOR=2 --co BIGTIFF=YES'.format(self.in_raster, self.out_raster, equation)
        subprocess.call(gdal_command, shell=True)

