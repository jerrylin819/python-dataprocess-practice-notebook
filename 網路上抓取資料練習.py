#利用requests套件從網路上抓取資料，並利用pandas套件將資料轉換成表格的形式

import pandas as pd
import requests

water_data = requests.get("https://apiservice.mol.gov.tw/OdService/rest/datastore/A17000000J-020038-f5m")
# print(water_data)
# print(water_data.text)
# print(water_data.json())
data_table = pd.DataFrame(water_data.json()["result"]["records"])
print(data_table)