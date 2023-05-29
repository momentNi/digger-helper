from diggerhelper.tools.DiggerHelperCheck import *
import requests

class Query(object):
    @staticmethod
    def repo(args):
        # 获取仓库名称
        repo_name = args.name
        # 获取指标名称
        metric_name = args.metric
        # 获取时间
        month = args.time
        # 参数合法性检查
        helper = DiggerHelperCheck()
        metric_name, month = helper.run(metric_name, month)
        # 拼接url
        url = "https://oss.x-lab.info/open_digger/github/" + repo_name + "/" + metric_name + ".json"
        # 发送请求
        response = requests.get(url)
        if response.status_code == 200:
            print("repo.name:" + repo_name)
            print("repo.url:https://github.com/" + repo_name)
            data = response.json()
            # 判断month是否存在 进行时间处理
            if month != '*': 
                data = data.get(month)
                print("month:" + month)
                print(metric_name + ":" + str(data))
            else :
                print(metric_name + ":" + str(data))
        else:
            print("Failed to retrieve data from URL")


    @staticmethod
    def user(args):
        # 获取用户名
        user_name = args.name
        # 获取指标名称
        metric_name = args.metric
        # 获取时间
        month = args.time
        # 参数合法性检查
        helper = DiggerHelperCheck()
        metric_name, month = helper.run(metric_name, month)
        # 拼接url
        url = "https://oss.x-lab.info/open_digger/github/" + user_name + "/" + metric_name + ".json"
        print(url)
        # 发送请求
        response = requests.get(url)
        if response.status_code == 200:
            print("user.name:" + user_name)
            print("user.url:https://github.com/" + user_name)
            data = response.json()
            # 判断month是否存在 进行时间处理
            if month != '*': 
                data = data.get(month)
                print("month:" + month)
                print(metric_name + ":" + str(data))
            else :
                print(data)
        else:
            print("Failed to retrieve data from URL")

