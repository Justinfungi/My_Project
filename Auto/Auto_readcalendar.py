#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pyttsx3
engine = pyttsx3.init()

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 170)     # setting up new voice rate

"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1


# In[17]:


def main():
    engine.say("Hi, i'm jarvas. What could i do for you")
    engine.runAndWait()

main()

