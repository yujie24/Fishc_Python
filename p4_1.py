# 条件分支，即 判断。常用if-else搭配

# 如果是 循环，一般用while语句。后面会用到。

score = int(input('请输入你的分数：'))
if score == 100:
	print('哇！你得了满分！')
elif 100>score>=90:
	print('A')
elif 90>score>=80:
	print('B')
elif 80>score>=70:
	print('C')
elif 70>score>=60:
	print('D')
elif 60>score:
	print('不及格哦！下次努力！')
elif 100<score or 0>score:
	print('输入错误！')
