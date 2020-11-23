import math

def apply_compound_interest(start, annual_compound_interest_rate, years) :
	return start * ((1 + annual_compound_interest_rate) ** years)

#print(apply_compound_interest(10000, 0.05, 7))

def yearly_to_monthly_rates(annual_compound_interest_rate) :
	return ((1 + annual_compound_interest_rate) ** (1/12)) - 1

#print(yearly_to_monthly_rates(0.05))

def monthly_to_yearly_rates(monthly_compound_interest_rate) :
	return ((1 + monthly_compound_interest_rate) ** 12) - 1

#print(monthly_to_yearly_rates(0.05))

def monthly_payment(start, annual_compound_interest_rate, years) :
	return (start * yearly_to_monthly_rates(annual_compound_interest_rate) * ((1 + annual_compound_interest_rate) ** years)) \
		/ (((1 + annual_compound_interest_rate) ** years) -  1)

#print(monthly_payment(200000, 4/100, 20))

def savings_plan_comparison(Ainterest, Ayears, Binterest, Byears) :
	print("Note! This gives B savings per year/A savings per year")
	return (((1 + Binterest) ** Byears) - 1) / (((1 + Ainterest) ** Ayears) - 1)

#print(savings_plan_comparison(0.03, 20, 0.03, 40))

def roots_of_quadratic_polynomial(A, B, C) :
	if B ** 2 - 4 * A * C > 0 :
		print("f(x) has two real roots")
		print("roots are {0} and {1}".format((-B + (B ** 2 - 4 * A * C) ** 0.5) / (2 * A), (-B - (B ** 2 - 4 * A * C) ** 0.5) / (2 * A)))
	elif B ** 2 - 4 * A * C == 0 :
		print("f(x) has exactly one real root")
		print("roots are {0}".format(-B / (2 * A)))
	else :
		print("f(x) has no real roots")

#roots_of_quadratic_polynomial(1,0,-4)

#note: n = n - i + 1
def arithmetic_progression(a, d, n) :
	return ((n + 1) / 2) * (2 * a + n * d)

#print(arithmetic_progression(0, 1, 100))

#note: n = n - i + 1
def geometric_progression(a, r, n) :
	return (a * (r ** (n + 1) - 1)) / (r - 1)

#This sums 1 + 2 + 4 + 8 + 16
#print(geometric_progression(1, 2, 4))

def divisible_by_9(n) :
	result = 0;
	for i in str(n) :
		result += int(i)
	return result % 9 == 0

#print(divisible_by_9(12345678))

def checking_product(a, b, c) :
	def helper(v) :
		v = str(v)
		while len(v) > 1 :
			result = 0
			for i in v :
				result += int(i)
			v = str(result)
		return int(v)
	return ((helper(a) * helper(b)) % 9) == (helper(c) % 9)

#print(checking_product(5318, 11223344, 596855292))

representations = {10 : "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F", 16 : "G", 17 : "H", 18 : "I", 19 : "J", 20 : "K", 21 : "L",
22 : "M", 23 : "N", 24 : "O", 25 : "P", 26 : "Q", 27 : "R", 28 : "S", 29 : "T", 30 : "U", 31 : "V", 32 : "W", 33 : "X", 34 : "Y", 35 : "Z", 36 : "_"}

def base_representation(n, b) :
	result = []
	while n >= b :
		temp = n % b
		if temp > 9 :
			temp = representations[temp]
		result.append(temp)
		n = math.floor(n / b)
	result.append(n)
	result.reverse()
	return result

#print(base_representation(1801131029198, 16))

def base_to_decimal(xs, b) :
	result = 0
	base = len(xs) - 1
	for val in xs :
		result += (val * (b ** base))
		base -= 1
	return result

#print(base_to_decimal([1, 0,0], 2)) 

def weighted_sum_of_sequence(seq) :
	key_list = list(representations.keys())
	val_list = list(representations.values())
	length_seq = len(seq)
	pos = 0
	weighted_sum = 0
	while length_seq > 0 :
		if seq[pos].isnumeric() :
			weighted_sum += length_seq * int(seq[pos])
		else :
			weighted_sum += length_seq * key_list[val_list.index(seq[pos])]
		length_seq -= 1
		pos += 1
	return weighted_sum

#print(weighted_sum_of_sequence("NO_FOOD"))

