import random
import time
import math
import heapsort

def test(ftn, xs) :
	start = int(time.time() * 1000)
	ftn(xs)
	end = int(time.time() * 1000)
	print("Time taken using {0} on list size {1} is {2}".format(ftn.__name__, len(xs), end - start))

def counting_sort_test(ftn, xs, xs_range) :
	start = int(time.time() * 1000)
	ftn(xs, xs_range)
	end = int(time.time() * 1000)
	print("Time taken using {0} on list size {1} is {2}".format(ftn.__name__, len(xs), end - start))

def generate_random_xs(size, sample_range) :
	lst = []
	for i in range(sample_range + 1) :
		lst.append(i)
	lst = random.sample(lst, size)
	return lst

lst = generate_random_xs(2000, 100000)

#quicksort has a runtime complexity of O(n * log n)
def quicksort(xs) :

	def add(xs, n, ys) :
		if xs == None :
			return n + ys
		elif ys == None :
			return xs + n
		else :
			return xs + n + ys

	def partition(xs, n) :
		#Rmbr to not include the pivot. If the pivot is included, infinite recursion will happen
		#Imagine you have 2 and 2, you'd move both 2s into the prev and infinite recursion occurs
		head = []
		tail = []
		xs.remove(n)
		for idx in range(len(xs)) :
			if xs[idx] <= n :
				head.append(xs[idx])
			elif xs[idx] > n :
				tail.append(xs[idx])
		return [[n] , head, tail]

	#Handles empty list cases
	if len(xs) == 0 :
		return None
	#If only one element left, there's nothing left to sort
	elif len(xs) == 1 :
		return xs
	else :
		partitioned = partition(xs, xs[random.randint(0, len(xs) - 1)])
		#Recursive
		return add(quicksort(partitioned[1]), partitioned[0], quicksort(partitioned[2]))

#Merge sort has a runtime complexity of O(n * log n)
def merge(xs) :
	def middle(xs) :
		return math.floor(len(xs) / 2)

	def merge_sort(xs, ys) :
		merged = []
		i = 0
		j = 0
		while i < len(xs) or j < len(ys) :
			if i >= len(xs) :
				merged += ys[j:]
				break
			elif j >= len(ys) :
				merged += xs[i:]
				break
			else :
				if xs[i] <= ys[j] :
					merged.append(xs[i])
					i += 1
				else :
					merged.append(ys[j])
					j += 1
		return merged

	if (len(xs) <= 2) :
		return xs
	else :
		mid = middle(xs)

		return merge_sort(merge(xs[:mid]), merge(xs[mid:]))

#Insertion_sort has a runtime complexity of O(n^2)
def insertion_sort(xs) :
	#For every element in list, check the preceding elements for any larger elements from the start
	#If larger, swap. Now we use the swapped element to check what's left of the preceding elements
	#O(n^2) runtime
	for idx in range(len(xs)) :
		for prev in range(idx) :
			if xs[idx] <= xs[prev] :
				xs[idx] , xs[prev] = xs[prev] , xs[idx]

	return xs

#Selection_sort has a runtime complexity of O(n^2)
def selection_sort(xs) :
	result = []
	for i in range(len(xs)) :
		smallest = xs[0]
		for idx in range(len(xs)) :
			if xs[idx] <= smallest :
				smallest = xs[idx]
		result.append(smallest)
		xs.remove(smallest)
	return result

#Counting_sort has a runtime complexity of O(n + k) whereby k is the range
def counting_sort(xs, xs_range) :
	#Must know the range beforehand
	#This is bad for comparing floats
	counts = {}
	for val in range(xs_range + 1) :
		counts[val] = 0
	
	for idx in range(len(xs)) :
		counts[xs[idx]] += 1

	for val in range(1, xs_range + 1) :
		counts[val] += counts[val - 1]

	xs = [None for x in xs]

	for val in range(xs_range + 1) :
		if counts[val] != 0 :
			for i in range(counts[val]) :
				if xs[i] == None :
					xs[i] = val
	return xs

#radix_sort has a runtime complexity of O((n+b) * logb(k)) where b is the base and k is the largest possible value
def radix_sort(xs) :

	def counting_sort_radix(xs, base) :
		
		counts = {}
		for idx in range(10) :
			counts[idx] = [0,[]]

		for idx in range(len(xs)) :
			base_val = int(xs[idx] / base) % 10
			counts[base_val][0] += 1
			counts[base_val][1].append(xs[idx])

		for count in range(1, 10) :
			counts[count][0] += counts[count - 1][0]	

		xs = [None for x in xs]

		for count in range(10) :
			if counts[count][0] != 0 :
				for i in range(counts[count][0]) :
					if xs[i] == None :
						xs[i] = counts[count][1].pop(0)
		return xs
	
	max_val = max(xs)
	num_bases = 1
	while max_val > 1 :
		num_bases += 1
		max_val /= 10
	
	for bases in range(num_bases) :
		base = 10 ** bases
		xs = counting_sort_radix(xs, base)

	return xs

