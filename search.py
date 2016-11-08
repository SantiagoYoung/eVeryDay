# -*- coding: utf-8 -*-
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



'''
      使用re，匹配每一行，包括注释和空白行，
      分别列出注释和空白行。

'''




























































