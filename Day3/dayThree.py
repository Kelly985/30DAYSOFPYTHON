# Program to display the Fibonacci sequence 

x = int(input("How many times? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of times is valid
if x <= 0:
   print("Please enter a positive number")
# if there is only one term, return n1
elif x == 1:
   print("Fibonacci sequence upto",x,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < x:
       print(n1)
       new_n = n1 + n2
       # update values
       n1 = n2
       n2 = new_n
       count += 1