#This will calculate anything outside an upper and lower bound
def outliers_iqr(data):

    lower_quartile = np.percentile(data, 25) #get 25th percentiles
    upper_quartile = np.percentile(data, 75)  #get 75th percentiles
    iqr = upper_quartile - lower_quartile  #get interquartile range
    lower_bound = lower_quartile - (iqr * 1.5) #lower bound is anything lower than a threshold 1.5 times the distance of the IQR
    upper_bound = upper_quartile + (iqr * 1.5) #upper bound is anything above than a threshold 1.5 times the distance of the IQR
    updated_vector = data  # init new vec column for data t be overwritten, preserves original data

    for idx, er in enumerate(data):
        if er >= upper_bound:
            updated_vector[idx] = np.nan #anything outside lower bound space is now not a number
        elif er <= lower_bound:
            updated_vector[idx] = np.nan #anything outside upper bound space is now not a number
    
    return updated_vector
