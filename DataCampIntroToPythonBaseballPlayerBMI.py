Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # height_in and weight_lb are available as regular lists
... 
... # Import numpy
... import numpy as np
... 
... # Create array from height_in with metric units: np_height_m
... np_height_m = np.array(height_in) * 0.0254
... 
... # Create array from weight_lb with metric units: np_weight_kg
... np_weight_kg = np.array(weight_lb) * 0.453592
... 
... # Calculate the BMI: bmi
... bmi = np_weight_kg / (np_height_m)**2
... 
... # Print out bmi
