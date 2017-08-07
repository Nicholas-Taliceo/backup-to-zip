# Backup to ZIP Scheduling Instructions
The overall goal of the `backup_to_zip.py` file is to allow the script to automatically run without user interference. This means that we ultimately *don't want* to open Python every time the computer reboots; we also don't want to input several parameters.

Rather, it would be preferable to find a way to *program* this script to start and execute at a particular time, with little or no user interference.

### Goals
1. Create a modified version of `backup_to_zip.py` that does not require asking the user from what directory to copy files and where to store the compressed ZIP file.
2. Allow the program to wait until the first of the month to execute the backup file.
3. If the computer is powered-down, wait until the next reboot to execute the Python script.
4. If possible, ask the user if s/he wants to take the time to backup the files, or wait until another specified time.
