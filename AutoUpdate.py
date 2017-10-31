#Auto Download and install Elvui
import zipfile
import os
import requests
from tqdm import tqdm
import shutil
def main():
    #does user know the current version?
    q = input("Do you know what version ElvUi is on?")
    if q != 'yes' or q != 'Yes':
        print("Falling back on known existing version! Starting ElvUi 10.68 Install")
        version = str(10.68)
    else:
        version = str(input('Input the version of ElvUi. Include the main version.\n Ex. 10.68\n'))

    #get wow install directory

    install = input('Please input wow install directory. Use two backslashes\n Ex. C:\\Program Files\\World of Warcraft')
    #delete current install

    try:
        shutil.rmtree(install+'\\Interface\\AddOns\\ElvUi')
        shutil.rmtree(install+'\\Interface\\AddOns\\ElvUi_Config')
        print("Previous install removed.Settings have been preserved.")
    except:
        print("ElvUi is not installed!")
    location=os.getcwd()
    #not my code, downloads elvui

    url = "https://www.tukui.org/downloads/elvui-"+version+".zip"
    response = requests.get(url, stream=True)
    print ('Starting Download!')
    with open("elvui-10.68.zip", "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)
    print ('Download Complete!\n Starting Install!')

    f = zipfile.ZipFile(location+'\\elvui-'+version+'.zip')
    f.extractall(install+'\\Interface\\AddOns')
    f.close()

    print ("Cleaning up...")

    os.remove(location+'\\elvui-'+version+'.zip')
    print("ElvUi Successfully updated to "+version)
main()

