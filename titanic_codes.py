# Soru 1: Bir dataframe yapısında veri seti çağırmak için gerekli kütüphaneyi çaığırınız.
import pandas as pd

# Soru 2: Titanik veri setini çağırınız.
df = pd.read_csv("titanic.csv")

# Soru 3:
# İlgili soruların çıktısını çalışma dosyanıza """ """ yöntemi ile kaydediniz.

# 3.1. Veri setinin boyut bilgisini çağırınız.
a = df.info
# print(a)
"""
0              1         0       3  ...   7.2500   NaN         S
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
4              5         0       3  ...   8.0500   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q
"""

# 3.2. Veri setinin sutunlarının isimlerini çağırınız.
a1 = list(df.columns)
# print(a1)
"""
['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
"""

# 3.3. Veri setinde bulunan değişkenler ve bu değişkenlerin veri yapısı bilgisini çağırınız.
a2 = df.dtypes
# print(a2)
"""
PassengerId      int64
Survived         int64
Pclass           int64
Name            object
Sex             object
Age            float64
SibSp            int64
Parch            int64
Ticket          object
Fare           float64
Cabin           object
Embarked        object
dtype: object
"""

# 3.4. Veri setini analiz etmek için değişkenlerin sayı ortalama vb bilgilerini çağırınız.
a3 = df.describe()
# print(a3)
"""
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
"""

# 3.5. Veri setinde bulunan eksik değerlerin sayısını hesaplayınız.
a4 = df.isnull().sum()
# print(a4)
"""
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
"""

# 3.6. Veri setinde bulunan "Embarked" kategorik değişkeninin kategorilerine göre sayısını hesaplayınız.
a5 = df["Embarked"].value_counts()
# print(a5)
"""
S    644
C    168
Q     77
Name: Embarked, dtype: int64
"""

# Soru 4:
# İlgili soruların çıktısını çalışma dosyanıza """ """ yöntemi ile kaydediniz.
# 4.1. Veri setinde 1, 3 ve 5. indekste bulunan verileri siliniz.
b1 = df.drop([1, 3, 5])
# print(b1)
"""
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
2              3         1       3  ...   7.9250   NaN         S
4              5         0       3  ...   8.0500   NaN         S
6              7         0       1  ...  51.8625   E46         S
7              8         0       3  ...  21.0750   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q

[888 rows x 12 columns]
"""

# 4.2. Veri setinde 1, 3 ve 5. indekste bulunan verileri KALICI olarak siliniz.
b2 = df.drop([1, 3, 5], inplace=True)
# print(df)
"""
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
2              3         1       3  ...   7.9250   NaN         S
4              5         0       3  ...   8.0500   NaN         S
6              7         0       1  ...  51.8625   E46         S
7              8         0       3  ...  21.0750   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q

[888 rows x 12 columns]
"""

# Soru 5:
# İlgili soruların çıktısını çalışma dosyanıza """ """ yöntemi ile kaydediniz.
# 5.1. Veri setini tekrar çağırınız.
c1 = df
# print(c1)
"""
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
2              3         1       3  ...   7.9250   NaN         S
4              5         0       3  ...   8.0500   NaN         S
6              7         0       1  ...  51.8625   E46         S
7              8         0       3  ...  21.0750   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q

[888 rows x 12 columns]
"""

# 5.2. Veri setinde bulunan satırlardan ilk 3 satırı ve sütunlardan "Name" sütununu çağırınız.
c2 = df.iloc[:3, 3]
# print(c2)
"""
0     Braund, Mr. Owen Harris
2      Heikkinen, Miss. Laina
4    Allen, Mr. William Henry
Name: Name, dtype: object
"""

# 5.3 Veri setinde bulunan satırlardan ilk 3 satırı ve sütunlardan "Name", "Age" sütunlarını birlikte çağırınız.
c3 = df.loc[:3, ["Name", "Age"]]
# print(c3)
"""
                      Name   Age
0  Braund, Mr. Owen Harris  22.0
2   Heikkinen, Miss. Laina  26.0
"""

# 5.4 Veri setinde yaşı 30'dan büyük olan kaç kişi vardır? Çıktı tek bir satırdan oluşturulmalıdır.
c4_age = df[df["Age"] > 30]
c4 = len(c4_age)
# print("Sonuç:", c4)
"""
Sonuç: 303
"""

