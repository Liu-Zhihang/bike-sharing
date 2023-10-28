import requests
import time
import os

def log_to_file(message):
    """Logs a message to a local file."""
    with open("download_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"{time.ctime()}: {message}\n")
        print(message)

def download_data(url):
    headers = {
        'Cookie': 'JSESSIONID=d68b2b3c-3*********',
        'Referer': 'https://opendata.sz.gov.cn/maintenance/personal/toApiTest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'
    }

    try:
        with open('Shared_Bike_Daily_Order_Data.csv', mode='w', encoding='utf-8') as f:
            for i in range(14000, 24465):
                data = {
                    'appKey': '311e2c6**********',
                    'page': i,
                    'rows': 10000
                }
                res = requests.post(url, headers=headers, data=data)

                for entry in res.json()['data']:
                    fields = ['START_TIME', 'START_LAT', 'END_TIME', 'END_LNG', 'USER_ID', 'START_LNG', 'END_LAT', 'COM_ID']
                    record = ','.join([entry.get(field, 'null') for field in fields])
                    f.write(record)
                    f.write('\n')

                log_to_file(f'Page {i} downloaded successfully.')

                if i % 1000 == 0:
                    log_to_file(f'{i} pages of shared bike data downloaded.')

    except Exception as e:
        log_to_file(f'Exception encountered at page {i}: {e}')

if __name__ == '__main__':
    start_time = time.time()
    url = 'https://opendata.sz.gov.cn/api/29200_00403627/1/service.xhtml'
    download_data(url)
    end_time = time.time()
    log_to_file(f'Data download completed in {str(end_time-start_time)} seconds.')
