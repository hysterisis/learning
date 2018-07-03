import sys

#script, encoding, errors = sys.argv

def main(language_file, encoding, errors) :
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors) :
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode (encoding, errors = errors)

    print (raw_bytes, "<===>", cooked_string)

#languages = open ("languages.txt",encoding="utf-16")
#main(languages,encoding,errors)

choice = input ( "> " )
if "0" in choice or "1" in choice :
    how_much = int ( choice )
else :
    print ( "Man, learn to type a number." )
