## CM4X WMT

### to get data via globus transfer (after having set up an endpoint)
> - a) Make directories in `/pub/kailau` for each dataset.
> - b) The files are initially put in the folder `~`, which is `data/homezvol3/kailau`.
> - c) After the transfer, you will have to move the files from `~/24-25/name_of_directory` to `/pub/kailau/directory_from_a`

```
conda activate environment 
cd /pub/kailau/globusconnectpersonal-3.2.5 
./globusconnectpersonal -start & 
globus login 
```

*get source endpoint* \
`globus endpoint search "CM4X"` 

*get destination endpoint*\
`echo "$(globus endpoint local-id)"`

```
sep=ed6b9060-122b-4d2e-b3e6-a38e1d66ae42
dep=8be94d74-6199-11ef-b749-0f922496edc5
globus transfer \ $sep:./budgets_sigma2/CM4Xp25_budgets_sigma2_1750-1754.zarr $dep:./24-25/CM4Xp25_1750-1754.zarr \--recursive --label="CM4Xp25 1750-1754"
```



