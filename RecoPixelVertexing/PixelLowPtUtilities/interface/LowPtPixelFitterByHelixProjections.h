#ifndef LowPtPixelFitterByHelixProjections_H
#define LowPtPixelFitterByHelixProjections_H

#include "RecoPixelVertexing/PixelTrackFitting/interface/PixelFitter.h"
#include "DataFormats/TrackingRecHit/interface/TrackingRecHit.h"
#include "RecoTracker/TkTrackingRegions/interface/TrackingRegion.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include <vector>

class TransientTrackingRecHitBuilder;
class TrackerGeometry;
class MagneticField;

class LowPtPixelFitterByHelixProjections : public PixelFitter {
public:
  LowPtPixelFitterByHelixProjections(  const edm::ParameterSet& cfg);
  virtual ~LowPtPixelFitterByHelixProjections() {}
    virtual reco::Track* run(
      const edm::EventSetup& es,
      const std::vector<const TrackingRecHit *>& hits,
      const TrackingRegion& region) const;
private:
  int charge(const std::vector<GlobalPoint> & points) const;
  float cotTheta(const GlobalPoint& pinner, const GlobalPoint& pouter,
    float radius, float phi, float d0, float& zip) const;
  float phi(float xC, float yC, int charge) const;
  float pt(float curvature) const;
  float zip(float d0, float curv, 
    const GlobalPoint& pinner, const GlobalPoint& pouter) const;
  double errZip2(float apt, float eta) const;
  double errTip2(float apt, float eta) const;

private:
  edm::ParameterSet theConfig;

  mutable const TrackerGeometry * theTracker;
  mutable const MagneticField * theField;
  mutable const TransientTrackingRecHitBuilder * theTTRecHitBuilder;

};
#endif
