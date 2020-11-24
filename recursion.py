
def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number-1)

def reverse(s):
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]

def isPalindrom(string):
    if len(string)<=1:
        return True
    if string[0] != string[-1]:
        return False
    return isPalindrom(string[1:-1])

def main():
    #result = factorial(5)
    #print(result)
    #reversed_string = reverse("qwertyuiop")
    text_to_test = "ASDFGHJKLLKJHGFDA"
    result = isPalindrom(text_to_test)
    print(f"Is {text_to_test} reversible (a palindrome)? {result}")

if __name__ == '__main__':
    main()