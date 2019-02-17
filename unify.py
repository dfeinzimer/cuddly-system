'''
function unify(E1, E2);
	begin
  		case
    		both E1 and E2 are constants or the empty list:    #recursion stops
        		if E1 = E2 then return {}
        		else
          			return FAIL;
        	E1 is a variable:
            	if E1 occurs in E2 then return FAIL
            		else return {E2 / E1}
            E2 is a variable:
              	if E2 occurs in E1 then return FAIL
              		else return {E1 / E2}
            either E1 or E2 are empty then return FAIL      # the lists are of different sizes
          	otherwise:                                           # both E1 and E2 are lists
              	begin
                	HE1 = first element of E1
                    HE2 = first element of E2
                    SUBS1 = unify(HE1, HE2)
                    if SUBS1 = FAIL then return FAIL
                  	TE1 = apply(SUBS1, rest of E1)
                    TE2 = apply(SUBS2, rest of E2)
                    SUBS2 = unify(TE1, TE2)
              		if SUBS2 = FAIL then return FAIL
        				else return composition(SUBS1, SUBS2)
       			end
	end
end
'''


def apply():
	# What does apply do?
	pass


def composition():
	# Implement composition()
	pass


def unify(E1, E2):

	# If both E1 and E2 are constants or empty lists
	if ((len(E1)==0 and len(E2)==0) or (E1[0].islower() and E2[0].islower())):
		print('E1 & E2 are lower')
		if (E1 == E2):
			return None
		else:
			return "Fail: E1 & E2 are not equal"


# Main function
if __name__ == "__main__":
	print("Test 1: Empty lists")
	print(unify([],[]))
	print()

	print("Test 2: Nonempty lists")
	print(unify(["justin","david","stephen"],["Person"]))
	print()

	print("Test 3: Two constant lists")
	print(unify(["justin","david","stephen"],["adam"]))
	print()
