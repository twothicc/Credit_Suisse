import random
import time
import math


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
	#Initialize counter vector
	counts = [0] * (xs_range + 1)
	
	for idx in range(len(xs)) :
		counts[xs[idx]] += 1
	
	#Create copy of xs
	xs2 = []
	#Appends count of values into xs2
	for val in range(xs_range + 1) :
		xs2 += [val] * counts[val]
	return xs2

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
	def heapify(lst, index, length):
		idx = index
		largest = index
		#changes largest to the index of the largest value between idx, idx * 2, idx * 2 + 1
		if (idx * 2 + 1) < length:
			if lst[idx * 2 + 1] > lst[idx * 2]:
				if lst[idx * 2 + 1] > lst[idx]:
					largest = idx * 2 + 1
			else:
				if lst[idx * 2] > lst[idx]:
					largest = idx * 2
		elif idx * 2 < length:
			if lst[idx * 2] > lst[idx]:
				largest = idx * 2
		#if largest was not idx, heapify must be applied to new sub branch as well
		if largest != idx:
			lst[idx], lst[largest] = lst[largest], lst[idx]
			heapify(lst, largest, length)

	def max_heapify(lst, length) :
		#is_change checks if anything has been changed
		max_half = len(lst) // 2
		for i in range(max_half) :
			idx = max_half - i - 1
			heapify(lst, idx, length)

	#length will determine the index in maxheap to check to. Rmbr index in this maxheap goes from 1,2,3,... so dunnid to minus 1
	length = len(lst)
	#Generate max heap
	max_heapify(lst, length)
	while length > 1 :
		#Swap first and last element, which are largest and smallest, then pop the last element, which is now largest
		lst[0], lst[length - 1] = lst[length - 1], lst[0]
		length -= 1
		#Re heapify lst
		heapify(lst, 0, length)

	return lst

def map2(f, xs) :
	result = []
	for i in map(f, xs) :
		result.append(i)
	return result;

def remove2(x, xs) :
	xs.remove(x)
	return xs

#Finds combinations of values in list that would give a target value
def combinations(xs, current, target) :
	if current == target :
		return [[]]
	elif len(xs) == 0 :
		return []
	else :
		a = combinations(xs[1:], current, target)
		b = map2(lambda x : [xs[0]] + x, combinations(xs[1:], current + xs[0], target))
		return b + a


# weights = [2,4,3,8,5]
# profits = [10,24,12,15,18]


def fractional_knapsack(ws, ps, W) :
	def quick_sort_altered(xs, ys) :

		def partition(x, y, xs, ys) :
			lesser_xs = []
			lesser_ys = []
			greater_xs = []
			greater_ys = []
			xs.remove(x)
			ys.remove(y)
			for i in range(len(xs)) :
				if (ys[i] / xs[i]) <= (y / x) :
					lesser_xs.append(xs[i])
					lesser_ys.append(ys[i])
				else :
					greater_xs.append(xs[i])
					greater_ys.append(ys[i])
			return [lesser_xs, lesser_ys, greater_xs, greater_ys]
		
		if len(xs) == 0 :
			return []
		else :
			pivot_xs = xs[0]
			pivot_ys = ys[0]

			result = partition(pivot_xs, pivot_ys, xs, ys)

			return quick_sort_altered(result[0], result[1]) + [[pivot_xs, pivot_ys]] + quick_sort_altered(result[2], result[3])
				
	sorted_list = quick_sort_altered(ws, ps)
	current_weight = 0
	current_profit = 0

	for idx in range(len(sorted_list)) :
		if current_weight + sorted_list[idx][0] <= W :
			current_weight += sorted_list[idx][0]
			current_profit += sorted_list[idx][1]
			print("picked {0} of item {1} and gained {2} profit".format(sorted_list[idx][0], idx, sorted_list[idx][1]))
		else :
			missing_weight = W - current_weight
			ratio = missing_weight / sorted_list[idx][0]
			profit_gained = ratio * sorted_list[idx][1]
			current_profit += profit_gained
			print("picked {0} of item {1} and gained {2} profit".format(missing_weight, idx, profit_gained))
			break

	return current_profit


def knapsack(ws, ps, n, W) :
	#If there's nothing left to pick, then we have to return 0 for no value added due to nothing being picked
	if n < 0 or W == 0 :
		return 0
	elif ws[n] > W :
		#If weight of ws is more than W, then we cannot pick it, drop the selection
		return knapsack(ws, ps, n - 1, W)
	else :
		#return the maximum of either combinations selecting a value at index, and combinations that don't select that value
		return max(ps[n] + knapsack(ws, ps, n - 1, W - ws[n]), knapsack(ws, ps, n - 1, W))

# val = [60, 100, 120, 80, 160] 
# wt = [10, 20, 30, 10, 20] 
# W = 50





