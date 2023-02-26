Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # height_in and weight_lb are available as a regular lists
... 
... # Import numpy
... import numpy as np
... 
... # Store weight and height lists as numpy arrays
... np_weight_lb = np.array(weight_lb)
... np_height_in = np.array(height_in)
... 
... # Print out the weight at index 50
... print(np_weight_lb[50])
... 
... # Print out sub-array of np_height_in: index 100 up to and including index 110
