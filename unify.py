def apply(Arg1, Arg2):
	print("apply()", Arg1, Arg2)
	for x in Arg2:
		if x == Arg1[0]:
			print("apply(): Match found:", Arg1, Arg2)
			x = Arg1[1]
			print("apply(): Done:", Arg1, Arg2)
	return Arg1, Arg2


def composition(List1, List2):
	apply(List1, List2)
	return List1 + List2


def unify(E1, E2):

	if (len(E1)==0 and len(E2)==0):
		print('Fail: E1 and E2 are empty')
		print('Program terminated')
		return []

	# If both E1 and E2 are constants or empty lists
	if (E1[0][0].islower() and E2[0][0].islower()):
		print('E1 & E2 are lower')
		if (E1 == E2):
			return []
		else:
			print("Fail: E1 & E2 are not equal")
			return False

	# If E1 is a variable
	if (E1[0][0].isupper() and len(E1)==1 ):
		print('E1 is a variable')
		for x in E2:
			if (x == E1[0]):
				print("Fail: E1 occurs in E2")
				return False
		print("Preparing to swap: ", E1, E2)
		return E2, E1

	# If E2 is a variable
	if (E2[0][0].isupper() and len(E2)==1):
		print('E2 is a variable')
		for x in E1:
			if (x == E2[0]):
				print("Fail: E2 occurs in E1")
				return False
		print("Preparing to swap: ", E1, E2)
		return E2, E1

	# Otherwise begin
    # HE1 = first element in E1
    # HE2 = first element in E2
	HE1 = E1[0]
	HE2 = E2[0]
	SUBS1 = unify(HE1, HE2)
	print("SUBS1:", SUBS1)
	if (SUBS1 == False):
		print("Fail: SUBS1 returned Fail")
		return False
    # TE1 = every element excluding the first in E1
    # TE2 = every element excluding the first in E2
	TE1 = apply(SUBS1, E1[:1])
	TE2 = apply(SUBS1, E2[:1])
	SUBS2 = unify(TE1, TE2)
	if (SUBS2 == False):
		print("Fail: SUBS2 returned Fail")
		return False
	else:
		return composition(SUBS1, SUBS2)


# Main function
if __name__ == "__main__":
	print("Test 1: unify([],[])")
	print("Result:", unify([],[]))
	print()

	print("Test 2: unify([justin, david, stephen],[Person1, Person2, Person3])")
	print("Result:", unify(["justin", "david", "stephen"],["Person1", "Person2", "Person3"]))
	print()

	print("Test 3: unify([justin, david, stephen],[adam, eve, jesus])")
	print("Result:", unify(["justin", "david", "stephen"],["adam", "eve", "jesus"]))
	print()

	print("Test 4: unify([Person1, random1],[Person1, random2])")
	print("Result:", unify(["Person1", "random1"],["Person1", "random2"]))
	print()

	print("Test 5: unify([a, b, c],[X, Y, Z])")
	print("Result:", unify(["a","b","c"],["X","Y","Z"]))
	print()

	print("Test 6: unify([a, b, c],[x, y, z])")
	print("Result:", unify(["a","b","c"],["x","y","z"]))
	print()

	print("Test 7: unify([j, j, b],[P1, P1, P2])")
	print("Result:", unify(["j","j","b"],["P1","P1","P2"]))
	print()
