import os

date = ["Mon", "Tues", "Wed", "Thurs", "Fri"]
folderName = "Mosquitto"
createFolderDestination ="/Users/butac/Desktop/"
folderPath = createFolderDestination+folderName+"/"

def creatingFolder():
    print("Hello World!")
    os.mkdir(createFolderDestination+folderName)






def creatingSubFolder():
    print("World Hello")
    mosquittoClass = ["Aeg", "Alb", "Aesp", "Chiro", "Oi", "5fas"]

    for y in range(5):
        for x in mosquittoClass:
            os.mkdir(folderPath+date[y]+x)






