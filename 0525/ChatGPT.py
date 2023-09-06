# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 14:40:28 2023

@author: s9571
"""

import os
import openai

openai.api_key = os.getenv("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")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="請問要如何考上台大?",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)