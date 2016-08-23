# -*- coding: utf-8 -*-
import json
import types
from BaseHandlerh import BaseHandler

class JsonHandler(BaseHandler):
    def post(self):
        content = self.get_argument("content")
        #  d1 = json.dumps(content, sort_keys=True, separators=(',', ': '), indent=5)  # 解析为python
        #  d1 = json.dumps(content)   #Serialize obj to a JSON formatted str
        d1 = json.loads(content)   #Deserialize s (a str or unicode instance containing a JSON document) to a Python object
        print type(d1) is types.DictType  # True
        print type(d1) is types.StringType # True
        print type(d1)
        # for value1 in d1.values():
        # for key, value in content.iteritems():
        #     if key == 'paramz':
        #         print "find paramz"
        # d2 = {"content", ""}
        print d1["paramz"]
        # d3 = d2["feeds"] # 新闻数组
        # for news in d3:
        #     print "11111 a new ", news
        self.write(content)

