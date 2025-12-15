#PROJECT:    Video/Audio File Organizer
#SKILLS:    This uses loops, conditionals, imports, and practical applications
#NOTES:    converted my image file types organizer into a Video/Audio file organizer


#IMPORTS
import os
import shutil


#STEP 1 - Obtain starting directory and assign to variable
initial_directory = os.getcwd()
initial_directory_list = os.listdir(os.getcwd())
print(initial_directory)    #for reference


#STEP 2 - Creating image file type folders
#video ↴
os.makedirs('Video Files\\MP4', exist_ok=True)
os.chdir('Video Files')    #update current directory to the newly created folder 'Video Files'
video_directory = os.getcwd()
os.makedirs('MOV', exist_ok=True)
os.makedirs('WEBM', exist_ok=True)
os.makedirs('MPEG-2', exist_ok=True)
os.makedirs('AVI', exist_ok=True)
#audio ↴
os.chdir(initial_directory)    #return to the initial directory 
os.makedirs('Audio Files\\MP3', exist_ok=True)
os.chdir('Audio Files')    #update current directory to the newly created folder 'Audio Files'
audio_directory = os.getcwd()
os.makedirs('AAC', exist_ok=True)
os.makedirs('WAV', exist_ok=True)
os.makedirs('FLAC', exist_ok=True)
os.makedirs('OGG', exist_ok=True)


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
#video  ↴
        if '.mp4' in file_name or '.MP4' in file_name:
            print('File Type:  MP4')
            shutil.move(file_name, f'{video_directory}\\MP4')
        elif '.mov' in file_name or '.MOV' in file_name:
            print('File Type:  MOV')
            shutil.move(file_name, f'{video_directory}\\MOV')
        elif '.webm' in file_name or '.WEBM' in file_name:
            print('File Type:  WEBM')
            shutil.move(file_name, f'{video_directory}\\WEBM')
        elif '.mpg' in file_name or '.mpeg' in file_name or '.MPG' in file_name or '.MPEG' in file_name:
            print('File Type:  MPEG-2')
            shutil.move(file_name, f'{video_directory}\\MPEG-2')
        elif '.avi' in file_name or '.AVI' in file_name:
            print('File Type:  AVI')
            shutil.move(file_name, f'{video_directory}\\AVI')
#audio ↴
        elif '.mp3' in file_name or '.MP3' in file_name:
            print('File Type:  MP3')
            shutil.move(file_name, f'{audio_directory}\\MP3')
        elif '.aac' in file_name or '.m4a' in file_name or '.AAC' in file_name or '.M4A' in file_name:
            print('File Type:  AAC / M4A')
            shutil.move(file_name, f'{audio_directory}\\AAC')
        elif '.wav' in file_name or '.WAV' in file_name:
            print('File Type:  WAV')
            shutil.move(file_name, f'{audio_directory}\\WAV')
        elif '.flac' in file_name or '.FLAC' in file_name:
            print('File Type:  FLAC')
            shutil.move(file_name, f'{new_directory}\\FLAC')
        elif '.ogg' in file_name or '.OGG' in file_name:
            print('File Type:  Ogg Vorbis')
            shutil.move(file_name, f'{new_directory}\\OGG')

        else:
            print('File Type:  NOT a Video/Audio File type')

    else:
        print('File not found')    #verifying the file exists
    

#STEP 4 - end results
print()
print(initial_directory_list)    #verifying all the files from the initial directory have been viewed
print()
print(new_directory)    #for reference
