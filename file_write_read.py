# file_write_read.py
# Write and read file

file = open("data.txt", "w")
file.write("Hello, this is a sample file.\n")
file.write("Python file handling example.")
file.close()

file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
