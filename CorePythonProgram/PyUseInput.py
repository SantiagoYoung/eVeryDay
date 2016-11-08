from pymouse import PyMouse
from pykeyboard import PyKeyboard


m = PyMouse()
k = PyKeyboard()

x_dim , y_dim = m.screen_size()
m.click(x_dim/2, y_dim/2)
k.type_string('Hello  World!')

PyKeyboard还有很多种方式来发送键盘键入：

# pressing a key
k.press_key('H')
# which you then follow with a release of the key
k.release_key('H')
# or you can 'tap' a key which does both
k.tap_key('e')
# note that that tap_key does support a way of     repeating keystrokes with a interval time between each
k.tap_key('l',n=2,interval=5)
# and you can send a string if needed too
k.type_string('o World!')
并且它还支持很多特殊按键：

#Create an Alt+Tab combo
k.press_key(k.alt_key)
k.tap_key(k.tab_key)
k.release_key(k.alt_key)
k.tap_key(k.function_keys[5]) # Tap F5
k.tap_key(k.numpad_keys['Home']) # Tap 'Home' on the numpad
k.tap_key(k.numpad_keys[5], n=3) # Tap 5 on the numpad, thrice
注意，你也可以使用press_keys方法将多个键一起发送（例如，使用某些组合键）：

# Mac example
k.press_keys(['Command','shift','3'])
# Windows example
k.press_keys([k.windows_l_key,'d'])
平台之间的一致性是一个很大的挑战，请参考你使用的操作系统对应的源码，来理解你需要使用的按键格式。例如：

# Windows
k.tap_key(k.alt_key)
# Mac
k.tap_key('Alternate')
我还想特别说明一下PyMouseEvent和PyKeyboardEvent的使用。

这些对象是一个架构用于监听鼠标和键盘的输入；他们除了监听之外不会做任何事，除非你继承他们【注1】。PyKeyboardEvent为编写完成，所以这里是一个继承PyMouseEvent的例子：

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
        '''Print Fibonacci numbers when the left click is pressed.'''
        if button == 1:
            if press:
                print self.fibo.next()
        else: # Exit if any other mouse button used
            self.stop()

C = Clickonacci()
C.run()

文／屋顶之树（简书作者）
原文链接：http://www.jianshu.com/p/552f96aa85dc
著作权归作者所有，转载请联系作者获得授权，并标注“简书作者”。