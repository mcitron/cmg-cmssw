import CMGTools.RootTools.fwlite.Config as cfg
from CMGTools.RootTools.fwlite.Config import printComps
from CMGTools.RootTools.RootTools import *

#Load all analyzers
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *

##------------------------------------------
## Choose the type of cut flow
## Signal or control sample
##------------------------------------------

#cutFlow = 'Signal'
cutFlow = 'SingleMu'
#cutFlow = 'DoubleMu'
#cutFlow = 'SinglePhoton'
#cutFlow = 'SingleEle'
#cutFlow = 'DoubleEle'
#cutFlow = 'MultiJetEnriched'
#cutFlow = 'Test'

##------------------------------------------
## Redefine analyzer parameters
##------------------------------------------

# Muons
#------------------------------
ttHLepAna.loose_muon_pt               = 10.
ttHLepAna.loose_muon_eta              = 2.5
ttHLepAna.loose_muon_id               = "POG_ID_Tight"
ttHLepAna.loose_muon_dxy              = 0.2
ttHLepAna.loose_muon_dz               = 0.5
ttHLepAna.loose_muon_relIso           = 0.12
#
## Electrons
##------------------------------
ttHLepAna.loose_electron_id           = "POG_Cuts_ID_2012_Loose"
#ttHLepAna.loose_electron_id          = "POG_CSA14_25ns_v1_Loose"  

ttHLepAna.loose_electron_pt           = 10
ttHLepAna.loose_electron_eta          = 2.5
ttHLepAna.loose_electron_dxy          = 0.02
ttHLepAna.loose_electron_dz           = 0.2
ttHLepAna.loose_electron_relIso       = 0.15
ttHLepAna.loose_electron_lostHits     = 1 
# ttHLepAna.inclusive_electron_lostHits = 999 # no cut
ttHLepAna.ele_isoCorr                 = "rhoArea"
ttHLepAna.ele_tightId                 = "Cuts_2012"

# Photons
#------------------------------
ttHPhoAna.ptMin                       = 25
ttHPhoAna.etaMax                      = 2.5
ttHPhoAna.gammaID                     = "PhotonCutBasedIDLoose"

# Taus 
#------------------------------
ttHTauAna.etaMax         = 2.3
ttHTauAna.dxyMax         = 99999.
ttHTauAna.dzMax          = 99999.
ttHTauAna.vetoLeptons    = False
ttHTauAna.vetoLeptonsPOG = True


# Jets (for event variables do apply the jetID and not PUID yet)
#------------------------------
ttHJetAna.relaxJetId      = False
ttHJetAna.doPuId          = False
ttHJetAna.jetEta          = 5.
ttHJetAna.jetEtaCentral   = 3.
ttHJetAna.jetPt           = 50.
ttHJetAna.recalibrateJets = False
ttHJetAna.jetLepDR        = 0.4
ttHJetMCAna.smearJets     = False

##------------------------------------------
##  ISOLATED TRACK
##------------------------------------------

# FIXME have to check isolation for control regions

# those are the cuts for the nonEMu
ttHIsoTrackAna = cfg.Analyzer(
            'ttHIsoTrackAnalyzer',
#            candidates='cmgCandidates',
#            candidatesTypes='std::vector<cmg::Candidate>',
            candidates      ='packedPFCandidates',
            candidatesTypes ='std::vector<pat::PackedCandidate>',
            ptMin           = 10, ### for pion 
            ptMinEMU        = 10, ### for EMU
            dzMax           = 0.05,
            #####
            isoDR           = 0.3,
            ptPartMin       = 0,
            dzPartMax       = 0.1,
            maxAbsIso       = 8,
            #####
            MaxIsoSum       = 0.1, ### unused
            MaxIsoSumEMU    = 0.2, ### unused
            doSecondVeto    = False,
            )


##------------------------------------------
##  ALPHAT VARIABLES
##------------------------------------------

# Make alphaT and biased delta phi
ttHAlphaTAna = cfg.Analyzer(
            'ttHAlphaTVarAnalyzer'
            )

# Make mtw, z mass and deltaR between leptons and jet
ttHAlphaTControlAna = cfg.Analyzer(
            'ttHAlphaTControlAnalyzer'
            )

#-------------------------------------------
# CUTS AND VETOS
#-------------------------------------------

#Start with the signal region default cut flow

#ESums
ttHJetMETSkim.jetPtCuts   = [100,100] # require the lead two jets to be above 100GeV
ttHJetMETSkim.htCut       = ('htJet50j', 200)
ttHJetMETSkim.mhtCut      = ('mhtJet50j', 0)
ttHJetMETSkim.nBJet       = ('CSVM', 0, "jet.pt() > 50")     # require at least 0 jets passing CSVM and pt > 50


