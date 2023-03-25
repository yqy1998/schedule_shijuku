import logging
import random
import os
import json
import math
import sys
import pandas as pd
import csv
import datetime
import pathlib

from sim.sim_config import SimConfig

# 实例： Python3 records.py configs/configs.json ix-25-22-12-28

if os.path.isfile(sys.argv[1]):
    cfg_json = open(sys.argv[1], "r")
    cfg = json.load(cfg_json, object_hook=SimConfig.decode_object)
    sim_cores = cfg.num_threads
    sim_loads = cfg.avg_system_load
    sim_time = cfg.sim_duration
    cfg_json.close()
    file_path = "analyses/" + sys.argv[2] + ".csv"
    dir_name = sys.argv[2]
    if os.path.isfile(file_path):
        df = pd.read_csv(file_path, dtype='object')
        ninety_nine = df.iloc[0]["99% Tail Latency"]
        ninety_nine_nine = df.iloc[0]["99.9% Tail Latency"]
        sim_throughput = df.iloc[0]["Throughput"]
        columns = ["运行名称", "核心数", "负载", "模拟时间", "99%尾延迟", "99.9#尾延迟", "吞吐量"]
        data = [str(sys.argv[2]), str(sim_cores), str(sim_loads), str(sim_time), str(ninety_nine), str(ninety_nine_nine)
                , str(sim_throughput)]
        if not os.path.isfile('multi_sim_data.csv'):
            with open('multi_sim_data.csv', mode='w') as file:
                writer = csv.writer(file)
                writer.writerow(columns)
        with open('multi_sim_data.csv', mode='a') as file:
            writer = csv.writer(file)
            writer.writerow(data)
        print("数据记录完成！")
    else:
        raise FileNotFoundError(file_path)
else:
    raise FileNotFoundError(sys.argv[1])



