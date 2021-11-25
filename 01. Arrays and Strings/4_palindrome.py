# Given a string, write a function to check 
# if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is 
# the same forwards and backwards. A permutation
# is a rearrangement of letters. 
# The palindrome does not need to be limited to just dictionary words.

# Python3 implementation to check if
# characters of a given string can
# be rearranged to form a palindrome

NO_OF_CHARS = 256

# function to check whether characters
# of a string can form a palindrome


def canFormPalindrome(st):

	# Create a count array and initialize
	# all values as 0
	count = [0] * (NO_OF_CHARS)

	# For each character in input strings,
	# increment count in the corresponding
	# count array
	for i in range(0, len(st)):
		count[ord(st[i])] = count[ord(st[i])] + 1

	# Count odd occurring characters
	odd = 0

	for i in range(0, NO_OF_CHARS):
		if (count[i] & 1):
			odd = odd + 1

		if (odd > 1):
			return False

	# Return true if odd count is 0 or 1,
	return True


# Driver code
if(canFormPalindrome("geeksforgeeks")):
	print("Yes")
else:
	print("No")

if(canFormPalindrome("geeksogeeks")):
	print("Yes")
else:
	print("No")


