import numpy as np
import ROOT 
from array import array

class Bin:
    def __init__(self,njet,bjet,ht,name=None, binYield=0):
	self._njet = njet
	self._bjet = bjet
	self._ht = np.array(ht)
	self._yield =binYield
	if name == None: self._name = "nJet"+str(njet)+"bJet"+str(bjet)+"htLow"+str(ht[0])+"htHigh"+str(ht[1])

    def __repr__(self):
	return "<Bin njet:{0} bjet:{1} htLow:{2} htHigh:{3} yield:{4}>".format(self._njet, self._bjet,self._ht[0],self._ht[1],self._yield)

    def __str__(self):
	return "Bin Details: njet:{0} bjet:{1} htLow:{2} htHigh:{3} yeild:{4}".format(self._njet, self._bjet,self._ht[0],self._ht[1],self._yield)

    def inBin(self,jets,bjet,ht):
	if jets == self._njet and bjet == self._bjet and self._ht[0] <= ht < self._ht[1]:
	    self._yield+=1
	    return True
	else: return False

class BinCollection:
    def __init__(self,njet,bjets,ht,name=None):
	self._bins = makeBins(njet,bjets,ht)
	# bins = array( 'f', [10.,11.,12.] )
	# h = ROOT.TH1F( 'h', 'h', 2, bins )
    def writeHisto(tDir):
	tDir.cd()
	self._histo.Write()
    def getBin(self,i):
	return self._bins[i]
    def __iter__(self):
	return iter(self._bins)


def makeBins(njet,bjets,htBins):
    Bins = []
    for i,ht in enumerate(htBins[1:]):
	for bjet in bjets:
	    Bins.append(Bin(njet,bjet,(htBins[i-2],ht)))
    return Bins



# if __name__ == '__main__':
#     njet = 1, bjet = 1
#     htBins = (100,200,300,400)

