# continue语句：终止本轮循环，并开始下一轮循环

# 注意：在开始下一循环前，会先测试循环条件

for i in range(10):
    if i % 2 != 0:
        print(i)
        continue
    i += 2
print(i)
