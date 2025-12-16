#⭐️ journal.py ⭐️

#Handles:
#	•	getting the text from the user
#	•	saving it into data/entries


#IMPORTS
import os
import shutil
from datetime import datetime


#BASE DEF
def space():
    for count in range(2):
        print()


#VARIABLES
date = datetime.now()
formatted_date = date.strftime('%m-%d-%Y  -  %A %I.%M.%S %p')    #including the '%S' is important as with each passing second the file name changes and therefore if the user enters multiple 'journal entries' in quick succession multiple files will be created for the same day (I may need to update this with the 'a', append, in the future to avoid creating a massive amount of files
#need to create a new date format for the 'a', append, feature to avoid spam


#STEP 1  |  user input
try:
    daily_entry = input()
except EOFError:    #enter with nothing
    daily_entry = ''
finally:
    print(formatted_sdate)
    space()
    print(daily_entry)
    space()

    

#STEP 2  |  creating an 'entry file'
initial_directory = os.getcwd()
print(initial_directory)    #for reference

with open(f'Daily Journal  -  {formatted_date}.md', 'w') as entry:
    entry.write(f'#{formatted_date} \n \n{daily_entry}')
