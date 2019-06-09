from Configs import app
import time
import os

class Logger:
    logPath = app.logPath
    moduleNmae = ''

    def __init__(self, module=''):
        self.moduleNmae = module

    # 写入LOG
    def write(self, text):
        # 构建文件path
        pathList = [
            self.logPath,
            self.moduleNmae,
            time.strftime('%Y%m', time.localtime(time.time())),
            time.strftime('%d', time.localtime(time.time())) + '.log'
        ]
        path = os.sep.join(pathList)
        print(path)
        # return 0
        # 判断文件是否存在
        mode = 'a'
        if not os.path.exists(os.path.dirname(path)):
            mode = 'w+'
            os.makedirs(os.path.dirname(path))
        elif not os.path.exists(path):
            mode = 'w+'
        print(mode)
        # 拼装log内容
        lines = [
            '\n',
            '-------- ' + time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time())) + " --------",
            '\n'
        ]
        if isinstance(text, list):
            for l in text:
                lines.append(l)
                lines.append('\n')
        else:
            lines.append(text)
            lines.append('\n')

        lines += [
            '-------------------------------------',
            '\n',
            '\n'
        ]

        with open(path, mode, encoding='utf-8') as f:
            f.writelines(lines)
