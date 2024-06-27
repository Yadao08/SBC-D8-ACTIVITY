#This program shows how to write data in a text file.

#append -eh dugang

file = open("textfile.txt","r")
#print (file.read())
#var = file.read(5)
'''var = file.readlines() # with new line char
print (var)
print (var[0])

lines = [line.strip() for line in open("textfile.txt")]
print (lines)
print (lines[0])

lines = [line.strip() for line in open("textfile.txt")]
for line in lines:
    print(line)'''

# write = open("textfile.txt","w")
#print (file.readlines())
# file.write("Hello world!\n")
# file.write("summer\n")
# file.write("goodbye\n"
# print("Hello world!", file = write)
# print("summer", file = write)
# print("goodbye", file = write)

# fname = "John"
# print(fname,file = write)

while True:
    write = open("textfile.txt","a")
    name = input("Name: ")
    print(name,file = write)
    write.close()