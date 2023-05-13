#a function to return the number of negative numbers 
numbers=[4,5,-78,7,-828,1,0,-28,-89,100,99,-99,-89,-250,45,8,11,36]

def negative_count(n_list):
    # THIS IS THE LONGEST METHOD, GIVEN BELOW IS IT'S ALTERNATE ONE LINE SOLUTION
    # count=0
    # for n in n_list:
    #     if n<0:
    #         count+=1
    # return count
    
    return len([n for n in n_list if n<0])

c=negative_count(numbers)
print(c)