def genupseq(L):
	"""
	>>> list(genupseq([4, 2, 3, 6, 6, 5, 7, 1, 3]))
	[4, 6, 6, 7]
	>>> list(genupseq([]))
	[]
	"""
	index = 0
	while index < len(L):
		result = L[index]
		yield result
		index+=1
		while index < len(L) and L[index] < result:
			index += 1


def permutations(lst):
	"""
	>>> permutations(['angie', 'cat'])
	[['angie', 'cat'], ['cat', 'angie']]
	>>> permutations([1, 2, 3])
	[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


	""" # enumerate may be useful?... either use first elem as first elem in permutation, or not
	if len(lst) <= 1:
		return [lst]
	result = []
	for i, k in enumerate(lst):	# i will be the index, and k will be the list element
		result = result + [[k] + sublist for sublist in permutations(lst[:i] + lst[i+1:])]
	return result


def kstairs(n, k):
	"""
	>>> kstairs(5, 2)
	8
	>>> kstairs(5,5)
	16
	>>> kstairs(10,5)
	464

	"""
	if n == 0:
		return 0
	if n <= k:
		return 2**(n-1)
	return sum([kstairs(n-i,k) for i in range(1, k+1)])

def binary(s):
	#returns binary tree containing list of values s
	root = s[0]
	list1 = [elem for elem in s if elem < root]
	list2 = [elem for elem in s if elem > root]
	left_branch = binary(list1)
	right_branch = binary(list2)
	return BTree(root, left_branch, right_branch)
#tree recursion... trust in the recursion!!

def generate_subsets():
	"""
	>>> subsets = generate_subsets()
	>>> for _ in range(3):
	...		print(next(subsets))
	...
	[[]]
	[[], [1]]
	[[], [1], [2], [1, 2]]
	"""
	n = 1
	subsets = [[]]
	while True:
		yield subsets    
		subsets = subsets + [set + [n] for set in subsets]
		n += 1

"""
def zip_generator(*iterables):
	# >>> z = zip_generator([1, 2, 3], [4, 5, 6], [7, 8])
	# >>> for i in z:
	# ...		print(i)
	# ...
	# [1, 4, 7]
	# [2, 5, 8]
	i = 0
	while i < min([len(iterable) for iterable in iterables]):
		yield [iterable[i] for iterable in iterables]
		i += 1
	return
	# or:
	# iterators = [iter(iterable) for iterable in iterables]
	# while True:
	# 	yield [next(iterator) for iterator in interators]



def perfect_squares():
"""	#tab these indentations once to fix doctests
	# >>> s = perfect_squares()
	# >>> type(s)
	# <class 'generator'>
	# >>> next(s)
	# 1
	# >>> next(s)
	# 4
	# >>> next(s)
	# 9
	# >>> next(s)
	# 16
"""
	i = 1
	while True:
		yield i**2
		i += 1
"""
"""
def zodd():
	def helper():
		return 100
	return helper

def signChecker(num):
"""
	# >>> signChecker(0) 
	# 0
	# >>> signChecker(1) 
	# '+'
	# >>> signChecker(-1) 
	# '-'
"""
	#python3 -m doctest file.py    to test the code
	#python3 -m doctest file.py -v   tells WHICH tests passed
	if num > 0:
		return '+'
	elif num < 0:
		return '-'
	else:
		return 0
"""

"""
print('Hi There! Enter a number, and I will return that value\'s fibonacci number')

def nextFib(num):
	if num == 0 or num == 1:
		return 1
	else:
		return nextFib(num-1) + nextFib(num-2)

"""


#tree 
def tree(label, branches=[]):
	for branch in branches:
		assert is_tree(branch)
	return [label] + list(branches)

def label(tree):
	return tree[0]

def branches(tree):
	return tree[1:]

def is_tree(tree):
	if type(tree) != list or len(tree) < 1:
		return False
	for branch in branches(tree):
		if not is_tree(branch):
			return False
	return True 

def is_leaf(tree):
	return not branches(tree)

def leaves(t):
	if is_leaf(t):
		return [label(t)]
	else:
		return sum([leaves(b) for b in branches(t)], [])



"""
# linked lists
class Link:
	empty = ()
	def __init__(self, first, rest=empty):
		assert rest is Link.empty or isinstance(rest, Link)
		self.first = first
		self.rest = rest
	
	def __repr__(self):
		if self.rest:
			rest_str = ', ' + repr(self.rest)
		else:
			rest_str = ''
		return 'Link({0}{1})'.format(self.first, rest_str)


	def __str__(self):
		string = '<'
		while self.rest is not Link.empty:
			string += str(self.first) + ', '
			self = self.rest
		return string + str(self.first) + '>'
"""

"""		Spring 2018 Midterm 2 Q4
def combo(a,b):
	if a==0 or b==0:
		return a+b
	elif a%10 == b%10:
		return combo(a//10, b//10) * 10 + b%10
	return min(combo(a//10, b)*10 + a%10, combo(a, b//10)*10 + b%10)
"""

"""	Spring 2018 Midterm 2 Q5a
def siblings(t):
	result = [b.label for b in t.branches if len(t.branches)>1]
	for b in t.branches:
		result.extend(siblings(b))
	return result
"""

"""	hw 9 Q1
(define (how-many s)
	(if (not (pair? s))		
		0)
	(+ (how-many (car s)) (how-many (cdr s))

		(if (number? (cdr s))
			1
			0)
		)
)
"""

"""
#exceptions handling - if x returns a ZeroDivisionError,
# execute all stuff inside the except body

try:
	x = 1/0
except ZeroDivisionError as e:
	print('handling a', type(e))
	zodd = lambda x: x*x
	x = 9

"""
"""	more exceptions stuff. A function that may return
	#the error can be in the "try" body. 

def invert(x):
	result = 1/x
	print('Bottom stuff never printed if x is 0. hoe')
	return result

def invert_safe(x):
	try:
		return invert(x)
	except ZeroDivisionError as e:
		#raise Exception('Go suck a dick')
		return str(e)
"""




