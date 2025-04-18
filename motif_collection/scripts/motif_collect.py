import os


path, dirs, files = next(os.walk("/data/user/abgvg9/benchmark/motif_collection/files/pdb"))
os.chdir("/data/user/abgvg9/benchmark/motif_collection/files")
for i in files:
    name = i.split("_")[0]
    os.chdir("args")
    o = open(name + "_motif_args", "w")
    o.write(
"""-extra_res_fa /data/user/abgvg9/benchmark/files/all/""" + name + "/test_params/" + name + """_lig.params
-ignore_unrecognized_res
-hb_score_cutoff -0.3
-water_score_cutoff -0.3
-pack_score_cutoff -0.5
-s /data/user/abgvg9/benchmark/motif_collection/files/pdb/""" + name + """_pdb_lig.pdb"""
    )
    o.close()
    os.chdir("../jobs")
    os.mkdir("/data/user/abgvg9/benchmark/motif_collection/out/" + name)
    o = open(name + "_motif.job", "w")
    o.write(
"""#!/bin/bash
#SBATCH -p short # Partition to submit to
#SBATCH -n 1 # Number of cores requested
#SBATCH -N 1 # Ensure that all cores are on one machine
#SBATCH -t 720 # Runtime in minutes
#SBATCH --mem=1280 # Memory per cpu in MB
#SBATCH -o /data/user/abgvg9/benchmark/motif_collection/job_out/""" + name + """_hostname_%A_%a.out # Standard out goes to this file
#SBATCH -e /data/user/abgvg9/benchmark/motif_collection/job_out/""" + name + """_hostname_hostname_%A_%a.err # Standard err goes to this filehostname
cd /data/user/abgvg9/benchmark/motif_collection/out/""" + name + """
/data/project/thymelab/running_Rosetta/ari_work/Rosetta_Code_copy/main/source/bin/ligand_motifs.linuxgccrelease @/data/user/abgvg9/benchmark/motif_collection/files/args/""" + name + "_motif_args"
    )
    o.close()
    os.system("sbatch " + name + "_motif.job")
    os.chdir("..")