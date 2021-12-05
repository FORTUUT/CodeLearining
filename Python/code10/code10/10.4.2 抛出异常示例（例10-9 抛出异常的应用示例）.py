# 10.4.2 抛出异常示例（例10-9 抛出异常的应用示例）.py
def payOut(quota):
    if (quota>5000):
        raise ValueError("The quota out of bounds!")
    else:
        return quota-quota*0.1
pay=payOut(4000)
print("实际支出金额是：",pay)
pay=payOut(5200)
print("实际支出金额是：",pay)


