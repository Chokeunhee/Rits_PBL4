'''
For PBL 4 Project.
Created on: 07 Dec 2020
Author: Alina
File: MaskGenerator.py
'''

import cv2
import numpy as np

class MaskGenerator:
    # On initialization, the contructor will generate both the left mask 
    # and right mask
    def __init__(self, imgLoader, config):

        self.leftMask = np.linspace(1, 0, imgLoader.getOverlapWidth())
        self.leftMask = self.leftMask ** config.getBlendingFactor()

        self.leftMask = np.tile(np.transpose(self.leftMask), (imgLoader.getImageMinHeight(),1))
        self.leftMask = cv2.merge([self.leftMask, self.leftMask, self.leftMask])

        self.rightMask = np.linspace(0, 1, imgLoader.getOverlapWidth())
        self.rightMask = self.rightMask ** config.getBlendingFactor()
        
        self.rightMask = np.tile(np.transpose(self.rightMask), (imgLoader.getImageMinHeight(),1))
        self.rightMask = cv2.merge([self.rightMask, self.rightMask, self.rightMask])

    # Returns the left mask
    def getLeftMask(self):
        return self.leftMask
    
    # Returns the right mask
    def getRightMask(self):
        return self.rightMask
