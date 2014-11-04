import os 
import logging 

from CMGTools.RootTools.fwlite.Analyzer import Analyzer
from CMGTools.RootTools.fwlite.Event import Event
from CMGTools.RootTools.statistics.Counter import Counter, Counters
from CMGTools.RootTools.fwlite.AutoHandle import AutoHandle
from CMGTools.RootTools.utils.DeltaR import deltaR

class ttHIsoTrackSkimmer( Analyzer ):
    def __init__(self, cfg_ana, cfg_comp, looperName ):
        #Rather than using the inherited init do own so can choose directory
        #name

        #super(ttHIsoTrackSkimmer,self).__init__(cfg_ana,cfg_comp,looperName)

        self.name = cfg_ana.name
        self.verbose = cfg_ana.verbose
        self.cfg_ana = cfg_ana
        self.cfg_comp = cfg_comp
        self.looperName = looperName
        if hasattr(cfg_ana, 'skimmerName'):
            self.dirName = '/'.join( [self.looperName, cfg_ana.skimmerName] )
        else:
            self.dirName = '/'.join( [self.looperName, self.name] )

        os.mkdir( self.dirName )

        # this is the main logger corresponding to the looper.
        # each analyzer could also declare its own logger
        self.mainLogger = logging.getLogger( looperName )
        self.beginLoopCalled = False


        self.ptCuts = cfg_ana.ptCuts if hasattr(cfg_ana, 'ptCuts') else []
        self.ptCuts += 10*[-1.]

        self.idCut = cfg_ana.idCut if hasattr(cfg_ana, 'idCut') else "True"
        self.idFunc = eval("lambda object : "+self.idCut);

    def declareHandles(self):
        super(ttHIsoTrackSkimmer, self).declareHandles()

    def beginLoop(self):
        super(ttHIsoTrackSkimmer,self).beginLoop()
        self.counters.addCounter('events')
        count = self.counters.counter('events')
        count.register('all events')
        count.register('vetoed events')
        count.register('accepted events')



    def process(self, iEvent, event):
        self.readCollections( iEvent )
        self.counters.counter('events').inc('all events')

        
        objects = []
        selectedObjects = getattr(event, self.cfg_ana.objects)
        for obj, ptCut in zip(selectedObjects, self.ptCuts):
	    allowTrack = False
	    for i in range (0,len(event.selectedMuons)) :
		if (i == self.cfg_ana.allowedMuon): break
		if(deltaR(event.selectedMuons[i].eta(), event.selectedMuons[i].phi(), obj.eta(), obj.phi()) < 0.01) : allowTrack=True

	    for i in range (0,len(event.selectedElectrons)) :
		if (i == self.cfg_ana.allowedElectron): break
		if(deltaR(event.selectedElectrons[i].eta(), event.selectedElectrons[i].phi(), obj.eta(), obj.phi()) < 0.01) : allowTrack=True

            if not self.idFunc(obj):
                continue
            if obj.pt() > ptCut and not allowTrack: 
                objects.append(obj)


        ret = False 
        if len(objects) >= self.cfg_ana.minObjects:
            ret = True
        if len(objects) > self.cfg_ana.maxObjects:
            if ret: self.counters.counter('events').inc('vetoed events')
            ret = False

        if ret: self.counters.counter('events').inc('accepted events')
        return ret
