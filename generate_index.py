from os import listdir
import os
from os.path import isfile, join
from shutil import copyfile
import string

def main():
    #here we do something
    directory = "recipes"
    fold_names = [x[1] for x in os.walk(directory)][0]
    fold_names = [fold_names[4],
                  fold_names[5],
                  fold_names[10],
                  fold_names[1],
                  fold_names[6],
                  fold_names[0],
                  fold_names[3],
                  fold_names[7],
                  fold_names[9],
                  fold_names[8],
                  fold_names[2]]
    f = open("README.md", "w")
    f.write("# Le ricette di Nonna Aua\n")
    for fold_name in fold_names:
        f.write("## " + fold_name.title() + "\n")
        file_names = [k for k in listdir(directory+"/"+fold_name) if isfile(join(directory+"/"+fold_name, k))]
        file_names = sorted(file_names, key=str.lower)

        for filename in file_names:
            filename = filename[:-3]
            f.write("* ["+filename.replace('-', ' ').title()+"](https://mmilanta.github.io/le_ricette_di_nonna_aua/recipes/"+fold_name+"/"+filename+")\n")
    f.close()
    print(fold_names)


main()