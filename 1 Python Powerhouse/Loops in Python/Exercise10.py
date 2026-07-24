# write your code here
a = input()
b = input()
ana = True
c = 0
if len(a) != len(b):
    ana = False
for i in a:
    if i not in b:
        ana = False
        c += 1

if c==0:
    print("Anagram")
else:
    print("Not Anagram")