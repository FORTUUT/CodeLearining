#7.4.3 Python的多继承—例7-14 多继承示例
class Phone:                  #电话类
    def receive(self):
        print("接电话")
    def send(self):
         print("打电话")

class Message:               #消息类
    def reveiveMsg(self):
        print("接收短信") 
    def sendMsg(self):
        print("发送短信")

class Mobile(Phone,Message):   #手机类
    pass

mobile=Mobile()
mobile.receive()
mobile.send()
mobile.reveiveMsg()
mobile.sendMsg()

