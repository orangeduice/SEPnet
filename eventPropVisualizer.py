# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 13:32:59 2022

@author: osjac
"""
import matplotlib.pyplot as plt
import pandas  as pd
import numpy as np


#change this if ploting more properties
fig, ax = plt.subplots(2,4)

plt.style.use('ggplot')

#processes to plot
processes = ['nonresll',
             'Zjets',
             'WZ',
             'ZZ',
             'DM_300']

#corresponding colors to processes
colors  = ["red",
           "blue",
           "green",
           "orange",
           "purple"]

data_all = {} # dictionary to hold all data
#loop through each sample
for s in processes:
    #data_all[s] = pd.read_csv('https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/csv/DM_ML_notebook/'+s+'.csv') # read data files
    data_all[s] = pd.read_csv(s+'.csv') 
    
#list of properties to plot, if add more change subplot numbers    
props =["lead_lep_pt",	
        "sublead_lep_pt",	
        "mll",	
        "ETmiss",	
        "dRll",	
        "dphi_pTll_ETmiss",	
        "fractional_pT_difference",	
        "ETmiss_over_HT"]

count = 0
#loop through subplots change this if needed
for i in range(0,2):
    for o in range(0,4):
        
        
        stacked_variable = [] # list to hold variable to stack
        stacked_weight = [] # list to hold weights to stack
        for s in processes: # loop over different processes
            stacked_variable.append(data_all[s][props[count]]) # get each value of variables
            stacked_weight.append(data_all[s]['totalWeight']) # get each value of weight
        
        #create bins
        binss = np.linspace(min(data_all[s][props[count]]),max(data_all[s][props[count]]),10)
        #plot histgram and grab y vaules 
        counts, bins, bars = ax[i,o].hist(stacked_variable, 
                                          weights = stacked_weight, 
                                          bins = binss, 
                                          label = processes, 
                                          stacked = False,
                                          alpha = 0.3,
                                          color = colors)
        #find bin centers
        bin_centers = 0.5*(binss[1:]+binss[:-1])
        
        #loop through each process and plot line graphs on top of histagram
        for a,b in zip(counts,colors):
            ax[i,o].plot(bin_centers,a,color = b,linewidth = 1)
        
        #set up labels and legend
        ax[i,o].set_xlabel(props[count])
        ax[i,o].legend() 
        count = count + 1

       
        
fig.set_size_inches(20, 10)        
plt.show()

