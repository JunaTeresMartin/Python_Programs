#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
two_digit_number = input("Type a two digit number: ")
print(type(two_digit_number))
two_digit_number=int(two_digit_number)#type casting
num=two_digit_number/10;
rem=two_digit_number//10;
print(num+rem)
