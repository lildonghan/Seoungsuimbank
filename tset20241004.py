from pandas import DataFrame

data = {
    "종목명": ["3R", "3SOFT", "ACTS"],
    "현재가": [1510, 1790, 1185],
    "등락률": [7.36, 1.65, 1.28],
}

df = DataFrame(data, index=["037730", "036360", "005760"])
df


df.to_csv("ABCD/today_stock2.csv", index=False)

df.to_excel("ABCD/today_stock2.xlsx", index=False)