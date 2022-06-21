import json
import socket

class QuestionsBank:

    def __init__(self, filename='answer.json') -> None:
        print('本机IP地址是:',socket.gethostbyname(socket.gethostname()))
        self.filename = filename
        self.nQues = []
        self.answersDict = {}
        self.initAnswers()

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

    def getAnswer(self, question):
        return self.answersDict.get(question)

if __name__ == '__main__':
    qb = QuestionsBank('answer/answerdict.json')
    print(qb.getAnswer(
        '承担安全评价、认证、检测、检验职责的机构租借资质、挂靠、出具虚假报告的，对其直接负责的主管人员和其他直接责任人员处（  ）的罚款。'))
