n=int(input("正方形边数："))

sepTOP="*"
sepMID="*"

for i in  range (0,n-1):
    sepTOP +="\t*"
    sepMID +="\t"

else:
    sepMID +="*"
    print(sepTOP)


for i in range (0,n-2):
    print(sepMID)

else:
    print(sepTOP)
