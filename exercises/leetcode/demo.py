def numJewelsInStones(J, S):
    jewel_set = list(J)
    count = 0
    
    for stone in S:
        if stone in jewel_set:
            count += 1
    
    return count

# Test the function
J = "aA"
S = "aAAabbbb"
print(numJewelsInStones(J, S))  # Output: 3
