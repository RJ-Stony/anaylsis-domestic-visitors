# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 08:58:05 2025

@author: Roh Jun Seok
"""

import pandas as pd

kto_201901 = pd.read_excel('./data/kto_201901.xlsx',
                           header=1,
                           usecols='A:G',
                           skipfooter=4)

kto_201901.head()
kto_201901.info()

kto_201901.describe()
'''
                 관광            상용  ...             기타              계
count      67.00000     67.000000  ...      67.000000      67.000000
mean    26396.80597    408.208955  ...    5564.208955   32979.194030
std    102954.04969   1416.040302  ...   17209.438418  122821.369969
min         0.00000      0.000000  ...      16.000000      54.000000
25%       505.00000     14.500000  ...     260.000000     927.000000
50%      1304.00000     45.000000  ...     912.000000    2695.000000
75%      8365.00000    176.500000  ...    2824.500000   14905.500000
max    765082.00000  10837.000000  ...  125521.000000  916950.000000
'''

# 각 컬럼에서 0인 부분만 필터링
condition = ((kto_201901['관광'] == 0) | (kto_201901['상용'] == 0) | (kto_201901['공용'] == 0) | (kto_201901['유학/연수'] == 0))
kto_201901[condition]

kto_201901['기준년월'] = '2019-01'
kto_201901.head()

kto_201901['국적'].unique()
continents_list = ['아시아주', '미주', '구주', '대양주', '아프리카주', '기타대륙', '교포소계']

condition = (kto_201901.국적.isin(continents_list) == False)
kto_201901_country = kto_201901[condition]

kto_201901_country_newindex = kto_201901_country.reset_index(drop=True)
kto_201901_country_newindex.head()

continents = ['아시아'] * 25 + ['아메리카'] * 5 + ['유럽'] * 23 + ['오세아니아'] * 3 + ['아프리카'] * 2 + ['기타'] + ['교포']

kto_201901_country_newindex['대륙'] = continents
kto_201901_country_newindex.tail()

kto_201901_country_newindex['관광객_비율(%)'] = round(kto_201901_country_newindex['관광'] / kto_201901_country_newindex['계'] * 100, 1)

def create_kto_data(yy, mm):
    # 1. 불러올 Excel 파일 경로를 지정
    file_path = f'./data/kto_{yy}{mm}.xlsx'
    
    # 2. Excel 파일 불러오기
    df = pd.read_excel(file_path, header=1, skipfooter=4, usecols='A:G')
    
    # 3. "기준년월" 컬럼 추가
    df['기준년월'] = f'{yy}-{mm}'
    
    # 4. "국적" 컬럼에서 대륙을 제거하고 국가만 남기기
    # 대륙 컬럼 생성을 위한 목록
    ignore_list = ['아시아주', '미주', '구주', '대양주', '아프리카주', '기타대륙', '교포소계']
    
    # 대륙 미포함 조건
    condition = (df['국적'].isin(ignore_list) == False)
    df_country = df[condition].reset_index(drop=True)
    
    # 5. "대륙" 컬럼 추가
    continents = ['아시아'] * 25 + ['아메리카'] * 5 + ['유럽'] * 23 + ['오세아니아'] * 3 + ['아프리카'] * 2 + ['기타'] + ['교포']
    df_country['대륙'] = continents
    
    # 6. 국가별 "관광객 비율(%)" 컬럼 추가
    df_country['관광객_비율(%)'] = round(df_country['관광'] / df_country['계'] * 100, 1)

    # 7. "전체 비율(%)" 컬럼 추가
    tourist_sum = sum(df_country['관광'])
    df_country['전체_비율(%)'] = round(df_country['관광'] / tourist_sum * 100, 1)
    
    # 8. 만들어진 데이터프레임 반환
    return df_country

kto_test = create_kto_data(2018, 12)
kto_test.head()
kto_test.info()

df = pd.DataFrame()

for yy in range(2010, 2021):
    for mm in range(1, 13):
        try:
            temp = create_kto_data(str(yy), str(mm).zfill(2))
            df = pd.concat([df, temp], ignore_index=True)
        except:
            pass
        
df.info()
df.to_excel('./files/kto_total.xlsx', index=False)

df.head()

import pandas as pd
df = pd.read_excel('./files/kto_total.xlsx')

for nation, temp in df.groupby('국적'):
    filename = f'[국적별 관광객 데이터] {nation}.xlsx'
    temp.to_excel(f'./국적별/{filename}', index=False)