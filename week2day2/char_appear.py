str=input()
cnt={}
word=str.split()
for char in word:
    cnt[char]=cnt.get(char,0)+1
print(cnt)