# 5.5 Veri setinde yaşı 30'dan  büyük olan kişilerin isimlerini bulunuz.
c5 = df.loc[df["Age"] > 30, "Name"]
# print(c5)
"""
4                           Allen, Mr. William Henry
6                            McCarthy, Mr. Timothy J
11                          Bonnell, Miss. Elizabeth
13                       Andersson, Mr. Anders Johan
15                  Hewlett, Mrs. (Mary D Kingcome) 
                           ...                      
873                      Vander Cruyssen, Mr. Victor
879    Potter, Mrs. Thomas Jr (Lily Alexenia Wilson)
881                               Markun, Mr. Johann
885             Rice, Mrs. William (Margaret Norton)
890                              Dooley, Mr. Patrick
Name: Name, Length: 303, dtype: object
"""

# 5.6 Veri setinde yaşı 30'dan büyük olan ve cinsiyeti erkek olan kişilerin sayısını hesaplayınız. Çıktı tek bir satırdan oluşturulmalıdır.
c6_count = df.loc[(df["Age"] > 30) & (df["Sex"] == "male")]
c6 = len(c6_count)
# print("Sonuç: ", c6)
"""
Sonuç:  202
"""

# 5.7 veri setinde bulunan bilgileri Embarked-Pclass-Sex değişken kırılımını dikkate alarak gruplandırınız.
c7 = df.groupby(["Embarked", "Pclass", "Sex"])
# print(c7)
"""
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001E8923ED340>
"""

# 5.8 Veri setinde yaşı 20'den  büyük olan kişilerin hem sayılarını hemde yaş ortalamalarını hesaplayalım
c8_count = len(df[df["Age"] < 20])
c8_age = df[df["Age"] < 20]
c8_mean = c8_age["Age"].mean()
# print("20'den küçük olanların sayısı:", c8_count)
# print("20'den küçüklerin ortalaması: ", c8_mean)
"""
20'den küçük olanların sayısı: 164
20'den küçüklerin yaş ortalaması:  11.97969512195122
"""

# 5.9 Veri setinde yaşı 20'den büyük olan kişilerin cinsiyetlerine göre sayılarını ve yaş ortalamalarını hesaplayınız.
c9_count_male = len(df[(df["Age"] > 20) & (df["Sex"] == "male")])
# print("20'den büyük erkeklerin sayısı: ", c9_count_male)
c9_male = df[(df["Age"] > 20) & (df["Sex"] == "male")]
c9_mean_male = c9_male["Age"].mean()
# print("20'den büyük erkeklerin yaş ortalaması: ", c9_mean_male)

c9_count_female = len(df[(df["Age"] > 20) & (df["Sex"] == "female")])
# print("20'den büyük kadınların sayısı: ", c9_count_female)
c9_female = df[(df["Age"] > 20) & (df["Sex"] == "female")]
c9_mean_female = c9_female["Age"].mean()
# print("20'den büyük kadınların yaş ortalaması: ", c9_mean_female)
"""
20'den büyük erkeklerin sayısı:  351
20'den büyük erkeklerin yaş ortalaması:  35.81054131054131
20'den büyük kadınların sayısı:  182
20'den büyük kadınların yaş ortalaması:  34.604395604395606
"""

# 5.10 Veri setinde yaşı 20'den büyük olan kişilerin Embarked-Pclass-Sex değişken kırılımını dikkate alarak
# sayılarını ve yaş ortalamalarını min max değerini  hesaplayınız.
c10 = df[df["Age"] > 20].groupby(["Embarked", "Pclass", "Sex"])["Age"].agg(["count", "mean", "min", "max"])
# print(c10)
"""
                        count       mean   min   max
Embarked Pclass Sex                                 
C        1      female     32  38.875000  21.0  60.0
                male       34  41.441176  22.0  71.0
         2      female      4  25.000000  22.0  28.0
                male        7  29.500000  23.0  36.0
         3      female      3  32.666667  24.0  45.0
                male       17  30.000000  22.0  45.5
Q        1      female      1  33.000000  33.0  33.0
                male        1  44.000000  44.0  44.0
         2      female      1  30.000000  30.0  30.0
                male        1  57.000000  57.0  57.0
         3      female      5  28.900000  21.0  39.0
                male        9  39.333333  21.0  70.5
S        1      female     34  37.294118  21.0  63.0
                male       59  44.533898  21.0  80.0
         2      female     53  34.367925  21.0  57.0
                male       72  35.826389  21.0  70.0
         3      female     47  31.042553  21.0  63.0
                male      151  31.668874  20.5  74.0
"""
