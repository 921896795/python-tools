import requests
import json
import psycopg2
import os
from datetime import datetime

BASE_URL = "https://www.nea.gov.cn"
API_URL = "https://www.nea.gov.cn/policy/ds_694d98bc00ff4b8aa78ee2782c27acba.json"

DB_CONFIG = {
    "host": "10.10.33.214",
    "database": "test_production",
    "user": "test_production",
    "password": "Jxic@1234&",
    "port": "5866"
}

def fatch_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        return data
    
def process_data(data):
    def extract_text_from_html(html_str):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_str, 'html.parser')
        clean_text = soup.get_text(separator=' ').strip() #文本提取
        return clean_text[:250] if clean_text else ''
    
    processed_data = []
    for item in data['datasource']:
        title = item.get('showTitle', '')
        clean_title = extract_text_from_html(title)
        processed_data.append(clean_title)
    print(processed_data)

if __name__ == "__main__":
    data = fatch_data()
    process_data(data)