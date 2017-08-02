# backup-to-zip

*Author*: Nicholas P. Taliceo
*Date*: 01 August 2017

## Purpose

To create a Python script that allows for an input directory and copies all folders and files in said folder and creates a compressed ZIP file in an output directory.

Inspiration for this script is to backup an external harddrive to a cloud-based storage system. Of course, this will also work for specific file paths, or general harddrives.

## Details

- Utilizes Python 3
- Originally built within PyCharm 2016.2.3; Windows 10

## Usage

* Open backup_to_zip.py in a Python 3+ IDE. Run this script.
* The first parameter is the **directory to be saved**. 
  * Input the pathname *exactly* as it appears in Windows Explorer.
* The second parameter is the output path, aka, **where the ZIP file will be saved.**

## Further Work

* Ideally, it would be great to figure out a way to programmatically backup my files, say at 09:00 on the first of every month.
  * This can only be done if the cloud storage path is logged-in **and** if the computer is on.
  * If the computer isn't on, then begin backing up files upon start up.
