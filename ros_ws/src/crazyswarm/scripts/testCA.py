#!/usr/bin/env python
#
# Testing collision avoidance
#############################

import numpy as np

from pycrazyswarm import *

if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs

    cf1 = allcfs.crazyfliesById[30]
    cf2 = allcfs.crazyfliesById[31]

    #cf1.setGroupMask(0b00000001)
    #cf2.setGroupMask(0b00000010)

    allcfs.takeoff(targetHeight=0.3, duration=2.0)
    timeHelper.sleep(2.5)

    z = 1.5
    TRIALS = 2
    TIMESCALE = 2.0
    for i in range(TRIALS):

        pos1 = np.array(cf1.initialPosition) + np.array([0.5, -1.0, 0.3])
        cf1.goTo(pos1, 0, 5.0*TIMESCALE)
        pos2 = np.array(cf2.initialPosition) + np.array([-0.5, 1.0, 0.3])
        cf2.goTo(pos2, 0, 5.0*TIMESCALE)
        timeHelper.sleep(5.0*TIMESCALE+0.5)

        pos1 = np.array(cf1.initialPosition) + np.array([0.5, 1.0, 0.3])
        cf1.goTo(pos1, 0, 5.0*TIMESCALE)
        pos2 = np.array(cf2.initialPosition) + np.array([-0.5, -1.0, 0.3])
        cf2.goTo(pos2, 0, 5.0*TIMESCALE)
        timeHelper.sleep(5.0*TIMESCALE+0.5)


    for cf in allcfs.crazyflies:
        pos = np.array(cf.initialPosition) + np.array([0, 0, 0.1])
        cf.goTo(pos, 0, 5.0)
    timeHelper.sleep(5.5)

    allcfs.land(targetHeight=0.05, duration=2.0)
    timeHelper.sleep(3.0)
