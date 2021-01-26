import os
import shutil
from GUI import *




date = "Mon"  #Mon, Tues, Wed, Thurs, Fri

folderLocation ="/Users/kelvi/Desktop/Mosquitto/"

imageMondaySourceLocation = "/Users/kelvi/Desktop/EW41/EW41/" + date[0:] + "/"



testingLocation1 = folderLocation[0:] + date[0:] + "AEG"
testingLocation2 = folderLocation[0:] + date[0:] + "ALB"
testingLocation3 = folderLocation[0:] + date[0:] + "Aesp"
testingLocation4 = folderLocation[0:] + date[0:] + "Chiro" 
testingLocation5 = folderLocation[0:] + date[0:] + "Oi"
testingLocation6 = folderLocation[0:] + date[0:] + "5fas"

if not os.path.exists(folderPath):
    creatingFolder()
    creatingSubFolder()

else:
    print("existing folder has been created")


image = os.listdir(imageMondaySourceLocation)
# print(image)
# print(len(image))
# print(type(image))


condition1Keyword = ['aeg', 'Aeg']
condition1 = [con1 for con1 in image if any(Con1 in con1 for Con1 in condition1Keyword)]

for images1 in condition1:
    shutil.move(imageMondaySourceLocation+images1, testingLocation1)



condition2Keyword = ['alb']
condition2 = [con2 for con2 in image if any(Con2 in con2 for Con2 in condition2Keyword)]

for images2 in condition2:
    shutil.move(imageMondaySourceLocation+images2, testingLocation2)



condition3Keyword = ['Aesp']
condition3 = [con3 for con3 in image if any(Con3 in con3 for Con3 in condition3Keyword)]

for images3 in condition3:
     shutil.move(imageMondaySourceLocation+images3, testingLocation3)



condition4Keyword = ['chiro']
condition4 = [con4 for con4 in image if any(Con4 in con4 for Con4 in condition4Keyword)]

for images4 in condition4:
    shutil.move(imageMondaySourceLocation+images4, testingLocation4)



condition5Keyword = ['oi']
condition5 = [con5 for con5 in image if any(Con5 in con5 for Con5 in condition5Keyword)]

for images5 in condition5:
    shutil.move(imageMondaySourceLocation+images5, testingLocation5)



condition6Keyword = ['5fas']
condition6 = [con6 for con6 in image if any(Con6 in con6 for Con6 in condition6Keyword)]

for images6 in condition6:
    shutil.move(imageMondaySourceLocation+images6, testingLocation6)






