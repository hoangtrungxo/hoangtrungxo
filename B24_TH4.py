s = input("Nhập câu của bạn: ")
d={"UPPER CASE":3, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print ("chữ số:", d["UPPER CASE"])
print ("chữ cái:", d["LOWER CASE"])

