#ifndef DigiSimLinks_DTDigiSimLink_h
#define DigiSimLinks_DTDigiSimLink_h

#include "boost/cstdint.hpp"
#include "SimDataFormats/EncodedEventId/interface/EncodedEventId.h"

class DTDigiSimLink {

 public:
  typedef uint32_t ChannelType;

  // Construct from the wire number and the digi number (this identifies 
  // uniquely multiple digis on the same wire), the TDC counts, the SimTrack Id and the EncodedEvent Id.
  explicit DTDigiSimLink(int wireNr, int digiNr, int nTDC, unsigned int trackId, EncodedEventId evId);

  // Construct from the wire number and the digi number (this identifies 
  // uniquely multiple digis on the same wire), the time (ns), the SimTrack Id and the EncodedEvent Id.
  // time is converted in TDC counts (1 TDC = 25./32. ns)
  explicit DTDigiSimLink(int wireNr, int digiNr, double tdrift, unsigned int trackId, EncodedEventId evId);

  // Default constructor.
  DTDigiSimLink();
  
  // The channel identifier and the digi number packed together
  ChannelType channel() const;
  
  // Return wire number
  int wire() const;

  // Identifies different digis within the same cell
  int number() const;

  // Get raw TDC count
  uint32_t countsTDC() const;

  // Get time in ns
  double time() const;

  // Return the SimTrack Id
  unsigned int SimTrackId()  const;

  // Return the Encoded Event Id
  EncodedEventId eventId()  const;

private:
  // The value of one TDC count in ns
  static const double reso;

  // Used to repack the channel number to an int
  struct ChannelPacking {
    uint16_t wi;
    uint16_t num;
  };
  
 private:
  uint16_t theWire;       // wire number
  uint16_t theDigiNumber; // digi number on the wire
  uint32_t theCounts;     // TDC count, up to 20 bits actually used
  uint32_t theSimTrackId; // identifier of the SimTrack that produced the digi
  EncodedEventId theEventId;
};

#include<iostream>
inline std::ostream & operator<<(std::ostream & o, const DTDigiSimLink& digisimlink) {
  return o << "wire:"<<digisimlink.wire()
	   << " digi:" << digisimlink.number()
	   << " time:" << digisimlink.time()
	   << " SimTrack:" << digisimlink.SimTrackId()
	   << " eventId:" << digisimlink.eventId().rawId();
}

#endif
