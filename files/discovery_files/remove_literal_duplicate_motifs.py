import os,sys

filename = sys.argv[1]

read_file = open(filename, "r")
#write_file = open("dups_removed_" + filename, "r")

motifs = []

motif_pair = []

counter = 0

for line in read_file.readlines():
	
	if len(motif_pair) == 0:
		motif_pair.append(line)
	else:
		counter = counter + 1
		if counter % 100 == 0:
			print(counter)

		motif_pair.append(line)

		keep_motif = True

		if motif_pair in motifs:
			keep_motif = False
			print("Hit a duplicate of:")
			print(motif_pair)

		if keep_motif:
			motifs.append(motif_pair)
			os.system(motif_pair[0] + " >> quicker_dupes_removed_" + filename)
			os.system(motif_pair[1] + " >> quicker_dupes_removed_" + filename)

		motif_pair = []
"""
for motif in motifs:
	#print(motif[0])
	#print(motif[1])
	write_file.write(motif[0])
	write_file.write(motif[1])
"""
