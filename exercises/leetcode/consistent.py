def count_consistent_strings(allowed, words):
    allowed_set = set(allowed)
    count = 0
    
    for word in words:
        if all(char in allowed_set for char in word):
            count += 1
    
    return count

# Test the function
allowed = "abc"
words = ["a", "b", "c", "ab", "ac", "bc", "abc", "def"]
count = count_consistent_strings(allowed, words)
print(count)  # Output: 7
