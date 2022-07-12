# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 14:06:16 2022

@author: Mathis
"""

import pyCGM2; LOGGER = pyCGM2.LOGGER

try:
    from pyCGM2 import btk
except:
    LOGGER.logger.info("[pyCGM2] pyCGM2-embedded btk not imported")
    try:
        import btk
    except:
        LOGGER.logger.error("[pyCGM2] btk not found on your system. install it for working with the API")

from pyCGM2.Tools import  btkTools
from pyCGM2.Signal import detect_peaks
from pyCGM2.Processing.ProgressionFrame import progressionFrameFilters
from pyCGM2.Processing.ProgressionFrame import progressionFrameProcedures
import newProgressionFrameProcedures
import newProgressionFrameFilter

# --- abstract procedure
class EventProcedure(object):
    def __init__(self):
        pass


#-------- EVENT PROCEDURES  ----------


class ZeniProcedure(EventProcedure):
    """
        Gait Event detection from Zeni et al, 2008
    """

    def __init__(self):
        super(ZeniProcedure, self).__init__()
        self.description = "Zeni (2008)"
        self.footStrikeOffset = 0
        self.footOffOffset = 0

    def setFootStrikeOffset(self,value):
        """set a systematic offset to each foot strike event

        Args:
            value (int): frame offset
        """

        self.footStrikeOffset = value

    def setFootOffOffset(self,value):
        """set a systematic offset to each foot off event

        Args:
            value (int): frame offset
        """
        self.footOffOffset = value

    def detect(self,acq,folder):
        """detect events

        Args:
            acq (Btk.Acquisition): a btk acquisition instance

        Return:
            int,int,int,int: frames indicating the left foot strike, the left foot off,
            the right foot strike and the right foot off respectively

        """


        ff=acq.GetFirstFrame()
        
        if btkTools.isPointsExist(acq,[f"{folder}:LBWT",f"{folder}:RBWT",f"{folder}:LHEE",f"{folder}:LTOE",f"{folder}:RHEE",f"{folder}:RTOE"]):
        
            pfp = newProgressionFrameProcedures.PelvisProgressionFrameProcedure()
            pff = newProgressionFrameFilter.ProgressionFrameFilter(acq,pfp)
            pff.compute(folder)
            progressionAxis = pff.outputs["progressionAxis"]
            globalFrame = pff.outputs["globalFrame"]
            forwardProgression = pff.outputs["forwardProgression"]


            longAxisIndex = 0 if progressionAxis == "X" else 1

            sacrum=(acq.GetPoint(f"{folder}:LBWT").GetValues() + acq.GetPoint(f"{folder}:RBWT").GetValues()) / 2.0

            #Left
            heel_left = acq.GetPoint(f"{folder}:LHEE").GetValues()
            toe_left = acq.GetPoint(f"{folder}:LTOE").GetValues()

            diffHeel_left = heel_left-sacrum
            diffToe_left = toe_left-sacrum

            #Right
            heel_right = acq.GetPoint(f"{folder}:RHEE").GetValues()
            toe_right = acq.GetPoint(f"{folder}:RTOE").GetValues()

            diffHeel_right = heel_right-sacrum
            diffToe_right = toe_right-sacrum


            if  forwardProgression:
                indexes_fs_left = detect_peaks.detect_peaks(diffHeel_left[:,longAxisIndex])+ff
                indexes_fo_left = detect_peaks.detect_peaks(-diffToe_left[:,longAxisIndex])+ff
            else:
                indexes_fs_left = detect_peaks.detect_peaks(-diffHeel_left[:,longAxisIndex])+ff
                indexes_fo_left = detect_peaks.detect_peaks(diffToe_left[:,longAxisIndex])+ff

            if  forwardProgression:
                indexes_fs_right = detect_peaks.detect_peaks(diffHeel_right[:,longAxisIndex])+ff
                indexes_fo_right = detect_peaks.detect_peaks(-diffToe_right[:,longAxisIndex])+ff
            else:
                indexes_fs_right = detect_peaks.detect_peaks(-diffHeel_right[:,longAxisIndex])+ff
                indexes_fo_right = detect_peaks.detect_peaks(diffToe_right[:,longAxisIndex])+ff

            return indexes_fs_left+self.footStrikeOffset,indexes_fo_left+self.footOffOffset, indexes_fs_right+self.footStrikeOffset, indexes_fo_right+self.footOffOffset

        else:
            LOGGER.logger.error(f"[pyCGM2]: Zeni event detector impossible to run. Pelvic {folder}:LBWT, {folder}:RBWT or foot markers(HEE or TOE) are missing ")
            return 0