file_name = input("File name: \n")
file = open(file_name, "r")
data = file.readlines()
file.close()
dataWrite = []
for st in data:
    if st[len(st)-1] == "\n":
        st = st[0:len(st)-1]
        st = st[::-1]
        st += "\n"
    else:
        st = st[::-1]
    dataWrite.append(st)
file = open(file_name, "w")
file.write("")
file.close()
file = open(file_name, "a")
file.writelines(dataWrite)
file.close()
