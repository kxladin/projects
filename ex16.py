from sys import argv

script, filename = argv

print(f"We're going to erase{filename}.")
print("If you don't want that, hit CTRL-C.")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

line_concat = line1 + "\n" + line2 + "\n" + line3

target.write(line_concat)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)

print("And finally, we close it.")
target.close()

print(f"Contents written into {filename} are: ")

temp = open(filename)
print(temp.read())

