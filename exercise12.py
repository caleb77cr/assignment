def work():
    my_string=["iradukunda","gwiza","moise"]
    my_dictionary={}
    for x in my_string:
        my_dictionary[x]=len(x)
    return my_dictionary
answer =work()
print(answer)