# -*- coding: utf-8 -*-
#  道阻且长，行则将至
# -----Sunnyln---
#  5/10/2024  1:28 PM
from Lib import config
'''
row_data = {
                    'Sample_ID': sample_id,
                    'Timestamp': None,  # 格式化时间戳为字符串
                    'Process': None,
                    'PID': None,
                    'URL': None,
                    'Address_Handle': None,
                    'Tab_Handle': None,
                    'Version': None,
                    'Window_Handle': None,
                    'Program_Name': None,
                    'Company': None,
                }



Sample_ID,Timestamp,Process,PID,URL,Address_Handle,Tab_Handle,Version,Window_Handle,Program_Name,Company
0143692D264FD906F10B8ECAB0F139D1,2012-05-07 12:32:32,explorer.exe,1820,,,,6.00.2900.5512,20094,,
0143692D264FD906F10B8ECAB0F139D1,2012-05-07 12:33:06,360Safe.exe,1732,,,,"7, 5, 0, 1501",1017e,360安全卫士,360.cn
0143692D264FD906F10B8ECAB0F139D1,2012-05-07 12:33:14,360chrome.exe,436,NULL,2027a,20290,5.2.0.804,,360极速浏览器,360.cn
0143692D264FD906F10B8ECAB0F139D1,2012-05-07 12:33:20,360Safe.exe,1732,,,,"7, 5, 0, 1501",1017e,,
0143692D264FD906F10B8ECAB0F139D1,2012-05-07 12:33:22,360chrome.exe,436,www.hao123.com,2027a,20290,5.2.0.804,,,
0143692D264FD906F10B8ECAB0F139D1,2012-05-07 12:33:24,360chrome.exe,436,www.hao123.com,2027a,301fa,5.2.0.804,,,
0143692D264FD906F10B8ECAB0F139D1,2012-05-07 12:33:36,360chrome.exe,436,www.hao123.com,401e2,NULL,5.2.0.804,,,
0143692D264FD906F10B8ECAB0F139D1,2012-05-07 12:33:38,360chrome.exe,436,www.hao123.com,5024c,301fa,5.2.0.804,,,
                '''
# ---------------------------
merged_data_path=config.merged_behavior_path
demographic_csv_path=config.demographic_csv_path