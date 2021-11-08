# Python3 program to illustrate String with unique
# characters
def uniqueCharacters(str):

	# Converting string to set
	setstring = set(str)
	
	# If length of set is equal to len of string
	# then it will have unique characters
	if(len(setstring) == len(str)):
		return True
	
	return False

str = "abcd"
print(uniqueCharacters(str))