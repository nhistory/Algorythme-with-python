# Write a method to replace all spaces in a string 
# with '%20'. You may assume that the string has 
# sufficient space at the end to hold the additional 
# characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, 
# please use a character array so that you can
# perform this operation in place.)

def main(urlString):
  urlList = urlString.split(" ")
  newUrlList = "%20".join(urlList)
  print(newUrlList)

urlString = "Mr John Smith"
main(urlString)