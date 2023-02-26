Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Create baseball, a list of lists
... baseball = [[180, 78.4],
...             [215, 102.7],
...             [210, 98.5],
...             [188, 75.2]]
... 
... # Import numpy
... import numpy as np
... 
... # Create a 2D numpy array from baseball: np_baseball
... np_baseball = np.array(baseball)
... 
... # Print out the type of np_baseball
... print(type(np_baseball))
... 
... # Print out the shape of np_baseball
