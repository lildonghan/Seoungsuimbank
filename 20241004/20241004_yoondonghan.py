# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly
import yfinance as yf
import plotly.graph_objects as go

# 서술형 문제 1
"""
답안 작성
깃허브에서 레포를 만들떄 add Readme 파일을 설정하고
gitignore 은 파이썬 으로 설정을한다. 깃을열어
which pytohon 명령어를 통해 파이썬의 구동을 확인
virtualenv venv 를 먼저 구동 가상환경 설정이되면
source venv/Scripts/activate 로 가상환경 에 진입
주피터 랩으로 maine.py 를 만들고 코드를 작성한다음
코드 작성이 끝나면 vc의 gitbash 터미널로 깃에 해당 파이썬코드를
커밋 한다.
git add 
git commit -m "test"
git push
깃허브에 해당 파이썬파일이 잘올라왔는지 확인을 한다.
"""

# 코드 문제 1
result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i * 2)
print(result)

# 답지
code_result1 = "[i * 2 for i in range(10) if i % 2 == 0]"
print(code_result1)

# # 코드 문제 2
my_dict = {'apple': 3, 'banana': 5, 'orange': 2}

# # 답지
my_dict = {'apple': 3, 'banana': 5, 'orange': 2}

for key, value in my_dict.items():
    print(f"{key} : {value}")

# 여기서부터 코드 작성

#코드 문제 3
series = pd.Series([25, 35, 45, 60, 75])


# 답지
# np.where를 사용하여 조건 적용
series = pd.Series([25, 35, 45, 60, 75])

code_result3 = np.where((series > 30) & (series < 60), series + 10, series)

result_series = pd.Series(code_result3)
print(result_series)



# 코드 문제 4
# 답지
iris = sns.load_dataset("iris")

iris.to_csv("output/code4_jungjihoon.csv", index=False)

iris.to_excel("output/code4_jungjihoon.xlsx", index=False)
print(code_result3)
# 여기서부터 코드 작성

# 코드 문제 5
data = [
    ["1,000", "1,100", '1,510'],
    ["1,410", "1,420", '1,790'],
    ["850", "900", '1,185'],
]
columns = ["03/02", "03/03", "03/04"]
df = pd.DataFrame(data=data, columns=columns)
df.info()

# 답지

def rm_comma(value):
    return int(value.replace(",", ""))

df["03/02"] = df["03/02"].apply(rm_comma)
df["03/03"] = df["03/03"].apply(rm_comma)

df.info()


print(df)
# 여기서부터 코드 작성

# 코드 문제 6
apple = yf.download("AAPL", start="2020-01-01", end = "2024-09-30")
fig, ax = plt.subplots()
ax.plot(apple['Open'], label = "Apple")
ax.legend()
plt.show()

# 답지
# 여기서부터 코드 작성

# 코드 문제 7
tips = sns.load_dataset("tips")

# 답지
# 여기서부터 코드 작성

# 코드 문제 8
apple = yf.download("AAPL", start="2024-05-01", end="2024-09-30")

# 답지
# 여기서부터 코드 작성
