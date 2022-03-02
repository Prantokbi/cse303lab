#6. Use a dictionary comprehension to count the length of each word in a sentence (use string above)
string = "Practice Problems to Drill List Comprehension in Your Head."
string = string.strip(".")
word_length = {words:len(words) for words in string.split()}
print(word_length)
