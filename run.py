import datetime
import os
import subprocess
import time

# 切换到 sim-sjk.py 所在目录的父目录
os.chdir('sim')
print("切换到目录sim...", os.getcwd())
time_format = datetime.datetime.now().strftime("%H:%M:%S")
print("当前时间:", datetime.datetime.now().strftime("%H:%M:%S"))


command = ['python3', 'sim-sjk.py', '../configs/config.json', "-d"]

start_time = time.time()

result = subprocess.run(command, capture_output=True)

if result.stdout:
    print(result.stdout.decode('utf-8'))

end_time = time.time()
print("当前时间:", datetime.datetime.now().strftime("%H:%M:%S"), "总共用时：",
      end_time - start_time, "秒", "约", (end_time - start_time) / 60, "分")

os.chdir('..')
print("")
print("执行分析过程...")
print('文件名：', 'sjk_{}'.format(time_format))

command = ['python3', 'analysis.py', 'sjk_{}'.format(time_format), 'sjk_{}'.format(time_format), '0']

result = subprocess.run(command, capture_output=True)

if result.stdout:
    print(result.stdout.decode('utf-8'))



