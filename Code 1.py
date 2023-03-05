import requests
import hashlib
import subprocess
import os



def STEP1():

    # Send GET message to download the file
    file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe.sha256'
    resp_msg = requests.get(file_url)
    # Check whether the download was successful
    if resp_msg.status_code == requests.codes.ok:
    # Extract binary file content from response message body

        file_content = resp_msg.content
        x = file_content.split()
        # Print the hash value
        return x[0]

def STEP2():

    # Send GET message to download the file
    file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe'
    resp_msg = requests.get(file_url)
    # Check whether the download was successful
    if resp_msg.status_code == requests.codes.ok:
    # Extract binary file content from response message body

        file_content = resp_msg.content
        
        # Print the hash value
        return file_content



def STEP3(file_content, x):

    # Calculate SHA-256 hash value
    image_hash = hashlib.sha256(file_content).hexdigest()

    print(x, image_hash)
    a = x.decode("utf-8")
    if a == image_hash:
        print("Both files are same")
        print(f"Hash: {a}")
 
    else:
        print("Files are different!")


def STEP4(file_content):


    # Save the binary file to disk
    with open(r'C:\Users\Owner\Desktop\SEMESTER4\Scripting\COMP593-Lab6\Result.exe', 'wb') as file:
        file.write(file_content)
        print("File has been saved to disk")


def STEP5():

   
    installer_path = r'C:\Users\Owner\Desktop\SEMESTER4\Scripting\COMP593-Lab6\Result.exe'
    subprocess.run([installer_path, '/L=1033', '/S'])
    
    print("File is executed and is run silently")
    return installer_path


def STEP6(installer_path):

    os.remove(installer_path)
    print("File has been removed as requested")

def main():
    x = STEP1()
    file_content = STEP2()
    STEP3(file_content, x)
    STEP4(file_content)
    installer_path = STEP5()
    STEP6(installer_path)
main()
