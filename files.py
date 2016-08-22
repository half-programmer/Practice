# coding=utf-8
# 文件处理
import json

from BaseHandlerh import BaseHandler
import time
from PIL import Image
import base64

class ImageHandler(BaseHandler):
    def post(self):
        imgfile = self.request.files.get('headimg')
        imgbody = self.request.files.get('body')
        retjson = {"name":"", "content":""}
        # 读
        # fo = open("E:\\VITA\\UI\\11.txt", "r")
        # 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式
        # print "文件名: ", fo.name
        # str = fo.read(25)
        # print str
        # fo.close()  # 关闭
        # 读

        # 写
        # fo = open("E:\\VITA\\UI\\11.txt", "a")
        # # 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。
        # # 也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
        # fo.write("Nihao")  # 写
        # fo.close()  # 关闭
        # 写

        # 读二进制
        # img = open("E:\\VITA\\UI\\image.jpg", "rb")
        # content = img.read(100)
        # print content
        # retjson
        # img.close()
        # self.write(content.decode('utf-8')) # 以UTF-8返回

        # 打开图片
        # img = Image.open("E:\\VITA\\UI\\image.jpg", "r")  # 打开图片
        # img = Image.open("E:\\VITA\\UI\\image.jpg", "r")  # 打开图片
        # retjson['content'] = img.tobytes() 这个乱码，并且转化非常慢

        # binarydata = img.save(r"E:\VITA\UI\binary_image")
        #img.show() //直接显示图片
        #self.write(img)

        # 使用二进制读图片
        # img = open(r"E:\VITA\UI\image.jpg", "r")
        # content = img.read()
        # img.close()
        # retjson['content'] = content


        with open(r"E:\VITA\UI\image.jpg") as f:
            data = f.read()

            print data
        self.write(json.dumps(retjson, ensure_ascii=False, indent=2))




