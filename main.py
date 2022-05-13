import datetime
import pandas as pd
import yfinance as yf

# files
input_file = 'rvn_taxes_21.csv'
output_file = 'tax_report_21.csv'

# start and end dates of deposits within previous tax year 
end = datetime.datetime(2021, 12, 31)
start = datetime.datetime(2021, 3, 12)

if __name__ == '__main__':
    # display all rows and columns from dataframe
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    # load wallet .csv file and reformat date column
    csv_df = pd.read_csv(input_file)
    csv_df['Date'] = pd.to_datetime(csv_df['Date']).dt.normalize()  # strip time from date column
    # print(csv_df)

    # download historical price information with predefined date range and format dataframe
    hist_df = yf.download(tickers='RVN-USD', start=start, end=end, progress=False)
    hist_df = hist_df.reset_index()
    # print(his_data)


    # merge dataframes and save to new file
    merged_dataframe = pd.merge(csv_df, hist_df)
    merged_dataframe["Cost_Basis"] = merged_dataframe["Amount (RVN)"] * merged_dataframe["Close"]
    merged_dataframe.loc['Total_Taxable'] = pd.Series(merged_dataframe['Cost_Basis'].sum(), index=['Cost_Basis'])
    # print(merged_dataframe)
    merged_dataframe.to_csv(output_file)


