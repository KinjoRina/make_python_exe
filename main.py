from dotenv import load_dotenv
import sys
extDataDir = os.getcwd()
if getattr(sys, 'frozen', False):
    extDataDir = sys._MEIPASS
load_dotenv(dotenv_path=os.path.join(extDataDir, '.env'))


import os
word = os.getenv('word')
from datetime import datetime

s = input("お名前は？")
y = int(input(f"こんにちは,{s}さん。歳は？"))

py = datetime.now().year-1991

if y== py:
    print("同い年")
    print(word)
elif y < py:
    print("若い!")
    print(word)
else:
    print("年上!")
    print(word)

input("何かキーを押すと終了")