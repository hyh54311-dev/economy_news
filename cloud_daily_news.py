import os
import requests
import json
from datetime import datetime
import google.generativeai as genai
import urllib.request
import ssl

# Google Gemini API genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def get_economic_news():
      model = genai.GenerativeModel("gemini-2.0-flash")
      prompt = "Search for and summarize the top 5 Korean economic news for today. Format as Markdown for Telegram."
      response = model.generate_content(prompt)
      return response.text

def send_telegram_message(message):
      token = os.environ.get("TELEGRAM_TOKEN")
      chat_id = os.environ.get("TELEGRAM_CHAT_ID")
      if not token or not chat_id: return
            url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

if __name__ == "__main__":
      news_summary = get_economic_news()
    send_telegram_message(news_summary)
