import json

def anl_to_and(lname, dname):
    res = []
    result = {'total_number':0}
    with open(f'{lname}.json', encoding='utf-8', mode='r') as f:
        res = json.load(f)
    for i in res:
        result[i['content']] = i['rightOptions']
        result['total_number'] += 1
    with open(f'{dname}.json', mode='w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

def merge_an(andf, ands):
    anfirst = {}
    ansecond = {}
    with open(f'{ands}.json', encoding='utf-8', mode='r') as f:
        ansecond = json.load(f)
    with open(f'{andf}.json', encoding='utf-8', mode='r') as f:
        anfirst = json.load(f)
    ansd = {**anfirst, **ansecond}
    ansd['total_number'] = len(ansd)-1
    with open(f'{andf}.json', mode='w', encoding='utf-8') as f:
        json.dump(ansd, f, indent=4, ensure_ascii=False)
    
if __name__ == '__main__':
    anl_to_and('answer/answer(1)', 'answer/answerdict')    
