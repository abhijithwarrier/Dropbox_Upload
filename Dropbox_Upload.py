# Programmer - python_scripts (Abhijith Warrier)

# A PYTHON SCRIPT TO UPLOAD FILES TO DROPBOX USING dropbox MODULE

# Importing the necessary packages
import os
import dropbox

# ---

# Defining Dropbox_Upload() with the user-input file as the input token
def Dropbox_Upload(input_file):
    # In order to make calls to the API, an instance of the Dropbox object has to be created.
    # Accessing the Dropbox account with the access token
    client = dropbox.Dropbox('YOUR ACCESS TOKEN')
    # Storing the folder in which file has to be uploaded (THIS IS OPTIONAL).
    # Only '/' indicated Dropbox root folder
    dropbox_upload_folder = '/Python_DropBox/'

    # Looping through each file present in the input_file[]
    for f in input_file:
        # Opening the user-input file in read-binary mode
        with open(f, 'rb') as i_file:
            # Fetching only file's name from f using os.path.basename() & storing in upload_filename
            upload_filename = os.path.basename(f)
            # Uploading file using files_upload() of dropbox.Dropbox class which takes 2 arguments
            # 1 - Contents of the input file (i_file) to be uploaded which is read using the read()
            # 2 - Name in which file will be uploaded along with optional Dropbox Folder
            client.files_upload(i_file.read(), dropbox_upload_folder + upload_filename)
            print("\n"+upload_filename+" UPLOADED SUCCESSFULLY TO "+dropbox_upload_folder)

# Driver Code
if __name__ == '__main__':
    # Creating an empty list named files_select
    file_list = []
    # Prompting the user to enter the file to upload to Dropbox
    print("\nSELECT THE FILES TO UPLOAD. ENTER DONE ONCE THE FILES ARE SELECTED \n")
    while True:
        # Storing the user-input file in file_input
        file_input = input("FILENAME : ")

        # Checking if the user-input is not done. If not done, then append file to the file_list
        if file_input.lower() != "done":
            file_list.append(file_input)
        # If user-input is done, then call Dropbox_Upload() with the file_list as the argument
        else:
            # Calling the Dropbox_Upload with the user-list file as the argument
            Dropbox_Upload(file_list)
            break

# ---
