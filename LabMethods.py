def get_binned_data(data,integration_time,max_time,min_time):
    """
    bin data into time bins with width = integration_time over the max_time - min_time interval

    Args:
        data: DataFrame of data
        integration_time: time bin (seconds) to average over
        max_time, min_time: range of times (in epoch time) to retrieve
    Returns:
        DataFrame with:
            deviceTime_unix, cpm, cpmError
    """

    # return empty dataframe if there is no data
    if len(data) == 0:
        return pd.DataFrame({})

    interval = dt.timedelta(minutes=integration_time).total_seconds()
    comp_df = pd.DataFrame(columns=['deviceTime_unix','cpm','cpmError'])

    # n_intervales should be an integer
    # - it's determined by the range of times (max-min) divided by the size of each interval
    n_intervals = int((max_time - min_time)/interval)
    data = data[(data['deviceTime_unix']>=(min_time)) & (data['deviceTime_unix']<(max_time))]

    for idx in range(n_intervals):
        idata = data[(data['deviceTime_unix']>=(max_time-interval)) & (data['deviceTime_unix']<(max_time))]

        max_time = max_time - interval
        ndata = len(idata)
        if ndata > 0:
            counts = idata.loc[:,'cpm'].sum()*5
            comp_df.loc[idx,'deviceTime_unix'] = idata.iloc[ndata//2,0]
            comp_df.loc[idx,'cpm'] = counts/(ndata*5)
            comp_df.loc[idx,'cpmError'] = np.sqrt(counts)/(ndata*5)
        elif idx > 0:
            # If there is no data in this interval, use the previous interval values
            # - as long as this isn't the first interval
            print("No data in idx {} from {} to {}".format(idx,max_time-interval,max_time))
            comp_df.loc[idx,'deviceTime_unix'] = comp_df.loc[idx-1,'deviceTime_unix']+interval
            comp_df.loc[idx,'cpm'] = comp_df.loc[idx-1,'cpm']
            comp_df.loc[idx,'cpmError'] = comp_df.loc[idx-1,'cpmError']

    return comp_df
