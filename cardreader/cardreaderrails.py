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
	cnx = mysql.connector.connect(user='root', password= "root", host = '127.0.0.1', database='cardreader_development')
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your user name or password")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	else:
		print(err)

#create cursor object		
cursor = cnx.cursor()

#queries & commands for MySQL database
add_student = ("INSERT INTO students (name, cuid, created, updated) VALUES (%s, %s, %s, %s)")
delete_student = ("DELETE FROM students WHERE cuid =  '{!s}' LIMIT 1")
update_updated = ("UPDATE students SET updated = '{!s}' WHERE cuid = '{!s}'")
reassign_card = ("UPDATE students SET Name = '{!s}' WHERE cuid = '{!s}'")

createq = ("SELECT Name, cuid, created, updated FROM students "
		"WHERE created BETWEEN %s and %s")
updatedq = ("SELECT Name, cuid, created, updated FROM students "
		"WHERE updated BETWEEN %s and %s")
cardq = ("SELECT name, cuid, created, updated FROM students "
			"WHERE MATCH(cuid) AGAINST('{!s}')")		


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
			for (Name, cuid, created, updated) in cursor:
				print("{}, {} was created on {:%d %b %Y} and last logged in {:%d %b %Y} \n".format(cuid, Name, created, updated))
			try:
				cursor.execute(update_updated.format(today, UID))
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
				new_name = raw_input("Please enter new name: \n")
				try:
					cursor.execute(reassign_card.format(new_name, UID))
					cnx.commit()
					print("Updated name")
				except:
					cnx.rollback()
					print("Something went wrong updating user")
			else:
				pass
			
		else:
			print "Card not in database"
			add = raw_input('Would you like to add new card? (Y/N)\n')
			if add.lower() == 'y':
				name =  raw_input('Enter Name:\n')
				data_student = (name, UID, today, today)
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
