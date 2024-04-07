def separate_odd_even(numbers):
    odd_numbers = []
    even_numbers = []
    
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return even_numbers, odd_numbers

# Example usage:
# element = int(input("how many no want to enter"))
# ls = []
# for i in range(0,element):
#     ls.append(input())
# print(ls)
ls = []
for i in range (0,100):
    ls.append(i)
# print(ls)


# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers, odd_numbers = separate_odd_even(l)

print("Even numbers:", even_numbers,"\nOdd numbers:", odd_numbers)
# print("Odd numbers:", odd_numbers)
