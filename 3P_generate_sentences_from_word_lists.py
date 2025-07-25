'''
 Please write a program to generate all sentences where subject is in ["I", "You"] and
 verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
'''

subject = ["I", "You"]
verb = ["Play", "Love"]
objects = ["Hockey","Football"]

result = []

for i in subject:
    for j in verb:
        for k in objects:
            sent = f'{i} {j} {k}'
            result.append(sent)
for sent in result:
    print(sent)
