import FinanceDataReader as fdr


df_krx = fdr.StockListing('KRX')  # KRX는 KOSPI,KOSDAQ,KONEX 모두 포함
print(df_krx.head())

