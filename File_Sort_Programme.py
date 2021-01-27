import shutil
import os
import re



# folder_name = "Sorted_Mosquito/" # title of the main folder
# main_folder_location = "/Users/kelvi/PycharmProjects/SortingFileScript/" + folder_name # location that the file will be created
# image_location = "/Users/kelvi/PycharmProjects/SortingFileScript/EW41/TestRun" # location of the images
#
#list_location = os.listdir(image_location)

def creating_folder(main_folder_location):
    if(os.path.exists(main_folder_location)):
        print("Exisitng File has been created")

    else:
        print("Main folder has been created !")
        os.mkdir(main_folder_location)


def mosquito_category_folder(main_folder_location):
    mosquito_class = ["m_aeg", "f_aeg", "m_aesp", "f_aesp", "m_alb", "f_alb", "m_aemal", "f_aemal", "f_others", "m_others", "unidentifiable"]

    for mosquito in mosquito_class:
        if(os.path.exists(main_folder_location + "/" + mosquito)):
            print("Existing File has been created !")

        else:
            print("Mosquito Category " + mosquito + "has been created !")
            print("\n")
            os.mkdir(main_folder_location + mosquito)


def check_items_folder(folder_name):
    if os.listdir(folder_name) != []:
        print("THERE IS ITEM IN THE UNIDENTIFIABLE FOLDER")
        print("PLEASE SORT THE IMAGES")

    else:
        print("THERE IS NO ITEM IN THE UNIDENTIFIABLE FOLDER")


def mosquito_sort_algorithm(image_location, main_folder_location):
    list_location = os.listdir(image_location)
    for images in list_location:

        if re.search(r"f.aeg\w+", images, re.I):
            print("Moving images. . . .")
            shutil.move(image_location + "/" + images, main_folder_location + "f_Aeg")

        elif re.search(r"m.aeg\w+", images, re.I):
            print("Moving images. . . .")
            shutil.move(image_location + "/" + images, main_folder_location + "m_Aeg")

        elif re.search(r"f.alb\w+", images, re.I):
            print("Moving images. . . .")
            shutil.move(image_location + "/" + images, main_folder_location + "f_Alb")

        elif re.search(r"m.alb\w+", images, re.I):
            print("Moving images. . . .")
            shutil.move(image_location + "/" + images, main_folder_location + "m_Alb")

        elif re.search(r"f.aesp\w+", images, re.I):
            print("Moving images. . . .")
            shutil.move(image_location + "/" + images, main_folder_location + "f_Aesp")

        elif re.search(r"m.aemal\w+", images, re.I):
            print("Moving images. . . .")
            shutil.move(image_location + "/" + images, main_folder_location + "m_aemal")

        elif re.search(r"f.aemal\w+", images, re.I):
            print("Moving images. . . .")
            shutil.move(image_location + "/" + images, main_folder_location + "f_aemal")

        elif re.search(r"m.others\w+", images, re.I):
            print("Moving images. . . .")
            shutil.move(image_location + "/" + images, main_folder_location + "m_others")

        elif re.search(r"f.others\w+", images, re.I):
            print("Moving images. . . .")
            shutil.move(image_location + "/" + images, main_folder_location + "f_others")

        else:

            if re.search(r"m.\w+", images, re.I):
                print("Moving images. . . .")
                shutil.move(image_location + "/" + images, main_folder_location + "m_others")

            elif re.search(r"f.\w+", images, re.I):
                print("Moving images. . . .")
                shutil.move(image_location + "/" + images, main_folder_location + "f_others")

            else:
                shutil.move(image_location + "/" + images, main_folder_location + "unidentifiable")


    check_items_folder(main_folder_location + "unidentifiable")




