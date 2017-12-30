favNum = 24
answer = int(input('请输入一个窝最喜欢的数字：'))
while True:
    if answer == favNum:
        break
    answer = input('错了！请再次输入：')
print('哈哈，厉害！')
print('窝最喜欢的数字就是%d'%favNum)
