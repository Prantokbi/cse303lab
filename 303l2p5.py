#5. Find all of the words in a string that are less than 5 letters (use string above)
string ="Practice Problems to Drill List Comprehension in Your Head."
string = string.rstrip(".")
new_string = [i for i in string.split(" ") if len(i)<5]
print(new_string)