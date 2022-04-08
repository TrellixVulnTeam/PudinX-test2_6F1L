#importing tiktokapi 
from TikTokApi import TikTokApi as tiktok
#import json for exporting data 
import json 
from jupyter_H import process_results
import pandas as pd 
import sys

def get_data(hashtag):
    verifyFP = "verify_l1kby30h_v6bFS8Sn_yrAT_4Qtu_AesH_4UHKAuPIo8kg"

    api = tiktok.get_instance(custom_verifyFp=verifyFP, use_test_endpoints=True)

    videos = api.by_hashtag(hashtag)
# with open ('export.json' , 'w')as f:
#    json.dump(videos, f)
    
    flattend_data = process_results(videos)
     

    df = pd.DataFrame.from_dict(flattend_data, orient='index')
    df['createTime'] = pd.to_datetime(df['createTime'],unit='s').dt.date
    df.to_csv('Export_Data.csv', index=False)

    

if __name__=='__main__':
     get_data(sys.argv[1])
