Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> KeyboardInterrupt
>>> # np_baseball is available
... 
... # Import numpy
... import numpy as np
... 
... # Print mean height (first column)
... avg = np.mean(np_baseball[:,0])
... print("Average: " + str(avg))
... 
... # Print median height. Replace 'None'
... med = np.median(np_baseball[:,0])
... print("Median: " + str(med))
... 
... # Print out the standard deviation on height. Replace 'None'
... stddev = np.std(np_baseball[:,0])
... print("Standard Deviation: " + str(stddev))
... 
... # Print out correlation between first and second column. Replace 'None'
... corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
