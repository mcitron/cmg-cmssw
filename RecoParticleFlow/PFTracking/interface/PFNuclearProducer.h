#ifndef PFNuclearProducer_H
#define PFNuclearProducer_H

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"

class PFTrackTransformer;
class PFNuclearProducer : public edm::EDProducer {
public:
  
  ///Constructor
  explicit PFNuclearProducer(const edm::ParameterSet&);
  
  ///Destructor
  ~PFNuclearProducer();
  
private:
  virtual void beginRun(edm::Run&,const edm::EventSetup&) ;
  virtual void endRun() ;
  
  ///Produce the PFRecTrack collection
  virtual void produce(edm::Event&, const edm::EventSetup&);
  
  ///PFTrackTransformer
  PFTrackTransformer *pfTransformer_; 
  double likelihoodCut_;
  std::vector<edm::InputTag> nuclearContainers_;
};
#endif
