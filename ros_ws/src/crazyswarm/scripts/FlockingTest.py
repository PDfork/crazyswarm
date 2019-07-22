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

    # Groups:
    # cf1.setGroupMask(0b00000001)
    # cf2.setGroupMask(0b00000010)

    # Params:
    z = 0.25

    allcfs.updateParams('sitAw/CAActive', 1)
    allcfs.updateParams('sitAw/Break', 1)
    allcfs.updateParams('flocking/SearchRadius', 3.0)
    allcfs.updateParams('flocking/SeparationRadius', 3.0)
    allcfs.updateParams('flocking/TargetRadius', 0.1)
    allcfs.updateParams('flocking/RepGain', 15.5)
    allcfs.updateParams('flocking/MaxSpeed', 0.3)
    allcfs.updateParams('flocking/Anisotropy', 0.5)
    allcfs.updateParams('flocking/Align', 1)
    allcfs.updateParams('flocking/Cohese', 1)
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

    ############
    # 3. Break #
    ############
    allcfs.updateParams('sitAw/Break', 1)

    #############
    # 4. Resume #
    #############
    allcfs.updateParams('sitAw/Break', 0)

    ####################
    # 5. Return & Land #
    ####################
    for cf in allcfs.crazyflies:
        pos = np.array(cf.initialPosition) + np.array([0, 0, 0.1])
        cf.goTo(pos, 0, 5.0)
    timeHelper.sleep(6.0)

    allcfs.land(targetHeight=0.05, duration=2.0)
    timeHelper.sleep(2.5)
