def file_to_lst_lst(filename, ch):
	content = []
	try:
		with open(filename, 'r') as file:
			for line in file:
				content.append(line.strip().split(" " + ch + " "))
		return content

	except FileNotFoundError:
		print(f"Error: The file '{filename}' does not exist.")
		return -1
