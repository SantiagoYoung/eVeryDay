import re


def query(filepath):


	query = re.compile('\w+')
	
	with open(filepath, 'r') as f:
		text = f.read()

	result = query.findall(text)

	words = ''
	for word in result:
		words = word + ' '

	return words

