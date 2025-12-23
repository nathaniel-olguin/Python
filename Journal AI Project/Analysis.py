#⭐️ analysis.py ⭐

#Handles:
#    reading the text
#    analyzing it
#    returning results
#    saving a report into reports


#IMPORTS
import os
from datetime import datetime


#FUNCTIONS
def character_count(file):    #the entry-dating formating is 45-ish (spacing and \n lines) characters long
    global simple_date
    timestamp_count = file.count(simple_date)    #counting the amount of times my entry-datetime formatting is present
    final_count = len(file) - (timestamp_count * round(45.5))    #wordcount - the number of timestamps
    print()    #space
    print(f'Journal Entries:      {timestamp_count}')    #number of times a journal entry was made calculated using the count of timestamps
    return f'Character Count:  {final_count}'    #word count


#VARIABLES
date = datetime.now()    #used for simple_date formatting
simple_date = date.strftime('%m-%d-%Y')    #used for locating each timestamp per entry

initial_directory = os.getcwd()    #reference
data_dir = f'{initial_directory}\\Data'    #directory that holds the files analysis.py will read
data_dir_list = os.listdir(data_dir)


#STEP 1  |  Read the latest journal 'Data' entry
print(data_dir_list)    #reference

if len(data_dir_list) < 2:    #if the 'Data' directory only has 1 entry read that entry
    with open(f'{data_dir}\\{data_dir_list[0]}', 'r') as data:
        content = data.read()
else:    #if the 'Data' directory has more than 1 entry read the latest(last) entry
    with open(f'{data_dir}\\{data_dir_list[-1]}', 'r') as data:
        content = data.read()
print(content)


#STEP 2  |  Anaylize the 'content'
print(character_count(content))
