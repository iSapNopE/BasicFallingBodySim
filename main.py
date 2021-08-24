import FallT
import os
import sys

u = []
s = []
t = []
g = []

print("Enter all measures in S.I. units")
print("")
print("Total Number of samples: ")
n = int(input())
if n < 1:
    sys.exit()

os.system("clear")
print("Enter only the numeric part of the mesurements!")

for i in range(n):
    u.append(float(input("Initial velocity: ")))
    s.append(float(input("Height of falling object: ")))
    t.append(FallT.timeC(u[i], s[i]))
    gtmp = ((2*((s[i])-(u[i]*t[i])))/(t[i]*t[i]))
    if gtmp > 0:
        gtmp = gtmp*-1
    g.append(gtmp)
    os.system("clear")

def listPrint(l):
    for i in l:
        print(i)

print("Values of u: ")
listPrint(u)
print()
print()
print("Values of s: ")
listPrint(s)
print()
print()
print("Values of t: ")
listPrint(t)
print()
print()
print("Derived values of g form s and t: ")
listPrint(g)
