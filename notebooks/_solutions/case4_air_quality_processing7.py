# Now we combine the dates and the hours into a datetime, and set this as the index
data_stacked.index = pd.to_datetime(data_stacked['date'] + data_stacked['hour'], format="%Y-%m-%d%H")