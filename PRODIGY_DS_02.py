import pandas as pd
import numpy as np

headers=["symboling","normalized-losses","make","fule-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]

df=pd.read_csv('/content/drive/MyDrive/car_dataset', names=headers)

df.head()

df.replace("?",np.nan,inplace=True)
df.head(5)

missing_data=df.isnull()
missing_data.head(5)

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")

avg_num_loss=df['normalized-losses'].astype("float").mean()
avg_num_loss

df['normalized-losses'].replace(np.nan,avg_num_loss,inplace=True)
df.head(10)

missing_data = df.isnull()
missing_data.head(5)

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")

avg_num_loss=df['price'].astype("float").mean()
avg_num_loss

df['price'].replace(np.nan,avg_num_loss,inplace=True)
df.head(10)

missing_data = df.isnull()
missing_data.head(5)

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")

avg_num_loss=df['bore'].astype("float").mean()
avg_num_loss

df['bore'].replace(np.nan,avg_num_loss,inplace=True)
df.head(10)

missing_data = df.isnull()
missing_data.head(5)

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")

avg_num_loss=df['stroke'].astype("float").mean()
avg_num_loss

df['stroke'].replace(np.nan,avg_num_loss,inplace=True)
df.head(10)

missing_data = df.isnull()
missing_data.head(5)

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")

avg_num_loss=df['horsepower'].astype("float").mean()
avg_num_loss

df['horsepower'].replace(np.nan,avg_num_loss,inplace=True)
df.head(10)

missing_data = df.isnull()
missing_data.head(5)

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")

avg_num_loss=df['peak-rpm'].astype("float").mean()
avg_num_loss

df['peak-rpm'].replace(np.nan,avg_num_loss,inplace=True)
df.head(10)

missing_data = df.isnull()
missing_data.head(5)

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")

#Most frequent item for num of doors

df['num-of-doors'].value_counts()
df['body-style'].value_counts()


df['num-of-doors'].value_counts().idxmax()

df['num-of-doors'].replace(np.nan,'four',inplace=True)
df.head(10)

missing_data = df.isnull()
missing_data.head(5)

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")

