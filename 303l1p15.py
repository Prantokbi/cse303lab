#Given a two list of numbers (hardcoded in the program)
#create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list.

lst1 =[1,2,3,4,5]
lst2 =[10,15,20,25,30]
new_lst1=[x for x in lst1 if x % 2 !=0]
new_lst2=[x for x in lst2 if x %2 == 0]
for x in new_lst2:
    new_lst1.append(x)
print(new_lst1)

