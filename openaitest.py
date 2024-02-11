from config import apikey
import os
import openai

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write a resignition letter to boss",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)

'''
{
  "warning": "This model version is deprecated. Migrate before January 4, 2024 to avoid disruption of service. Learn more https://platform.openai.com/docs/deprecations",
  "id": "cmpl-85py1vUwjkir7ttMIWL6XeOkC7R91",
  "object": "text_completion",
  "created": 1696402093,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "\n\nDear [Boss Name],\n\nI am writing to inform you of my intention to resign from my position as [Position] with [Company Name].\n\nThis decision has been a difficult one for me but, after careful consideration, I have come to the conclusion that it is the best course of action for me to take at this time.\n\nI sincerely appreciate everything I have learned during my time here, as well as the support and encouragement you have provided me.\n\nI am happy to discuss transitioning the work I have been doing, and am willing to fulfil my notice period during this time.\n\nSincerely,\n\n[Your Name]",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 7,
    "completion_tokens": 135,
    "total_tokens": 142
  }
}

'''