#!/bin/env python2.7
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#                                                        cardbase.py                                                           #
#                     python module used in conjuction with an arduino and the MRC522 reader and MySQL                         #
#                                                   date:08/08/2016                                                            #
#                                             author: Joshua Daniels-Holgate                                                   #
#                               project site: github.com/vaemavric/projects/cardreader                                         #
#                                                 written in notepad++                                                         #
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
import serial
import serial.tools.list_ports as list_ports
import mysql.connector
from mysql.connector import errorcode
import datetime
from datetime import date, datetime
from msvcrt import getch
from msvcrt import kbhit
from time import sleep

#Requires a MySQL 5.7 database with engine: InnoDB and columns: 'name' (VARCHAR(45)), 'year' (VARCHAR(255)), 
#'age' (VARCHAR(255)), 'contact' (VARCHAR(255))  'cuid' (VARCHAR(45)), 'created' (DATE), 'updated' (DATE), 
#'school' (VARCHAR(255))

#requires a FULLTEXT index on column 'cuid'
#if used in conjuction with ruby on rails webserver, create the model using rails and then edit using SQL queries or MySQL workbench
#import the module
#create instance of the 'cardreader' class with the arguments host IP address, database name, table name and optionally username and password for root MySQL account
class cardreader:
	today = datetime.now().date()
	def __init__(self, h, db, table, un="admin", pw="adminpass"):
		self.un = un
		self.pw = pw
		self.h=h
		self.db = db
		self.table =table
		#create a database connection
		try:
			self.cnx = mysql.connector.connect(user=un, password=pw, host =h, database=db)
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Something is wrong with your user name or password")
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print("Database does not exist")
			else:
				print(err)
		#create database cursor
		self.cursor = self.cnx.cursor()
			
		
	
	#automatically detect the com port that the arduino is operating on
	#currently windows only
	def connectArduino():
		ports = list(list_ports.comports())
		for p in ports:
			if "USB-SERIAL CH340" in p[1]:
				ard = p[0]
				#ard = p[1][-6:-1]
		try:
			
			print " Arduino connected on: " + ard
			return serial.Serial(ard)
		except:
			print("Unable to connect to arduino")
			quit()
			
	ser = connectArduino()
	
	def readSerial(self):
		return self.ser.readline().replace(" ", "").rstrip()
	
	#CRUD functions, self explanatory names
	def addStudent(self, name, cuid, school, year = "ENTER YEAR", age = "ENTER AGE", contact = "ENTER CONTACT"):
		try:
			self.cursor.execute("INSERT INTO {!s} (name, year, age, contact, cuid, created, updated, school) VALUES ('{!s}', '{!s}', '{!s}', '{!s}', '{!s}', '{!s}', '{!s}', '{!s}')".format(self.table, name, year, age, contact, cuid, self.today, self.today, school))
			self.cnx.commit()
		except:
			self.cnx.rollback()
			print("Error adding Student")
	def deleteStudent(self, cuid):
		try:
			self.cursor.execute("DELETE FROM {!s} WHERE cuid =  '{!s}' LIMIT 1".format(self.table, cuid))
			self.cnx.commit()
		except:
			self.cnx.rollback()
			print("Error deleting student")
	def updateStudent(self, cuid):
		try:
			self.cursor.execute("UPDATE {!s} SET updated = '{!s}' WHERE cuid = '{!s}'".format(self.table, self.today, cuid))
			self.cnx.commit()
		except:
			self.cnx.rollback()
			print("Error updating last login")
	def reassignCard(self, cuid, name):
		try:
			self.cursor.execute("UPDATE {!s} SET Name = '{!s}' WHERE cuid = '{!s}'".format(self.table, name, cuid))
			self.cnx.commit()
		except:
			self.cnx.rollback()
			print("Error reassigning card")
	
	def findCard(self, cuid):
		self.cursor.execute("SELECT name, cuid, created, updated FROM {!s} WHERE MATCH(cuid) AGAINST('{!s}')".format(self.table, cuid))
	#prints the result of a database search
	def printCard(self, cuid):
		self.findCard(cuid)
		for (Name, cuid, created, updated) in self.cursor:
			print("{}, {} was created on {:%d %b %Y} and last logged in {:%d %b %Y} \n".format(cuid, Name, created, updated))
	#a function to return the number of rows returned from the database querey (should be 1 or 0)
	def cursorRowcount(self, cuid):
		self.findCard(cuid)
		self.cursor.fetchall()
		return self.cursor.rowcount
			
	def quitCardbase(self):
		print"Quitting cardbase.py..."
		print"Closing cursor"
		self.cursor.close()
		print"Closing Database connection"
		self.cnx.rollback()
		self.cnx.close()
		print "Closing serial"
		self.ser.close()
		print"Quitting"
		quit()	

	

	
if __name__ == "__main__":
	#creating an instance of the cardreader object. In this case connects to MySQL isntance running on my webserver.
	cards = cardreader('54.194.12.154', 'register_development', 'students')
	print "Press 'd' to delete card or 'r' to reassign card\n"
	print "Press control+c or command+c to quit"
	print "Scan card to continue. "
	while True:
		try:

			#code to get the cuid of the card being presented
			#CHANGE TO TRY/EXCEPT SO THAT CODE DOES NOT HANG
			if(cards.ser.inWaiting()!=0):
				delete = False
				reassign = False
				#code to detect keypresses to change mode
				if kbhit() == 1:
					key = ord(getch())
					#100 = keycode for 'd'
					if key == 100:
						delete = True
					#114 = keycode for 'r'
					elif key == 114:
						reassign = True
					else:
						pass
				cuid = cards.readSerial()
				#message to show that there has been a successful card read and its cuid
				print "Card read! UID: " + cuid
				#THIS CODE SHOULD ONLY RUN IF A CARD IS DETECTED
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
						cards.updateStudent(cuid)
						pass
				else:
					print "Card not in database"
					add = raw_input('Would you like to add new card? (Y/N)\n')
					if add.lower() == 'y':
						cards.addStudent(raw_input('Enter Name:\n'), cuid, raw_input('Enter School:\n'))	
					else:
						pass
				print "Scan card to continue. "
			else:
				
				pass
		#quits python script when command c is pressed
		except(KeyboardInterrupt, SystemExit):
			cards.quitCardbase()