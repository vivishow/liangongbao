import json
import socket

class QuestionsBank:

    def __init__(self, filename='answer.json') -> None:
        print('本机IP地址是:',socket.gethostbyname(socket.gethostname()))
        self.filename = filename
        self.nQues = []
        self.answersDict = {}
        self.answers = self.initAnswers()

    def writeAnswers(self):
        if self.nQues:
            self.nQues.pop()
        for i in self.nQues:
            del i['quesNo']
            del i['quesId']
            if not i in self.answers:
                self.answers.append(i)
        with open(self.filename, mode='w', encoding='utf-8') as f:
            json.dump(self.answers, f, indent=4, ensure_ascii=False)
        self.nQues = []

    def initAnswers(self):
        res = []
        with open(self.filename, encoding='utf-8', mode='r') as f:
            res = json.load(f)
        for i in res:
            self.answersDict[i['content']] = i['rightOptions']
        return res

    def handleNQues(self, question):
        if 'rightOptions' in question:
            print('不是第一题')
            if self.nQues:
                print('有上一题')
                self.nQues[-1]['rightOptions'] = question['rightOptions']
            # self.nQues.append(question['ques'])
        else:
            self.nQues = []
            print('第一题')
            # self.nQues.append(question['ques'])
        self.nQues.append(question['ques'])
        return self.nQues

    def getAnswer(self, question):
        answer = None
        if question in self.answersDict:
            answer = self.answersDict[question]
        return answer

if __name__ == '__main__':
    qb = QuestionsBank('answer/answer.json')
    print(qb.getAnswer('根据《安全生产法》的规定，关于安全生产条件的说法，正确的是（  ）。'))
