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
        item_in_folder = "THERE IS ITEM IN THE UNIDENTIFIABLE FOLDER \n PLEASE SORT THE IMAGES"
        return item_in_folder

    else:
        item_in_folder ="THERE IS NO ITEM IN THE UNIDENTIFIABLE FOLDER"
        return item_in_folder

def mosquito_sort_algorithm(image_location, main_folder_location):
    list_location = os.listdir(image_location)
    for images in list_location:

        if re.search(r"AEGf\w+", images, re.I):
            print("Moving images. . . .")
            shutil.copy(image_location + "/" + images, main_folder_location + "f_Aeg")

        elif re.search(r"AEGm\w+", images, re.I):
            print("Moving images. . . .")
            shutil.copy(image_location + "/" + images, main_folder_location + "m_Aeg")

        elif re.search(r"ALBf\w+", images, re.I):
            print("Moving images. . . .")
            shutil.copy(image_location + "/" + images, main_folder_location + "f_Alb")

        elif re.search(r"ALBm\w+", images, re.I):
            print("Moving images. . . .")
            shutil.copy(image_location + "/" + images, main_folder_location + "m_Alb")

        elif re.search(r"AESPf\w+", images, re.I):
            print("Moving images. . . .")
            shutil.copy(image_location + "/" + images, main_folder_location + "f_Aesp")

        elif re.search(r"AESPm\w+", images, re.I):
            print("Moving images. . . .")
            shutil.copy(image_location + "/" + images, main_folder_location + "m_Aesp")

        elif re.search(r"AEMALm\w+", images, re.I):
            print("Moving images. . . .")
            shutil.copy(image_location + "/" + images, main_folder_location + "m_aemal")

        elif re.search(r"AEMALf\w+", images, re.I):
            print("Moving images. . . .")
            shutil.copy(image_location + "/" + images, main_folder_location + "f_aemal")

        elif re.search(r"m.others\w+", images, re.I):
            print("Moving images. . . .")
            shutil.copy(image_location + "/" + images, main_folder_location + "m_others")

        elif re.search(r"f.others\w+", images, re.I):
            print("Moving images. . . .")
            shutil.copy(image_location + "/" + images, main_folder_location + "f_others")

        else:

            if re.search(r"m.\w+", images, re.I):
                print("Moving images. . . .")
                shutil.copy(image_location + "/" + images, main_folder_location + "m_others")

            elif re.search(r"f.\w+", images, re.I):
                print("Moving images. . . .")
                shutil.copy(image_location + "/" + images, main_folder_location + "f_others")

            else:
                shutil.copy(image_location + "/" + images, main_folder_location + "unidentifiable")


    check_items_folder(main_folder_location + "unidentifiable")




