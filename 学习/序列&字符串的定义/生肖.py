#记录生效，根据年份来判断生肖

chinese_zodiac="猴鸡狗猪鼠牛虎兔龙蛇马羊"

print(chinese_zodiac[0:4])
#输出从0开始到3
print(chinese_zodiac[-1])

year=2018
print(year%12)
print(chinese_zodiac[year%12])

print("狗"in chinese_zodiac)
print("狗"not in chinese_zodiac)
print(chinese_zodiac+'abcd')
print(chinese_zodiac*3)

