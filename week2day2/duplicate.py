students=["tej","keerthi","tejaswini","tej"]
dupli=set()
seen=set()
for name in students:
    if name in seen:
        dupli.add(name)
    else :
        seen.add(name)
print(list(dupli))