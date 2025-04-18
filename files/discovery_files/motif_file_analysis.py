import os,sys

file = sys.argv[1]

print(file)

motif_file = open(file, "r")

#create dictionary of residues as they appear in the motif file
res_dict = {}

for line in motif_file.readlines():
	if line.startswith("SINGLE"):
		res = line.split()[1]
		#print(res)

		if res not in res_dict:
			res_dict[res] = 1
		else:
			res_dict[res] = res_dict[res] + 1

total = 0

for res in res_dict:
	print(res + ": " + str(res_dict[res]))
	total += res_dict[res]

print("TOTAL: " + str(total))

