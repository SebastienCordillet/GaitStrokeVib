# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 14:54:03 2022

@author: Mathis
"""

from pyCGM2.Events import eventFilters
import newEventProcedure
from pyCGM2.Signal import signal_processing
# import main
import newEventFilters

def zeni(acqGait, folder:str, footStrikeOffset=0, footOffOffset=0, **kwargs):
    """kinematic-based event detector according Zeni et al(2008).

    This method need the presence of the markers "LBWT","RBWT","LHEE","LTOE","RHEE","RTOE"


    *Reference:*
    Zeni, J. A.; Richards, J. G.; Higginson, J. S. (2008) Two simple methods for determining gait events during treadmill and overground walking using kinematic data. In : Gait & posture, vol. 27, n° 4, p. 710–714. DOI: 10.1016/j.gaitpost.2007.07.007.

    Args:
        acqGait (btk.Acquisition): an acquisition instance.
        footStrikeOffset (int): systematic offset to add to all `footStrikeOffset` events. Default is 0.
        footOffOffset (int): systematic offset to add to all `footOffOffset` events. Default is 0.

    Keyword Arguments:
        fc_lowPass_marker (double) : cut-off frequency of the lowpass filter applied on markers
        order_lowPass_marker (int): order of the lowpass filter applied on markers

    Returns:
        acqGait ( btk.Acquisition): updated acquisition with detected events.
        state (bool): state of the detector


    """
    folder=folder[2:4]+folder[0:2]
    # folder="BJ"
    acqGait.ClearEvents()

    if "fc_lowPass_marker" in kwargs.keys() and kwargs["fc_lowPass_marker"] != 0:
        fc = kwargs["fc_lowPass_marker"]
        order = 4
        if "order_lowPass_marker" in kwargs.keys():
            order = kwargs["order_lowPass_marker"]
        signal_processing.markerFiltering(
            acqGait, [f"{folder}:LBWT", f"{folder}:RBWT", f"{folder}:LHEE", f"{folder}:LTOE", f"{folder}:RHEE", f"{folder}:RTOE"], order=order, fc=fc)

    # ----------------------EVENT DETECTOR-------------------------------
    evp = newEventProcedure.ZeniProcedure()
    evp.setFootStrikeOffset(footStrikeOffset)
    evp.setFootOffOffset(footOffOffset)

    # event filter
    evf = newEventFilters.EventFilter(evp, acqGait)
    evf.detect(folder)
    state = evf.getState()
    return acqGait, state