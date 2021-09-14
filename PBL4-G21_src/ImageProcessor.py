'''
For PBL 4 Project.
Created on: 03 Dec 2020
Author: Sako Mahito
File: ImageProcessor.py
'''

import cv2
import numpy as np

class ImageProcessor:
    # Return a blended image from the overlap image and the mask
    def blendMask(self, overlapImage, mask):

        # blend the overlap regions, clip and make into int
        blend = overlapImage * mask
        blend = np.clip((blend), 0, 255)
        blend = np.uint8(blend)
        
        return blend

    # Returns a merge image of the non-overlap image with the blended image
    def stitchImage(self, nonOverlapImage, blend):
        # concatenate the images for the stitched result
        return np.concatenate((nonOverlapImage, blend), axis=1)

    # Returns an image which have been applied with gamme correction
    def gammaCorrection(self, img, gamma):
        # Build gamma correction table
        invGamma = 1.0 / gamma
        gammaTable = np.array([((i / 255.0) ** invGamma) * 255
                for i in np.arange(0, 256)]).astype("uint8")
        
        img = cv2.LUT(img, gammaTable) #GAMMA CORRECTION
        return img
        