import os, sys

blast_output = sys.argv[1]
input_motif_list = sys.argv[2]

#read in a list of all homologous pdbs from the blast output (determined as from lines that start with a ">", taking the next 4 characters)
blast_output_file = open(blast_output, "r")

#dictionary of query id and assoriated homologous pdbs
pdb_blacklist = {}

query = ""

for line in blast_output_file.readlines():
	if line.startswith("Query="):
		query = line.split()[1].strip("\n")
		pdb_blacklist[query] = []

	if line.startswith(">"):
		
		pdb_name = line[1:5].upper()

		if pdb_name not in pdb_blacklist[query]:
			#print(pdb_name)
			pdb_blacklist[query].append(pdb_name)

	#other homologs listed under ">" lines. start with a space. Investigate if starts with a space and character indices 1-5 are upper case
	if line.startswith(" ") and line[1:5].isupper():
		
		pdb_name = line[1:5].upper()

		if pdb_name not in pdb_blacklist[query]:
			#print(pdb_name)
			pdb_blacklist[query].append(pdb_name)

	#for key in pdb_blacklist.keys():
		#print(key, pdb_blacklist[key])

#read in all motifs from motif list
line_counter = 0
input_motif_file = open(input_motif_list, "r")

motif_list = []

motif_line_holder = ""
real_motif_line = ""

for line in input_motif_file.readlines():
	
	#hold main motif info (including remark with pdb name)
	if(line_counter % 2 == 0):
		motif_line_holder = line.upper()
		real_motif_line = line
	else:
		#we have the motif info and are now getting positional data
		#append as list to motif_list
		motif_list.append([motif_line_holder,line, real_motif_line])

	line_counter = line_counter + 1

print(len(motif_list))
input_motif_file.close()

#iterate through all keys (systems) in the blacklist and remove all homologous pdbs from the motif list
#print to a new motifs file, named based on the query/key, make new files in the same place as the original motifs file

#break up path and filename for input motif list (if path is included)
motif_list_path = ""
motif_list_name = input_motif_list
if len(input_motif_list.split("/")) > 1:
	motif_list_path_holder = input_motif_list.split("/")[0:len(input_motif_list.split("/")) - 2]
	motif_list_name = input_motif_list.split("/")[len(input_motif_list.split("/")) - 1]

	for string in motif_list_path_holder:
		motif_list_path = motif_list_path + string + "/"

print(motif_list_path, motif_list_name)

key_counter = 1
for key in pdb_blacklist.keys():
	print(key, key_counter)
	print(motif_list_path + key + "_" + motif_list_name)
	out_motif_file = open( motif_list_path + key + "_" + motif_list_name, "w")

	#run motif list against blacklist
	for motif in motif_list:

		keep_motif = True

		for bl_lig in pdb_blacklist[key]:
			if bl_lig in motif[0]:
				#print(bl_lig, motif)
				keep_motif = False
				break

		if keep_motif:
			out_motif_file.write(motif[2])
			out_motif_file.write(motif[1])

	key_counter = key_counter + 1
	out_motif_file.close()
