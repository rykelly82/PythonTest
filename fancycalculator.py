opened_file = open('newfile.txt', mode = 'r')

with open('newfile.txt', 'r') as file_to_read:
    contents = str(file_to_read.read().splitlines())

#split_contents = contents.split(",")

print(contents)




