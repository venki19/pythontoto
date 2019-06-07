import os
import shutil
os.chdir('C:\\Users\\rathodv\\Downloads\\') #Make sure you add your source and destination path below

dir_src = ("C:\\Users\\rathodv\\Downloads\\")
dir_dst = ("C:\\Users\\rathodv\\Pictures\\Saved Pictures\\")

for filename in os.listdir("C:\\Users\\rathodv\\Downloads\\"):
    if filename.endswith('.pdf'):
        shutil.copy(dir_src + filename, dir_dst)
    print(filename)


import os
import shutil
os.chdir('C:\\Users\\rathodv\\Downloads\\') #Make sure you add your source and destination path below

dir_src = ("C:\\Users\\rathodv\\Downloads\\")
dir_dst = ("C:\\Users\\rathodv\\Pictures\\Saved Pictures\\")

for filename in os.listdir("C:\\Users\\rathodv\\Downloads\\"):
    if filename.__contains__('2018-04-05'):
        shutil.copy(dir_src + filename, dir_dst)
    print(filename)


import os
import shutil
os.chdir('C:\\Users\\rathodv\\Downloads\\') #Make sure you add your source and destination path below

dir_src = ("C:\\Users\\rathodv\\Downloads\\")
dir_dst = ("C:\\Users\\rathodv\\Pictures\\Saved Pictures\\")

for filename in os.listdir("C:\\Users\\rathodv\\Downloads\\"):
    if filename.startswith('N') and filename.endswith('.msg'):
        shutil.copy(dir_src + filename, dir_dst)
    print(filename)