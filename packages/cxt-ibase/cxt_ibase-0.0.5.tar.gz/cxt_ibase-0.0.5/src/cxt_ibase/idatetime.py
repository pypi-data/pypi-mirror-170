from datetime import datetime, timedelta
import numpy as np

def datetimerange(start, end, step=timedelta(days=1)):
    
    assert(start <= end), "The start time must be later than the end time"
    
    date_current = start 

    while date_current <= end:
        yield date_current
        date_current += step

def timerange(start, end, step=timedelta(days=1)):
    t_generator = datetimerange(start, end, step)
    return np.array(list(t_generator))
    
