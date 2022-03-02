#7. Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by anysingle digit besides 1 (2–9)
nums = [i for i in range(1,1001) if [x for x in range(2,10) if i%x==0] ]
print(nums)