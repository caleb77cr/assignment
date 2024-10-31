def number():
    my_list=[1,2,3,4]
    sum_even = 0
    sum_odd = 0
    
    for num in my_list:
        if num%2==0:
            sum_even+=num
        else:
            sum_odd+=num    
    my_tupple=(sum_even,sum_odd)       
    return my_tupple
answer=number()
print(answer) 
