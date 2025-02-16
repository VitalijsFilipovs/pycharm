# print(type(open("files/names.txt")))
# open("files/names.txt")
file = open("files/names1.txt", "r")
# 'r' open for reading (default)
# 'w' open for writing, truncating the file first
# 'x' create a new file and open it for writing
# 'a' open for writing, appending to the end of the file if it exists
# 'b' binary mode
# 't' text mode (default)
# '+' open a disk file for updating (reading and writing)

# print(file.read())
# print(file.read())
# print(file.readlines())
# print(file.readlines())

# file.write("aaaa")
# file.writelines(["aaaa\n", "sfsfggddgg"])

for line in file:     # chitaet fail
    print(line, end="")

file.close()

# print(file.read())
# print(file.readlines())
# print(file.name)
# print(file.mode)
# print(file.encoding)











