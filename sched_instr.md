# Backup to ZIP Scheduling Instructions
The overall goal of the `backup_to_zip.py` file is to allow the script to automatically run without user interference. This means that we ultimately *don't want* to open Python every time the computer reboots; we also don't want to input several parameters.

Rather, it would be preferable to find a way to *program* this script to start and execute at a particular time, with little or no user interference.

### Goals
1. Create a modified version of `backup_to_zip.py` that does not require asking the user from what directory to copy files and where to store the compressed ZIP file.
2. Allow the program to wait until the first of the month to execute the backup file.
3. If the computer is powered-down, wait until the next reboot to execute the Python script.
4. If possible, ask the user if s/he wants to take the time to backup the files, or wait until another specified time.

### Resources
* [Automate the Boring Stuff - Schedulers](https://automatetheboringstuff.com/schedulers.html)
* [How to Automatically Run Programs and Set Reminders With the Windows Task Scheduler (How-To Geek)](https://www.howtogeek.com/123393/how-to-automatically-run-programs-and-set-reminders-with-the-windows-task-scheduler/)

### Instructions

*Note:* This will be using the *Windows* operating system.

1. In the search bar, type "Task Scheduler" and open the shortcut.
2. Click the Create Basic Task link at the right-hand side of the Task Scheduler window.
3. Add a name and description for the task. Click Next.
4. On the Task Trigger page, choose the Monthly radio button. Click Next.
    1. Choose the first of the subsequent month at 12:00.
    2. Check "Synchronize across time zones".
    3. Choose all months.
    4. Under "Days", choose the first (1).
    5. On
5. Under "Action" choose the "Start a program" radio button. Click Next.
    1. Click Browse... and select the program you wish to run.
    2. It is suggested that you choose to save this file directly under the C drive.
6. Review what has been established and click Finish.
7. Once the task has been created, navigate to where it is stored, right-click and click on Properties. In the Settings tab, check "Run task as soon as possible after a scheduled start is missed". Click OK.

### Supplemental Graphics in Task Scheduler

The "General" tab of Task Scheduler:

![Image of General Task Scheduler](https://github.com/Nicholas-Taliceo/backup-to-zip/blob/master/graphics/sched_general.png)

The "Trigger" tab of Task Scheduler:

![Image of Trigger Task Scheduler](https://github.com/Nicholas-Taliceo/backup-to-zip/blob/master/graphics/sched_trigger.png)

The "Action" tab of Task Scheduler:

![Image of Action Task Scheduler](https://github.com/Nicholas-Taliceo/backup-to-zip/blob/master/graphics/sched_action.png)
