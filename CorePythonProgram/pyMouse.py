#!/usr/bin/env python
from pymouse import PyMouseEvent

def fibo():
	a = 0 
	yield a
	b = 1
	yield b
	while True:
		a, b = b, a+b
		yield b
class Clickonacci(PyMouseEvent):
	def __init__(self):
		PyMouseEvent.__init__(self)
		self.fibo = fibo()
	def click(self, x, y, button, press):
		if button == '1':
			if press:
				print self.fibo.next()
		else:
			self.stop()
if __name__ == '__main__':
	C = Clickonacci()
	C.run()
