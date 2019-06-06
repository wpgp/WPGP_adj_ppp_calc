from pathlib import Path
from adj_ppp_calc import AdjPPPCalc

def main():
    in_raster = BASE_DIR.joinpath('datain/btn_ppp_2000.tif')
    out_raster = BASE_DIR.joinpath('dataout/btn_ppp_adj_2000.tif')
    AdjPPPCalc('BTN', in_raster, 2000, out_raster, 0.5)
    print(in_raster.exists())



if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent.parent
    main()