Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # height_in is available as a regular list
... 
... # Import numpy
... import numpy as np
... 
... # Create a numpy array from height_in: np_height_in
... np_height_in = np.array(height_in)
... 
... # Print out np_height_in
... print(np_height_in)
... 
... # Convert np_height_in to m: np_height_m
... np_height_m = np_height_in * 0.0254
... 
... # Print np_height_m
