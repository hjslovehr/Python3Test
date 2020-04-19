import tkinter

root = tkinter.Tk()

def center_window(w, h):
    # 获取屏幕 宽、高
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws/2) - (w/2)
    y = (hs/2) - h
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

center_window(400, 200)
root.resizable(False, False)
root.wm_title('My first python gui')
root.update()
root.mainloop()


if __name__ == '__main__':
    pass

