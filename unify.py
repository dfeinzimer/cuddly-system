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

def apply():
  # What does apply do?

def unify(E1, E)
  # if both E1 and E2 are constants (lowercase letters) or the empty list2):
  if (E1[0].islower() and E2[0].islower())
  	if (E1 == E2)
    	ren {}
    else
		  	return Fa
  # if E1 is a variable
  if (E1[0].isupper())    # if E1 occurs (or shows up) in E2 
      if E1 in E2
    	return False
      else 
      	return {E2 / E1}
  # if E2 is a variable 
  if (E2[0].isupper())
  	  # if E2 occurs (or shows up) in E1
      if E2 in E1 
      	return False
      else 
      	return {E1 / E2}
  # if E1 or E2 are empty
  if (E1 = {} || E2 = {})
      return False
  else # (OTHERWISE)
      HE1 = E1[0]	# HE1 = first element of E1
      HE2 = E2[0]   # HE2 = first element of E2
      SUBS1 = unify(HE1, HE2)
      if (SUBS1.equals(False))
      	return False
      TE1 = apply(SUBS1, E1.range(1,))
      TE2 = apply(SUBS1, E2.range(1,))
      SUBS2 = unify(TE1, TE2)
      if (SUBS2.equaal(False))
      	return False
      else
      	return composition(SUBS1,SUBS2)
      
      
      
      
      
      
