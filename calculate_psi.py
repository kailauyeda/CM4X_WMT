import numpy as np
import xarray as xr
import argparse
import glob 
import os

# function to calculate psi for every time step in the dataset (monthly for 5 yrs)
def calculate_psi(filename,aabw_interface,yq_lat,ref_dens):
    # CM4X_filepath = '/dfs9/hfdrake_hpc/datasets/CM4X/pp/ocean_month_rho2/ts/monthly/5yr/'
    vmo_chunks = {'time':1,'xh':360}
    
    ds = xr.open_dataset(filename, use_cftime=True).sel(rho2_i = slice(aabw_interface,None),
                                                               rho2_l = slice(aabw_interface,None)
                                                                ).sel(yq = yq_lat, method='nearest'
                                                                ).chunk(vmo_chunks)['vmo'].to_dataset(name='vmo')
    psi = (ds.vmo / ref_dens).sum('xh').sum('rho2_l').compute()
    ku_filepath = '/pub/kailau/hackathon/30S_AABW_transports/'
    psi.to_netcdf(ku_filepath + '30S_AABW_transport_' + os.path.basename(filename), mode='w',format='NETCDF4')

# require variables
if (__name__ =="__main__"):
    parser = argparse.ArgumentParser(description="Script that calculates meridional transport through 30oS from CM4-0.125 data")
    parser.add_argument("--FILENAME",required=True,type=str)
    parser.add_argument("--AABW_INTERFACE",required=True,type=float)
    parser.add_argument("--YQ_LAT",required=True,type=float)
    parser.add_argument("--REF_DENS",required=True,type=float)

    args = parser.parse_args()

    
# do something
calculate_psi(args.FILENAME, args.AABW_INTERFACE, args.YQ_LAT, args.REF_DENS)
        
