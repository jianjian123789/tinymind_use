from tinyenv.flags import flags

# 所有在介面中輸入的參數都會被自動加載。
FLAGS = flags()
# 使用參數的方法和原來相同。
print(FLAGS.iterations)  # 1000
print(FLAGS.name)
for i in range(100):
    if i%5==0:
        print(i)
print(FLAGS.dir)