# print(knapsack(wt, val, len(wt) - 1, W))
def coin_change_restrict(coins, types, T, M) :
	coin_idx = [[types, 0] for t in types]

	def smaller(xs, ys) :
		if len(xs) < len(ys) :
			if len(xs) == 0 :
				return ys
			else :
				return xs
		else :
			if len(ys) == 0 :
				return xs
			else :
				return ys

	def coin_change(coins, coin_idx, n, combi, curr, T, M) :
		if T == 0 or n < 0 :
			return []
		elif curr == T :
			return combi
		elif curr + coins[n] > T :
			return coin_change(coins, coin_idx, n - 1, combi, curr, T, M)
		else :
			selection = coins[n]
			to_add = True
			new_coin_idx = []
			for i in coin_idx :
				if i[0] == selection :
					if i[1] == M :
						to_add = False
						break
					new_coin_idx.append([i[0],i[1] + 1])
				else :
					new_coin_idx.append(i)

			if to_add :
				return smaller(coin_change(coins, coin_idx, n - 1, combi, curr, T, M), coin_change(coins, new_coin_idx, n - 1, [selection] + combi, curr + selection, T, M))
			else :
				return coin_change(coins, coin_idx, n - 1, combi, curr, T, M)

	return coin_change(coins, coin_idx, len(coins) - 1, [], 0, T, M)

# coins = [10,10,20,50,5,10,20,50,5,5,10]
# print(coin_change_restrict(coins, [5,10,20,50], 120, 2))



#dynamic programming approach to finding fibonacci
#This function actually gives descending sequence of fibonacci values
def fibonacci(n) :

	def fibonacci_helper(n, k, initial) :
		if k == n :
			return initial
		else :
			return fibonacci_helper(n, k + 1, [initial[1] + initial[0]] + initial)

	return fibonacci_helper(n, 1, [1,0])


def longest_common_subsequence(xs, ys) :
	def LCS(xs, ys, m, n) :
		#Base case would be when index < 0, cuz when index = 0, its still a value
		if m < 0 or n < 0 :
			return 0
		else :
			if xs[m] == ys[n] :
				#If the values are equal, then its a subsequence or continuation of one. We must add + 1
				return 1 + LCS(xs, ys, m - 1, n - 1)
			else :
				#Shld consider say
				# A D E
				# D A D
				# A =/= D but we must consider chance that next index has value equals to A, which in this case is true
				return max(LCS(xs, ys, m, n - 1), LCS(xs, ys, m - 1, n))
	return LCS(xs, ys, len(xs) - 1, len(ys) - 1)
X = "AXYT"
Y = "AYZX"
print(longest_common_subsequence(X, Y))

#returns longest common order subsequence (ascending order)
def longest_common_ordered_subsequence(xs, ys) :
	def LCOS(xs, ys, m, n) :
		if m < 0 or n < 0 :
			return 0
		else :
			#If indexes are similar, we need to check if their preceding indexes are smaller or equals and similar
			if xs[m] == ys[n] :
				#If preceding indexes are smaller or equals and similar, then + 1
				if xs[m - 1] <= xs[m] and ys[n - 1] == xs[m - 1] :
					return 1 + LCOS(xs, ys, m - 1, n - 1)
				#If preceding indexes do not meet above condition, then just return 1, cuz we haven't accounted for the duo that's similar
				else :
					return 1
			else :
				#If indexes are not similar, maybe ordered indexes end at diff indexes, need check throughout
				return max(LCOS(xs, ys, m - 1, n), LCOS(xs, ys, m, n - 1))
	return LCOS(xs, ys, len(xs) - 1, len(ys) - 1)

X = "AAABBT"
Y = "TAAXBB"
print(longest_common_ordered_subsequence(X, Y))

#returns longest ordered subsequence in an array. Ascending order but includes equals
def ordered_subsequence(xs, f) :
	def LOS(xs, n, curr) :
		if n < 0 :
			return 0
		else :
			if xs[n - 1] <= xs[n] :
				return LOS(xs, n - 1, curr + 1) 
			else :
				return f(curr + 1, LOS(xs, n - 1, 0))
	return LOS(xs, len(xs) - 1, 0)

print(ordered_subsequence("AAABAAAAAABAAABAAB", max))

def max_min(xs) :
	if len(xs) <= 2 :
		return [max(xs), min(xs)]
	else :
		mid = math.floor(len(xs) / 2)

		max1, min1 = max_min(xs[:mid + 1])

		max2, min2 = max_min(xs[mid + 1:])

		return [max(max1, max2), min(min1, min2)]


print(max_min([1,2,4,7,23,32,1,43,134]))

#Needs work
def knapsack_dynamic(ws, ps, W) :
	DP = [[] for x in range(len(ws) + 1)]
	for weight in range(W + 1) :
		curr_weight = weight
		for weight_ele in range(len(ws) + 1) :
			if weight == 0 :
				DP[weight_ele].append(0)
			else :
				if weight_ele == 0 :
					DP[weight_ele].append(0)
				else :
					if curr_weight - ws[weight_ele - 1] >= 0 :
						DP[weight_ele].append(max(DP[weight_ele - 1][weight], ps[weight_ele - 1] + DP[weight_ele - 1][weight]))
						curr_weight -= ws[weight_ele - 1]
					else :
						if weight - ws[weight_ele - 1] >= 0 :
							DP[weight_ele].append(max(DP[weight_ele - 1][weight], ps[weight_ele - 1]))
						else :
							DP[weight_ele].append(DP[weight_ele - 1][weight])
	for i in DP :
		print(i)
	return DP[len(ws)][W]

print(knapsack_dynamic([1,2,3], [10,15,40], 6))
