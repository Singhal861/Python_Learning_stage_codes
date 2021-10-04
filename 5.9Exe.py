# Oh soldier prettify my folder
import os


# def soldier(path2, format1):
def soldier(path1, file, path2, format1):
    os.chdir(path1)
    os.listdir()
    for fil in os.listdir():
        if fil != file:
            os.renames(fil, fil.capitalize())
    os.chdir(path2)
    os.listdir()
    for count, f in enumerate(os.listdir()):
        if f.endswith(format1) or f.endswith(format1.upper()):
            os.rename(f, f"Img{count}.{format1}")


path1 = input("Enter your path for Capitalise file = ")
file = input("Enter the file name of directory which you don't want to change = ")
path2 = input("Enter your path for Rename file = ")
format1 = input("Which type of file format you want to Rename = ")

# soldier( path2, format1)
soldier(path1, file, path2, format1)
