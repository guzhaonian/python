# 引用uiautomator2包
import uiautomator2 as u2
import time
 
# 使用设备唯一标志码链接设备，其中9phqaetw是通过adb获取的设备标志码
# d = u2.connect('9phqaetw')  
d = u2.connect()  # 当前只有一个设备时可以用这个
 
 
d.unlock()  # 解锁屏幕
time.sleep(2)  # 等待手机反应2秒钟
 
# 锁屏密码
password = "123456789"
 
# 输入锁屏密码
for c in password:
    d(text=c).click()
    time.sleep(0.1)  # 间隔0.3秒单击一次屏幕
# a = d.app_current() 
# print(a)
