score=int(input("请输入学生的成绩"))
if score>=80:
    if score>=90:
        print("该学员成绩等级为A")
    else:
        print("该学员成绩等级为B")
elif  score>=60:
    if score>=70:
        print("该学员成绩等级为C")
    else:
        print("该学员成绩等级为D")
else:
    print("该学员成绩等级为E")