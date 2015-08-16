#=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# cipheradv.py                                                                 #
# a python script to encrypt and decrypt a message or file using a specified-  #
# cipher                                                                       #
# date: 15/08/2015                                                             #
# author: vaemavric                                                            #
# written in vi                                                                #
#=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#boobs
# translate(mode, message, cipher) takes three arguements: 
#  mode (String): the mode the program is running in;
#  message (String): the message to be encoded;
#  cipher (String): the cipher used to encode the message
# returns the string 'translated'.
# The cipher used is different for each character in the message. (inc. spaces)
# Each letter is converted into its ascii key, which is then shifted down 32,
# so that the maths is easier. The cipher key is then added, and the resulting
# number is taken modulo 94, such that it will correspond to an ascii character
# 32 is then added such that the ascii code corresponds to a symbol.
def translate(mode, message, cipher):
 translated = ''
# This cipher argument given is a single string consisiting of several keys-  
# separated by spaces, this turns the cipher object into a list of these keys.
 cipher = cipher.split() 
# 'i' is a number used to record how many times the for loop has been carried-
# out, it is used to work out which key to encrypt each letter.  
 i = 0
# for loop, encrypts each letter invididually and adds them to the string-
# 'translated'
 for symbol in message:
  num = ord(symbol) -32
  if mode[0] == 'd':
   num += -int(cipher[i%len(cipher)])
  else:
   num += int(cipher[i%len(cipher)]) 
  num %= 94
  num += 32
  translated += chr(num)
  i += 1
 return translated

# translateFile(mode, cipher, filename) takes three arguements:
#  mode (String): the mode the program is running in;
#  cipher (String): the cipher used to encode the file;
#  filename (String): the txt file to be encoded. DO NOT INCLUDE FILE EXT
# The specified file is opened and each line is read, it is then passed to-
# the translate function, where it is encrypted/decrypted. The returned-
# string is then written to the output file as a new line
def translateFile(mode, cipher, filename):
# opens the input file as read only
 try:
  inp = open(filename  + '.txt', 'r')
 except:
  print('file does not exist')
# tests if the programing is running in encrypt or decrypt mode
 if mode[0] == 'd':
# removes 'encrypted' from the file name to avoid exsessive file names 
# creates a new file with the same name as the original file + decrypted
  if 'encrypted' in filename:
   filenew = filename.replace('encrypted', '')
   outp = open(filenew + 'decrypted.txt', 'w') 
# creates a new file with the same name as the original file + encrypted
  else:
   outp = open(filename + 'decrypted.txt', 'w')
 else:
  outp = open(filename + 'encrypted.txt', 'w')
 for i in range(file_len(filename)):
  line = inp.next()
  if mode[0] == 'd':
# remove the carriage return symbol.
   line = line.replace(line[-2:], '')
  outp.write(translate(mode, line, cipher))
  outp.write('\n') 
 inp.close()
 outp.close()
 

# getMode() returns the mode the program will run in, either encrypt or decrypt
def getMode():
 while True:
# a list of valid arguments
  validA = ['e', 'd', 'encrypt', 'decrypt']
  mode = raw_input('Do you want to encrypt or decrypt \n').lower()
  if mode in validA: 
   return mode
  else:
   print('mode is either %s' ) % validA

# getMessage() returns the message from user input
def getMessage():
   return raw_input('Enter message: \n')

# getCipher() returns the value of the cipher, from user input. It takes any-
# integer value
# the cipher entered should be in the form int int int. each int will be used-
# to encode the respective letter in a word.
def getCipher():
 return raw_input('enter cipher key:\n') 

# getFilename() returns the name of the file to be encrypted/decrypted from-
# user input
def getFilename():
 return raw_input('enter the filename:\n')

# file_len(filename) returns the number of lines in the file 
def file_len(filename):
 with open(filename + '.txt') as f:
  for i, index in enumerate(f):
   pass
  i += 1
  return i

try:
 translateFile(getMode(),
  getCipher(), getFilename()) 
except:
 print('application quit')
 quit()
