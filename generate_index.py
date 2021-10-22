from os import listdir
import os
from os.path import isfile, join
from shutil import copyfile
import string

def main():
    #here we do something
    directory = "recipes"
    fold_names = [x[1] for x in os.walk(directory)][0]
    f = open("index.md", "w")
    f.write("# Le ricette di Nonna Aua\n")
    for fold_name in fold_names:
        f.write("## " + fold_name.title() + "\n")
        file_names = [k for k in listdir(directory+"/"+fold_name) if isfile(join(directory+"/"+fold_name, k))]
        for filename in file_names:
            f.write("["+filename.replace('-', ' ').title()+"](https://mmilanta.github.io/le_ricette_di_nonna_aua/recipes/"+filename+")\n")
    f.close()
    print(fold_names)


main()