#SHA-1 generator: http://www.sha1-online.com 
from urllib.request import urlopen, hashlib
import time

sha1hash = input("Input the SHA1 hash to crack:\n>")

website = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8')


def cracker():
  start_time = time.time()
  for guess in website.split('\n'):
      hashedGuess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()
      if hashedGuess == sha1hash:
          print("The password is ", str(guess))
          print("--- %s seconds ---" % (time.time() - start_time))
          quit()
      elif hashedGuess != sha1hash:
          print("Password guess ",str(guess)," does not match, trying next...")
  print("--- %s seconds ---" % (time.time() - start_time))
  print("Password not in database.")

cracker()