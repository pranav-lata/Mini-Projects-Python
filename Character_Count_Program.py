import os 

name_of_dir = input("Enter the name of the text file: ")

destination = r"C:\Users\Pranav\Desktop"

file = open(destination+name_of_dir+'.txt','w')   # file open , create
data = input("Enter the data into the file: ")
file.write(data)
file.close()

new_ls = []
for i in data.split():
    new_ls.append((i))

print("The number of characters present in your provided data are -->",len(new_ls))