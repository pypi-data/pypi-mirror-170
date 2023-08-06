## **What is it used for?**

Convert a Pandas DataFrame/Series with dtype str/string/object to the best available dtypes

### Installation

```python
pip install a-pandas-ex-string-to-dtypes
```

### Usage

```python
    from a_pandas_ex_string_to_dtypes import pd_add_string_to_dtypes
    import pandas as pd
    pd_add_string_to_dtypes()
    df = pd.read_csv("https://github.com/pandas-dev/pandas/raw/main/doc/data/titanic.csv")
    print(df)
    print(df.dtypes)   
    
    
         PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
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
    [891 rows x 12 columns]  
    
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
    
    
    
    
    
    dfstring = pd.concat(
        [df[x].astype("string") for x in df.columns], axis=1, ignore_index=True
    )
    dfstring.columns=df.columns
    print(dfstring)
    print(dfstring.dtypes)  
    
        PassengerId Survived Pclass  ...     Fare Cabin Embarked
    0             1        0      3  ...     7.25  <NA>        S
    1             2        1      1  ...  71.2833   C85        C
    2             3        1      3  ...    7.925  <NA>        S
    3             4        1      1  ...     53.1  C123        S
    4             5        0      3  ...     8.05  <NA>        S
    ..          ...      ...    ...  ...      ...   ...      ...
    886         887        0      2  ...     13.0  <NA>        S
    887         888        1      1  ...     30.0   B42        S
    888         889        0      3  ...    23.45  <NA>        S
    889         890        1      1  ...     30.0  C148        C
    890         891        0      3  ...     7.75  <NA>        Q
    [891 rows x 12 columns]    
    
    
    PassengerId    string
    Survived       string
    Pclass         string
    Name           string
    Sex            string
    Age            string
    SibSp          string
    Parch          string
    Ticket         string
    Fare           string
    Cabin          string
    Embarked       string
    dtype: object    
    
    
    
    converted = dfstring.ds_string_to_best_dtype()
    print(converted)
    print(converted.dtypes)
         PassengerId  Survived  Pclass  ...     Fare Cabin Embarked
    0              1         0       3  ...   7.2500  <NA>        S
    1              2         1       1  ...  71.2833   C85        C
    2              3         1       3  ...   7.9250  <NA>        S
    3              4         1       1  ...  53.1000  C123        S
    4              5         0       3  ...   8.0500  <NA>        S
    ..           ...       ...     ...  ...      ...   ...      ...
    886          887         0       2  ...  13.0000  <NA>        S
    887          888         1       1  ...  30.0000   B42        S
    888          889         0       3  ...  23.4500  <NA>        S
    889          890         1       1  ...  30.0000  C148        C
    890          891         0       3  ...   7.7500  <NA>        Q
    [891 rows x 12 columns]    
    
    
    PassengerId      uint16
    Survived          uint8
    Pclass            uint8
    Name             string
    Sex            category
    Age              object
    SibSp             uint8
    Parch             uint8
    Ticket           object
    Fare            float64
    Cabin          category
    Embarked       category
    dtype: object    
    
    
        Parameters:
            df: Union[pd.DataFrame, pd.Series]
        Returns:
            Union[pd.DataFrame, pd.Series]
```
