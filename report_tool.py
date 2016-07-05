import datetime
import logging
import os
import shutil
import sys
import mail_function

source_path = "./Sendfolder"
archive_path = "./SendFolder/Archive"

#logging configuration
logging.basicConfig(filename="C:\\SendFolder\\Logs\\info.log",
                     level=logging.INFO)

#create archive folder if not existent
if not os.path.isdir(archive_path):
    logging.info(datetime.datetime.now().strftime("%Y/%m/%d - %H:%M:%S Folder was not found, creating folder"))
    input("Folder was not found, creating folder. Press any key to continue: ")
    os.mkdir(archive_path)

# list to store .csv files
file_list = []

for each in [x for x in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, x))]:
    if each.endswith('csv'):
        file_list.append(each)

#check if csv files are found in file_list
if file_list != []:
    files_to_send = []
    for each in file_list:
        # check if files already contain the timestamp of: "%Y%m%d_" (20160330)

        try:
            date_check = each.split('_')[0][:8]
            year_ = int(date_check[0:4])
            month_ = int(date_check[4:6])
            day_ = int(date_check[6:8])
            datetime.date(year_, month_, day_)

        # no timestamp
        except ValueError as e:
            value_error_message = str(e)
            if value_error_message in ['day is out of range for month', 'month must be in 1..12']:
                print('We have a timestamp, just not a valid one.')
                print('Stripping invalid date, and placing a valid one.')
                rename_file = each.split('_')[0][8:]

            print("Renaming {0}".format(each))
            change_name = datetime.datetime.now().strftime("%Y%m%d_") + each
            os.rename(source_path + each, source_path + change_name)
            shutil.move(source_path + change_name, archive_path + change_name)
            files_to_send.append(change_name)

        # timestamp found
        else:
            # list of archive folder files
            archive_files = [x for x in os.listdir(archive_path) if os.path.isfile(os.path.join(archive_path, x))]

            # if file is already in the archive, pass
            if each in archive_files:
                pass

            # it's not in the archive, send it there
            else:
                print("Renaming {0}".format(each))
                change_name = datetime.datetime.now().strftime("%Y%m%d_") + each
                os.rename(source_path + each, source_path + change_name)
                shutil.move(source_path + change_name, archive_path + change_name)
                files_to_send.append(change_name)
    print(files_to_send)
    final_attachment = []
    final_attachment = final_attachment.append(files_to_send + each)
    mail_function.mail_send(final_attachment)

# csv files don't exist in the source_dir
else:
    print("No csv files found, exiting...")
    sys.exit()