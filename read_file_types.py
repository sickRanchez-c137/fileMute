read_from = "names.csv"

# do not change the following lines
out_file_name = "supported_file_info.py"
dict_name = "def initialize_dict():\n\tfile_magic_dict = {}\n"
outfile = open(out_file_name,"w")
outfile.write(f"{dict_name}")

no_lines = 0
list_of_file_types = list()

with open(read_from,"r") as infile:
    # loop to read the file
    while(True):
        # read a single line each time
        in_string = infile.readline()
        # strip of the endline chars
        in_string = in_string.strip()
        # check if end reached or empty line
        if not in_string:
            break
        elif in_string=="":
            continue

        no_lines+=1
        file_desc,file_ext,magic_number = in_string.split(",")
        file_ext = file_ext.split('.')[-1]
        str_to_write=""
        if file_ext in list_of_file_types:
            str_to_write = f"\tfile_magic_dict[\"{file_ext}\"][0].append(\"{magic_number}\")\n"
            str_to_write += f"\tfile_magic_dict[\"{file_ext}\"][1].append(\"{file_desc}\")\n"
            outfile.write(str_to_write)
        else:
            str_to_write = f"\tfile_magic_dict[\"{file_ext}\"] = [[\"{magic_number}\"],[\"{file_desc}\"]]\n"
            outfile.write(str_to_write)
        list_of_file_types.append(file_ext)
outfile.write("\treturn file_magic_dict")
outfile.close()

print(f"..read {no_lines} lines from file {read_from}")
