# 应命中
eval(user_input)
# 应命中（即使参数是变量）
x = "evil"; eval(x)
# 应排除（当前规则会排除）
eval("1+2")