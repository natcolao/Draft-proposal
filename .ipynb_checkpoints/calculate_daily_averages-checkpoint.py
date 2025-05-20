
def calculate_daily_average(data):
    """
    Used for time series frequency conversion and averaging. The argument "D" is a frequency string that signifies "calendar day" and calculates mean of the numerical columns for each day.

    Parameters
    ------------
    data : pd.DataFrame
        This is the time series data (Pandas DataFrame with a DatetimeIndex)
        that will be converted to a calendar day and averaged.

    Return
    ------------
   This is a new DataFrame containing the averaged values for each
        calendar day. The index will be the daily dates.
    """
    

return df.resample("D").mean()
    