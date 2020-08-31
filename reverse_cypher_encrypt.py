

class Encryptor: 
	"""A program that will encrypt any message/key pair with a transfer cypher."""

	def __init__(self, message, key):
		"""This class requires a message and a key to operate."""
		self.message = message
		self.key = key


	def transfer_encrypt(self):
		"""A method that will encrypt any message given to the program with a transfer encryption.""" 
		#Creates a list that has the key's number of 'columns' which are each filled with char column + key.
		#For example, if the key is 8, column 0 will contain char 0, char 8, char 16, etc. If column is 1, then 9, 17, etc. 
		encrypt_list = [""] * self.key		
		for column in range(self.key):
			index_number = column
			while index_number < len(self.message):
				encrypt_list[column] += self.message[index_number]
				index_number += self.key
		#encrypt_list is now a single string. 
		return ''.join(encrypt_list)











