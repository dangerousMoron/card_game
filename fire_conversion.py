#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 20:06:14 2020

@author: tfinney
"""

import pint

u = pint.UnitRegistry()

inten = 1*u.Btu/(u.ft*u.s)

# print())

m_inten = inten.to(u.kW/u.m)
print(m_inten)


test = 1 * u.kW/u.m
print(test.to(u.Btu/(u.ft*u.s)))


dist = 1*u.ft

print(dist.to(u.m))
dist = dist.to(u.m)

a = 1*u.m
b = a.to(u.ft)
# print(b)

rhs = (dist.magnitude) * 0.45 * (1/m_inten.magnitude)**(0.46)
# rhs = (1/dist.magnitude) * 0.45 * (m_inten.magnitude)**(0.46)
print(rhs)

# test2 = 3.28 * 0.45 * (1/0.28)**0.46
# print(test2)
# print(1/test2)

