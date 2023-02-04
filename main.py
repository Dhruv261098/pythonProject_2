# write the file in python

# here r represent we want to read the file
f = open('inputFile.txt','r')

# here w represent we write in the file, this command will crate the NewFile
NewFile = open('NewFile.txt','w')
FailPeople = open('failPeople.txt', 'w')

# here line, line_split & f are variables, split() is function
# line.split() will split the line in 3 colums as you could define in the file (Name[0] number[1] P/F[2])

for line in f:
    line_split= line.split()
    if line_split[2] == 'P':
        NewFile.write(line)
# Above command write each line which pass the condition in newly created file.

    if line_split[2] == 'F':
        FailPeople.write(line)
# Above command write each line which pass the condition in newly created file.

#another way to write above two things is as below
""""
for line in f:
    line_split= line.split()
    if line_split[2] == 'P':
        NewFile.write(line)
    else:
     FailPeople.write(line)

"""

f.close()
NewFile.close()
FailPeople.close()