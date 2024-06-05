import json
import csv

def anl_to_and(lname, dname):
    '''
    老版本answer.json文件转换为新版本answerdict.json文件
    lname:老版本answer.json文件名
    dname:新版本answerdict.json文件名
    '''
    res = []
    result = {'total_number':0}
    with open(f'{lname}.json', encoding='utf-8', mode='r') as f:
        res = json.load(f)
    for i in res:
        result[i['content']] = i.get('rightOptions')
        result['total_number'] += 1
    with open(f'{dname}.json', mode='w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

def merge_an(andf, ands):
    '''
    合并answerdict.json文件
    andf:老版本answerdict.json文件名
    ands:新版本answerdict.json文件名
    '''
    anfirst = {}
    ansecond = {}
    with open(f'{ands}.json', encoding='utf-8', mode='r') as f:
        ansecond = json.load(f)
    with open(f'{andf}.json', encoding='utf-8', mode='r') as f:
        anfirst = json.load(f)
    ansd = {**ansecond, **anfirst}
    ansd['total_number'] = len(ansd)-1
    with open(f'{andf}.json', mode='w', encoding='utf-8') as f:
        json.dump(ansd, f, indent=4, ensure_ascii=False)

def json_to_csv(jname, cname):
    headers = ['题目', '答案']
    ques_dict = {}
    with open(f'{jname}.json', encoding='utf-8', mode='r') as f:
        ques_dict = json.load(f)
    with open(f'{cname}.csv', mode='w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for i in ques_dict:
            if i == 'total_number':
                continue
            writer.writerow([i, ques_dict[i]])

def json_to_txt(jname, tname):
    with open(f'{jname}.json', encoding='utf-8', mode='r') as f:
        ques_dict = json.load(f)
    del ques_dict['total_number']
    ques_list = [[k,json.dumps(v,ensure_ascii=False)] for k,v in ques_dict.items()]
    ques_list = ["######".join(i) for i in ques_list]
    ques_list = [i+'\n' for i in ques_list]
    with open(f"{tname}.txt", 'w', encoding='utf-8') as f:
        # json.dump(ques_list,f,ensure_ascii=False)
        f.writelines(ques_list)
    
if __name__ == '__main__':
    # anl_to_and('answer/answer', 'answer/answer1') 
    # merge_an('answer/answerdict', 'answer/answer') 
    json_to_csv('../liangongbao/answer/answerdict', '../liangongbao/answer/answercsv')
    json_to_txt('../liangongbao/answer/answerdict', '../liangongbao/answer/answertxt')
