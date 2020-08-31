import math

class Decryptor:
	"""A program that will decrypt any message/key pair with a transfer cypher."""	
	def __init__(self, message, key):
		"""This class requires a message and a key to operate."""
		self.message = message
		self.key = key

	def transfer_decrypt(self):
		"""A method that will decrypt a transfer cypher."""
		#The columns are 
		num_columns = int(math.ceil(len(self.message)/float(self.key)))
		num_blankspace = (num_columns * self.key) - len(self.message)
		len_last_row = self.key - num_blankspace
		decrypt_list = [''] * num_columns

		column = 0
		row = 0 

		for char in self.message:
			#char is added to a column, the column is advanced.		
			decrypt_list[column] += char
			column += 1
			#If column is above index, or the row of the last column is equal or beyond the max 
			#last columns max row length, then progress to the next row. 
			if (column == num_columns) or (column == num_columns - 1 and row >= len_last_row): 
				column = 0 
				row += 1
		#decrypt_list is now a single string. 
		return ''.join(decrypt_list)







