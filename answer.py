import json


# data_list = [
#     {
#         "quesId": "ovFWoCRHz0eJpAikHKFcnVqpeQniAPcA7AD4APgAgzTLDOQglTk4",
#         "rightOptions": [
#             "时间",
#             "地点",
#             "内容",
#             "发现的问题及其处理情况"
#         ]
#     }
# ]

def writeAnswer(data, filename='answer.json'):

    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def getAnswer(filename='answer.json'):
    res = {}
    with open(filename, encoding='utf-8', mode='r') as f:
        res = json.load(f)

    return res

    
if __name__ == '__main__':
    print(getAnswer())
    # data = {
    #     "ovFWoCRHz0eJpAikHKFcnVqpeQniAPcA7AD4APgAgzTLDOQglTk4": [
    #         "时间",
    #         "地点",
    #         "内容",
    #         "发现的问题及其处理情况"
    #     ]
    # }

    # writeAnswer(data)
