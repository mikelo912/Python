# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import openai

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

ans = response['choices'][0]['text'].strip()
print(ans)