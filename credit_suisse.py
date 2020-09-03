

samples = [1,2,6,3,17,82,23,234]

#Assumes that the sample contains only positive integers
#sample should take in the integer array
#n should be the value that needs to be formed
#This function will look to find combinations of values in sample that will give n
def find_solution(n, sample) :

	sample_edit = []

	#reference will store the original sample
	reference = []

	#sample_edit will contain elements that are of the form [value at index of sample, [index of this value]]
	#[index of this value] will serve as a tool for us to record history of changes. We refer to it as 'history'
	for idx in range(len(sample)) :

		sample_edit.append([sample[idx], [idx]])

		reference.append(sample[idx])

	print(sample_edit)

	#val() just a convenient function to quickly return a value at an index of sample_edit
	def val(idx) :

		return sample_edit[idx][0]

	length = len(sample_edit)

	#If n already exists within sample_edit, just return it. No need to form any combinations
	for ele_idx in range(length) :

		if val(ele_idx) == n :

			print([ele_idx])

			return [ele_idx]

	#On each rotation, we will find add each value of sample_edit with value at (- value of rotation) from its own index.
	#If the addition > n, we won't do anything to it
	#If the addition <= n, we must make permanent the changes to the value in sample_edit
	#Then, we must also reflect add-ons to the combination by adding the (- value of rotation) to the 'history' of each element in sample_edit
	for rotation in range(1, length) :

		for ele_idx in range(length) :

			change = ele_idx - rotation

			if change < 0 :

				change += length
			
			if (val(ele_idx) + reference[change]) <= n :

				sample_edit[ele_idx][0] += reference[change]

				sample_edit[ele_idx][1].append(-rotation)

		#If all the values > n, there is no longer a need to make changes to the combinations we've created. So we break the loop
		#Else we will continue looping till rotation is == (length of sample_edit - 1) to avoid duplicate values being chosen in our combinations
		if all([val(idx) >= n in range(length)]) :

			break

	print(sample_edit)

	filtered_soln = []

	#Since we only added the (- value of rotation) as changes to 'history', we must now add the first element of 'history', which is the original index, to each of these (- value of rotation)s
	#Only then can we get the actual indexes of the values we chose to combine to make n
	for idx in range(length) : 

		if sample_edit[idx][0] == n :

			for hist_idx in range(1, len(sample_edit[idx][1])) :

				real_idx = sample_edit[idx][1][0] + sample_edit[idx][1][hist_idx]

				if real_idx < 0 :

					real_idx += length

				sample_edit[idx][1][hist_idx] = real_idx

			filtered_soln.append(sample_edit[idx][1])

	print(filtered_soln)

	#If there are no solutions, then just return No Solution
	if len(filtered_soln) > 0 :
		#There can be many solutions, so we have to pick the one with the smallest indices.
		#One way is to bubblesort filtered_soln by the sum of each of its elements
		for i in range(len(filtered_soln)): 

			for j in range(0, len(filtered_soln) - i - 1): 

				if sum(filtered_soln[j]) > sum(filtered_soln[j + 1]) : 

					filtered_soln[j], filtered_soln[j + 1] = filtered_soln[j + 1], filtered_soln[j]

		print(sorted(filtered_soln[0]))

		#Combination with the smallest indices will be returned
		return sorted(filtered_soln[0])
	else :

		return 'No Solution'

    





print(find_solution(40, samples))

