import time


def timer(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		return_value = func()
		total = time.time() - start
		print('Time:', total)
		return return_value
	
	return wrapper


@timer
def test():
	for _ in range(1000000):
		pass


@timer
def test2():
	time.sleep(2)


test()
test2()
