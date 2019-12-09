#coding=gbk
import random
f = open('摄影主题库.txt',encoding='utf-8')
f2 = open('往期主题.txt',encoding='utf-8',mode='r+')
contents = []
contentsOld = []
content = f.readlines()#读取主题内容
contentOld = f2.readlines()
count = len(content)#统计主题数目
print('备选主题共'+str(count)+'个')
for each_lines in content:
    if each_lines != '':
        contents.append(each_lines.replace('\n','').replace('\t',''))
for each_lines in contentOld:
    if each_lines != '':
        contentsOld.append(each_lines.replace('\n','').replace('\t',''))
print(contentsOld)
def lotte(count):
    rand = random.randint(0, count-1)  # 根据主题数量生成随机数
    print('随机数：'+ str(rand))
    theTheme = content[rand]#抽签
    theTheme = theTheme.replace('\n','').replace('\t','')
    if theTheme in contentsOld:
        theTheme = lotte(count)#存在超出默认递归深度的问题。
        return theTheme
    else:
        return theTheme
try:
    theTheme = lotte(count)
    print('本期主题抽签结果：'+theTheme)
    f2.write(theTheme+'\n')
except Exception as e:
    print(e)
    print('好像没有新主题了哦')
f.close()
f2.close()