'''backup_to_zip_sched.py

PURPOSE: This script asks the user for a directory to create a backup ZIP file
         that is then stored in another directory. This is geared to save a
         copy said files in the Desktop version of cloud-based storage, such as
         OneDrive, Google Drive, Box, Dropbox, or otherwise.

         This is ultimately an improvement on backup_to_zip.py that includes the
         option of scheduling backup times.

FURTHER
READING: This code was created, in part from:
         https://automatetheboringstuff.com/chapter9/

         Hidden file detection was inspired from this thread:
         https://stackoverflow.com/questions/284115/cross-platform-hidden-file-
         detection/6365265#6365265

         To compress the ZIP file, follow this thread:
         https://stackoverflow.com/questions/18151839/python-zipfile-module-
         doesnt-compress-files

         An overview of the event scheduler (sched) module:
         https://docs.python.org/3/library/sched.html#module-sched

INPUT:   folder = the input folder or directory to save as a ZIP file
         output = the output location to save the ZIP file

AUTHOR:  Nicholas P. Taliceo | ntaliceo@gmail.com
         www.NicholasTaliceo.com

DATE:    06 August 2017
'''

import ctypes
import datetime
import os
import zipfile
import zlib

from numpy import unicode


def is_hidden(filepath):
    name = os.path.basename(os.path.abspath(filepath))
    return name.startswith('.') or has_hidden_attribute(filepath)


def has_hidden_attribute(filepath):
    try:
        attrs = ctypes.windll.kernel32.GetFileAttributesW(unicode(filepath))
        assert attrs != -1
        result = bool(attrs & 2)
    except (AttributeError, AssertionError):
        result = False
    return result


def backup_to_zip(directory, output):
    # Backup the entire contents of "folder" into a ZIP file.
    thedir = os.path.abspath(directory)

    # Determine the ZIP filename.
    zip_file_name = datetime.datetime.today().strftime('%Y%m%d') + '.zip'

    # Create the ZIP file.
    print('Creating %s...' % zip_file_name)
    backup_zip = zipfile.ZipFile(os.path.abspath(output) + '\\' +
                                 zip_file_name, 'w', zipfile.ZIP_DEFLATED)

    # For each top-level folder in the directory, walk through each folder
    # and compress all files found in that folder.
    for top_folder in os.listdir(thedir):
        # Exclude the archive folder, which contains PC backup (file too large).
        if top_folder != 'archive':
            path = os.path.join(thedir, top_folder)

            # Walk the entire folder tree and compress the files in each folder.
            for foldername, subfolders, filenames in os.walk(path,
                                                             topdown=True):
                if has_hidden_attribute(path):
                    pass
                else:
                    try:
                        print('Adding files in %s...' % foldername)
                        # Add the current folder to the ZIP file.
                        backup_zip.write(foldername)
                        # Add all the files in this folder to the ZIP file.
                        for filename in filenames:
                            new_base = os.path.basename(path) + '_'
                            if filename.startswith(
                                    new_base) and filename.endswith(
                                    '.zip'):
                                continue  # Don't backup the backup ZIP files.
                            backup_zip.write(os.path.join(foldername, filename))
                    except (PermissionError, OSError):
                        pass

    backup_zip.close()
    print("Done.")


directory = 'G:\\'
output = 'C:\\Users\\Nick\\Box Sync\\archive'
backup_to_zip(directory, output)
