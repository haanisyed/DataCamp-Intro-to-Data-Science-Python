Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # baseball is available as a regular list of lists
... # updated is available as 2D numpy array
... 
... # Import numpy package
... import numpy as np
... 
... # Create np_baseball (3 cols)
... np_baseball = np.array(baseball)
... 
... # Print out addition of np_baseball and updated
... print(np_baseball + updated)
... 
... # Create numpy array: conversion
... conversion = np.array([0.0254, 0.453592, 1])
... 
... # Print out product of np_baseball and conversion
