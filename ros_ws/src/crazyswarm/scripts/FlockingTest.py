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

    # Groups:
    # cf1.setGroupMask(0b00000001)
    # cf2.setGroupMask(0b00000010)

    # Params:
    z = 0.2

    allcfs.updateParams('sitAw/Break', 0)
    allcfs.updateParams('flocking/SearchRadius', 3.0)
    allcfs.updateParams('flocking/SeparationRadius', 1.5)
    allcfs.updateParams('flocking/TargetRadius', 0.15)
    allcfs.updateParams('flocking/RepGain', 1.0)
    allcfs.updateParams('flocking/MaxSpeed', 0.5)
    allcfs.updateParams('flocking/Anisotropy', 0.5)
    allcfs.updateParams('flocking/Align', 0)
    allcfs.updateParams('flocking/Cohese', 0)
    allcfs.updateParams('flocking/Separate', 1)
    timeHelper.sleep(3.0)

    ##############
    # 1. Takeoff #
    ##############
    allcfs.takeoff(targetHeight=z, duration=2.0)
    for cf in allcfs.crazyflies:
        pos = np.array(cf.initialPosition) + np.array([0, 0, z])
        cf.goTo(pos, 0, 2.0)
    timeHelper.sleep(2.5)

    #####################
    # 2. Start Flocking #
    #####################
    allcfs.updateParams('flocking/Active', 1)
    timeHelper.sleep(1.0)

    ########################
    # 3. Change Directions #
    ########################
    for cf in allcfs.crazyflies:
        pos =  np.array(cf.initialPosition) + np.array([0.0, -1.0, z])
        cf.goTo(pos, 0, 3.0)
    timeHelper.sleep(7.0)
    for cf in allcfs.crazyflies:
        pos =  np.array(cf.initialPosition) + np.array([1.0, -1.0, z])
        cf.goTo(pos, 0, 3.0)
    timeHelper.sleep(7.0)
    for cf in allcfs.crazyflies:
        pos =  np.array(cf.initialPosition) + np.array([1.0, 0.0, z])
        cf.goTo(pos, 0, 3.0)
    timeHelper.sleep(7.0)
    for cf in allcfs.crazyflies:
        pos =  np.array(cf.initialPosition) + np.array([0.0, 0.0, z])
        cf.goTo(pos, 0, 3.0)
    timeHelper.sleep(5.0)

    ###################
    # 4. End Flocking #
    ###################
    allcfs.updateParams('sitAw/Break', 1)
    timeHelper.sleep(1.0)
    allcfs.updateParams('flocking/Active', 0)
    timeHelper.sleep(1.0)
    allcfs.updateParams('sitAw/Break', 0)
    timeHelper.sleep(1.0)

    ####################
    # 5. Return & Land #
    ####################
    for cf in allcfs.crazyflies:
        pos = np.array(cf.initialPosition) + np.array([0, 0, 0.1])
        cf.goTo(pos, 0, 5.0)
    timeHelper.sleep(6.0)

    allcfs.land(targetHeight=0.05, duration=2.0)
    timeHelper.sleep(2.5)
