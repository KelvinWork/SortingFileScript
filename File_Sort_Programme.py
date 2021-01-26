import shutil
import os
import re

folder_name = "Sorted_Mosquito/"
main_folder_location = "/CodingProjects/SortingFileScript/" + folder_name
image_location = "/CodingProjects/SortingFileScript/EW41/TestRun"

list_location = os.listdir(image_location)
print(list_location)
print(type(list_location))


def creating_folder():
    if(os.path.exists(main_folder_location)):
        print("Exisitng File has been created")

    else:
        print("Main folder has been created !")
        os.mkdir(main_folder_location)


def mosquito_category_folder():
    mosquito_class = ["Male_Aeg", "Female_Aeg", "Male_Aesp", "Female_Aesp", "Male_Alb", "Female_Alb"]

    for mosquito in mosquito_class:
        if(os.path.exists(main_folder_location + "/" + mosquito)):
            print("Existing File has been created !")

        else:
            print("Mosquito Category " + mosquito + "has been created !")
            print("\n")
            os.mkdir(main_folder_location + mosquito)


def mosquito_sort_algorithm(list_location):
    for images in list_location:

        if re.search(r"f.aeg\w+", images, re.I):
            print("its a match")
            shutil.move(image_location + "/" + images, main_folder_location + "Female_Aeg")

        elif re.search(r"m.aeg\w+", images, re.I):
            print("its a match")
            shutil.move(image_location + "/" + images, main_folder_location + "Male_Aeg")

        elif re.search(r"f.alb\w+", images, re.I):
            print("its a match")
            shutil.move(image_location + "/" + images, main_folder_location + "Female_Alb")

        elif re.search(r"m.alb\w+", images, re.I):
            print("its a match")
            shutil.move(image_location + "/" + images, main_folder_location + "Male_Alb")

        elif re.search(r"f.aesp\w+", images, re.I):
            print("its a match")
            shutil.move(image_location + "/" + images, main_folder_location + "Female_Aesp")

        elif re.search(r"m.aesp\w+", images, re.I):
            print("its a match")
            shutil.move(image_location + "/" + images, main_folder_location + "Male_Aesp")

        else:
            print("The folder has no images")

mosquito_sort_algorithm(list_location)