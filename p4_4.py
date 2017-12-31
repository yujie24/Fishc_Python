# break语句：终止当前循环，跳出循环体

favNum = 24
answer = int(input('请输入一个窝最喜欢的数字：'))
while True:
    if answer == favNum:
        break           # 若输入正确，就执行break语句，即跳出while循环体
    answer = int(input('错了！请再次输入：'))    # 要跟上面一样，加一个int将其转换为整型，某则这个循环没办法终止。
print('哈哈，厉害！')
print('窝最喜欢的数字就是%d'%favNum)
