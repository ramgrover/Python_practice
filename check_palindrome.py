def is_palindrome(s):
    return s == s[::-1]

# Example usage:
input_string = "R a m a m a R"
result = is_palindrome(input_string)

if result:
    print(f"The string '{input_string}' is a palindrome.")
else:
    print(f"The string '{input_string}' is not a palindrome.")