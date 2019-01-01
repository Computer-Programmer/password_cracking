#SHA-1 generator: http://www.sha1-online.com 
import hashlib
import time

sha1hash = raw_input("Input the SHA1 hash to crack:\n>")

text_file = open("passwordlist.txt", "r")
passwords = text_file.read()

def cracker():
  start_time = time.time()
  for guess in passwords.split('\n'):
      hashedGuess = hashlib.sha1(bytes(guess)).hexdigest()
      if hashedGuess == sha1hash:
          print"The password is ", str(guess)
          print ("--- %s seconds ---" % (time.time() - start_time))
          quit()
      elif hashedGuess != sha1hash:
          print"Password guess ",str(guess)," does not match, trying next..."
  print("--- %s seconds ---" % (time.time() - start_time))
  print "Password not in database."

cracker()