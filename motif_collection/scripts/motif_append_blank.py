import os

os.chdir("/data/user/abgvg9/benchmark/motif_collection/files")
a = open("blank_motifs.motifs", "a")
for name in os.listdir("/data/user/abgvg9/benchmark/motif_collection/out"):
    o = open("/data/user/abgvg9/benchmark/motif_collection/out/" + name + "/AllMattMotifsFile.motifs")
    a.write(o.read())
    o.close()
a.close()
