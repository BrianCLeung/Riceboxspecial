# code and function for moving files.

import os

target_folder = r'D:\Target folder\fallout' + '\\' # Transfer files TO this folder.
source_folder = r'D:\Game screenshots\Fallout4' + '\\' # Transfer files FROM this folder.

# for path, dir, files in os.walk(source_folder):
#     if files:
#         for file in files:
#             if not os.path.isfile(target_folder + file):
#                 os.rename(path + '\\' + file, target_folder + file)


def move_files(sourceFolder, targetFolder):
    try:
        for path, dir, files in os.walk(sourceFolder):
            if files:
                for file in files:
                    if not os.path.isfile(targetFolder + file):
                        os.rename(path + '\\' + file, targetFolder + file)
        print('All files moved')
    except Exception as e:
        print(e)

move_files(source_folder, target_folder)