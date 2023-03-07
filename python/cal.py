#coding:utf-8

class Cal(object):
    def add(self,a,b):
        return a+b

    def minus(self,a,b):
        return a-b

    def div(self,a,b):
        try:
            return a/b
        except:
            return  "divdend can't be 0"

    def mul(self,a,b):
        return a*b
