import re
match=re.search(r'[1-9]\d{5}','BIT 100081')
if match:
    print(match.group(0))


print("============================================")
match=re.match(r'[1-9]\d{5}','BIT 100081')
if match:
    print(match.group(0))

match=re.match(r'[1-9]\d{5}','100081  BIT')
if match:
    print(match.group(0))

print("==========findall==================================")
ls=re.findall(r'[1-9]\d{5}','BIT 100081 TSU100084')
print(ls)


print("==========split==================================")
ls=re.split(r'[1-9]\d{5}','BIT 100081 TSU100084')
print(ls)
ls=re.split(r'[1-9]\d{5}','BIT 100081 TSU100084',maxsplit=1)
print(ls)


print("==========finditer=================================")
for m in re.finditer(r'[1-9]\d{5}','BIT 100081 TSU100084'):
    if m:
        print(m.group(0))

print("==========sub=================================")
re.sub(r'[1-9]\d{5}',':zipple','BIT 100081 TSU100084')
print(re.sub(r'[1-9]\d{5}',':zipple','BIT 100081 TSU100084'))