#remove spaces and colons from remarks section of pdb file

import os,sys

instream = open("updated_discovery_motif_list.motifs", "r")
outstream = open("updated_motifs_list_cleaned.motifs", "w")

for line in instream.readlines():
	if line.startswith("SINGLE"):
		#work with string contents before and after REMARK
		remark_contents = line.split("REMARK")
		#print(remark_contents)

		if(len(remark_contents) == 1):
			outstream.write(line)
			continue

		#remove Hbond section from remarks
		remark_no_spaces = remark_contents[1].split(" Hbond")[0]

		#replace all spaces in  remark_no_spaces with underscores
		remark_no_spaces = remark_no_spaces.replace(" ",  "_")

		#remove all colons
		remark_no_spaces = remark_no_spaces.replace(":",  "")

		#add newline to end of remark_no_spaces if it has no newline
		if(remark_no_spaces[len(remark_no_spaces)-1]  != "\n"):
			remark_no_spaces += "\n"

		#rebuild SINGLE line
		single_line = remark_contents[0] + " REMARK " + remark_no_spaces

		#print(single_line)
		outstream.write(single_line)
	else:
		outstream.write(line)
		#print(line)
