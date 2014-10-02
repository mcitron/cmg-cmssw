
from CMGTools.RootTools.fwlite.Analyzer import Analyzer
from CMGTools.RootTools.fwlite.Event import Event
from CMGTools.RootTools.statistics.Counter import Counter, Counters
from CMGTools.RootTools.fwlite.AutoHandle import AutoHandle

class ttHAlphaTSkimmer( Analyzer ):
    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(ttHAlphaTSkimmer,self).__init__(cfg_ana,cfg_comp,looperName)

    def declareHandles(self):
        super(ttHAlphaTSkimmer, self).declareHandles()

    def beginLoop(self):
        super(ttHAlphaTSkimmer,self).beginLoop()
        self.counters.addCounter('events')
        count = self.counters.counter('events')
        count.register('all events')
        count.register('pass alphaTCuts')
        count.register('pass forwardJetVeto')
        count.register('accepted events')


    def process(self, iEvent, event):
        self.readCollections( iEvent )
        self.counters.counter('events').inc('all events')

        #Veto forward jets that have passed the jet requirement
        if self.cfg_ana.forwardJetVeto and len(event.cleanJetsFwd) > 0:
            return False
        self.counters.counter('events').inc('pass forwardJetVeto')
            
        #Check if the event passes the alphaT cut
        for aTCut in self.cfg_ana.alphaTCuts:
            if event.alphaT > aTCut[0] and event.htJet40j >= aTCut[1] and event.htJet40j < aTCut[2]:
                self.counters.counter('events').inc('pass alphaTCuts')
                self.counters.counter('events').inc('accepted events')
                return True

        #If none of the alphaT cuts are passed, veto the event
        return False
