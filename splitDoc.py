# -*- coding:gb2312 -*-

f = open('dialog.txt')
question = []
answer = []
flag = 2   #�жϵ������ĸ��˵Ļ���Ȼ��Ž����˵�������
for each_line in f :

    if each_line.find(':'):
        print  each_line
        (role, line_spoken) = each_line.split('��' ,1)
        if role == '����':
            question.append(line_spoken)
            flag = 1
        if role == '���Ȼ�':
            answer.append(line_spoken)
            flag = 0
    elif flag == 1 :
        question.append(each_line)
    elif flag == 0 :
        answer.append(each_line)
    else:
        print '��һ���д���'
question_lines = open('Yanglan.txt','w')
answer_lines = open('Piaojinhui.txt','w')
question_lines.writelines(question)
answer_lines.writelines(answer)

f.close()
question_lines.close()
answer_lines.close()