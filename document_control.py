import time, os, sys

class Doc_Control:
	"""A class that will manage input files.""" 

	def __init__(self):
		"""The main sunction for Doc_control, each method is needed in different circumstances so no need for anything in at startup."""

	def check_for_file(self, file_name): 
		"""Will check to make sure that the given file exists. Will suggest that the user check that the file exists and is input correctly."""
		self.file_name = file_name
		if not os.path.exists(self.file_name):
			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
			print(" WARNING: This file does not exist, make sure it was inputed correctly and it is in the same file as the reverse_cypher python files.")
			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
			return True
		else: 
			return False

	def assign_output_file(self):
		"""This method will ask user to input a file name for their output file."""
		#Makes sure that the user has provided a text file that will not be rejected by the file store method.
		output_ok = True
		while output_ok:
			self.output_name = input("Please give a file name in the format |file_name.txt| by which you would like the output file to be called. -->")
			if " " in self.output_name or "|" in self.output_name or "-" in self.output_name or "/" in self.output_name:
				print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
				print(" WARNING: This output file name cannot be used, make sure it does not contain any spaces, -, /, or | symbols.")
				print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
			elif ".txt" not in self.output_name:
				print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
				print(" WARNING: .txt must be included the output file name.")
				print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
			#Ensures that the file does not already exist in the relevent path. If it does exist, will prompt user to verify they want to write over that file name.
			elif os.path.exists(self.output_name):
				ok_go = True
				while ok_go:
					ok_overwrite = input("The output file name already exists, you sure you want to write over it? (Y)es or (N)o -->")
					if ok_overwrite.lower().startswith('y'):
						output_ok = False
						ok_go = False
					elif ok_overwrite.lower().startswith('n'):
						ok_go = False
			else:
				output_ok = False
		#When file passes, an output file name will be assigned to self.output_name and given to main program.
		return self.output_name

	def open_file(self, text_file_name):
		"""Opens the text file and returns it as a string."""
		self.text_file_name = text_file_name
		file_obj = open(self.text_file_name)
		content = file_obj.read()
		file_obj.close()
		return content















