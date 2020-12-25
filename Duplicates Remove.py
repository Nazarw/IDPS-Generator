lines_seen = set()
with open("sniped_cleaned.txt", "w") as output_file:
	for each_line in open("idps.txt", "r"):
	    if each_line not in lines_seen:
	        output_file.write(each_line)
	        lines_seen.add(each_line)