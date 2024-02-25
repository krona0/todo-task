import os

def cr_dir(a):
    for i in range(1,int(a) + 1):
        os.makedirs('text' + str(i))
#        print(i)

def ls_dir():
    for i in list:
        print(str(i))

print('当前目录: ' + os.getcwd())
fmnu = input('你想创建多少文件夹: ')
print(fmnu)
cr_dir(fmnu)
print('已为你创建' + str(fmnu) + '文件夹')
list = os.listdir('./')
#print(list[0])
print('当前目录文件为: ')
ls_dir()


#os.makedirs('test')
#print(os.getcwd())
