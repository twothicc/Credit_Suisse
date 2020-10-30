


class pair(object) :
	def __init__(self, head, tail) :
		self.head = head
		self.tail = tail

def head(xs) :
	if isinstance(xs, pair) :
		return xs.head
	else :
		raise Exception("argument provided is not a pair")

def tail(xs) :
	if isinstance(xs, pair) :
		return xs.tail
	else :
		raise Exception("argument provided is not a pair")

def linked_list(*args) :
	result = None
	arg_length = len(args) - 1
	for pos in range(arg_length + 1) :
		result = pair(args[arg_length - pos], result)
	return result



def is_linked_list(xs) :
	if isinstance(xs, pair) :
		if isinstance(tail(xs), pair) or tail(xs) == None :
			return True
		else :
			return False
	elif xs == None :
		return True
	else :
		return False

def is_pair(xs) :
	return isinstance(xs, pair)

def is_null(xs) :
	return xs == None

def LL_ref(xs, pos) :
	if not is_linked_list(xs) or not isinstance(pos, int) :
		raise Exception("invalid argument(s) provided")
	else :
		if pos == 0 :
			return head(xs)
		else :
			return LL_ref(tail(xs), pos - 1)

def display_LL(xs) :
	if is_linked_list(xs) :
		def helper(xs, initial) :
			if is_null(xs) :
				return initial
			else :
				return "[" + str(head(xs)) + "," + helper(tail(xs), initial) + "]"
		print(helper(xs, "None"))
	elif is_pair(xs) :
		print("[" + str(head(xs)) + "," + str(tail(xs)) + "]")
	else :
		raise Exception("argument provided is neither a linked_list nor a pair")
		


def reverse(xs) :
	if not is_linked_list(xs) :
		raise Exception("argument(s) provided are not linked_lists")
	else :
		def helper(xs, initial) :
			if is_null(xs) :
				return initial
			else :
				return helper(tail(xs), pair(head(xs), initial))
		return helper(xs, None)

def append_LL(xs, ys) :
	if not is_linked_list(xs) or not is_linked_list(ys) :
		raise Exception("argument(s) provided are not linked_lists")
	else :
		def helper(xs, ys, initial) :
			if is_null(xs) :
				if is_null(ys) :
					return reverse(initial)
				else :
					return helper(xs, tail(ys), pair(head(ys), initial))
			else :
				return helper(tail(xs), ys, pair(head(xs), initial))
		return helper(xs, ys, None)

def remove(v, xs) :
	if not is_linked_list(xs) :
		raise Exception("argument(s) provided are not linked_lists")
	else :
		if is_null(xs) :
			return xs
		elif head(xs) == v :
			return tail(xs)
		else :
			return pair(head(xs), remove(v, tail(xs)))

def remove_all(v, xs) :
	if not is_linked_list(xs) :
		raise Exception("argument(s) provided are not linked_lists")
	else :
		if is_null(xs) :
			return xs
		elif head(xs) == v :
			return remove_all(v, tail(xs))
		else :
			return pair(head(xs), remove_all(v, tail(xs)))


def map_LL(f, xs) :
	if not is_linked_list(xs) or not callable(f):
		raise Exception("invalid argument(s) provided")
	else :
		if is_null(xs) :
			return xs
		else :
			return pair(f(head(xs)), map_LL(f, tail(xs)))

def filter_LL(pred, xs) :
	if not is_linked_list(xs) or not callable(pred) :
		raise Exception("invalid argument(s) provided")
	else :
		if is_null(xs) :
			return xs
		else :
			if pred(head(xs)) :
				return pair(head(xs), filter_LL(pred, tail(xs)))
			else :
				return filter_LL(pred, tail(xs))


def accumulate_LL(f, initial, xs) :
	if not is_linked_list(xs) or not callable(f) :
		raise Exception("invalid argument(s) provided")
	else :
		if is_null(xs) :
			return initial
		else :
			return f(head(xs), accumulate_LL(f, initial, tail(xs)))
#display_LL(tail(append_LL(xs, xs)));

# display_LL(accumulate_LL(lambda x,y : append_LL(linked_list(x), y), None, xs))

def member_LL(x, xs) :
	if is_null(xs) :
		return False
	else :
		if head(xs) == x :
			return True
		else :
			return member_LL(x, tail(xs))

def set_head(xs, v) :
	if not is_pair(xs) :
		raise Exception("argument provided is not a pair")
	else :
		xs.head = v

def set_tail(xs, v) :
	if not is_pair(xs) :
		raise Exception("argument provided is not a pair")
	else :
		xs.tail = v

def is_array(xs) :
	return isinstance(xs, list)

def build_list(n, f) :
	if not isinstance(n, int) or not callable(f) :
		raise Exception("invalid argument(s) provided")
	else :
		def helper(k) :
			if k == n :
				return None
			else :
				return pair(f(k), helper(k + 1))
		return helper(0)

def LL_to_stream(xs) :
	if is_null(xs) :
		return None
	else :
		return pair(head(xs), lambda : LL_to_stream(tail(xs)))

def stream_tail(s) :
	return tail(s)()

def stream_ref(s, pos) :
	if pos == 0 :
		return head(s)
	else :
		return stream_ref(stream_tail(s), pos - 1)

def stream_append(s1, s2) :
	if is_null(s1) :
		return s2
	else :
		return pair(head(s1), lambda : stream_append(stream_tail(s1), s2))

def eval_stream(s, n) :
	def helper(s, n) :
		if is_null(s) :
			return None
		elif n == 0 :
			return None
		else :
			return pair(head(s), helper(stream_tail(s), n - 1))
	display_LL(helper(s, n))

#DO NOT USE THIS ON AN INFINITE STREAM UNLESS INFINITE RECURSION IS WHAT YOU WISH FOR
def is_stream(s) :
	return is_null(s) or is_pair(s) and is_stream(stream_tail(s))


def stream_remove(v, s) :
	if is_null(s) :
		return s
	else :
		if head(s) == v :
			return stream_tail(s)
		else :
			return pair(head(s), lambda : stream_remove(v, stream_tail(s)))

def stream_remove_all(v, s) :
	if is_null(s) :
		return s
	else :
		if head(s) == v :
			return stream_remove_all(v, stream_tail(s))
		else :
			return pair(head(s), lambda : stream_remove_all(v, stream_tail(s)))

def stream_filter(pred, s) :
	if is_null(s) :
		return s
	else :
		if not pred(head(s)) :
			return stream_filter(pred, stream_tail(s))
		else :
			return pair(head(s), lambda : stream_filter(pred, stream_tail(s))) 

def stream_map(f, s) :
	if is_null(s) :
		return s
	else :
		return pair(f(head(s)), lambda : stream_map(f, stream_tail(s)))

def add_stream(s1, s2) :
	if is_null(s1) :
		return s2
	elif is_null(s2) :
		return s1
	else :
		return pair(head(s1) + head(s2), lambda : add_stream(stream_tail(s1), stream_tail(s2)))

def build_stream(n, f) :
	def helper(k) :
		if k == n :
			return None
		else :
			return pair(f(k), lambda : helper(k + 1))
	return helper(0)

def integers_from(start) :
	return pair(start, lambda : integers_from(start + 1))
 
# xs = linked_list(1,2,2,4,5)

# st = LL_to_stream(xs)

# ones = pair(1, lambda : ones)

# stuff = pair(1, lambda : add_stream(stuff, ones))

# eval_stream(stuff ,5)

# eval_stream(integers_from(3), 20)

# eval_stream(build_stream(9, lambda x : x + 1), 10)

# print(is_stream(st))


