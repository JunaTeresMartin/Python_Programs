

def find_min_sets(digits, y):
    #digits = list(digits)# Convert digits to a list of integers
    count = 0
    i = 0
    n=0
    for i in range (len(digits)):
        n=n*10+int(digits[i])
        if n<y:
            count+=1

        n=int(digits[i])
    print(count)   


# Test the function
digits = "456105"
y = 500
min_sets = find_min_sets(digits, y)
print(f"The minimum number of sets is: {min_sets}")
