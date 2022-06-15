import json
from copy import deepcopy
from mitmproxy import http
from QuestionsBank import QuestionsBank

# 启动记录答案
# mitmdump -s test.py -w record/6-4-01 -p 8888 "~d h5we.lgb360.com"

qb = QuestionsBank('answer/answer.json')


def request(flow: http.HTTPFlow) -> None:
    if "lgb360.com/aqy/ques/" in flow.request.pretty_url and flow.request.method == 'POST':
        req_content = json.loads(flow.request.content.decode(
            'UTF-8')) if flow.request.content else {}
        if 'quesId' in req_content:
            print('reqc',req_content)
            answer = qb.getAnswer(qb.nQues[-1]['content'])
            if answer and answer[0] in qb.nQues[-1]['options']:
                req_content['answerOptions'] = answer
                flow.request.content = json.dumps(req_content).encode('UTF-8')
                print('modify req', json.loads(
                    flow.request.content.decode('UTF-8')))


def response(flow: http.HTTPFlow) -> None:
    if "lgb360.com/aqy/ques/" in flow.request.pretty_url:
        content = json.loads(flow.response.content.decode('UTF-8'))
        print(content)
        if 'data' in content and not 'count' in content['data']:
            question = deepcopy(content['data'])
            if 'ques' in question:
                print('\n本轮问题列表', len(qb.handleNQues(question)),)
                answer = qb.getAnswer(question['ques']['content'])
            else:
                answer = None
            if answer :
                print('答案:', answer)
                content['data']['ques']['content'] = question['ques']['content'] + \
                    '\n提示:'+'\n'.join(answer)
            else:
                print('暂时没有答案')
            if ('rightOptions' in question and not 'isRight' in question) or not 'ques' in question:
                print('本轮答题结束')
                qb.writeAnswers()
            flow.response.content = json.dumps(content).encode('UTF-8')
