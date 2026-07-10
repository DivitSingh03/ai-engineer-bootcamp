def reverse_string(str):
    '''
    This function takes a string as input and returns it reversed
    '''
    reversed = ""
    for char in str:
        reversed = char + reversed
    return reversed

def check_palindrome(str):
    if str == reverse_string(str):
        print("Palindrome")
    else:
        print("Not a palindrome")

def factorial(num):
    while num > 0:
        if num == 1:
            return 1
        else:
            return factorial(num-1) * num
    return 1
        
        
def second_laargest(lst):
    largest = float("-inf")
    second = float("-inf")
    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num
    
    return second

def char_frequency(str):
    dict = {}
    for char in str:
        if char not in dict.keys():
            dict[char] = 1
        else:
            dict[char] += 1

    return dict


def main():
    while True:
        code = int(input('''Choose:

        1 Reverse String

        2 Palindrome

        3 Factorial

        4 Character Frequency

        5 Second Largest

        6 Exit
        
        --> '''))
        match code:
            case 1:
                str = input("Enter a string to reverse : ")
                print(reverse_string(str))
            case 2:
                str = input("Enter a string to check palindrome : ")
                print(check_palindrome(str))
            case 3:
                num = int(input("Enter a number to calculate its factorial : "))
                print(check_palindrome(num))
            case 4:
                str = input("Enter a string to check char frequency : ")
                print(char_frequency(str))
            case 5:
                lst = []
                str = input("Enter a list seperated by comma to check second largest : ")
                for char in str:
                    if char == ',':
                        continue
                    else:
                        lst.append(int(char))
                print(second_laargest(lst))
            case 6:
                break            


main()
    








