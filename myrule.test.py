# ruleid: python.dangerous-eval
eval(user_input)

# ruleid: python.dangerous-eval
eval(get_string_from_db())

# ruleid: python.dangerous-eval
eval("__import__('os').system('ls')")   # 虽然是字符串字面量，但仍是危险写法，规则当前会漏报（见局限说明）

# ok: python.dangerous-eval
eval("1 + 2")   # 纯数学常量，无害

# ok: python.dangerous-eval
result = 42
print(result)