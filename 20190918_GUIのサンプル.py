import tkinter
from tkinter import messagebox

# ボタンイベント
def btn_click():
    global content
    content = txt.get()
    if not content:
        messagebox.showinfo('入力内容', '何も入力されてないよ？')
        return

    messagebox.showinfo('入力内容', f'「 {content} 」 が入力されました！')
    root.quit()
    root.destroy()

# tkクラス生成
root = tkinter.Tk()
# 画面サイズ、画面出現位置
width = 600
height = 300
x = (root.winfo_screenwidth() - width) // 2
y = (root.winfo_screenheight() - height) // 2
geometory = f'{width}x{height}+{x}+{y}'  # ここは小文字のｘじゃなきゃだめ
root.geometry(geometory)
# 画面タイトル
root.title('はじめてのGUI')
# ラベル
lbl = tkinter.Label(text='1.なんか入力して下さい')
lbl.place(x=30, y=80)
# テキストボックス
txt = tkinter.Entry(width=50)
txt.place(x=30, y=100)
# ボタン
btn = tkinter.Button(root, text='表示', command=btn_click)
btn.place(x=280, y=230)
# ウィンドウ表示
root.mainloop()