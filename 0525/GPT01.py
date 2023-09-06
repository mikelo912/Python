# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import openai

#openai的金鑰
openai.api_key = "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"

q = input("請輸入要詢問的問題:")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=q,
  temperature=0,
  max_tokens=1000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

#回應內容是json格式
#print(response)
ans = response['choices'][0]['text'].strip() #strip()去前後空白
print(ans)