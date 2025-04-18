import os

os.chdir("/data/user/abgvg9/benchmark/motif_collection/files")
a = open("motif_list_with_benchmark_motifs.motifs", "a")
for name in os.listdir("/data/user/abgvg9/benchmark/motif_collection/out"):
    o = open("/data/user/abgvg9/benchmark/motif_collection/out/" + name + "/AllMattMotifsFile.motifs")
    a.write(o.read())
    o.close()
a.close()