#Bubble_sort has a runtime complexity of O(n^2)
#For every element in list, it checks with every following element in list. If its larger, it swaps and continues checking
def bubble_sort(xs) :
	for idx in range(len(xs)) :
		for j in range(idx, len(xs)) :
			if xs[idx] > xs[j] :
				xs[idx], xs[j] = xs[j], xs[idx]
	return xs



#Super Weenie Hub Jr
#Do not do these for lists > 10000 in size. Its crazy long
#test(insertion_sort, lst)
#test(bubble_sort, lst)
#test(selection_sort, lst)

#Fast af club
#counting_sort_test(counting_sort, lst, 10000000)
#test(quicksort, lst)
#test(merge, lst)

#Sometimes fast sometimes slow club
#test(radix_sort, lst)
def binary_search(xs, n) :
	def binary_search_inner(xs, l, r, n) :
		mid = l + math.floor((r - l) / 2)

		if xs[mid] == n :
			return mid
		elif xs[mid] < n :
			return binary_search(xs, 0, mid - 1, n)
		else :
			return binary_search(xs, mid + 1, r, n)
	return binary_search_inner(xs, 0, len(xs) - 1, n)



class Node(object) :
	def __init__(self, n) :
		self.entry = n
		self.left = None
		self.right = None

	#Inserting a value into the bst. Return True/False for Success/Failure
	def insert(self, n) :
		#If entry is None, means left, right branch are None too, change entry to value
		if self.entry == None :
			self.entry = n
			return True
		else :
			#If entry is equals to n, n is a duplicate value, bst cannot take duplicate values
			if n == self.entry :
				return False
			#If n is less then entry
			elif n < self.entry :
				#If left child node is None, means we can insert value as a new Node as a left branch
				if self.left == None :
					self.left = Node(n)
					return True
				#If left child node is a value, means we have to continue traversing down the tree
				else :
					return self.left.insert(n)
			#If n is more than entry
			else :
				#If right child node is None, means we can insert value as a new Node as a right branch
				if self.right == None :
					self.right = Node(n)
					return True
				#If right child node is a value, means we have to continue traversing down the tree
				else :
					return self.right.insert(n)

	#For finding whether a value exists in bst. returns True/False for Exist/Absent
	def find(self, n) :
		#If entry is equals to n, means value exists
		if self.entry == n :
			return True
		#If n is less than entry, its in left branch
		elif n < self.entry :
			#If left child node is None, n cannot exist in bst
			if self.left == None :
				return False
			#If left child node is a value, n can exist in left branch
			else :
				return self.left.find(n)
		#If n is more than entry, its in right branch
		else :
			#If right child node is None, n cannot exist in bst
			if self.right == None :
				return False
			#If right child node is a value, n can exist in right branch
			else :
				return self.right.find(n)

	#For conversion to list
	def show(self) :
		#The order in the equations determine how we traverse the bst, very impt
		if self.entry != None :
			if self.left == None and self.right == None :
				return [self.entry]
			elif self.left == None :
				return [self.entry] + self.right.show()
			elif self.right == None :
				return self.left.show() + [self.entry]
			else :
				return  self.left.show() + [self.entry] + self.right.show()
		else :
			return []

	#Visualize the tree
	#We use level here to represent the level from which we found a value entry
	def draw(self, level) :
		#Again the order in the equations here allow us to just pick the last element in the list later
		if self.entry != None :
			if self.left == None and self.right == None :
				return [[str(self.entry), level]]
			elif self.left == None :
				return [[str(self.entry), level]] + self.right.draw(level + 1)
			elif self.right == None :
				return [[str(self.entry), level]] + self.left.draw(level + 1)
			else :
				return  [[str(self.entry), level]] + self.left.draw(level + 1) + self.right.draw(level + 1)
		else :
			return []

	#Find maximum value
	def max(self) :
		#Keep searching till right Node is None
		#Don't have to worry about a None entry with 2 None leaf nodes because the None will be accounted for 
		if self.right == None :
			return self.entry
		else :
			return self.right.find_max()

	#Remove a value from the tree. returns True/False for success/failure
	def remove(self, n) :
		#If entry is not n, no need to remove
		if self.entry != n :
			if n < self.entry :
				#If left node is None, means element to be removed does not exist
				if self.left == None :
					return False
				#If left node is a value, means element to be removed could be in left branch
				else :
					return self.left.remove(n)
			else :
				#If right node is None, means element to be removed does not exist
				if self.right == None :
					return False
				#If right node is a value, means element to be removed could be in right branch
				else :
					return self.right.remove(n)
		#If entry is n, removal needs to happen, consider 4 cases
		else :
			#If both child nodes are None
			if self.left == None and self.right == None :
				self.entry = None
				return True
			#If only left child node is None
			elif self.left == None :
				self.entry = self.right.entry
				self.left = self.right.left
				self.right = self.right.right
				return True
			#If only right child node is None
			elif self.right == None :
				self.entry = self.left.entry
				self.left = self.left.left
				self.right = self.left.right
				return True
			#If both child nodes have values. Could be containing 1 node or multiple nodes
			else :
				#Find maximum entry in left branch
				left_maximum = self.left.max()
				#Convert left branch to list
				left_list = self.left.show()

				#Remove maximum entry from list
				left_list.remove(left_maximum)
				#Set entry to be the maximum entry, effectively removing n
				self.entry = left_maximum

				#This handles the case whereby the left branch only contains 1 node
				first = None
				#This handles the case whereby left branch has multiple nodes
				if len(left_list) != 0:
					first = Node(left_list[0])
					#Cannot just attach a bst object here
					#Must build a new bst from only Node objects.
					for idx in range(1, len(left_list)) :
						first.insert(left_list[idx])

				#Attach the new tree as the left branch of the node
				self.left = first
				return True

