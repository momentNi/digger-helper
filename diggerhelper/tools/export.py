import json
import requests

from diggerhelper.tools.DiggerHelperCheck import DiggerHelperCheck


class Export(object):
    @staticmethod
    def download(args):
        output = args.output
        file_type = args.type
        # 获取仓库名称
        repo_name = args.name
        # 获取指标名称
        metric_name = args.metric
        # 获取时间
        month = args.time
        # 参数合法性检查
        helper = DiggerHelperCheck()
        metric_name, month = helper.run(metric_name, month)
        helper.check_filetype(file_type, output)
        # 拼接url
        url = "https://oss.x-lab.info/open_digger/github/" + repo_name + "/" + metric_name + ".json"
        # 发送请求
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            with open(output, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        else:
            print("Failed to download data from URL")


    @staticmethod
    def web(args):
        output = args.output
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
            data = response.json()
            with open(output, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        else:
            print("Failed to download data from URL")