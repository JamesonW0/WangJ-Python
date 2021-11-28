import random

with open("english2.txt", "r") as file_input:
    with open("newfile.txt", "w") as output:
        for line in file_input:
            if len(line.strip('\n')) > 4:
                output.write(line)
