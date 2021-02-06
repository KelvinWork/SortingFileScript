# function testing script for integration.

from File_Sort_Programme import *


the_main_folder = "/Users/kelvi/PycharmProjects/SortingFileScript/quest/"

files = os.listdir(the_main_folder)
for file in files:
    #mosquito_category_folder(the_main_folder + file + "/")
    #print(file)  #quest1
    #print("Above file name \n")
    list_source = os.listdir(the_main_folder +file)
    #print(the_main_folder + file + "/")
    for item in list_source:
        print(item)

        print(the_main_folder + file + "/" + item)
        if re.search(r"AEGf\w+", item, re.I):
            print("Entered")
            shutil.copy(the_main_folder + file + "/" + item, the_main_folder + file + "/" + "i1/")
            pass


