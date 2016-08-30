import cardbase
from msvcrt import getch
from msvcrt import kbhit

if __name__ == "__main__":
	cards = cardbase.cardreader('python', 'python', '127.0.0.1', 'cardreader_development', 'students')
	print "Press 'd' to delete card or 'r' to reassign card\n"
	while True:
		try:
			print "Scan card to continue. "
			delete = False
			reassign = False
			if kbhit() == 1:
				key = ord(getch())
				if key == 100:
					delete = True
				elif key == 114:
					reassign = True
				else:
					pass
			cuid = cards.readSerial()
			print "Card read! UID: " + cuid
			if cards.cursorRowcount(cuid) == 1:
				cards.printCard(cuid)
				if delete:
					if raw_input("Are you sure you want to delete? (Y/N) \n").lower() == 'y':
						cards.deleteStudent(cuid)
						print "Student Deleted"
					else:
						pass
				elif reassign:
					if raw_input("Are you sure you want to reassign? (Y/N) \n").lower() == 'y':
						cards.reassignCard(cuid, raw_input("Please enter new name: \n"))
						print "Card with UID: {!s} reassigned".format(cuid)
					else:
						pass
				else:
					pass
			else:
				print "Card not in database"
				add = raw_input('Would you like to add new card? (Y/N)\n')
				if add.lower() == 'y':
					cards.addStudent(raw_input('Enter Name:\n'), cuid)
					
				else:
					pass
	

		except(KeyboardInterrupt, SystemExit):
			cards.quitCardbase()