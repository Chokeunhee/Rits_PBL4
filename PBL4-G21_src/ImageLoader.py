'''
For PBL 4 Project.
Created on: 07 Dec 2020
Author: Shaiful Nizam
File: ImageLoader.py
'''

import cv2

class ImageLoader:
    # On initialization the contructor will split the the image into the working
    # components like the left and right non-overlap image, and the left and 
    # right overlap image.
    def __init__(self, configReader):
        self.leftImage = cv2.imread(configReader.getLeftImgFilename())
        self.rightImage = cv2.imread(configReader.getRightImgFilename())

        lh, lw, lc = self.leftImage.shape
        rh, rw, rc = self.rightImage.shape
        print("Left Width =", lw, " Left Height =", lh)
        print("Right Width =", rw, " Right Height =", rh)

        # get dimensions: height, width, channel
        heightLeftImg, widthLeftImg, channelLeftImg = self.leftImage.shape
        heightRightImg, widthRightImg, channelLeftImg = self.rightImage.shape

        # compute min height
        self.minHeight = min(heightLeftImg, heightRightImg)

        self.widthOverlap = configReader.getImgWidth() - int(
            configReader.getImgWidth() * configReader.getProjetorDist()/
            configReader.getProjectedImgWidth()) # width of overlap

        print("Overlap =", self.widthOverlap)
        # compute start x position of mask in each image
        startLeftMask = configReader.getImgWidth() - self.widthOverlap
        startRightMask = 0

        # crop left image into 2 parts vertically
        self.leftNonOverlapImage = self.leftImage[0:self.minHeight, 0:startLeftMask]
        self.leftOverlapImage = self.leftImage[0:self.minHeight, startLeftMask:configReader.getImgWidth()]

        # crop right image into 2 parts vetically
        self.rightOverlapImage = self.rightImage[0:self.minHeight, startRightMask:self.widthOverlap]
        self.rightNonOverlapImage = self.rightImage[0:self.minHeight, self.widthOverlap:configReader.getImgWidth()+1]

    # Returns the left image        
    def getLeftImage(self):
        return self.leftImage
    
    # Returns the right image
    def getRightImage(self):
        return self.rightImage
    
    # Returns the left non-overlap image
    def getLeftNonOverlapImage(self):
        return self.leftNonOverlapImage
    
    # Returns the right non-overlap image
    def getRightNonOverlapImage(self):
        return self.rightNonOverlapImage
    
    # Returns the left overlap image
    def getLeftOverlapImage(self):
        return self.leftOverlapImage
    
    # Returns the right overlap image
    def getRightOverlapImage(self):
        return self.rightOverlapImage
    
    # Returns the value of the overlap width
    def getOverlapWidth(self):
        return self.widthOverlap
    
    # Returns the value of the min height of the image
    def getImageMinHeight(self):
        return self.minHeight

