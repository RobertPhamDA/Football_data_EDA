

import pandas as pd

def loadData():
  df_sales = pd.DataFrame({
    'product_id': [1, 2, 3, 4, 5],
    'price': [100, 200, 150, None, 300],
    'quantity': [2, 5, None, 3, 1]
  })
  return df_sales

def calculateRevenue(df_sales):
  df_sales['revenue'] = df_sales['price'] * df_sales['quantity']
  return df_sales

def main():
  df_sales = loadData()
  df_sales = calculateRevenue(df_sales)
  print(df_sales)

if __name__ == "__main__":
  main()