#Photons
ttHPhotonSkim = cfg.Analyzer(
    'ttHObjectSkimmer',
    skimmerName = 'ttHPhotonSkimmer',
    objects = 'selectedPhotons',
    minObjects = 0,
    maxObjects = 0,
    #idCut  = "object.relIso03 < 0.2" # can give a cut
    #ptCuts = [20,10],                # can give a set of pt cuts on the objects
    )

#Muons
ttHMuonSkim = cfg.Analyzer(
    'ttHObjectSkimmer',
    skimmerName = 'ttHMuonSkimmer',
    objects = 'selectedMuons',
    minObjects = 0,
    maxObjects = 0,
    #idCut  = "object.relIso03 < 0.2" # can give a cut
    #ptCuts = [20,10],                # can give a set of pt cuts on the objects
    )

#Electrons
ttHElectronSkim = cfg.Analyzer(
    'ttHObjectSkimmer',
    skimmerName = 'ttHElectronSkimmer',
    objects = 'selectedElectrons',
    minObjects = 0,
    maxObjects = 0,
    #idCut  = "object.relIso03 < 0.2" # can give a cut
    #ptCuts = [20,10],                # can give a set of pt cuts on the objects
    )

#Isolated tracks
ttHIsoTrackSkim = cfg.Analyzer(
    'ttHIsoTrackSkimmer',
    objects = 'selectedIsoTrack',
    minObjects = 0,
    maxObjects = 0,
    allowedMuon = 0,
    allowedElectron = 0,
    #idCut  = "object.relIso03 < 0.2" # can give a cut
    #ptCuts = [20,10],                # can give a set of pt cuts on the objects
    )

#AlphaT Specific cuts

ttHAlphaTSkim = cfg.Analyzer(
            'ttHAlphaTSkimmer',
            forwardJetVeto = True,
            alphaTCuts = [(0.65, 200, 275),   #AlphaT cut in HT region
                          (0.60, 275, 325),   #(aT, HTlow, HThigh)
                          (0.55, 325, 99999)],#Any region not specified will be vetoed
            invertAlphaT = False, #Invert the alphaT requirement
            mhtDivMetCut = ('mhtJet50j','met',1.25), #MHT/MET cut
            )

ttHAlphaTControlSkim = cfg.Analyzer(
            'ttHAlphaTControlSkimmer',
            mtwCut = (-99999,99999),
            mllCut = (-99999,99999),
            lepDeltaRCut = 0,
            photonDeltaRCut = 0,
            )


# (FIXME Instead of everything here, have an alphaT core file (like susyCore) which
# does the default selection and cutflow. Then have the rest of this file below)

# Modify the cuts for the control regions
if cutFlow=='SingleMu':
    ttHLepAna.loose_muon_pt   = 30.
    ttHLepAna.loose_muon_eta  = 2.1
    ttHMuonSkim.minObjects  = 1
    ttHMuonSkim.maxObjects  = 1
    ttHIsoTrackAna.leadMuonRemove  = True 
    ttHIsoTrackSkim.allowedMuon  = 1 #
    ttHAlphaTSkim.alphaTCuts = [(0.0, 200,99999 )]   #Turn off AlphaT cut 
    ttHAlphaTControlSkim.mtwCut = (30,125)
    ttHAlphaTControlSkim.lepDeltaRCut = 0.5

elif cutFlow=='DoubleMu':
    ttHLepAna.loose_muon_pt   = 30.
    ttHLepAna.loose_muon_eta  = 2.1
    ttHMuonSkim.minObjects  = 2
    ttHMuonSkim.maxObjects  = 2
    ttHIsoTrackAna.leadTwoMuonRemove  = True 
    ttHIsoTrackSkim.allowedMuon  = 2 #
    ttHAlphaTSkim.alphaTCuts = [(0.0, 200,99999 )]   #Turn off AlphaT cut
    ttHAlphaTControlSkim.mllCut = (66.2,116.2)
    ttHAlphaTControlSkim.lepDeltaRCut = 0.5

elif cutFlow=='SinglePhoton':
    ttHPhotonSkim.minObjects  = 1
    ttHPhotonSkim.maxObjects  = 9999
    ttHPhotonSkim.idCut = "abs(object.eta()) < 1.45" #uses the object skimmer
    ttHPhotonSkim.ptCuts = [165]
    ttHAlphaTControlSkim.photonDeltaRCut = 0.5

