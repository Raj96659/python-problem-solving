# Write a Python program to find uncommon words from two Strings
string1 = "This is the first string"
string2 = "This is the second string"

str1_split = string1.split()
str2_split = string2.split()

uncommon_word1 = []
uncommon_word2 = []
final_result = []
for i in str1_split:
    if i not in str2_split:
        uncommon_word1.append(i)
        final_result.append(i)

for j in str2_split:
    if j not in str1_split:
        uncommon_word2.append(j)
        final_result.append(j)
        
print(uncommon_word1 ,uncommon_word2)

print(final_result)

# print(str1_split)
# print(str2_split)
