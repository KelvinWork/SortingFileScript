import os

date = "Mon"
folderName = "Mosquitto"
createFolderDestination ="/Users/kelvi/Desktop/"
folderPath = createFolderDestination+folderName+"/"

def creatingFolder():
    print("Hello World!")
    os.mkdir(createFolderDestination+folderName)






def creatingSubFolder():
    print("World Hello")
    mosquittoClass = ["Aeg", "Alb", "Aesp", "Chiro", "Oi", "5fas"]

    for x in mosquittoClass:
        os.mkdir(folderPath+date+x)






