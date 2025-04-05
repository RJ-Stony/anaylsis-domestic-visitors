import pandas as pd
import matplotlib.pyplot as plt

# 한글 폰트 설정
from matplotlib import font_manager, rc
import platform

if platform.system() == 'Windows':
    path = 'c:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
elif platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
else:
    print('Check your OS system')
    
df = pd.read_excel('./files/youtube_rank.xlsx')
df.head()

df.info()

df['replaced_subscriber'] = df['Subscriber'].str.replace('만', '0000')
df['replaced_subscriber'] = df['replaced_subscriber'].astype(int)

pivot_df = df.pivot_table(index='Category',
                          values='replaced_subscriber',
                          aggfunc=['sum', 'count'])

pivot_df.columns = ['subscriber_sum', 'category_count']
pivot_df.head()

pivot_df = pivot_df.reset_index()
'''
      Category  subscriber_sum  category_count
0  [BJ/인물/연예인]       238590000              57
1  [IT/기술/컴퓨터]        11070000               6
2      [TV/방송]       285970000             108
3         [게임]        76830000              45
4      [교육/강의]        31090000              18
'''

pivot_sorted = pivot_df.sort_values(by='subscriber_sum', ascending=False)

top_7 = pivot_sorted.iloc[:7].copy()

others_sum = pivot_sorted.iloc[7:]['subscriber_sum'].sum()

top_7.reset_index(drop=True, inplace=True)
others_row = pd.DataFrame({
    'Category': ['[기타]'],
    'subscriber_sum': [others_sum]
})
plot_df = pd.concat([top_7, others_row], ignore_index=True)

fig, ax = plt.subplots(figsize=(12, 8))

explode = [0.05] * len(plot_df)
colors = plt.cm.Pastel1(range(len(plot_df)))

patches, texts, autotexts = ax.pie(
    plot_df['subscriber_sum'],
    explode=explode,
    labels=plot_df['Category'],
    autopct='%1.1f%%',
    shadow=True,
    startangle=90,
    colors=colors
)

for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_fontsize(11)

ax.set_title("Category별 Subscriber Sum 비율", fontsize=16)
ax.axis('equal')
plt.show()

pivot_sorted2 = pivot_df.sort_values(by='category_count', ascending=False)

top_7_2 = pivot_sorted2.iloc[:7].copy()

others_count = pivot_sorted2.iloc[7:]['category_count'].sum()

top_7_2.reset_index(drop=True, inplace=True)
others_row2 = pd.DataFrame({
    'Category': ['[기타]'],
    'category_count': [others_count]
})
plot_df2 = pd.concat([top_7_2, others_row2], ignore_index=True)

fig, ax = plt.subplots(figsize=(12, 8))

explode = [0.05] * len(plot_df2)
colors = plt.cm.Pastel1(range(len(plot_df2)))

patches, texts, autotexts = ax.pie(
    plot_df2['category_count'],
    explode=explode,
    labels=plot_df2['Category'],
    autopct='%1.1f%%',
    shadow=True,
    startangle=90,
    colors=colors
)

for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_fontsize(11)

ax.set_title("Category별 Category Count 비율", fontsize=16)
ax.axis('equal')
plt.show()
