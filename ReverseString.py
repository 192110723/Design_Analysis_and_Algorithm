def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
string = input("Enter a string: ")
print("Reverse of the string:", reverse_string(string))
