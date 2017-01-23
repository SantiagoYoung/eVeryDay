

__new__(cls, *args, **kwargs)
__init__(self, *args, **kwargs)
__del__(self)


__cmp__(self, other)
__eq__(self, other)
__ne__(self, other)
__lt__(self, other)
__gt__(self, other)


class Word(str):
	def __new__(cls, word):
		if ' ' in word:
			print 'Value contains spaces. Truncating to first space.'
			word = word[:word.index(' ')]
		return str.__new__(cls, word)

	def __gt__(self,other):
		return len(self)>len(other)
	def __lt__(self,other):
		return len(self)<len(other)
	def __ge__(self,other):
		return len(self)>=len(other)
	def __le__(self,other):
		return len(self)<=len(other)


def __setattr__(self, name, value):
	self.name = value
def __setattr__(self, name, value):
	self.__dict__[name] = value



class AccessCounter(object):

	def __init__(self, val):
		super(AccessCounter, self).__setattr__('counter', 0)
		super(AccessCounter, self).__setattr__('value', val)

	def __setattr__(self, name, value):
		if name == 'value':
			super(AccessCounter, self).__setattr__('counter',
			 self.counter + 1)
		super(AccessCounter, self).__setattr__(name, value)
	def __delattr__(self, name):
		if name == 'value':
			super(AccessCounter, self).__setattr__('counter', 
				self.counter + 1)
		super(AccessCounter, self).__delattr__(name)


class FunctionalList(object):

	def __init__(self, values=None):
		if values is None:
			self.values = []
		else:
			slef.values = values
	def __len__(self):
		return len(self.values)

	def __getitem__(self, key):
		return self.values[key]
	def __setitem(self, key, value):
		self.values[key] = value
	def __delitem__(self, key):
		del self.values[key]
	def __iter__(self):
		return iter(self.values)

	def __reversed__(self):
		return reversed(self.values)
	def append(self, value):
		self.values.append(value)
	def head(self, value):
		return self.values[0]
	def tail(self, value):
		return self.values[1:]
	def init(self):
		return self.values[:-1]
	def last(self):
		return self.values[-1]
	def drop(self, n):
		return self.values[n:]
	def take(self, n):
		return self.values[:n]




__call__

class Entity(object):

	def __init__(self, size, x, y):
		self.x, self.y = x, y
		self.size = size
	def __call__(self, x, y):
		self.x, self.y = x, y


class Closer(object):

	def __init__(self, obj):
		self.obj = obj

	def __enter__(self):
		return self.obj

	def __exit__(self, exception_type, exception_val, trace):
		try:
			self.obj.close()
		except AttributeError:
			print "Not u ."
			return True


class Meter(object):

	def __init__(self, value=0):
		self.value = float(value)

	def __get__(self, instance, owner):
		return self.value

	def __set__(self, instance, value):
		self.value = float(value)

class Foot(object):
	def __get__(self, instance, owner):
		return instance.meter * 9

	def __set__(self, instance, value):
		instance.meter = float(value)/9

class Distance(object):
	meter = Meter()
	foot = Foot()









from Queue import Queue
import time
import threading
q = Queue()

# email func
def send_email():
	pass

class EmailThread(threading.Thread):
	def __init__(self, queue):
		self._q = queue
		super(EmailThread, self).__init__()
		self.daemon(True)
		self.start()
	def run(self):
		while 1:
			f, subject, text, sender, receiver = q.get()
			try:
				f(subject, text, sender, receiver)
			except:
				pass

			self._q.task_done()

# views func
def verify_code(request):

	.....
	q.put(send_email, subject,
		text, sender, receiver)

	email = EmailThread(q)
	time.sleep(5)
	q.join()
	.....

	return


@api_view('post')
def login(request):

	username = request.data.get('username', None)
	pwd_1 = request.data.get('pwd_1', None)
	pwd_2 = request.data.get('pwd_2', None)
    
    # check function to check username or password
	def check():
		pass
	try:
		user = User.objects.get(username=username)
	except.User.DoesnotExist:
		return Response('status':0)
	auth.login(request,user)
	return Response('msg': '')


