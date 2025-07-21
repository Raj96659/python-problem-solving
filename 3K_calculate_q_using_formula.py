'''
 Write a program that calculates and prints the value according to the given formula:
 𝑄=Square root of 2𝐶𝐷/H

 Following are the fixed values of C and H:
 C is 50. H is 30.
 D is the variable whose values should be input to your program in a comma
separated sequence.

 Example
 Let us assume the following comma separated input sequence is given to the
 program:
 100,150,180
 The output of the program should be:
 18,22,24

'''


C = 50
H = 30
D = list(map(int,input("Enter D : ").split()))

for i in D:
    Q = ((2*C*i)/H)**0.5
    print(int(Q))
