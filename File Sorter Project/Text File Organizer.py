#PROJECT:    Text File Organizer
#SKILLS:    This uses loops, conditionals, imports, and practical applications
#NOTES:    turned my image file types organizer into a text file organizer


#IMPORTS
import os
import shutil


#STEP 1 - Obtain starting directory and assign to variable
initial_directory = os.getcwd()
initial_directory_list = os.listdir(os.getcwd())
print(initial_directory)    #for reference


#STEP 2 - Creating image file type folders
os.makedirs('Text Files\\PY', exist_ok=True)
os.chdir('Text Files')    #update initial directory to the newly created folder 'Text Files'
new_directory = os.getcwd()
os.makedirs('TXT', exist_ok=True)
os.makedirs('CSV', exist_ok=True)
os.makedirs('MD', exist_ok=True)
os.makedirs('XML', exist_ok=True)
os.makedirs('JSON', exist_ok=True)
os.makedirs('DOCX', exist_ok=True)
os.makedirs('DOC', exist_ok=True)
os.makedirs('RTF', exist_ok=True)
os.makedirs('ODT', exist_ok=True)
os.makedirs('PDF', exist_ok=True)
os.makedirs('HTML', exist_ok=True)
os.makedirs('HTM', exist_ok=True)
os.makedirs('CSS', exist_ok=True)
os.makedirs('JS', exist_ok=True)
os.makedirs('JAVA', exist_ok=True)
os.makedirs('PPTX', exist_ok=True)
os.makedirs('XLSX', exist_ok=True)


#STEP 3 - switch back to initial directory to verify file types
os.chdir(initial_directory)    #return to the initial directory 
while len(initial_directory_list) > 0:
    file_name = initial_directory_list.pop(0)    #first value of the list is removed and set to variable:  file_name
    print()
    print(file_name)
    if os.path.exists(file_name):    #verifying the file exists
        print('File Found')
        print(f'File Size:  {os.stat(file_name).st_size}')
        #verify image file type then move the file types into the new_directory, then the designated file type folder
        if '.py' in file_name or '.PY' in file_name:
            print('File Type:  PY')
            shutil.move(file_name, f'{new_directory}\\PY')
        elif '.txt' in file_name or '.TXT' in file_name:
            print('File Type:  TXT')
            shutil.move(file_name, f'{new_directory}\\TXT')
        elif '.csv' in file_name or '.CSV' in file_name:
            print('File Type:  CSV')
            shutil.move(file_name, f'{new_directory}\\CSV')
        elif '.md' in file_name or '.MD' in file_name:
            print('File Type:  MD')
            shutil.move(file_name, f'{new_directory}\\MD')
        elif '.xml' in file_name or '.XML' in file_name:
            print('File Type:  XML')
            shutil.move(file_name, f'{new_directory}\\XML')
        elif '.json' in file_name or '.JSON' in file_name:
            print('File Type:  JSON')
            shutil.move(file_name, f'{new_directory}\\JSON')
        elif '.docx' in file_name or '.DOCX' in file_name:
            print('File Type:  DOCX')
            shutil.move(file_name, f'{new_directory}\\DOCX')
        elif '.doc' in file_name or '.DOC' in file_name:
            print('File Type:  DOC')
            shutil.move(file_name, f'{new_directory}\\DOC')
        elif '.rtf' in file_name or '.RTF' in file_name:
            print('File Type:  RTF')
            shutil.move(file_name, f'{new_directory}\\RTF')
        elif '.odt' in file_name or '.ODT' in file_name:
            print('File Type:  ODT')
            shutil.move(file_name, f'{new_directory}\\ODT')
        elif '.pdf' in file_name or '.PDF' in file_name:
            print('File Type:  PDF')
            shutil.move(file_name, f'{new_directory}\\PDF')
        elif '.html' in file_name or '.HTML' in file_name:
            print('File Type:  HTML')
            shutil.move(file_name, f'{new_directory}\\HTML')
        elif '.htm' in file_name or '.HTM' in file_name:
            print('File Type:  HTM')
            shutil.move(file_name, f'{new_directory}\\HTM')
        elif '.css' in file_name or '.CSS' in file_name:
            print('File Type:  CSS')
            shutil.move(file_name, f'{new_directory}\\CSS')
        elif '.js' in file_name or '.JS' in file_name:
            print('File Type:  JS')
            shutil.move(file_name, f'{new_directory}\\JS')
        elif '.java' in file_name or '.JAVA' in file_name:
            print('File Type:  JAVA')
            shutil.move(file_name, f'{new_directory}\\JAVA')
        elif '.pptx' in file_name or '.PPTX' in file_name:
            print('File Type:  PPTX')
            shutil.move(file_name, f'{new_directory}\\PPTX')
        elif '.xlsx' in file_name or '.XLSX' in file_name:
            print('File Type:  XLSX')
            shutil.move(file_name, f'{new_directory}\\XLSX')
        else:
            print('File Type:  NOT a TEXT File type')

    else:
        print('File not found')    #verifying the file exists
    

#STEP 4 - end results
print()
print(initial_directory_list)    #verifying all the files from the initial directory have been viewed
print()
print(new_directory)    #for reference
