#ifndef CD_KFTrajectoryFitter_H_
#define CD_KFTrajectoryFitter_H_

/** \class KFTrajectoryFitter
 *  A Standard Kalman fit. Ported from ORCA
 *
 *  $Date: 2011/01/06 17:04:16 $
 *  $Revision: 1.13 $
 *  \author todorov, cerati
 */

#include "TrackingTools/GeomPropagators/interface/Propagator.h"
#include "TrackingTools/TrajectoryState/interface/TrajectoryStateOnSurface.h"
#include "TrackingTools/TrajectoryState/interface/FreeTrajectoryState.h"
#include "TrackingTools/PatternTools/interface/TrajectoryStateUpdator.h"
#include "TrackingTools/PatternTools/interface/Trajectory.h"
#include "TrackingTools/TrackFitters/interface/TrajectoryFitter.h"
#include "TrackingTools/PatternTools/interface/TrajectoryMeasurement.h"
#include "TrackingTools/PatternTools/interface/MeasurementEstimator.h"
#include "TrackingTools/DetLayers/interface/DetLayerGeometry.h"

class KFTrajectoryFitter : public TrajectoryFitter {

private:

  typedef TrajectoryStateOnSurface TSOS;
  typedef FreeTrajectoryState FTS;
  typedef TrajectoryMeasurement TM;

public:


  // backward compatible (too many places it uses as such...)
  KFTrajectoryFitter(const Propagator& aPropagator,
		     const TrajectoryStateUpdator& aUpdator,
		     const MeasurementEstimator& aEstimator,
		     int minHits = 3,
		     const DetLayerGeometry* detLayerGeometry=0) :
    thePropagator(aPropagator.clone()),
    theUpdator(aUpdator.clone()),
    theEstimator(aEstimator.clone()),
    theGeometry(detLayerGeometry),
    minHits_(minHits),
    owner(true){ 
    if(!theGeometry) theGeometry = &dummyGeometry;
    // FIXME. Why this first constructor is needed? who is using it? Can it be removed?
    // it is uses in many many places
    }
  

  KFTrajectoryFitter(const Propagator* aPropagator,
		     const TrajectoryStateUpdator* aUpdator,
		     const MeasurementEstimator* aEstimator,
		     int minHits = 3,
		     const DetLayerGeometry* detLayerGeometry=0) : 
    thePropagator(aPropagator),
    theUpdator(aUpdator),
    theEstimator(aEstimator),
    theGeometry(detLayerGeometry),
    minHits_(minHits),
    owner(false){
      if(!theGeometry) theGeometry = &dummyGeometry;
    }

  ~KFTrajectoryFitter(){
    if (owner) {
      delete thePropagator;
      delete theUpdator;
      delete theEstimator;
    }
  }
  
  virtual std::vector<Trajectory> fit(const Trajectory& aTraj) const;
  virtual std::vector<Trajectory> fit(const TrajectorySeed& aSeed,
				      const RecHitContainer& hits) const;

  virtual std::vector<Trajectory> fit(const TrajectorySeed& aSeed,
				      const RecHitContainer& hits, 
				      const TSOS& firstPredTsos) const;

  const Propagator* propagator() const {return thePropagator;}
  const TrajectoryStateUpdator* updator() const {return theUpdator;}
  const MeasurementEstimator* estimator() const {return theEstimator;}
  
  virtual KFTrajectoryFitter* clone() const
  {
    return owner ? 
      new KFTrajectoryFitter(*thePropagator,*theUpdator,*theEstimator,minHits_,theGeometry) :
      new KFTrajectoryFitter(thePropagator,theUpdator,theEstimator,minHits_,theGeometry);
  }
  
private:
  KFTrajectoryFitter(KFTrajectoryFitter const&);
		     

  static const DetLayerGeometry dummyGeometry;
  const Propagator* thePropagator;
  const TrajectoryStateUpdator* theUpdator;
  const MeasurementEstimator* theEstimator;
  const DetLayerGeometry* theGeometry;
  int minHits_;
  bool owner;
};

#endif //CD_KFTrajectoryFitter_H_
