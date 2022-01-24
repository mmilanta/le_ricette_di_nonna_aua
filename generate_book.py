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
    # LATEX folder
    latex_folder = "LateXrecipes"
    if not os.path.exists(latex_folder):
        os.makedirs(latex_folder)
    for fold in fold_names:
        if not os.path.exists(latex_folder+ "/"+fold):
            os.makedirs(latex_folder+ "/"+fold)
    f = open("LateXbook/index.tex",'w')
    
    for fold_name in fold_names:
        file_names = [k for k in listdir(directory+"/"+fold_name) if isfile(join(directory+"/"+fold_name, k))]
        file_names = sorted(file_names, key=str.lower)

        for filename in file_names:
            f.write("\\input{../"+latex_folder+"/"+fold_name+"/"+filename[:-3]+".tex"+"}\n")
            f.write("\\newpage\n")
            create_recipe(fold_name, filename, recipe_folder = directory, latex_folder = latex_folder)
        
        if fold_name == "pane & co":
            fold_name = "pane \& co"
        f.write("\\chapter{"+fold_name.title()+"}\n")
    
def create_recipe(fold_name, file_name, recipe_folder, latex_folder):
    title = "Pippo"
    ingredients = []
    steps = []
    notes = []
    f = open(recipe_folder + "/"+ fold_name + "/" + file_name, "r")
    lines = f.readlines()
    reading_ingredients = False
    reading_steps = False
    reading_notes = False
    for line in lines:
        if line[:2] == "# ":
            title = (line[2:])[:-1]
        if line[:14] == "## ingredients":
            reading_ingredients = True
        if line[:8] == "## steps":
            reading_steps = True
            reading_ingredients = False
        if line[:8] == "## notes":
            reading_notes = True
            reading_steps = False
            reading_ingredients = False
        if line[:11] == "## based on":
            break
        if reading_ingredients and "*" == line[0]:
            ingredients.append((line[2:])[:-1])
        if reading_steps and "1" == line[0]:
            steps.append((line[2:])[:-1])
        if reading_notes and "*" == line[0]:
            notes.append((line[2:])[:-1])
    f.close()
    file_name = file_name[:-3]+".tex"
    f = open(latex_folder + "/"+ fold_name + "/" + file_name, "w")
    f.write("\section{"+title+"}\n")
    f.write("\subsection{Ingredienti}\n")

    if len(ingredients) > 0:
        f.write("\\begin{itemize}\n")
        for i in ingredients:
            f.write("\item " + i + "\n")
        f.write("\end{itemize}\n")

    f.write("\subsection{Procedimento}\n")
    f.write("\\begin{enumerate}\n")
    for s in steps:
        f.write("\item " + s + "\n")
    f.write("\end{enumerate}\n")

    if len(notes) > 0:
        f.write("\subsection{Note}\n")
        f.write("\\begin{itemize}\n")
        for n in notes:
            f.write("\item " + n + "\n")
        f.write("\end{itemize}\n")
    f.close()
main()