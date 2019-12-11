import pytest
import time
import os

if __name__ == '__main__':
    list = ("test_work2.py", "test_work.py","test_params.py")
    string = ""
    for i in list:
        string += str(i) + " "
    print(string)
    command = "pytest %s --alluredir " % string
    print(command)
    report = time.strftime('%Y-%m-%d_%H:%M')
    f_path = './report/' + str(report)
    # f_path = './report/' + '2019-10-12_16:04'
    xml_path = f_path + '/xml'
    report_path = f_path + '/report'
    # os.system('pytest test_work2.py test_work.py --alluredir ' + xml_path)
    os.system(command + xml_path)
    # os.system('pytest --alluredir ' + xml_path)
    os.system('allure generate ' + xml_path + ' -o ' + report_path)
