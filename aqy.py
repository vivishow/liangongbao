# import sys
# sys.path.append("c:\\users\\cxy03\\miniconda3\\envs\\lgb\\lib\\site-packages")
# sys.path.append("c:\\users\\cxy03\\miniconda3\\lib\\site-packages")
import json
from copy import deepcopy
from mitmproxy import http
from QuestionsBank import QuestionsBank

# 启动记录答案
# mitmdump -s test.py -w record/6-4-01 -p 8888 

qb = QuestionsBank('answer/answerdict.json')


def request(flow: http.HTTPFlow) -> None:
    if "lgb360.com/aqy/ques/" in flow.request.pretty_url and flow.request.method == 'POST':
        req_content = json.loads(flow.request.content.decode(
            'UTF-8')) if flow.request.content else {}
        if 'quesId' in req_content:
            answer = qb.getAnswer(qb.nQues[-1]['content'],qb.nQues[-1]['options'])
            if answer and answer[0] in qb.nQues[-1]['options']:
                req_content['answerOptions'] = answer
                flow.request.content = json.dumps(req_content).encode('UTF-8')

def response(flow: http.HTTPFlow) -> None:
    if "lgb360.com/aqy/ques/" in flow.request.pretty_url:
        content = json.loads(flow.response.content.decode('UTF-8'))

        if content.get('data',{}).get('ques') or content.get('data',{}).get('rightOptions'):
            # 第一题只能获得‘ques', 最后一题没有'ques'，所以要判断是否有'ques'
            question = deepcopy(content['data'])
            answer = None
            if question.get('rightOptions'):
                print(f'正确答案：{question["rightOptions"]}\n')
            if 'ques' in question:
                # 不是最后一题时，获得答案
                print(f'第{question["ques"]["quesNo"]}题\n{question["ques"]["content"]}\n{question["ques"]["options"]}')
                qb.handleNQues(question)
                answer = qb.getAnswer(question['ques']['content'], question["ques"]["options"])
            else: 
                qb.writeAnswers()
                print('答题完成')
            if answer:
                print(answer)

        # if 'data' in content and not 'count' in content['data']:
        #     question = deepcopy(content['data'])
        #     if 'ques' in question:
        #         qb.handleNQues(question)
        #         answer = qb.getAnswer(question['ques']['content'])
        #     else:
        #         answer = None
        #     if answer :
        #         print('答案:', answer, '\n\n')
        #         # right_answer = []
        #         # for o in content['data']['ques']['options']:
        #         #     if o in answer:
        #         #         o = o + '(正确)'
        #         #     right_answer.append(o)
        #         # content['data']['ques']['options'] = right_answer
        #     else:
        #         print('暂时没有答案')
        #     if ('rightOptions' in question and not 'isRight' in question) or not 'ques' in question:
        #         print('本轮答题结束')
        #         qb.writeAnswers()
        #     flow.response.content = json.dumps(content).encode('UTF-8')
