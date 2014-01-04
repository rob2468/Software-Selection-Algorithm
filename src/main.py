#!/usr/bin/env python
from gensimudata import UNUM
from gensimudata import SNUM
from gensimudata import S
from gensimudata import advise
from gensimudata import invocateCo
from gensimudata import curUser
from gensimudata import w

import time
import pprint

def qualifySoftware():
    sq = []
    for i in range(SNUM):
        row = []
        for j in range(5):
            row.append(0)
        sq.append(row)
    
    for i in range(SNUM):
        # advisor
        for v in range(UNUM):
            if advise[v][curUser]==1:
                sq[i][0] += invocateCo[v][S[i].publisher]
                
        # developer
        if advise[S[i].publisher][curUser]==1:
            sq[i][1] = 1
        else:
            sq[i][1] = 0
        
        # paper
        sq[i][2] = S[i].paper
        
        # reputation
        for v in range(UNUM):
            sq[i][3] += invocateCo[v][S[i].publisher]
        
    # normalization
    for i in range(5):
        maxValue = sq[0][i]
        minValue = sq[0][i]
        for j in range(SNUM):
            if sq[j][i] > maxValue:
                maxValue = sq[j][i]
            if sq[j][i] < minValue:
                minValue = sq[j][i]
        for j in range(SNUM):
            if maxValue == minValue:
                sq[j][i] = 0
            else:
                sq[j][i] = (sq[j][i] - minValue)*1.0/(maxValue - minValue)
    
    # compute the quality for each software
    for i in range(SNUM):
        for j in range(4):
            sq[i][4] += sq[i][j]*w[j]
            
    # rank the software by sq[i][4]
    software = []
    for i in range(SNUM):
        software.append(sq[i][4])
    software.sort(cmp=None, key=None, reverse=False)
    
    res = []
    if len(software) <= 5:
        res = software
    else:
        for i in range(5):
            res.append(software[i])
    return res

if __name__ == "__main__":
    starttime=time.time()
    res = qualifySoftware()
    endtime=time.time()
    print (endtime-starttime)*1000, "ms"
    