import json
from copy import deepcopy
from mitmproxy import http
from QuestionsBank import QuestionsBank

# 启动记录答案
# mitmdump -s test.py -w record/6-4-01 -p 8888 "~d h5we.lgb360.com"

qb = QuestionsBank('answer/answer.json')

def response(flow: http.HTTPFlow) -> None:
    if "lgb360.com/aqy/ques/" in flow.request.pretty_url:
        content = json.loads(flow.response.content.decode('UTF-8'))
        print(content)
        if 'data' in content and not 'count' in content['data']:
            question = deepcopy(content['data'])
            if 'ques' in question:
                print('\n本轮问题列表', len(qb.handleNQues(question)),)
                answer = qb.getAnswer(question)
            else:
                answer = None
            if answer:
                print('answer:', answer)
                # content['data']['ques']['content'] = question['ques']['content'] + \
                #     '\n提示:'+'\n'.join(answer)
            else:
                print('no answer')
            if ('rightOptions' in question and not 'isRight' in question) or not 'ques' in question:
                print('本轮答题结束')
                qb.writeAnswers()
            flow.response.content = json.dumps(content).encode('UTF-8')
