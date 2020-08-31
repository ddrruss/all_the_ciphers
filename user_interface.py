from reverse_cypher_encrypt import Encryptor
from reverse_cypher_decrypt import Decryptor
from dict_control import Dict_Control
from document_control import Doc_Control
import math


class Interface:
	"""Includes modules that interact with the user along the program."""
	def __init__(self):
		"""Sets up the class Interface."""
		self.introducer()
		if self.code_mode == "1":
			if self.input_mode == "1":
				self.encrypt_message()
			else:
				self.encrypt_text_file()
				#print("work in progress")
		elif self.code_mode == "2":
			if self.input_mode == "1":
				self.decrypt_message()
			else:
				self.decrypt_text_file()
		else:
			if self.input_mode == "1":
				self.hack_message()
			else:
				self.hack_text_file()
				
				
	def introducer(self):	
		"""A module that introduces the program and prompts user with set-up options."""
		#Introduces the program.
		print("\n"*4)
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"*2)
		print("This is a program that will encrypt or decrypt a message or file.")
		print("Remember to use the same key that you used to encrypt the message or file to decrypt.")
		print("You can press Ctrl c at anytime to quit the program.\n")
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"*2)

		#Sets the program to encrypt or decrypt. Will keep asking if a non-answer is given.
		print("1. Encrypt")
		print("2. Decrypt")
		print("3. Hack")
		while True:
			self.code_mode = input("Enter number to encrypt or decrypt. --> ")
			if self.code_mode == "1" or self.code_mode == "2" or self.code_mode == "3":
				break
			else:
				continue

		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

		#Sets the input mode. Will keep asking if a non-answer is given.
		print("1.Type or paste message")
		print("2.Provide message in a text file.")
		while True: 
			self.input_mode = input("Enter number to indicate input mode. --> ")
			if self.input_mode == "1" or self.input_mode == "2": 
				break
			else:
				continue

		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
	
	
	def setup_key_encrypt(self):
		"""A method that will ensure the user passes a relevent encryption key."""
		self.max_key = math.floor(len(self.message) / 2)
		while True:
			key = input(f"Please enter a key value less than or equal to {self.max_key}. --> ")
			try:
				self.key = int(key)
			except ValueError:
				print("Key needs to be a number.")
				continue
			if self.key > self.max_key: 			
				print(f"{key} is too big of a number.")	
			elif self.key == 0:
				print("0 cannot be a key")			
			else:			
				break

	def setup_key_decrypt(self):
		"""A method that will ensure the user passes a relevent decryption key."""
		self.max_key = math.floor(len(self.message) / 2)
		while True:
			key = input("Please enter the key that was used to encrypt your message.--> ")
			try:
				self.key = int(key)
			except ValueError:
				print("Key needs to be a number.")
				continue
			if self.key > self.max_key: 			
				print(f"{key} is too big of a number.")
			elif self.key == 0:
				print("0 cannot be a key.")				
			else:			
				break

	def verify_decrypt_key(self):
		"""Will verify that the decrypt key is the correct key by decrypting and cross referencing results with dictionary files for english words."""
		percent_english = Dict_Control(self.my_code).check_key()
		#If more than half the words are english, the key will pass. 
		if percent_english > 50:
			self.right_key = False
		#If the key does not pass, the program will give you a warning and prompt you for another key. 
		else: 
			print(f"After decryption, it looks like only {percent_english}% of your words are english, you may have entered the wrong key?")

	def verify_hack_key(self):
		"""Will verify that the decrypt key is the correct key by cross referencing decrypted results with dictionary files for english words."""
		self.percent_english = Dict_Control(self.my_code).check_key()
		#If more than half the words are english, the key will pass. 
		if self.percent_english > 50:
			self.hack_plausible = True
		 
		


	def encrypt_message(self):
		"""Method will collect typed or pasted message and then encrypt it."""
		#Will not let user input useless messages that cannot be encrypted.
		while True:
			self.message = input("Please enter a message you would like to encrypt. --> ")
			if self.message != "" and len(self.message) > 4:
				break
		self.setup_key_encrypt()
		my_code = Encryptor(self.message, self.key)
		print(my_code.transfer_encrypt()+ "|")

	def encrypt_text_file(self):
		"""Method will ask user for the name of the text file, check if it is in the correct location and then encrypt it."""
		#Ensures that the file has something that can be encrypted.
		file_contains_message = True
		while file_contains_message:
			file_exists = True
			#Checks to see if the file exists.
			while file_exists:
				self.text_file_name = input("Please enter the name of the text file you wish to encrypt in format |file_name.txt|.--> ")
				if ".txt" in self.text_file_name:
					file_exists = Doc_Control().check_for_file(self.text_file_name)
				else: 
					continue
			#Reads file and prompts user to provide an encryption key that is appropriate for the message in the file.
			while True: 
				self.message = Doc_Control().open_file(self.text_file_name)
				if self.message != "" and len(self.message) > 4:
					file_contains_message = False
					break
				else:
					print("Your file does not contain an encryptable message.")
					break		
		self.setup_key_encrypt()
		self.output_file = Doc_Control().assign_output_file()
		my_code = Encryptor(self.message, self.key)
		my_code = my_code.transfer_encrypt()
		output_file_obj = open(self.output_file, 'w')
		output_file_obj.write(my_code)
		output_file_obj.close()		
		print("\nYour file has been encrypted.")


	def decrypt_message(self):
		"""Method will  collect typed or pasted message and then decrypt it."""

		#Will not let user input useless messages that cannot be decrypted.
		while True:
			self.message = input("Please enter a message you would like to decrypt. --> ")
			if self.message != "" and len(self.message) > 4:
				break
		#Decrypts message but verifys correct key before giving user their decrypted message.
		self.right_key = True
		while self.right_key:
			self.setup_key_decrypt()
			self.my_code = Decryptor(self.message, self.key).transfer_decrypt()
			self.verify_decrypt_key()
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
		print("Your decrypted message is")
		print(self.my_code + "|")


	def decrypt_text_file(self):
		"""Method will ask user for the name of the text file, check if it is in the correct location and then decrypt it."""
		#Ensures that the file has something that can be decrypted.
		file_contains_message = True
		while file_contains_message:
			file_exists = True
			#Checks to see if the file exists.
			while file_exists:
				self.text_file_name = input("Please enter the name of the text file you wish to decrypt in format |file_name.txt|.--> ")
				if ".txt" in self.text_file_name:
					file_exists = Doc_Control().check_for_file(self.text_file_name)
				else: 
					continue
			#Decrypts message but verifys correct key before giving user their decrypted message.
			while True: 
				self.message = Doc_Control().open_file(self.text_file_name)
				if self.message != "" and len(self.message) > 4:
					file_contains_message = False
					break
				else:
					print("Your file does not contain an encryptable message.")
					break
		self.right_key = True
		while self.right_key:
			self.setup_key_decrypt()
			self.my_code = Decryptor(self.message, self.key).transfer_decrypt()
			self.verify_decrypt_key()
		self.output_file = Doc_Control().assign_output_file()
		output_file_obj = open(self.output_file, 'w')
		output_file_obj.write(self.my_code)
		output_file_obj.close()		
		print("\nYour file has been decrypted.")



	def hack_message(self):
		"""Method will  collect typed or pasted message and then hack it."""
		#Will not let user input useless messages that cannot be hacked.
		while True:
			self.message = input("Please enter a message you would like to hack. --> ")
			if self.message != "" and len(self.message) > 4:
				break			
		max_key = len(self.message)
		self.i = 1
		potential_hits = []
		#Runs through all potential keys. 
		for self.i in range(1, max_key):
			print(f"Trying key #{self.i}")			
			self.my_code = Decryptor(self.message, self.i).transfer_decrypt()
			self.hack_plausible = False
			self.verify_hack_key()
			if self.hack_plausible:
				potential_hits.append(f"Key #{self.i} yeilded {self.percent_english}% english words after decryption.\n" + "\t" + self.my_code[:50])
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
		print("Hacking results:\n")
		for hit in potential_hits:
			print("\t" + hit + "|\n")


	def hack_text_file(self):
		"""Method will ask user for the name of the text file, check if it is in the correct location and then hack it."""
		#Ensures that the file has something that can be hacked.
		file_contains_message = True
		while file_contains_message:
			file_exists = True
			#Checks to see if the file exists.
			while file_exists:
				self.text_file_name = input("Please enter the name of the text file you wish to decrypt in format |file_name.txt|.--> ")
				if ".txt" in self.text_file_name:
					file_exists = Doc_Control().check_for_file(self.text_file_name)
				else: 
					continue
			#Verifys file contains a message before before running through hack and giving user their list of decryption hits.
			while True: 
				self.message = Doc_Control().open_file(self.text_file_name)
				if self.message != "" and len(self.message) > 4:
					file_contains_message = False
					break
				else:
					print("Your file does not contain a hackable message.")
					break			
		max_key = len(self.message)
		self.i = 1
		potential_hits = []
		#Runs through all potential keys. 
		for self.i in range(1, max_key):
			print(f"Trying key #{self.i} of {max_key} possible keys")			
			self.my_code = Decryptor(self.message, self.i).transfer_decrypt()
			self.hack_plausible = False
			self.verify_hack_key()
			if self.hack_plausible:
				potential_hits.append(f"Key #{self.i} yeilded {self.percent_english}% english words after decryption.\n" + "\t" + self.my_code[:50])
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
		print("Hacking results:\n")
		for hit in potential_hits:
			print("\t" + hit + "|\n")



