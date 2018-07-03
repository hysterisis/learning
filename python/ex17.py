from sys import argv
from os.path import exists

script, from_file, to_file = argv

# truncating and writing to to a file
print(f"Below is the contents of the file {from_file}")
filehandle = open(from_file)
print(filehandle.read())

print("\n\n\nAre you sure you want to truncate and overwrite the file? ")
input("> ")
filehandle.close()
filehandle = open(from_file,'w')
filehandle.truncate()

print ("Now lets write sometthing to the file. You can add upto 3 lines.")

line1=input("Line 1: ")
line2=input("Line 2: ")
line3=input("Line 3: ")

print("Writing the lines to the file")
filehandle.write(line1)
filehandle.write("\n")
filehandle.write(line2)
filehandle.write("\n")
filehandle.write(line3)
filehandle.write("\n")

print("Contents written to file, now closing the file")
filehandle.close()

print(f"Preparing to copy from {from_file} to {to_file}")
print(f"Does the target file exists ? {exists(to_file)}")
print("Ready to copy?")
input("> ")

in_file=open(from_file)
indata = in_file.read()

out_file = open(to_file,'w')
out_file.write(indata)

print("Done Writing")
in_file.close()
out_file.close()
