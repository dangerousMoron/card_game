#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 20:49:24 2020

@author: tfinney
"""

import numpy
import pint

import matplotlib.pyplot as pyplot 

u = pint.UnitRegistry()

eU = 1*(u.Btu/u.ft/u.s)

eI = numpy.linspace(0,100)*eU #flame intensity english

# def flame_conv

eh = 0.45*eI**0.46 * (u.ft/(eU**0.46)) #flmae hiehgt enlgish


# pyplot.plot(eI,eh)

mU = (1*u.kW/u.m)

# mI = numpy.linspace(0,100)*mU
mI = eI.to(mU)

mh = 0.0775*mI**0.46 * (u.m/(mU**0.46))

eh2 = mh.to(u.ft)

pyplot.plot(eI,eh)
pyplot.plot(eI,eh2)