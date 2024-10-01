#!/usr/bin/python3

# ЛУННЫХ фаз калькулятор.
# Author: Sean B. Palmer, inamidst.com | Доработано nezatykaev
# Cf. http://en.wikipedia.org/wiki/Lunar_phase#Lunar_phase_calculation

import math, decimal, datetime
dec = decimal.Decimal

def position(now=None): 
   if now is None: 
      now = datetime.datetime.now()

   diff = now - datetime.datetime(2001, 1, 1)
   days = dec(diff.days) + (dec(diff.seconds) / dec(86400))
   lunations = dec("0.20439731") + (days * dec("0.03386319269"))

   return lunations % dec(1)

def phase(pos): 
   index = (pos * dec(8)) + dec("0.5")
   index = math.floor(index)
   return {
      0: "Новолуние", 
      1: "Растущая", 
      2: "Растущая / Первая четверть", 
      3: "Растущая", 
      4: "Полнолуние", 
      5: "Убывающая", 
      6: "Убывающая / Последняя четверть", 
      7: "Убывающая"
   }[int(index) & 7]

def main(): 
   pos = position()
   phasename = phase(pos)

   roundedpos = round(float(pos), 3)
   #print "%s (%s)" % (phasename, roundedpos)
   print (phasename, roundedpos)

if __name__=="__main__": 
   main()
