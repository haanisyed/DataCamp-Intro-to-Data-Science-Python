Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # baseball is available as a regular list of lists
... 
... # Import numpy package
... import numpy as np
... 
... # Create np_baseball (2 cols)
... np_baseball = np.array(baseball)
... 
... # Print out the 50th row of np_baseball
... print(np_baseball[50])
... 
... # Select the entire second column of np_baseball: np_weight_lb
... print(np_baseball[49,:])
... np_weight_lb = (np_baseball[:, 1])
... 
... # Print out height of 124th player
