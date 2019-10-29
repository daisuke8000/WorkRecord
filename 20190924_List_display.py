import os
import sys
import subprocess
import time
import tkinter as tk
import tkinter.filedialog
from tkinter import messagebox

#Load_Dir
dock = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\Desktop\\"

#<13~21行目までは汎用性が欲しかったので作りました。不要であれば消していただいていいです。>
Selectname = [("選択フォルダ","*.Dir")]
root = tkinter.Tk()
root.withdraw()
tkinter.messagebox.showinfo('Folder to Select','対象のフォルダを選択してください！')

# Folder to Select
dock = tkinter.filedialog.askdirectory(initialdir = dock)
if dock == "":
    print("Close an application")

#Init
list1 = []
root = ""

#PythonFileSearch
def change(full):
    for files in os.listdir(full):
        base, ext = os.path.splitext(files)
        if ext == '.py':
            list1.append(files)
            a = files#FullName
            b = full+files#fullPath
            c = base#Name
            d = ext#拡張子
            e = os.path.splitext(files)#タプル型でのFullName
            f = list1#FullName_list
            g = len(f)#list_size

    return a,b,c,d,e,f,g

aa,bb,cc,dd,ee,ff,gg = (change(dock))

def callback(i):
    def x():
        print(str(i)+"が押されました。実行します。")
        cmd = os.path.abspath(dock+i)
        subprocess.call("python "+cmd)
    return x

def main():
    # tk
    root = tkinter.Tk()
    # MainFrame,ScreenPosition
    width = 500
    height = 300
    w = (root.winfo_screenwidth() - width) // 2
    h = (root.winfo_screenheight() - height) // 2
    geometory = f'{width}x{height}+{w}+{h}'  # ここは小文字のｘじゃなきゃだめ。「かける」じゃないよ。
    root.geometry(geometory)
    # Title
    root.title('List_Display-Ver1.0(Model_M)')
    # Canbaswidget
    canvas = tk.Canvas(root)
    bar = tk.Scrollbar(root, orient=tk.VERTICAL)
    bar.pack(side=tk.RIGHT, fill=tk.Y)
    bar.config(command=canvas.yview)
    # CanvasScroll(+1はヘッダ分)
    sc_hgt=int(150/6*(gg+0.7))
    canvas.config(scrollregion=(0,0,300,sc_hgt+5)) 
    # CanvasScroll-Op(Canvasの可動域をScreoobarに通知する処理)
    canvas.config(width = width-5, height=height-5,yscrollcommand=bar.set)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH)
    frame = tk.Frame(canvas)
    canvas.create_window((0,1), window=frame, anchor=tk.NW)
    # Button
    btn = []    
    # 動的生成
    for i in ff:
        btn = tkinter.Button(frame, text=i,anchor="w",command = callback(i),relief=tk.RIDGE,width=60,bg='LightSkyBlue')
        btn.pack(fill=tk.X,padx=10)
    # Window Open
    root.mainloop()

if __name__ == "__main__":
    main()
pass