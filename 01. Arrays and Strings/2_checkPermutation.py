NO_OF_CHARS = 256

def permutation(str1,str2):
  count1 = [0]* NO_OF_CHARS
  count2 = [0]* NO_OF_CHARS

  for i in str1:
    count1[ord(i)] = count1[ord(i)]+1
    print(ord(i))
  
  for i in str2:
    count2[ord(i)] = count2[ord(i)]+1
    print(ord(i))

  if len(str1) != len(str2):
    return False
  
  for i in range(NO_OF_CHARS):
    if count1[i] != count2[i]:
      return False
  
  return True

str1 = "abcd"
str2 = "dcba"
if permutation(str1, str2):
  print("Yes")
else:
  print("No")