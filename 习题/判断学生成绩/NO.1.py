#判断学生成绩，成绩等级A~E。其中，90分以上为‘A’，80~89分为'B'，
#70~79分为‘C’，60~69分为‘D’，60分以下为‘E’

score=int(input("请输入学生的成绩"))

if score <60:
    print("该学员等级为E")
elif score >=60 and score<70:
    print("该学员等级为D")
elif score >= 70 and score < 80:
    print("该学员等级为C")
elif score >= 80 and score < 90:
    print("该学员等级为B")
else:
    print("该学员等级为A")



