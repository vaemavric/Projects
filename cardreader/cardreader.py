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
from datetime import date, datetime, timedelta
today = datetime.now().date()
tomorrow = datetime.now().date() + timedelta(days=1)
#connect to mysql database
try:
	cnx = mysql.connector.connect(user='python', password= "python", host = '127.0.0.1', database='students')
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your user name or password")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	else:
		print(err)
	
cursor = cnx.cursor()
add_student = ("INSERT INTO students (Name, Card_Number, DateC, LastL) VALUES (%s, %s, %s, %s)")
#data_student = ('James', 'hello', today, tomorrow)
#cursor.execute(add_student, data_student)
#cnx.commit()

query = ("SELECT Name, Card_Number, DateC, LastL FROM students "
		"WHERE DateC BETWEEN %s and %s")
cardquery = ("SELECT Name, Card_Number, DateC, LastL FROM students "
			"WHERE MATCH(Card_Number) AGAINST('{!s}')")		
#cursor.execute(query, ("2016-07-09", tomorrow))
#for (Name, Card_Number, DateC, LastL) in cursor:
#	print("{}, {} was created on {:%d %b %Y} and last logged in {:%d %b %Y}".format(
#    Card_Number, Name, DateC, LastL))

#ser =  serial.Serial("COM15")

#code for auto selecting arduino board
ports = list(serial.tools.list_ports.comports())
for p in ports:
	if "USB-SERIAL CH340" in p[1]:
		ard = p[1][-6:-1]
print " Arduino connected on: " + ard
ser = serial.Serial(ard)

while True:
	try:
		UID =  ser.readline().replace(" ", "").rstrip()
		print "Card read! UID: " + UID
		
		cursor.execute(cardquery.format(UID))
		cursor.fetchall()
		if cursor.rowcount == 1:
			cursor.execute(cardquery.format(UID))
			for (Name, Card_Number, DateC, LastL) in cursor:
				print("{}, {} was created on {:%d %b %Y} and last logged in {:%d %b %Y}".format(Card_Number, Name, DateC, LastL))
				print("\n")
		else:
			print "Card not recorded"
			add = raw_input('Would you like to add new card? (y/n)\n')
			if add == 'y':
				name =  raw_input('Enter Name:\n')
				data_student = (name, UID, today, today)
				try:
					cursor.execute(add_student, data_student)
					cnx.commit()
				except:
					cursor.rollback()
				print 'User added'
			else:
				pass
			print("\n")
	except(KeyboardInterrupt, SystemExit):
		print"Quitting cardreader.py..."
		print"Closing cursor"
		cursor.close()
		print"Closing Database connection"
		cnx.close()
		print"Quitting"
		quit()
cursor.close()
cnx.close()
quit()