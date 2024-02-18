Python script that uses the os and hashlib modules to monitor changes in a directory. This script calculates the MD5 hash of all files in a directory and stores them. If a file’s hash changes, it means the file has been modified.

Please replace YOUR_DIRECTORY_PATH with the path of the directory you want to monitor.

This script only detects changes when it’s run, so you might want to schedule it to run at regular intervals using a tool like cron. 
Also, at the moment please note that this script does not handle file deletions or additions.
