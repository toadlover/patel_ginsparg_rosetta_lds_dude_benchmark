import os
import re


os.chdir('/data/user/abgvg9/benchmark/motif_collection/files/pdb')
path, dirs, files = next(os.walk("/data/user/abgvg9/benchmark/files/neighbor_out"))
for i in files:
    name = re.search("_(.*).txt", i).group(1)
    print(name)
    pdb_lig = open(name + "_pdb_lig.pdb", "w")
    pdb = open("/data/user/abgvg9/benchmark/files/all/" + name + "/" + name +'.pdb')
    lig = open("/data/user/abgvg9/benchmark/files/" + name + "-lig.pdb")

    for line in pdb.readlines():
        if not line.startswith("TER"):
            pdb_lig.write(line)

    for line in lig.readlines():
        if not line.split()[3] == "HOH":
            line = line.replace(line.split()[3], "cry")
            pdb_lig.write(line)
    pdb_lig.close()
