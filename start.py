#coding=gbk
import random
f = open('��Ӱ�����.txt',encoding='utf-8')
f2 = open('��������.txt',encoding='utf-8',mode='r+')
contents = []
contentsOld = []
content = f.readlines()#��ȡ��������
contentOld = f2.readlines()
count = len(content)#ͳ��������Ŀ
print('��ѡ���⹲'+str(count)+'��')
for each_lines in content:
    if each_lines != '':
        contents.append(each_lines.replace('\n','').replace('\t',''))
for each_lines in contentOld:
    if each_lines != '':
        contentsOld.append(each_lines.replace('\n','').replace('\t',''))
print(contentsOld)
def lotte(count):
    rand = random.randint(0, count-1)  # ���������������������
    print('�������'+ str(rand))
    theTheme = content[rand]#��ǩ
    theTheme = theTheme.replace('\n','').replace('\t','')
    if theTheme in contentsOld:
        theTheme = lotte(count)#���ڳ���Ĭ�ϵݹ���ȵ����⡣
        return theTheme
    else:
        return theTheme
try:
    theTheme = lotte(count)
    print('���������ǩ�����'+theTheme)
    f2.write(theTheme+'\n')
except Exception as e:
    print(e)
    print('����û����������Ŷ')
f.close()
f2.close()