
from CMGTools.RootTools.fwlite.Analyzer import Analyzer
from CMGTools.RootTools.fwlite.Event import Event
from CMGTools.RootTools.statistics.Counter import Counter, Counters
from CMGTools.RootTools.fwlite.AutoHandle import AutoHandle

class ttHPhotonSkimmer( Analyzer ):
    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(ttHPhotonSkimmer,self).__init__(cfg_ana,cfg_comp,looperName)
        self.ptCuts = cfg_ana.ptCuts if hasattr(cfg_ana, 'ptCuts') else []
        self.ptCuts += 10*[-1.]

        self.idCut = cfg_ana.idCut if hasattr(cfg_ana, 'idCut') else "True"
        self.idFunc = eval("lambda photon : "+self.idCut);

    def declareHandles(self):
        super(ttHPhotonSkimmer, self).declareHandles()

    def beginLoop(self):
        super(ttHPhotonSkimmer,self).beginLoop()
        self.counters.addCounter('events')
        count = self.counters.counter('events')
        count.register('all events')
        count.register('vetoed events')
        count.register('accepted events')


    def process(self, iEvent, event):
        self.readCollections( iEvent )
        self.counters.counter('events').inc('all events')

        
        photons = []
        for pho, ptCut in zip(event.selectedPhotons, self.ptCuts):
            if not self.idFunc(pho):
                continue
            if pho.pt() > ptCut: 
                photons.append(pho)

        ret = False 
        if len(photons) >= self.cfg_ana.minPhotons:
            ret = True
        if len(photons) > self.cfg_ana.maxPhotons:
            if ret: self.counters.counter('events').inc('vetoed events')
            ret = False

        if ret: self.counters.counter('events').inc('accepted events')
        return ret