elif cutFlow=='SingleEle':
    ttHElectronSkim.minObjects  = 1
    ttHElectronSkim.maxObjects  = 1
    ttHIsoTrackSkim.allowedElectron  = 1 #

elif cutFlow=='DoubleEle':
    ttHElectronSkim.minObjects  = 2
    ttHElectronSkim.maxObjects  = 2
    ttHIsoTrackSkim.allowedElectron  = 2 #

elif cutFlow=='MultiJetEnriched':
    ttHAlphaTSkim.invertAlphaT = True

elif cutFlow=='Test':
    ttHMuonSkim.maxObjects     = 99
    ttHMuonSkim.minObjects     = 0
    ttHElectronSkim.maxObjects     = 99
    ttHElectronSkim.minObjects     = 0
    ttHAlphaTSkim.invertAlphaT = True
    ttHPhotonSkim.minPhotons  = 0
    ttHPhotonSkim.maxPhotons  = 9999
    ttHPhotonSkim.ptCuts = [25]
    ttHIsoTrackSkim.minObjects  = 0 # FIXME Muons count as isolated tracks
    ttHIsoTrackSkim.maxObjects  = 9999 #

##------------------------------------------
##  PRODUCER
##------------------------------------------

from CMGTools.TTHAnalysis.samples.samples_8TeV_v517 import triggers_RA1_Bulk, triggers_RA1_Prompt, triggers_RA1_Parked, triggers_RA1_Single_Mu, triggers_RA1_Photon, triggers_RA1_Muon

# Tree Producer
treeProducer = cfg.Analyzer(
        'treeProducerSusyAlphaT',
        vectorTree = True,
        PDFWeights = PDFWeights,
        triggerBits = {
            'Bulk'     : triggers_RA1_Bulk,
            'Prompt'   : triggers_RA1_Prompt,
            'Parked'   : triggers_RA1_Parked,
            'SingleMu' : triggers_RA1_Single_Mu,
            'Photon'   : triggers_RA1_Photon,
            'Muon'     : triggers_RA1_Muon,
            }
        )

#-------- SAMPLES AND TRIGGERS -----------
from CMGTools.TTHAnalysis.samples.samples_13TeV_CSA14 import *

# CSA13 PU20bx25 samples: DYJetsM50_PU20bx25, DYJetsM50pythia6_PU20bx25, DYJetsM50_HT200to400_PU20bx25, DYJetsM50_HT400to600_PU20bx25, DYJetsM50_HT600toInf_PU20bx25, DYJetsMuMuM50_PtZ180_PU20bx25, DYJetsMuMuM6pythia8_PU20bx25, DYJetsMuMuM15pythia8_PU20bx25, DYJetsMuMuM50pythia8_PU20bx25, DYJetsEEpythia8_PU20bx25, DYJetsMuMupythia8_PU20bx25, EWKWmin_PU20bx25, EWKWplus_PU20bx25, EWKZjj_PU20bx25, EleGun_PU20bx25, GGHTauTau_PU20bx25, GGHZZ4L_PU20bx25, GJet_PU20bx25, JPsiPt20_PU20bx25, JPsiPt7_PU20bx25, MinBias_PU20bx25, MuMinGunPt100_PU20bx25, MuMinGunPt10_PU20bx25, MuPlusGunPt100_PU20bx25, MuPlusGunPt10_PU20bx25, NeutrinoGun_PU20bx25, QCDEM_20to30_PU20bx25, QCDEM_30to80_PU20bx25, QCDEM_80to170_PU20bx25, QCDMu_20to30_PU20bx25, QCDMu_30to50_PU20bx25, QCDMu_50to80_PU20bx25, QCDMu_80to120_PU20bx25, QCDMu_pythia6_120to170_PU20bx25, QCDMu_pythia6_20to30_PU20bx25, QCDMu_pythia6_30to50_PU20bx25, QCDMu_pythia6_50to80_PU20bx25, QCDMu_pythia6_80to120_PU20bx25, T1tttt_PU20bx25, TTHBB_PU20bx25, TTHGG_PU20bx25, TTHTauTau_PU20bx25, TTHWW_PU20bx25, TTHZZ4L_PU20bx25, TTJets_PU20bx25, TTJets_PUS14, TTpythia8_PU20bx25, VBFHBB_PU20bx25, VBFHGG_PU20bx25, VBFHWWSemi_PU20bx25, VBFHWW_PU20bx25, VBFHZG_PU20bx25, VBFHZZ4L_PU20bx25, VHMuMu_PU20bx25, VHTauTau_PU20bx25, VHWWInc_PU20bx25, VHWWLep_PU20bx25, VHZZ4L_PU20bx25, WENupyhia8_PU20bx25, WJets_PU20bx25, WminTau_PU20bx25, WplusMu_PU20bx25, WplusTau_PU20bx25, ZHBBInv_PU20bx25, ZHBBLL_PU20bx25, ZHLLInv_PU20bx25



