# 10.4.2 抛出异常示例（例10-9 抛出异常的应用示例）2.py
def payOut(quota):
    if (quota>5000):
        raise ValueError("The quota out of bounds!") #抛出异常
    else:
        return quota-quota*0.1
try:
  pay=payOut(4000)
  print("实际支出金额是：",pay)
  pay=payOut(5200)
  print("实际支出金额是：",pay)
except Exception:   #Exception类捕获异常
  print("支出金额不合要求")



