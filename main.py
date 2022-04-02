from dotenv import load_dotenv
load_dotenv()
import os
word = os.getenv('word')
print(word)