import os


for name in os.listdir("/data/user/abgvg9/benchmark/motif_collection/out"):
    print("\n" + name + "\n")
    l = []
    o = open("/data/user/abgvg9/benchmark/motif_collection/out/" + name + '/AllMattMotifsFile.motifs', "r")
    for line in o.readlines():
        if line.startswith("SINGLE"):
            line = line.split()
            if line[12] not in l:
                print(line[12])
                l.append(line[12])
    o.close()
    w = open("/data/user/abgvg9/benchmark/motif_collection/out/" + name + "/output_" + name + ".txt", "w")
    for i in l:
        a, b = i[0:3], i[3:]
        w.write("ROS " + b + " Res " + a + "\n")
    w.close()