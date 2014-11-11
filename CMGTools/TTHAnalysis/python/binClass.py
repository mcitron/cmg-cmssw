import numpy as np
import ROOT 
from array import array

class Bin:
    def __init__(self,njet,bjet,htRange,name=None, binYield=0):
	self._njet = njet
	self._bjet = bjet
	self._htRange = np.array(htRange)
	self._yield =binYield
	if name == None: self._name = "nJet"+str(njet)+"nBJet"+str(bjet)+"htLow"+str(htRange[0])+"htHigh"+str(htRange[1])+"bin"

    def __repr__(self):
	return "<Bin njet:{0} bjet:{1} htLow:{2} htHigh:{3} yield:{4}>".format(self._njet, self._bjet,self._htRange[0],self._htRange[1],self._yield)

    def __str__(self):
	return "Bin Details: njet:{0} bjet:{1} htLow:{2} htHigh:{3} yeild:{4}".format(self._njet, self._bjet,self._htRange[0],self._htRange[1],self._yield)

    def inBin(self,jets,bjet,ht):
	if jets == self._njet and bjet == self._bjet and self._htRange[0] <= ht < self._htRange[1]:
	    self._yield+=1
	    return True
	else: return False
    def name(self):
	return self._name

class BinCollection:
    def __init__(self,njets=None,bjets=None,htRanges=None,bins=None,name=None):
	if not (bins == None):
	    self._bins = bins
	else:
	    print njets,bjets,htRanges
	    self._bins = makeBins(njets,bjets,htRanges)
    def __repr__(self):
	hello = ""
	for binn in self._bins:
	    hello += binn.name()+"\n"

	return hello

    def getBin(self,i):
	return self._bins[i]
    def getBins(self):
	return self._bins
    def __iter__(self):
	return iter(self._bins)
    def __add__(self,b):
	newBins = self._bins + b.getBins()
	return BinCollection(bins=newBins)


def makeBins(njets,bjets,htRanges):
    Bins = []
    for njet in njets:
	for i,ht in enumerate(htRanges[1:]):
	    for bjet in bjets:
		Bins.append(Bin(njet,bjet,(htRanges[i],ht)))
    return Bins



# if __name__ == '__main__':
#     njet = 1, bjet = 1
#     htBins = (100,200,300,400)

