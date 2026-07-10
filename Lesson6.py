# 1. Ask the user to enter a word or sentence 
text = input("Enter a word or sentence: ")
# 2. Reverse the string and store it in revText 
revText = text[::-1]
# 3. replace text with the reversed string
text = revText
# 4. Print a message 
print("You are shown the reversed string")
# 5. Print the reversed string
print(text)