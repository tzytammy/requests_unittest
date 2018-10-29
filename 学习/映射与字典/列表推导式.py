'''variable = [out_exp_res for out_exp in input_list if out_exp == 2]
  out_exp_res:　　列表生成元素表达式，可以是有返回值的函数。
  for out_exp in input_list：　　迭代input_list将out_exp传入out_exp_res表达式中。
  if out_exp == 2：　　根据条件过滤哪些值可以。'''

multiples = [i for i in range(30) if i % 3 is 0]
print(multiples)
# Output: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]


def squared(x):
    return x*x
multiples = [squared(i) for i in range(30) if i % 3 is 0]
print (multiples)
#  Output: [0, 9, 36, 81, 144, 225, 324, 441, 576, 729]


multiples = (i for i in range(30) if i % 3 is 0)
print(type(multiples))
#  Output: <type 'generator'>

