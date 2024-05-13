import os, shutil
path = r"C:/Users/98912\Desktop/Python Tasks/Ordering files/"
file_name = os.listdir(path)

folder_names = ["ods files", "image files", "text files", "pdf files"]
for loop in range (0,4):
    if not os.path.exists (path + folder_names[loop]):
        print (path + folder_names[loop])
        os.makedirs((path + folder_names[loop]))
for file in file_name:
    if ".ods" in file and not os.path.exists(path + "ods files/" + file):
        shutil.move(path + file, path + "ods files/" + file)

    elif ".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)

    elif ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file)
    elif ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf files/" + file)
