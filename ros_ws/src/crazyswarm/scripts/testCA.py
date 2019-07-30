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

    cf1.prefix = "cf30"
    cf2.prefix = "cf31"

    # cf1.setParam('sitAw/CAActive', 1)
    # cf2.setParam('sitAw/CAActive', 1)
    # cf1.setParam('sitAw/SearchRadius', 3.0)
    # cf2.setParam('sitAw/SearchRadius', 3.0)
    # cf1.setParam('sitAw/SeparationRadius', 2.0)
    # cf2.setParam('sitAw/SeparationRadius', 2.0)
    # cf1.setParam('sitAw/TargetRadius', 0.1)
    # cf2.setParam('sitAw/TargetRadius', 0.1)
    # cf1.setParam('sitAw/RepGain', 10.0)
    # cf2.setParam('sitAw/RepGain', 10.0)
    # cf1.setParam('sitAw/MaxSpeed', 0.3)
    # cf2.setParam('sitAw/MaxSpeed', 0.3)
    # cf1.setParam('sitAw/Anisotropy', 0.5)
    # cf2.setParam('sitAw/Anisotropy', 0.5)
    allcfs.updateParams('flocking/SearchRadius', 3.0)
    allcfs.updateParams('flocking/SeparationRadius', 1.0)
    allcfs.updateParams('flocking/TargetRadius', 0.1)
    allcfs.updateParams('flocking/RepGain', 5.0)
    allcfs.updateParams('flocking/MaxSpeed', 0.3)
    allcfs.updateParams('flocking/Anisotropy', 0.5)
    allcfs.updateParams('flocking/Separate', 1)

    timeHelper.sleep(3.0)

    #cf1.setGroupMask(0b00000001)
    #cf2.setGroupMask(0b00000010)

    z = 0.25
    x_offset = 0.3
    y_offset = 1.0
    TRIALS = 2
    TIMESCALE = 2.0


    allcfs.takeoff(targetHeight=z, duration=2.0)
    for cf in allcfs.crazyflies:
        pos = np.array(cf.initialPosition) + np.array([0, 0, z])
        cf.goTo(pos, 0, 2.0)
    timeHelper.sleep(2.5)

    allcfs.updateParams('flocking/Active', 1)

    for i in range(TRIALS):

        pos1 = np.array(cf1.initialPosition) + np.array([x_offset, -y_offset, z])
        cf1.goTo(pos1, 0, 0.01*TIMESCALE)
        pos2 = np.array(cf2.initialPosition) + np.array([-x_offset, y_offset, z])
        cf2.goTo(pos2, 0, 0.01*TIMESCALE)
        timeHelper.sleep(5.0*TIMESCALE+0.5)

        pos1 = np.array(cf1.initialPosition) + np.array([x_offset, y_offset, z])
        cf1.goTo(pos1, 0, 0.01*TIMESCALE)
        pos2 = np.array(cf2.initialPosition) + np.array([-x_offset, -y_offset, z])
        cf2.goTo(pos2, 0, 0.01*TIMESCALE)
        timeHelper.sleep(5.0*TIMESCALE+0.5)

    for cf in allcfs.crazyflies:
        pos = np.array(cf.initialPosition) + np.array([0, 0, 0.1])
        cf.goTo(pos, 0, 2.0)
    timeHelper.sleep(2.5)

    cf1.setParam('sitAw/Break', 1)
    cf2.setParam('sitAw/Break', 1)

    timeHelper.sleep(3.0)

    cf1.setParam('sitAw/Break', 0)
    cf2.setParam('sitAw/Break', 0)
    allcfs.updateParams('flocking/Active', 0)

    for cf in allcfs.crazyflies:
        pos = np.array(cf.initialPosition) + np.array([0, 0, 0.1])
        cf.goTo(pos, 0, 5.0*TIMESCALE)
    timeHelper.sleep(5.5*TIMESCALE+0.5)

    allcfs.land(targetHeight=0.05, duration=2.0)
    timeHelper.sleep(2.5)
