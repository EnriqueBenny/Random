#%%Import
import pandas as pd
import pygsheets
#%%Permissions
gc = pygsheets.authorize(service_file='/Users/erikuben/Documents/Programming/GitHub/Random/Calling/rexburg42-ss-attendance-370611-ecfe0a080e17.json')
sh= gc.open_by_key('1n-W0qbmjBniHnEUwMXX48sZoslwy-0_hs4HMe4exLm4')
#%%
url = 'Calling/rexburg42-ss-attendance-370611-ecfe0a080e17.json'
dat = pd.read_json(url)
df= pd.DataFrame(dat)
#%%
df
# %%
