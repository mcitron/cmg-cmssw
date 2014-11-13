from CMGTools.TTHAnalysis.samples.getFiles import getFiles
from CMGTools.TTHAnalysis.samples.getMyFiles import getMyFiles
import CMGTools.RootTools.fwlite.Config as cfg
import os

from CMGTools.TTHAnalysis.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

#AlphaT sample (see https://twiki.cern.ch/twiki/bin/viewauth/CMS/AlphaT#MC_samples_for_CSA14_exercise)

#PU20bx25
#Component for WJetsToLNu
WJetsToLNu_HT100to200_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("WJetsToLNu_HT100to200_PU_S14_POSTLS170", "/WJetsToLNu_HT-100to200_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_WJetsToLNu_HT-100to200_Tune4C_13TeV-madgraph-tauola_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
WJetsToLNu_HT200to400_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("WJetsToLNu_HT200to400_PU_S14_POSTLS170", "/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
WJetsToLNu_HT400to600_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("WJetsToLNu_HT400to600_PU_S14_POSTLS170", "/WJetsToLNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_WJetsToLNu_HT-400to600_Tune4C_13TeV-madgraph-tauola_Spring14dr_PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
WJetsToLNu_HT600toInf_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("WJetsToLNu_HT600toInf_PU_S14_POSTLS170", "/WJetsToLNu_HT-600toInf_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_WJetsToLNu_HT-600toInf_Tune4C_13TeV-madgraph-tauola_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
WJetsToLNu = [
WJetsToLNu_HT100to200_PU_S14_POSTLS170,
WJetsToLNu_HT200to400_PU_S14_POSTLS170,
WJetsToLNu_HT400to600_PU_S14_POSTLS170,
WJetsToLNu_HT600toInf_PU_S14_POSTLS170,
]

#Component for DYJets
DYJetsToLL_PU20bx25 = kreator.makeMCComponent("DYJetsToLL_PU20bx25","/DYJetsToLL_M-50_13TeV-pythia6/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM", "CMS" , "*.root")
DYJetsToLL = [
DYJetsToLL_PU20bx25
]

#Component for ZJetsToNuNu
ZJetsToNuNu_HT100to200_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("ZJetsToNuNu_HT100to200_PU_S14_POSTLS170", "/ZJetsToNuNu_HT-100to200_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_ZJetsToNuNu_HT-100to200_Tune4C_13TeV-madgraph-tauola_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
ZJetsToNuNu_HT200to400_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("ZJetsToNuNu_HT200to400_PU_S14_POSTLS170", "/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
ZJetsToNuNu_HT400to600_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("ZJetsToNuNu_HT400to600_PU_S14_POSTLS170", "/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
ZJetsToNuNu_HT600toInf_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("ZJetsToNuNu_HT600toInf_PU_S14_POSTLS170", "/ZJetsToNuNu_HT-600toInf_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_ZJetsToNuNu_HT-600toInf_Tune4C_13TeV-madgraph-tauola_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
ZJetsToNuNu = [
ZJetsToNuNu_HT100to200_PU_S14_POSTLS170,
ZJetsToNuNu_HT200to400_PU_S14_POSTLS170,
ZJetsToNuNu_HT400to600_PU_S14_POSTLS170,
ZJetsToNuNu_HT600toInf_PU_S14_POSTLS170,
]

#Component for GJets
GJets_HT100to200_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("GJets_HT100to200_PU_S14_POSTLS170", "/GJets_HT-100to200_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_GJets_HT-100to200_Tune4C_13TeV-madgraph-tauola_Spring14dr_PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
GJets_HT200to400_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("GJets_HT200to400_PU_S14_POSTLS170", "/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
GJets_HT400to600_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("GJets_HT400to600_PU_S14_POSTLS170", "/GJets_HT-400to600_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_GJets_HT-400to600_Tune4C_13TeV-madgraph-tauola_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
GJets_HT600toInf_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("GJets_HT600toInf_PU_S14_POSTLS170", "/GJets_HT-600toInf_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_GJets_HT-600toInf_Tune4C_13TeV-madgraph-tauola_Spring14dr-PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
GJets = [
GJets_HT100to200_PU_S14_POSTLS170,
GJets_HT200to400_PU_S14_POSTLS170,
GJets_HT400to600_PU_S14_POSTLS170,
GJets_HT600toInf_PU_S14_POSTLS170,
]

#Components for TTbar
TTbar_PU20bx25 = kreator.makeMCComponent("TTbar_PU20bx25","/TT_Tune4C_13TeV-pythia8-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
TTbar =[
TTbar_PU20bx25
]

#Components for SUSY samples
SMS_T1bbbb_2J_mGl1000_mLSP900_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("SMS_T1bbbb_2J_mGl1000_mLSP900_PU_S14_POSTLS170", "/SMS-T1bbbb_2J_mGl-1000_mLSP-900_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_SMS-T1bbbb_2J_mGl-1000_mLSP-900_Tune4C_13TeV-madgraph-tauola_PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
SMS_T1bbbb_2J_mGl1500_mLSP100_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("SMS_T1bbbb_2J_mGl1500_mLSP100_PU_S14_POSTLS170", "/SMS-T1bbbb_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_SMS-T1bbbb_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola_PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
SMS_T1qqqq_2J_mGl1000_mLSP800_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("SMS_T1qqqq_2J_mGl1000_mLSP800_PU_S14_POSTLS170", "/SMS-T1qqqq_2J_mGl-1000_mLSP-800_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_SMS-T1qqqq_2J_mGl-1000_mLSP-800_Tune4C_13TeV-madgraph-tauola_PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
SMS_T1qqqq_2J_mGl1400_mLSP100_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("SMS_T1qqqq_2J_mGl1400_mLSP100_PU_S14_POSTLS170", "/SMS-T1qqqq_2J_mGl-1400_mLSP-100_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_SMS-T1qqqq_2J_mGl-1400_mLSP-100_Tune4C_13TeV-madgraph-tauola_PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
SMS_T1tttt_2J_mGl1200_mLSP800_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("SMS_T1tttt_2J_mGl1200_mLSP800_PU_S14_POSTLS170", "/SMS-T1tttt_2J_mGl-1200_mLSP-800_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_SMS-T1tttt_2J_mGl-1200_mLSP-800_Tune4C_13TeV-madgraph-tauola_PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")
SMS_T1tttt_2J_mGl1500_mLSP100_PU_S14_POSTLS170 = kreator.makeMyPrivateMCComponent("SMS_T1tttt_2J_mGl1500_mLSP100_PU_S14_POSTLS170", "/SMS-T1tttt_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/phys_susy-miniAODforSusy_SMS-T1tttt_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola_PU_S14_POSTLS170-af38aa319b7b7c91a6797b31c3be19b7/USER", "PRIVATE", ".*root", "phys03")

SusyPrivateSamples = [
    SMS_T1bbbb_2J_mGl1000_mLSP900_PU_S14_POSTLS170,
    SMS_T1bbbb_2J_mGl1500_mLSP100_PU_S14_POSTLS170,
    SMS_T1qqqq_2J_mGl1000_mLSP800_PU_S14_POSTLS170,
    SMS_T1qqqq_2J_mGl1400_mLSP100_PU_S14_POSTLS170,
    SMS_T1tttt_2J_mGl1200_mLSP800_PU_S14_POSTLS170,
    SMS_T1tttt_2J_mGl1500_mLSP100_PU_S14_POSTLS170,
    ]

#Combine different samples for running, modify to configure which sample you want to use
mcSamples = WJetsToLNu+DYJetsToLL+ZJetsToNuNu+GJets+TTbar+SusyPrivateSamples

dataDir = os.environ['CMSSW_BASE']+"/src/CMGTools/TTHAnalysis/data"

from CMGTools.TTHAnalysis.setup.Efficiencies import *

#Define splitting
for comp in mcSamples:
    comp.isMC = True
    comp.isData = False
    comp.splitFactor = 100 #  if comp.name in [ "WJets", "DY3JetsM50", "DY4JetsM50","W1Jets","W2Jets","W3Jets","W4Jets","TTJetsHad" ] else 100
    comp.puFileMC=dataDir+"/puProfile_Summer12_53X.root"
    comp.puFileData=dataDir+"/puProfile_Data12.root"
    comp.efficiency = eff2012




# samples below don't work now as some are not at Tier-2 CERN, need fix later
# WJetsToLNu_PU20bx25 = kreator.makeMCComponent("WJetsToLNu_PU20bx25","/WJetsToLNu_13TeV-madgraph-pythia8-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM", "CMS" , "*.root")
# # "/DYJetsToLL_M-50_13TeV-pythia6/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM"
# # "/DYJetsToLL_M-50_13TeV-madgraph-pythia8-tauola_v2/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM"
# # "/DYJetsToLL_M-50_13TeV-madgraph-pythia8/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM"
# ZJetsToNuNu_HT100to200_PU20bx25 = kreator.makeMCComponent("ZJetsToNuNu_HT100to200_PU20bx25","/ZJetsToNuNu_HT-100to200_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
# ZJetsToNuNu_HT200to400_PU20bx25 = kreator.makeMCComponent("ZJetsToNuNu_HT200to400_PU20bx25","/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
# ZJetsToNuNu_HT400to600_PU20bx25 = kreator.makeMCComponent("ZJetsToNuNu_HT400to600_PU20bx25","/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
# ZJetsToNuNu_HT600toInf_PU20bx25 = kreator.makeMCComponent("ZJetsToNuNu_HT600toInf_PU20bx25","/ZJetsToNuNu_HT-600toInf_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
# GJets_HT100to200_PU20bx25 = kreator.makeMCComponent("GJets_HT100to200_PU20bx25","/GJets_HT-100to200_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
# GJets_HT200to400_PU20bx25 = kreator.makeMCComponent("GJets_HT200to400_PU20bx25","/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
# GJets_HT400to600_PU20bx25 = kreator.makeMCComponent("GJets_HT400to600_PU20bx25","/GJets_HT-400to600_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
# GJets_HT600toInf_PU20bx25 = kreator.makeMCComponent("GJets_HT600toInf_PU20bx25","/GJets_HT-600toInf_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
# T1bbbb_mGl1000mLSP900_PU20bx25 = kreator.makeMCComponent("T1bbbb_mGl1000mLSP900_PU20bx25","/SMS-T1bbbb_2J_mGl-1000_mLSP-900_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM","CMS","*.root")
# # "/SMS-T1bbbb_2J_mGl-1000_mLSP-900_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM"
# # "/SMS-T1bbbb_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM"
# # "/SMS-T1bbbb_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v3/MINIAODSIM"
# T1tttt_mGl1200mLSP800_PU20bx25 = kreator.makeMCComponent("T1tttt_mGl1200mLSP800_PU20bx25","/SMS-T1tttt_2J_mGl-1200_mLSP-800_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM","CMS","*.root")
# # "/SMS-T1tttt_2J_mGl-1200_mLSP-800_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM"
# # "/SMS-T1tttt_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM"
# # "/SMS-T1tttt_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM"
# T1qqqq_mGl1000mLSP800_PU20bx25 = kreator.makeMCComponent("SMS-T1qqqq_2J_mGl-1000_mLSP-800_Tune4C_13TeV-madgraph-tauolaLSP800_PU20bx25","/SMS-T1qqqq_2J_mGl-1000_mLSP-800_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM","CMS","*root")
# # "/SMS-T1qqqq_2J_mGl-1000_mLSP-800_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM"
# # "/SMS-T1qqqq_2J_mGl-1400_mLSP-100_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM"
# # "/SMS-T1qqqq_2J_mGl-1400_mLSP-100_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM"
# TToBLNu_schannelEMu_PU20bx25 = kreator.makeMCComponent("TToBLNu_schannelEMu_PU20bx25","/TToBLNu_s-channel-EMu_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
# TToBLNu_tchannelEMu_PU20bx25 = kreator.makeMCComponent("TToBLNu_tchannelEMu_PU20bx25","/TToBLNu_t-channel-EMu_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
# TToBLNu_tWchannelDREMu_PU20bx25 = kreator.makeMCComponent("TToBLNu_tWchannelDREMu_PU20bx25","/TToBLNu_tW-channel-DR-EMu_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM","CMS","*.root")

# samples below don't work now as some are not at Tier-2 CERN, need fix later
# WJetsToLNu_PU20bx25,
# DYJetsToLL_PU20bx25,
# ZJetsToNuNu_HT100to200_PU20bx25, 
# ZJetsToNuNu_HT200to400_PU20bx25, 
# ZJetsToNuNu_HT400to600_PU20bx25, 
# ZJetsToNuNu_HT600toInf_PU20bx25, 
# GJets_HT100to200_PU20bx25, 
# GJets_HT200to400_PU20bx25, 
# GJets_HT400to600_PU20bx25, 
# GJets_HT600toInf_PU20bx25, 
# TToBLNu_schannelEMu_PU20bx25,
# TToBLNu_tchannelEMu_PU20bx25,
# TToBLNu_tWchannelDREMu_PU20bx25, 
# T1qqqq_mGl1000mLSP800_PU20bx25,
# T1bbbb_mGl1000mLSP900_PU20bx25,
# T1tttt_mGl1200mLSP800_PU20bx25,
