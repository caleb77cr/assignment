
#perfect list
my_list = []
for i in range(1, 10000):
 divisor_sum = 0
 for j in range(1, i):
    if i % j == 0:
      divisor_sum= divisor_sum + j
 if divisor_sum == i:  
      my_list.append(i)
print(my_list)