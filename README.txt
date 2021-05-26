
*********************************BIRTHDAY REMINDER********************************
**********************************************************************************

This script is a birthday reminder which notifies you if there is any birthday celebration
for a friend on one of the days you have in your database.txt file.

win10toast was used to display nofications of birthdays. This is not part of the standard python
modules, use PIP INSTALL win10toast to install.

The progam is working perfectly fine. All that you have to do is to add it to startup, so it runs anytime
you start your PC to check if there is any birthday on that day.

 - REQUIRED MODULES -

Time
datetime
os
winsound
win10toast (needs pip to install)

NOTE: You would need to create a database.txt file where the birthday and names of friends would be. The 
python program would run through this file every startup (You can use a scheduler) to check for a birthday for that day.

Content of the database.txt file should be in this format:

	>> Month-Day Firstname Lastname
    e.g >> 05-23 John Doe

- ADDITIONAL FILES - 

image - birthday.ico
sound - happyBirthday.wav


