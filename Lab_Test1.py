#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 1.
np.random.seed(0)  
aqi_readings = np.random.normal(100, 20, 1440)  
noise = np.random.normal(0, 5, 1440)  
aqi_noisy = aqi_readings + noise

# 2.
b, a = signal.butter(3, 0.1)  
aqi_smoothed = signal.filtfilt(b, a, aqi_noisy)

# 3.
hourly_avg = np.array([np.mean(aqi_smoothed[i:i+60]) for i in range(0, 1440, 60)])

# 4.
plt.figure(figsize=(12, 6))
plt.plot(aqi_noisy, label='Noisy AQI Data', alpha=0.6)
plt.plot(aqi_smoothed, label='Smoothed AQI Data', alpha=0.8, linewidth=2)
plt.scatter(np.arange(0, 1440, 60), hourly_avg, color='red', label='Hourly Averages', zorder=5)

plt.title('AQI Data: Noisy, Smoothed, and Hourly Averages')
plt.xlabel('Minutes')
plt.ylabel('AQI Value')
plt.legend()
plt.grid(True)

# 5.
threshold = 100
exceed_indices = np.where(aqi_noisy > threshold)[0]


intervals = np.split(exceed_indices, np.where(np.diff(exceed_indices) != 1)[0] + 1)
long_intervals = [interval for interval in intervals if len(interval) > 15]


for interval in long_intervals:
    plt.axvspan(interval[0], interval[-1], color='red')

plt.show()















































# In[ ]:





# In[ ]:





# In[ ]:




