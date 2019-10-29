import tkinter as tk

#ボタンバインド用関数
def btn_click():
  onp = textbox1.get()
  var.set(onp)
  if len(onp)!=8:
    var1.set('Error')
  else:
    var1.set('Success')

#MainWindow
root = tk.Tk()
root.title(u"Input-Output app")
width = 400
height = 200
x = (root.winfo_screenwidth() - width) // 2
y = (root.winfo_screenheight() - height) // 2
geometory = f'{width}x{height}+{x}+{y}'  # ここは小文字のｘじゃなきゃだめ
root.geometry(geometory)

#ラベル更新用
var = tk.StringVar()
var.set("Waiting…")
var1 = tk.StringVar()
var1.set("Waiting2…")

#Frame_grid
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

#Frame_wiget
frame = tk.Frame(root)
btn = tk.Button(frame, text='Push', command=btn_click)
textbox1 = tk.Entry(frame, width=40)
textbox1.bind("<Key-Return>",  lambda x:btn_click())
#textbox1.bind("<Key-Return>",  lambda x:btn_click())
label2_1 = tk.Label(frame, text='Ouput',width = 10)
label2_2 = tk.Label(frame, textvariable=var,width = 10)
label3_1 = tk.Label(frame, text='Result',width = 10)
label3_2 = tk.Label(frame, textvariable=var1,width = 10)

#Wiget_Grid
frame.grid(row=0, column=0, sticky='nwse')
frame.grid_columnconfigure((0, 1, 2 ,3), weight=1)
frame.grid_rowconfigure((0, 1 ,2), weight=1)

#
btn.grid(row=0, column=0)
textbox1.grid(row=0, column=1, columnspan=2)
label2_1.grid(row=1, column=0)
label2_2.grid(row=1, column=1, columnspan=2)
label3_1.grid(row=2, column=0)
label3_2.grid(row=2, column=1, columnspan=2)

root.mainloop()
