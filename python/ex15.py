from sys import argv

script, filename = argv

txt = open(filename)

print (f"The finame entered by you in {filename}")
print(txt.read())

print("Enter another file to open")
filename = input("> ")

txt.close();
txt = open(filename)

print(txt.read())   
