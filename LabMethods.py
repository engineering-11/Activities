import numpy as np
import pandas as pd
import datetime as dt

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

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
            comp_df.loc[idx,'deviceTime_unix'] = comp_df.loc[idx-1,'deviceTime_unix']+interval
            comp_df.loc[idx,'cpm'] = comp_df.loc[idx-1,'cpm']
            comp_df.loc[idx,'cpmError'] = comp_df.loc[idx-1,'cpmError']

    return comp_df

def bin_correlation_data(data1, data2, nrebin):
    # First we need to set the relevant time column as the index
    # We also need to make sure the values are datetime types
    # - when setting the unix time to datetime we must specificy that these
    #    values are in unites of seconds
    data1 = data1.set_index(['deviceTime_unix'])
    data1.index = pd.to_datetime(data1.index, unit='s')
    data2 = data2.set_index(['deviceTime_unix'])
    data2.index = pd.to_datetime(data2.index, unit='s')

    # resample downsamples our DataFrame
    # For example: resample("20T").mean() will combined 20 Time measurements and return the mean as the new entry
    # We reset the index because we now have reduced our total number of entries by a factor of 20
    # the *label='right'* option assigns the "Time" column using the most recent time in the set of 20 measurements
    data1_binned = data1.resample(str(rebin)+"T", label='right').mean().reset_index()
    data2_binned = data2.resample(str(rebin)+"T", label='right').mean().reset_index()
    # Force the two binned data sets to have the same length by cutting off the end of the longer one
    if len(data1_binned) > len(data2_binned):
        data1_binned = data1_binned.drop(data1_binned.index[len(data2_binned):])
    elif len(data2_binned) > len(data1_binned):
        data2_binned = data2_binned.drop(data2_binned.index[len(data1_binned):])

    # Check for any NaN entries - this can happen when binning if there were
    inds1 = pd.isnull(data1_binned).any(1).to_numpy().nonzero()[0]
    inds2 = pd.isnull(data2_binned).any(1).to_numpy().nonzero()[0]

    indsnan = np.concatenate([inds1,inds2])
    indsnan = np.unique(indsnan)

    j = len(indsnan)-1

    while (j>=0):
        data1_binned = data1_binned.drop(data1_binned.index[indsnan[j]])
        data2_binned = data2_binned.drop(data2_binned.index[indsnan[j]])
        j = j-1
    return data1_binned, data2_binned
