import tkinter as tk

# 创建主界面
win = tk.Tk()

# 设置窗口标题
win.title("图书管理系统")

# 设置窗口大小
win.geometry("500x500")

# 创建标签
label = tk.Label(win, text = "图书管理系统", font = ("Arial", 50))

# 将标签放置在主界面的中央
label.pack(expand = True, fill = "both")

# 在标签下方创建两个按钮
button1 = tk.Button(win, text = "登录", font = ("Arial", 20))
button1.pack(side = "left", padx = 50, pady = 50)

button2 = tk.Button(win, text = "注册", font = ("Arial", 20))
button2.pack(side = "right", padx = 50, pady = 50)

# 当按下登录按钮时创建一个新的界面，新的界面创建两行输入框
def login():
    new_win = tk.Toplevel(win)
    new_win.title("登录界面")
    new_win.geometry("500x500")
    
    label1 = tk.Label(new_win, text = "用户名", font = ("Arial", 10))
    label1.grid(row = 0, column = 0, padx = 20, pady = 20)
    
    entry1 = tk.Entry(new_win, font = ("Arial", 10))
    entry1.grid(row=0, column=1, padx = 20, pady = 20)
    
    label2 = tk.Label(new_win, text = "密码", font = ("Arial", 10))
    label2.grid(row=1, column=0, padx = 20, pady = 20)
    
    entry2 = tk.Entry(new_win, font = ("Arial", 10))
    entry2.grid(row=1, column=1, padx = 20, pady = 20)
    
    button3 = tk.Button(new_win, text = "登录", font = ("Arial", 10))
    button3.grid(row=2, column=0, padx = 20, pady = 20)
    
    button4 = tk.Button(new_win, text = "取消", font = ("Arial", 10))
    button4.grid(row=2, column=1, padx = 20, pady = 20)
    
# 当按下注册按钮时创建一个新的界面，新的界面创建两行输入框
def register():
    new_win = tk.Toplevel(win)
    new_win.title("注册界面")
    new_win.geometry("500x500")
    
    label1 = tk.Label(new_win, text = "用户名", font = ("Arial", 10))
    label1.grid(row = 0, column = 0, padx = 20, pady = 20)
    
    entry1 = tk.Entry(new_win, font = ("Arial", 10))
    entry1.grid(row=0, column=1, padx = 20, pady = 20)
    
    label2 = tk.Label(new_win, text = "密码", font = ("Arial", 10))
    label2.grid(row=1, column=0, padx = 20, pady = 20)
    
    entry2 = tk.Entry(new_win, font = ("Arial", 10))
    entry2.grid(row=1, column=1, padx = 20, pady = 20)

    label3 = tk.Label(new_win, text = "确认密码", font = ("Arial", 10))
    label3.grid(row=2, column=0, padx = 20, pady = 20)
    
    entry3 = tk.Entry(new_win, font = ("Arial", 10))
    entry3.grid(row=2, column=1, padx = 20, pady = 20)
    
    button3 = tk.Button(new_win, text = "注册", font = ("Arial", 10))
    button3.grid(row=3, column=0, padx = 20, pady = 20)
    
    button4 = tk.Button(new_win, text = "取消", font = ("Arial", 10))
    button4.grid(row=3, column=1, padx = 20, pady = 20)
    
# 绑定按钮的点击事件
button1.config(command = login)
button2.config(command = register)

# 运行主循环
win.mainloop()