# Selected samples as defined on the AlphaT twiki
WJetsToLNu   = [ WJetsToLNu_HT100to200_PU_S14_POSTLS170, WJetsToLNu_HT200to400_PU_S14_POSTLS170, WJetsToLNu_HT400to600_PU_S14_POSTLS170, WJetsToLNu_HT600toInf_PU_S14_POSTLS170]

# Currently not defined in the samples file could be added from here: https://cmsweb.cern.ch/das/request?view=list&limit=100&instance=prod%2Fglobal&input=dataset%3D%2F*DYJetsToLL*13TeV*%2F*PU20bx25*%2F*AODSIM
#DYJetsToLL  = []
# Currently not defined in the samples file could be added from here: https://cmsweb.cern.ch/das/request?view=list&limit=100&instance=prod%2Fglobal&input=dataset%3D%2F*ZJetsToNuNu*13TeV*%2F*PU20bx25*%2F*AODSIM
#ZJetsToNuNu = []
# https://cmsweb.cern.ch/das/request?view=list&limit=100&instance=prod%2Fglobal&input=dataset%3D%2F*GJets*13TeV*%2F*PU20bx25*%2F*AODSIM
#GJets       = []

# NOT INCLUDING: /TTJets_MSDecaysCKM_central_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM
TTbar        = [ TTpythia8_PU20bx25 ]
# https://cmsweb.cern.ch/das/request?view=list&limit=100&instance=prod%2Fglobal&input=dataset%3D%2FTToBLNu*13TeV*%2FSpring*PU20bx25*%2F*AODSIM
#TToBLNu     = []
# https://cmsweb.cern.ch/das/request?view=list&limit=100&instance=prod%2Fglobal&input=dataset%3D%2FSMS-T1qqqq*13TeV*%2FSpring*PU20bx25*%2F*AODSIM
#T1qqqq       = []
# https://cmsweb.cern.ch/das/request?view=list&limit=100&instance=prod%2Fglobal&input=dataset%3D%2FSMS-T1bbbb*13TeV*%2FSpring*PU20bx25*%2F*AODSIM
#T1bbbb       = []
T1tttt       = [ T1tttt_PU20bx25 ]


selectedComponents = [ SingleMu, DoubleElectron, TTHToWW_PUS14, DYJetsM50_PU20bx25, TTJets_PUS14 ]
selectedComponents = []
selectedComponents.extend( WJetsToLNu )
selectedComponents.extend( TTbar )




#-------- SEQUENCE

sequence = cfg.Sequence(susyCoreSequence + [
                        ttHPhotonSkim,
                        ttHMuonSkim,
                        ttHElectronSkim,
                        ttHIsoTrackAna,
                        ttHIsoTrackSkim,
                        ttHAlphaTAna,
                        ttHAlphaTControlAna,
                        ttHAlphaTSkim,
                        ttHAlphaTControlSkim,
                        treeProducer,
                        ])


#-------- HOW TO RUN
test = 1

# Test a single component, using a single thread.
#--------------------------------------------------
if test==1:
    comp               = T1tttt_PU20bx25
    if cutFlow == 'Test':
        comp = VBFHGG_PU20bx25 
    if cutFlow == 'SinglePhoton':
        comp = VBFHGG_PU20bx25 
    #comp.files = ['/afs/cern.ch/work/p/pandolf/CMSSW_7_0_6_patch1_2/src/CMGTools/TTHAnalysis/cfg/pickevents.root']
    comp.files         = comp.files[:2]
    
    selectedComponents = [comp]
    comp.splitFactor   = 1
#--------------------------------------------------

# Test all components (1 thread per component).
#--------------------------------------------------
elif test==2:
    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files       = comp.files[:1]
#--------------------------------------------------

# Run on local files
#--------------------------------------------------
elif test==4:
    comp = TTJets_PU20bx25

#    comp.name = 'TTJets'
    #    comp.files = [ '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/063013AD-9907-E411-8135-0026189438BD.root' ]

    comp.files = [ '/afs/cern.ch/user/m/mbaber/WORK/public/CSA14Samples/TT_Tune4C_13TeV-pythia8_PU20bx25.root' ]

    selectedComponents = [comp]
    comp.splitFactor = 1
#--------------------------------------------------


config = cfg.Config( components = selectedComponents,
                     sequence = sequence )

printComps(config.components, True)
        
