myfile = open("project2.txt" , "r")
all_lines = myfile.readlines()
for line in all_lines:
    upper_case_line = line.upper()
    line = upper_case_line.split(":")
    print(line[0])
    print(line[2])