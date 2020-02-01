from win10toast import ToastNotifier
import time
import os
from datetime import datetime, timedelta
import winsound



iconPath = 'birthday.ico' #path for birthday icon

toaster = ToastNotifier() #create new toaster object

today = time.strftime('%m-%d') #string representation of today's Month and d

def main():
	file = open('database.txt', 'r')

	for line in file:
		if today in line:
			store(line)
			date_name = line.split(' ')
			date = date_name[0]
			firstname = date_name[1]
			lastname = date_name[2]

			winsound.PlaySound('happybirthday.wav', winsound.SND_ASYNC)

			toaster.show_toast("Hello User!",
			f"Today is {firstname}'s Birthday!\n\nGo to CELEBRANTS.TXT to see all the\ncelebrants.",
			 icon_path= iconPath,
			 duration=15)
			

	file.close()


def store(line):
	date_name = line.split(' ')
	date = date_name[0]
	firstname = date_name[1]
	lastname = date_name[2]

	file1 = open('celebrants.txt', 'a+') #a+ for appending and reading
	file1.seek(0) #To take the pointer to start of file
	lines = file1.read()

	dateString = datetime.strftime(datetime.today(), "%Y-%m-%d %H:%M")


	if dateString in lines:
		file1.write(firstname +" "+lastname)
	else:
		file1.write(dateString +"\n")
		file1.write(firstname +" "+lastname)

	file1.close()


if os.path.exists('celebrants.txt'):

	#Check if you can clear 'celebrants' file
	file2 = open('celebrants.txt', 'r')
	
	date = file2.readline().strip()
	dategroup = date.split(' ')
	date = dategroup[0]
	inddate = date.split('-')
	date1 = int(inddate[0])
	date2 = int(inddate[1])
	date3 = int(inddate[2])
	timegroup = dategroup[1]
	time = timegroup.split(':')
	time1 = int(time[0])
	time2 = int(time[1])

	olddate = datetime(date1, date2, date3, time1, time2)
	file2.close()

	currentTime = datetime.today()
	newdate = olddate + timedelta(minutes = 2)

	if currentTime >= newdate:
		os.remove('celebrants.txt')

else:
	main()

# if __name__ == '__main__':
# 	main()



