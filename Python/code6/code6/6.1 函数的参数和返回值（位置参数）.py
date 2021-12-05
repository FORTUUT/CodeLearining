#6.1 函数的参数和返回值（位置参数）
def getvolume(r,h):
      print("圆的半径r={}, 圆的高={}, 圆的体积V={:<8.2f}".format(r,h,3.14*r*r*h))

getvolume(3,4)
getvolume(4,3)
# 调用函数时，执行getvolume(3,4)和getvolume(4,3)，
# 两个函数的逻辑含义是不同的。