def encode_mod_37(seq) :
	seq = list(seq)
	seq.append("1")
	seq = "".join(seq)
	weight = weighted_sum_of_sequence(seq) - 1
	while weight % 37 == 0 :
		weight = weight / 37
	c = 0
	while (weight + c) % 37 != 0 :
		c += 1
	seq = list(seq)
	seq.pop()
	seq.append(representations[c])

	return "".join(seq)

#print(encode_mod_37("A6_7"))

#returns false if no error. true if error
def is_error_encode_37(seq) :
	return not weighted_sum_of_sequence(seq) % 37 == 0

#print(is_error_encode_37("A6_7Q"))

#ISBN_seq takes in a string ISBN sequence without dashes
def ISBN_check_checkdigit(ISBN_seq, check_digit) :
	ISBN_seq = list(ISBN_seq)
	ISBN_seq.append("1")
	ISBN_seq_weight = weighted_sum_of_sequence(ISBN_seq) - 1
	ISBN_seq_weight += check_digit
	return ISBN_seq_weight % 11 == 0

def ISBN_find_checkdigit(ISBN_seq) :
	ISBN_seq = list(ISBN_seq)
	ISBN_seq.append("1")
	ISBN_seq_weight = weighted_sum_of_sequence(ISBN_seq) - 1
	checkdigit = 0
	while (ISBN_seq_weight + checkdigit) % 11 != 0 :
		checkdigit += 1
	return checkdigit

#check digit of 10 leads to a ISBN_seq weight that is % 11 = 0
#print(ISBN_check_checkdigit("013152447", 10))

#Finds checkdigit of incomplete ISBN seq
#print(ISBN_find_checkdigit("013152447"))

#digit 6 replace by 9 leads to error
#print(ISBN_check_checkdigit("188954445", 10))

def construct_hamming_code(msg) :
	if len(msg) == 4 :
		s1, s2, s3, s4 = [int(x) for x in msg]
		s5, s6, s7 = [None, None, None]
		if (s1 + s3 + s4) % 2 == 0 :
			s5 = 0
		else :
			s5 = 1
		if (s1 + s2 + s4) % 2 == 0 :
			s6 = 0
		else :
			s6 = 1
		if (s1 + s2 + s3) % 2 == 0 :
			s7 = 0
		else :
			s7 = 1
		return "".join([str(x) for x in [s1,s2,s3,s4,s5,s6,s7]])
	else :
		raise Exception("msg given is not 4 bit")


#print(construct_hamming_code("0100"))

def parity_check_hamming_code(hamming_code) :
	def correct_hamming_code(pos) :
		temp = list(hamming_code)
		if temp[pos] == "1" :
			temp[pos] = "0"
		else :
			temp[pos] = "1"
		return "".join(temp) 


	if len(hamming_code) == 7 :
		s1, s2, s3, s4, s5, s6, s7 = [int(x) for x in hamming_code]
		A, B, C = [0, 0, 0]
		if not (s1 + s3 + s4 + s5) % 2 == 0 :
			A = 1
			print("A fails parity check")
		if not (s1 + s2 + s4 + s6) % 2 == 0 :
			B = 1
			print("B fails parity check")
		if not (s1 + s2 + s3 + s7) % 2 == 0 :
			C = 1
			print("C fails parity check")

		if A == 1 and B == 1 and C == 1 :
			print("s1 error")
			return correct_hamming_code(0)
		elif B == 1 and C == 1 :
			print("s2 error")
			return correct_hamming_code(1)
		elif A == 1 and C == 1 :
			print("s3 error")
			return correct_hamming_code(2)
		elif A == 1 and B == 1 :
			print("s4 error")
			return correct_hamming_code(3)
		elif A == 1 :
			print("s5 error")
			return correct_hamming_code(4)
		elif B == 1 :
			print("s6 error")
			return correct_hamming_code(5)
		elif C == 1 :
			print("s7 error")
			return correct_hamming_code(6)
		else :
			print("no errors")
			return hamming_code
	else :
		raise Exception("msg given is not 7 bit")

#print(parity_check_hamming_code("1010101"))

#https://accuratedemocracy.com/download/software/calc.html
#FOR BORDA AND HARE

#http://condorcet.ericgorr.net/
#FOR CONDORCET AND HARE


