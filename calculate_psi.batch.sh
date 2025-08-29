#!/bin/bash -l
#SBATCH --job-name=calculatePsi
#SBATCH -A hfdrake_lab
#SBATCH -p free
#SBATCH --array=0-49 #50 files between 1850-2100
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --output=logs/%x_%A_%a.out # jobName_arrayMasterAllocation_arrayIndex
#SBATCH --error=logs/%x_%A_%a.err
#SBATCH -t 02:00:00 # time limit is 2 hrs (HH:MM:SS)

# configure bash shell environment. activate environment
source ~/.bashrc
conda activate environment

# specify file directory 
CM4X_filepath=/dfs9/hfdrake_hpc/datasets/CM4X/pp/ocean_month_rho2/ts/monthly/5yr/

# search for files from 1850-2100. put into bash array. call this array historic_picontrol_vmo_files
historic_picontrol_vmo_files=($(find $CM4X_filepath -name '*.[1-2]*.vmo.nc' | sort)) 

# select a single file from this file array
file=${historic_picontrol_vmo_files[$SLURM_ARRAY_TASK_ID]}

# set variables
AABW_INTERFACE=1037.0755
YQ_LAT=-30
REF_DENS=1035

# say something
echo "Processing $file"

# call python script
python calculate_psi.py \
	--FILENAME="$file" \
	--AABW_INTERFACE="$AABW_INTERFACE" \
       	--YQ_LAT="$YQ_LAT" \
       	--REF_DENS="$REF_DENS"

