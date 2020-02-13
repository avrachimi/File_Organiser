from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

folders = ["1_Images", "2_PDFs", "3_ZIP", "4_DMGs", "5_Word", "6_PowerPoint", "7_Excel", "8_Other", "9_Folders"]

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):

        ''' Created a list for each type of items since I might add more extensions in the future '''
        imageExtensions = [".jpg", ".JPG", ".jpeg", ".JPEG", ".png", ".PNG", ".heic", ".HEIC"]
        pdfExtensions = [".pdf", ".PDF"]
        zipExtensions = [".zip", ".tar", ".ZIP", ".TAR"]
        dmgExtensions = [".dmg", ".DMG"]
        wordExtensions = [".docx", ".doc", ".DOCX", ".DOC"]
        powerpointExtensions = [".ppt", ".pptx", ".PPT", ".PPTX"]
        excelExtensions = [".csv", ".xlsx", ".xlsm", ".CSV", ".XLSX", ".XLSM"]



        for filename in os.listdir(folder_to_track):

            filename, extension = os.path.splitext(filename)
            src = folder_to_track + "/" + filename + extension
            new_destination = ""

            if (filename not in folders):
                if (extension in imageExtensions):
                    new_destination = folder_to_track + "/1_Images/" + filename + extension
                elif (extension in pdfExtensions):
                    new_destination = folder_to_track + "/2_PDFs/" + filename + extension
                elif (extension in zipExtensions):
                    new_destination = folder_to_track + "/3_ZIP/" + filename + extension
                elif (extension in dmgExtensions):
                    new_destination = folder_to_track + "/4_DMGs/" + filename + extension
                elif (extension in wordExtensions):
                    new_destination = folder_to_track + "/5_Word/" + filename + extension
                elif (extension in powerpointExtensions):
                    new_destination = folder_to_track + "/6_PowerPoint/" + filename + extension
                elif (extension in excelExtensions):
                    new_destination = folder_to_track + "/7_Excel/" + filename + extension
                elif (extension == ""):
                    new_destination = folder_to_track + "/9_Folders/" + filename + extension
                else:
                    new_destination = folder_to_track + "/8_Other/" + filename + extension

                os.rename(src, new_destination)


# Change directory depending on your username and your desired directory
folder_to_track = "/Users/smems/Dropbox"
event_handler = MyHandler()

try:
    for folderName in folders:
        os.mkdir(folder_to_track + "/" + folderName)

except OSError:
    print ("Creation of the directories failed.")
else:
    print ("Successfully created the directories.")

observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)

observer.start()

try:
    while (True):
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()