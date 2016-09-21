# -*- coding:gb2312 -*-

f = open('dialog.txt')
question = []
answer = []
flag = 2   #判断当行是哪个人的话，然后放进该人的数组中
for each_line in f :

    if each_line.find(':'):
        print  each_line
        (role, line_spoken) = each_line.split('：' ,1)
        if role == '杨澜':
            question.append(line_spoken)
            flag = 1
        if role == '朴槿惠':
            answer.append(line_spoken)
            flag = 0
    elif flag == 1 :
        question.append(each_line)
    elif flag == 0 :
        answer.append(each_line)
    else:
        print '第一行有错误'
question_lines = open('Yanglan.txt','w')
answer_lines = open('Piaojinhui.txt','w')
question_lines.writelines(question)
answer_lines.writelines(answer)

f.close()
question_lines.close()
answer_lines.close()