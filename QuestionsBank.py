import json
import socket
from openai import OpenAI

class QuestionsBank:

    def __init__(self, filename='answer.json') -> None:
        print('本机IP地址是:',socket.gethostbyname(socket.gethostname()))
        self.filename = filename
        self.nQues = []
        self.answersDict = {}
        self.initAnswers()
        self.api_key = ""
        self.ai_model = ''
        self.ai_url=""


    def ai_answer(self, question):
        client = OpenAI(
            api_key= self.api_key,
            base_url=self.ai_url,
        )
        completion = client.chat.completions.create(
            model=self.ai_model,
            messages=[
                {
                    "role": "assistant",
                    "content": "你是一个安全生产管理方面的专家，会直接告诉别人正确的答案",
                },
                {
                    "role": "user",
                    "content": f'{question} 答案是',
                },
            ],
            top_p=0.1,
            temperature=0.1,
        )
        content = completion.choices[0].message.content
        return content

    def writeAnswers(self):
        if self.nQues:
            self.nQues.pop()
        for i in self.nQues:
            self.answersDict[i['content']] = i['rightOptions']
        self.answersDict['total_number'] = len(self.answersDict) - 1
        with open(self.filename, mode='w', encoding='utf-8') as f:
            json.dump(self.answersDict, f, indent=4, ensure_ascii=False)
        self.nQues = []

    def initAnswers(self):
        with open(self.filename, encoding='utf-8', mode='r') as f:
            self.answersDict = json.load(f)
        return self.answersDict

    def handleNQues(self, question):
        if 'rightOptions' in question:
            # print('不是第一题')
            if self.nQues:
                # print('有上一题')
                self.nQues[-1]['rightOptions'] = question['rightOptions']
        else:
            self.nQues = []
            # print('第一题')
        self.nQues.append(question['ques'])
        return self.nQues

    def getAnswer(self, question, options):
        answer = self.answersDict.get(question)
        if not answer:
            recommend = self.ai_answer(f'{question} 选项：{options}')
            answer = f'ai推荐{recommend}\n'
        else:
            answer = f'答案是: {answer}'
        return answer

if __name__ == '__main__':
    qb = QuestionsBank('answer/answerdict.json')
    print(qb.getAnswer(
        '承担安全评价、认证、检测、检验职责的机构租借资质、挂靠、出具虚假报告的，对其直接负责的主管人员和其他直接责任人员处（  ）的罚款。'))
