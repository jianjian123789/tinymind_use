from tinyenv.flags import flags

# �����ڽ�����ݔ��ą����������ԄӼ��d��
FLAGS = flags()
# ʹ�Å����ķ�����ԭ����ͬ��
print(FLAGS.iterations)  # 1000
print(FLAGS.name)
for i in range(100):
    if i%5==0:
        print(i)
print(FLAGS.dir)
