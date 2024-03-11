def count_digit_occurrences(start, end, digit):
    digit_count = 0

    for num in range(start, end + 1):
        digit_count += str(num).count(str(digit))
        print(str(num))

    return digit_count

# Take input from the user
start_range = int(input("Enter start range: "))
end_range = int(input("Enter end range: "))
digit_to_count = int(input("Enter digit to count: "))

# Calculate occurrences and display result
occurrences = count_digit_occurrences(start_range, end_range, digit_to_count)
print(f"Digit {digit_to_count} appears {occurrences} times in the range {start_range}-{end_range}")
