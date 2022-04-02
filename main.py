# -*- coding: utf8 -*-
from dotenv import load_dotenv
import sys
import os
extDataDir = os.getcwd()
if getattr(sys, 'frozen', False):
    extDataDir = sys._MEIPASS
load_dotenv(dotenv_path=os.path.join(extDataDir, '.env'))


import os
word = os.getenv('word')
"""from datetime import datetime

s = input("お名前は？")
y = int(input(f"こんにちは,{s}さん。歳は？"))

py = datetime.now().year-1991"""

import tkinter as tk

root = tk.Tk()
root.title(u"会話")
root.geometry("400x300")


#エントリー
EditBox = tk.Entry(width=50)
EditBox.insert(tk.END,"挿入する文字列")
EditBox.pack()

#ボタン
Button = tk.Button(text=u'ボタンです')
Button.pack()


#ここで，valueにEntryの中身が入る
value = EditBox.get()



"""if y== py:
    print(value)
    print(word)
elif y < py:
    print("若い!")
    print(word)
else:
    print("年上!")
    print(word)

input("何かキーを押すと終了")
"""


root.mainloop()