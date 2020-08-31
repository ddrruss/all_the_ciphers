
class Dict_Control:
	"""A class that will manage the dictionary file and use it to verify decryption by passing a percent english score, 
	giving the percent of the words in tha message that are english.""" 

	def __init__(self, message):
		"""The main Dict_Control method.""" 
		self.message = message
		UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		self.LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'
		self.load_dictionary()



	def check_key(self):
		"""Will return a value indicating percent of the words in the decrypted message that are english."""
		self.process_message()
		self.num_english()
		return self.percent_english

	def load_dictionary(self):
		"""Loads a dictionary file that will be referenced to ensure correct key and hack unknown messages."""
		dictionary_file = open('dictionary.txt')
		self.english_words = {}
		for word in dictionary_file.read().split('\n'):
			self.english_words[word] = None
		dictionary_file.close()
		

	def process_message(self):
		"""Takes the message and removes spaces and non-letter characters and returns it as a processed string."""
		self.message = self.message.upper()
		letters_only = []
		for char in self.message: 
			if char in self.LETTERS_AND_SPACE:
				letters_only.append(char)
		self.processed_message = ''.join(letters_only)
		
		

	def num_english(self):
		"""Checks if your processed message is correctly decrypted."""
		possible_words = self.processed_message.split()
		if possible_words == []:
			self.percent_english = 0
			
		else:
			num_english = 0
			for word in possible_words:
				if word in self.english_words: 
					num_english += 1
			self.percent_english = (float(num_english) / len(possible_words)) * 100
		
		










