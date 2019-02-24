#!/usr/bin/env python
# coding: utf-8

# HYPOTHESIS TESTING FUNDAMENTELS WITH ONE DATASET

# In[6]:


#import packages
import math as m
import numpy as np
import scipy.stats as st
#from scipy import stats as st

#create datascientist salary dataset
dataset = [117.313, 104.002, 113.038, 101.936, 84.560, 113.136, 80.740, 100.536, 105.052, 87.201, 91.986, 94.868, 
           90.45, 102.48, 85.27, 112.276, 108.637, 96.818, 92.307, 114.564, 109.714, 108.833, 115.295, 89.279, 
           81.720, 89.344, 114.426, 90.410, 95.118, 113.382]
print('data scientist salary : ', dataset)
print('*********************************')
print('')

#descriptive statistics
len_dataset = len(dataset)
mean_dataset = np.mean(dataset)
std_dev_dataset = np.std(dataset)
std_err_dataset = std_dev_dataset / (m.sqrt(len_dataset))

print('')
print('length of dataset : ', len_dataset)
print('mean of dataset : ', mean_dataset)
print('standard deviation of dataset : ', std_dev_dataset)
print('standard error of dataset : ', std_err_dataset)
print('*********************************')
print('')

#the hypothesis testing : data scientist salary $113.000. This is two-sided
hypothesis_test_value = 113.000

#t-table : unknown population variance, sample size < 30, gauss distribution
#t_value = st.t.ppf(1-0.05, 30) #n=30, @=0.05, one-sided
t_value = st.t.ppf(1-0.025, 30) #n=30, @=0.05, two-sided
print('t-value two-sided: ', t_value)
print('*********************************')
print('')

#margin of error
moe = t_value * std_err_dataset
print('')
print ('margin of error : ', moe)
print('*********************************')
print('')


ci = (mean_dataset-moe, mean_dataset+moe)
print('')
print('confidence interval for %95 : ', ci)
print('*********************************')
print('')

print('')
print('Result : $113.000 out of area for %95 confidence interval, to hypothesis test is rejected.')
print('*********************************')
print('')


#the hypothesis testing : data scientist salary $113.000. This is two-sided

#t-table : unknown population variance, sample size < 30, gauss distribution
#t_value = st.t.ppf(1-0.05, 30) #n=30, @=0.05, one-sided
t_value = st.t.ppf(1-0.005, 30) #n=30, @=0.01, two-sided
print('t-value two-sided: ', t_value)
print('*********************************')
print('')

#margin of error
moe = t_value * std_err_dataset
print('')
print ('margin of error : ', moe)
print('*********************************')
print('')


ci = (mean_dataset-moe, mean_dataset+moe)
print('')
print('confidence interval for %99 : ', ci)
print('*********************************')
print('')

print('')
print('Result : $113.000 out of area for %99 confidence interval, to hypothesis test is rejected.')
print('*********************************')
print('')


#on the other hand, we can do with formula. First we should calculate Tscore after that compare t_table_value
T_score = (mean_dataset - hypothesis_test_value) / std_err_dataset

print('')
print('Tscore : ', T_score)
print('This value out of confidence interval')
print('Our interval [-2.75, +2.75]')
print('So we reject null hypothesis that data scientist salary 113.000$')


# HYPOTHESIS TESTING WITH TWO DEPENDENT DATASETS

# In[10]:


#packages
import math as m
import numpy as np
import scipy.stats as st
#from scipy import stats as st

#datasets
patient_before_weight = [103.68, 110.68, 119.05, 101.75, 91.69, 112.03, 88.84, 105.18, 110.37, 120.99]
patient_after_weight = [92.87, 101.58, 105.66, 96.18, 86.97, 105.90, 80.56, 97.00, 99.27, 107.44]
print ('before weight : ', patient_before_weight)
print('')
print('*********************************************')
print('')
print ('after weight : ', patient_after_weight)
print('*********************************************')
print('')

#diffenrence between before and after
patient_difference_weight = list(np.array(patient_after_weight) - np.array(patient_before_weight))
print ('differences weights : ', patient_difference_weight)
print('*********************************************')
print('')

#descriptive statistics
len_dataset = len(patient_difference_weight)
mean_dataset = np.mean(patient_difference_weight)
std_dev_dataset = np.std(patient_difference_weight)
std_err_dataset = std_dev_dataset / (m.sqrt(len_dataset))

print('')
print('length of dataset : ', len_dataset)
print('mean of dataset : ', mean_dataset)
print('standard deviation of dataset : ', std_dev_dataset)
print('standard error of dataset : ', std_err_dataset)
print('*********************************************')
print('')


#the hypothesis testing : lose weight is not successful is, weight difference smaller or equal than zero. This is one-sided.
max_hypothesis_test_value = 0

#t-table : unknown population variance, sample size < 30, gauss distribution
#t_value = 2.262 #please check t-table value for %95 or @=0.05
#t_value = st.t.ppf(1-0.025, 30) #n=10, @=0.05, two-sided
t_value = st.t.ppf(1-0.05, 10) #n=10, @=0.05, one-sided
print('t-value one-sided: ', t_value)
print('*********************************')
print('')

#margin of error
moe = t_value * std_err_dataset
print ('margin of error : ', moe)
print('*********************************************')
print('')

#confidence interval
ci = (mean_dataset-moe, mean_dataset+moe)
print('confidence interval for %95 : ', ci)
print('*********************************************')
print('')

#RESULT
print('')
print('RESULT : This program is successful') 
print('Because people lost weight: [-11.194220586792486, -6.971779413207518]')
print('Null hypothesis is rejected for %95')
print('*********************************************')
print('')

#on the other hand, we can do with formula. First we should calculate Tscore after that compare t_table_value
T_score = (mean_dataset - max_hypothesis_test_value) / std_err_dataset

print('')
print('RESULT')
print('Tscore : ', T_score)
print('This value out of confidence interval')
print('Our t_value [1.8] or greater than')
print('So we reject null hypothesis')


# You want to calculate confidence interval for two independent dataset, you should apply formula.
