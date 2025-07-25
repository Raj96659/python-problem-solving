'''
Create a function that replaces all the vowels in a string with a specified character.

 Examples
 replace_vowels("the aardvark", "#") 
➞ "th# ##rdv#rk"

 replace_vowels("minnie mouse", "?") 
➞ "m?nn?? m??s?"

 replace_vowels("shakespeare", "*") 
➞ "shkspr*"
'''

def replace_vowels(user_input, sym):
    result = ""
    vowels = 'aeiouAEIOU'
    for i in user_input:
        if i in vowels:
            result += sym  # Just directly add the symbol
        else:
            result += i
    return result

# Input
user_input = input("Enter the string: ")
sym = input("Enter the symbol: ")

# Result
res = replace_vowels(user_input, sym)
print(res)
