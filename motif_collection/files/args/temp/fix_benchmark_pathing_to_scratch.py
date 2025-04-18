import os,sys

# replace /data/user/abgvg9/benchmark/ with /data/user/abgvg9/benchmark/
"""
\/data\/project\/thymelab\/running_Rosetta\/ari_work\/REU_shared_space\/
\/data\/user\/abgvg9\/benchmark\/

sed -i 's/\/data\/project\/thymelab\/running_Rosetta\/ari_work\/REU_shared_space\//\/data\/user\/abgvg9\/benchmark\//g' test_args
sed -i 's/\/benchmark\/benchmark\//\/benchmark\//g' test_args

less /scratch/abgvg9/benchmark/files/all/aa2ar/test_params/aa2ar_lig.params
"""

location = os.getcwd()

for r,d,f in os.walk(location):
	for file in f:
		#run sed replacement on all files to change the path to the data/user...
		print(r + "/" + file)
		print("sed -i 's/\/data\/project\/thymelab\/running_Rosetta\/ari_work\/REU_shared_space\//\/data\/user\/abgvg9\/benchmark\//g' " + r + "/" + file)
		print("sed -i 's/\/benchmark\/benchmark\//\/benchmark\//g' " + r + "/" + file)
		os.system("sed -i 's/\/data\/project\/thymelab\/running_Rosetta\/ari_work\/REU_shared_space\//\/data\/user\/abgvg9\/benchmark\//g' " + r + "/" + file)
		os.system("sed -i 's/\/benchmark\/benchmark\//\/benchmark\//g' " + r + "/" + file)
		#os.system("sed -i 's/\/data\/project\/thymelab\/running_Rosetta\/ari_work\/REU_shared_space\//\/data\/user\/abgvg9\/benchmark\//g'")
