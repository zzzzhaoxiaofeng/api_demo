import pytest
import time
import subprocess
import csv

if __name__ == '__main__':

    # tmp = time.strftime("%Y%m%d-%H%M%S",time.localtime(time.time()))
    # pytest.main(['-s', f'--alluredir=./report/{tmp}/json/', '--reruns=3', '--reruns-delay=1'])
    # subprocess.call(f"allure generate ./report/{tmp}/json -o ./report/{tmp}/html",shell=True)

    pytest.main(['-s','./cases/test_ddt.py', f'--alluredir=./report/{tmp}/json/', '--reruns=3', '--reruns-delay=1'])




    # def __csv_reader(filename):
    #     reslut = []
    #     with open(file=f"./data/{filename}", mode="r", encoding="utf-8") as f:
    #         readers = csv.reader(f)
    #         for content in readers:
    #             reslut.append(content)
    #     return reslut[1:]
    #
    #
    # print(__csv_reader("add_event.csv"))