#Functions include :
#insert(n), find(n), to_list(), remove(n), str()
class BST(object) :

	def __init__(self, xs = []) :
		#Base case shld return an empty bst
		self.root = Node(None)

		#We're essentially building a tree here using insert functions repeatedly on the root node
		for idx in range(len(xs)) :
			if self.root.entry != None :
				if not self.root.insert(xs[idx]) :
					print('Duplicate entry {0} not added'.format(xs[idx]))
			else :
				self.root.entry = xs[idx]

	def insert(self, n) :
		if not self.root.insert(n) :
			print('duplicate {0} not inserted'.format(n))

	def find(self, n) :
		return self.root.find(n)

	def to_list(self) :
		return self.root.show()

	def remove(self, n) :
		#Just for visual purposes
		if self.root.remove(n) :
			print('{0} removed'.format(n))
			return True
		else :
			print('{0} is not found in BST'.format(n))
			return False

	#Overloading str() function for bst object
	def __str__(self) :
		#Who cares about auxiliary space
		lst = self.root.draw(0)
		levels = lst[len(lst) - 1][1] + 1
		level = []
		for i in range(levels) :
			level.append([])

		for i in range(len(lst)) :
			level[lst[i][1]].append(lst[i][0])

		result = ''
		for lvl in level :
			result += ' , '.join(lvl) + '\n'
		return result

	

# tree = BST([1,4,8,9,12,3])

# #Test drawing tree
# print(str(tree))

# #Test find and insert
# print(tree.find(2))
# tree.insert(2)
# print(tree.find(2))
# print(tree.to_list())

# #Test remove on root node
# print(str(tree))
# tree.remove(1)
# print(tree.to_list())
# tree.insert(1)
# print(str(tree))

# #Test remove on leaf node
# tree.remove(12)
# print(tree.to_list())

# #Test if structure of bst is still intact after removing leaf node
# tree.insert(12)
# print(tree.to_list())

# print(tree.remove(12))

# tree.insert(11)
# print(tree.to_list())



#heap_sort has n * log n runtime complexity with 1 space complexity	
def heap_sort(lst) :
	#length here limits the index of the maxheap that max_heapify will check till. This allows us to not check
	#already sorted indexes
	def max_heapify(lst, length):
		#is_change checks if anything has been changed
		#If something is changed, need to run max_heapify again to verify if changes are correct
		is_change = False
		max_half = math.floor(len(lst) / 2)
		for i in range(max_half) :
			idx = max_half - i 
			#Must add -1 to all the calculations with idx since its represented in 1,2,3,... while list index is 0,1,2,3,...
			if (idx * 2 - 1) < length :
				if lst[idx - 1] < lst[idx * 2 - 1] :
					lst[idx - 1], lst[idx * 2 - 1] = lst[idx * 2 - 1], lst[idx - 1]
					is_change = True
					
			if (idx * 2) < length :
				if lst[idx - 1] < lst[idx * 2] :
					lst[idx - 1], lst[idx * 2] = lst[idx * 2], lst[idx - 1]
					is_change = True
		#Recursively runs max_heapify till list is sorted
		if is_change :
			return max_heapify(lst, length)
		else :
			return lst

	#length will determine the index in maxheap to check to. Rmbr index in this maxheap goes from 1,2,3,... so dunnid to minus 1
	length = len(lst)
	while length > 1 :
		lst = max_heapify(lst, length)
		#Swap first and last element, which are largest and smallest, then pop the last element, which is now largest
		lst[0], lst[length - 1] = lst[length - 1], lst[0]
		#Then add to another list
		length -= 1
	
	return lst



test(heap_sort, lst)
test(heapsort.heapSort, lst)
test(merge, lst)