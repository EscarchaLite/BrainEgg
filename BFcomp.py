## SET UP

# Imports sys library and stores the name of the input and output files
import sys

program = sys.argv[1]
newFile = sys.argv[2]

# Opens files

program = open(program, "r")
newFile = open(newFile, "w")

contents = program.readlines()

# Writes setup to file

setup = '''data = [0]
for n in range(1000000):
    data.append(0)

pointer = [500000]

'''

print("Setup reached")

indentationLevel = ""

newFile.write(setup)

print("Compiling...")

#Goes through every command and line...

for line in contents:
    for command in line:
        if command == ">":
            newFile.write(indentationLevel + '''pointer[0] += 1
''')
        if command == "<":
            newFile.write(indentationLevel + '''pointer[0] -= 1
''')
        if command == "+":
            newFile.write(indentationLevel + '''data[pointer[0]] += 1
''' + indentationLevel + '''data[pointer[0]] = data[pointer[0]] % 256
''')
        if command == "-":
            newFile.write(indentationLevel + '''data[pointer[0]] -= 1
''' + indentationLevel +'''data[pointer[0]] = data[pointer[0]] % 256
''')
        if command == "[":
            newFile.write(indentationLevel + '''while data[pointer[0]] != 0:
''')
            indentationLevel += "   "
        if command == "]":
            indentationLevel = list(indentationLevel)
            for n in range(3):
                indentationLevel.pop(0)
            indentationLevel="".join(map(str,indentationLevel))
        if command == ".":
            newFile.write(indentationLevel + '''print(chr(data[pointer[0]]), end = "")
''')
        if command == ",":
            newFile.write(indentationLevel + '''s = input() or ""
''' + indentationLevel + '''if len(s) != 0:
''' + indentationLevel + '''   data[pointer[0]] = ord(s[0])
''' + indentationLevel + '''else:
''' + indentationLevel + '''   data[pointer[0]] = 0
'''
)

newFile.write("print("")")
print("Compile complete")
print("Exiting...")
