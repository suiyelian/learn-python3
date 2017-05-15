# 流程控
#
import string
import sys
print(len("1"))

code = [s+z+c for s in "mf" for z in "smlx" for c in "bgw"
        if not (s == "f" and z == "x")]
print(code)
print(set("apple"))
print({'a','p','p','l','e'})
print(len(set("apple")))

x = 'a' in set("apple")

print(x)
d1 = {"1":1,"name":2}
print(d1)


words = {}
strip = string.whitespace + string.punctuation+string.digits+"\""

for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            word = word.strip(strip)
            if len(word)>2:
                words[word]=word.get(word,0)+1
for word in sorted(words):
    print("'{0}'occrus{1}times".format(word,words[word]))