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

    cf1 = allcfs.crazyfliesById[27]
    cf2 = allcfs.crazyfliesById[29]
    cf3 = allcfs.crazyfliesById[30]
    cf4 = allcfs.crazyfliesById[31]

    cf1.prefix = "cf27"
    cf2.prefix = "cf29"
    cf3.prefix = "cf30"
    cf4.prefix = "cf31"

    # Params:
    z = 0.2

    allcfs.updateParams('sitAw/Break', 0)
    allcfs.updateParams('flocking/Xmin', -5.0)
    allcfs.updateParams('flocking/Xmax', 5.0)
    allcfs.updateParams('flocking/Ymin', -5.0)
    allcfs.updateParams('flocking/Ymax', 5.0)
    allcfs.updateParams('flocking/SearchRadius', 3.0)
    allcfs.updateParams('flocking/SeparationRadius', 1.5)
    allcfs.updateParams('flocking/TargetRadius', 0.3)
    allcfs.updateParams('flocking/RepGain', 0.75)
    allcfs.updateParams('flocking/MaxSpeed', 0.7)
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
    TRIALS = 2
    T_TRAJ = 3.0
    T_STEP = 8.0
    T_DELAY = 1.0

    ini1 = np.array(cf1.initialPosition) + np.array([0.0, 0.0, z])
    ini2 = np.array(cf2.initialPosition) + np.array([0.0, 0.0, z])
    ini3 = np.array(cf3.initialPosition) + np.array([0.0, 0.0, z])
    ini4 = np.array(cf4.initialPosition) + np.array([0.0, 0.0, z])
    pos1 = np.array(cf1.initialPosition) + np.array([0.5, -1.25, z])
    pos2 = np.array(cf2.initialPosition) + np.array([1.25, 0.5, z])
    pos3 = np.array(cf3.initialPosition) + np.array([-0.5, 1.25, z])
    pos4 = np.array(cf4.initialPosition) + np.array([-1.25, -0.5, z])

    for i in range(TRIALS):
        cf1.goTo(pos1, 0, T_TRAJ)
        timeHelper.sleep(T_DELAY)
        cf2.goTo(ini1, 0, T_TRAJ)
        timeHelper.sleep(T_DELAY)
        cf3.goTo(ini2, 0, T_TRAJ)
        timeHelper.sleep(T_DELAY)
        cf4.goTo(ini3, 0, T_TRAJ)
        timeHelper.sleep(T_STEP)

        cf1.goTo(pos2, 0, T_TRAJ)
        timeHelper.sleep(T_DELAY)
        cf2.goTo(ini4, 0, T_TRAJ)
        timeHelper.sleep(T_DELAY)
        cf3.goTo(ini1, 0, T_TRAJ)
        timeHelper.sleep(T_DELAY)
        cf4.goTo(ini2, 0, T_TRAJ)
        timeHelper.sleep(T_STEP)

        cf1.goTo(pos3, 0, T_TRAJ)
        timeHelper.sleep(T_DELAY)
        cf2.goTo(ini3, 0, T_TRAJ)
        timeHelper.sleep(T_DELAY)
        cf3.goTo(ini4, 0, T_TRAJ)
        timeHelper.sleep(T_DELAY)
        cf4.goTo(ini1, 0, T_TRAJ)
        timeHelper.sleep(T_STEP)

        cf1.goTo(pos4, 0, T_TRAJ)
        timeHelper.sleep(T_DELAY)
        cf2.goTo(ini2, 0, T_TRAJ)
        timeHelper.sleep(T_DELAY)
        cf3.goTo(ini3, 0, T_TRAJ)
        timeHelper.sleep(T_DELAY)
        cf4.goTo(ini4, 0, T_TRAJ)
        timeHelper.sleep(T_STEP)

    ###################
    # 4. End Flocking #
    ###################
    cf1.goTo(ini1, 0, T_TRAJ)
    cf2.goTo(ini2, 0, T_TRAJ)
    cf3.goTo(ini3, 0, T_TRAJ)
    cf4.goTo(ini4, 0, T_TRAJ)
    timeHelper.sleep(T_STEP)
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
