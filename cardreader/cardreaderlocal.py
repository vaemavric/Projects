#!/bin/env python2.7
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#                                                      cardreader.py                                                           #
#                          python script used in conjuction with an arduino and the MRC522 reader                              #
#                                                   date:09/07/2016                                                            #
#                                             author: Joshua Daniels-Holgate                                                   #
#                                         site: github.com/vaemavric/projects                                                  #
#                                                 written in notepad++                                                         #
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

import serial
import serial.tools.list_ports
import mysql.connector
from mysql.connector import errorcode
import datetime
from datetime import date, datetime
from msvcrt import getch
from msvcrt import kbhit
from time import sleep
today = datetime.now().date()

#connect to mysql database
try:
	cnx = mysql.connector.connect(user='python', password= "python", host = '127.0.0.1', database='students')
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your user Name or password")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	else:
		print(err)

#create cursor object		
cursor = cnx.cursor()

#queries & commands for MySQL database
add_student = ("INSERT INTO students (Name, Card_Number, DateC, LastL) VALUES (%s, %s, %s, %s)")
delete_student = ("DELETE FROM students WHERE Card_Number =  '{!s}' LIMIT 1")
update_LastL = ("UPDATE students SET LastL = '{!s}' WHERE Card_Number = '{!s}'")
reassign_card = ("UPDATE students SET Name = '{!s}' WHERE Card_Number = '{!s}'")

createq = ("SELECT Name, Card_Number, DateC, LastL FROM students "
		"WHERE DateC BETWEEN %s and %s")
LastLq = ("SELECT Name, Card_Number, DateC, LastL FROM students "
		"WHERE LastL BETWEEN %s and %s")
cardq = ("SELECT Name, Card_Number, DateC, LastL FROM students "
			"WHERE MATCH(Card_Number) AGAINST('{!s}')")		


#code for auto selecting arduino board
ports = list(serial.tools.list_ports.comports())
for p in ports:
	if "USB-SERIAL CH340" in p[1]:
		ard = p[1][-6:-1]


try:
	ser = serial.Serial(ard)
	print " Arduino connected on: " + ard
except:
	print("Unable to connect to arduino")
	quit()
	

quite =  False
while True:
	try:
		UID =  ser.readline().replace(" ", "").rstrip()
		print "Card read! UID: " + UID
		
		cursor.execute(cardq.format(UID))
		cursor.fetchall()
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
		if cursor.rowcount == 1:
			cursor.execute(cardq.format(UID))
			for (Name, Card_Number, DateC, LastL) in cursor:
				print("{}, {} was DateC on {:%d %b %Y} and last logged in {:%d %b %Y} \n".format(Card_Number, Name, DateC, LastL))
			try:
				cursor.execute(update_LastL.format(today, UID))
				cnx.commit()
			except:
				cnx.rollback()
				print("Something went wrong updating student")
			if delete == True:
				d = raw_input("are you sure you want to delete? (Y/N) \n")
				if d.lower() == 'y':
					try:
						cursor.execute(delete_student.format(UID))
						cnx.commit()
						print("Student deleted")
					except:
						cnx.rollback()
						print("Something went wrong deleting student")
				else:
					pass
			elif reassign == True:
				new_Name = raw_input("Please enter new Name: \n")
				try:
					cursor.execute(reassign_card.format(new_Name, UID))
					cnx.commit()
					print("LastL Name")
				except:
					cnx.rollback()
					print("Something went wrong updating user")
			else:
				pass
			
		else:
			print "Card not in database"
			add = raw_input('Would you like to add new card? (Y/N)\n')
			if add.lower() == 'y':
				Name =  raw_input('Enter Name:\n')
				data_student = (Name, UID, today, today)
				try:
					cursor.execute(add_student, data_student)
					cnx.commit()
					print 'User added'
				except:
					cnx.rollback()
					print("Something went wrong adding new user.")
				
			else:
				pass
		
	except(KeyboardInterrupt, SystemExit):
		print"Quitting cardreader.py..."
		print"Closing cursor"
		cursor.close()
		cnx.rollback()
		print"Closing Database connection"
		cnx.close()
		print"Quitting"
		quit()
