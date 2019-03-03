import json
from PyQt5.QtWidgets import QApplication, QLabel
from aip import AipOcr
from PyQt5 import QtWidgets
import time
import THEKEY2BD



class BaiDuOcr:
    def __init__(self):
        self.api_id = THEKEY2BD.THEKE2BD_api_id
        self.api_key = THEKEY2BD.THEKE2BD_api_key
        self.secret_key = THEKEY2BD.THEKE2BD_secret_key
        self.client = AipOcr(self.api_id, self.api_key, self.secret_key)
    def invoke(self,path):

        self.image = self.get_file_content(path)
        """ 调用通用文字识别, 图片参数为本地图片 """
        self.client.basicGeneral(self.image);
        """ 如果有可选参数 """
        options = {}
        options["language_type"] = "CHN_ENG"
        options["detect_direction"] = "true"
        options["detect_language"] = "true"
        options["probability"] = "true"

        """ 带参数调用通用文字识别, 图片参数为本地图片 """
        data = self.client.basicGeneral(self.image, options)
        # print(data['words_result'])
        d=data['words_result']
        return d



    def invokeHigh(self,path):
        self.image = self.get_file_content(path)

        """ 调用通用文字识别（高精度版） """
        self.client.basicAccurate(self.image);

        """ 如果有可选参数 """
        options = {}
        options["language_type"] = "CHN_ENG"
        options["detect_direction"] = "true"
        options["detect_language"] = "true"
        options["probability"] = "true"

        """ 带参数调用通用文字识别（高精度版） """
        data=self.client.basicAccurate(self.image, options)
        d = data['words_result']
        return d
        # print(data['words_result'])

    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()




