'''
For PBL 4 Project.
Created on: 7 Dec 2020
Author: Shaiful Nizam
File: pbl4_main_G21.py
'''

import cv2
from ConfigReader import ConfigReader
from ImageLoader import ImageLoader
from MaskGenerator import MaskGenerator
from ImageProcessor import ImageProcessor

if __name__ == '__main__':

    # Create ConfigReader object
    config = ConfigReader()
    
    config.read('config.ini')
    print("[config.ini]")
    print("Left img =", config.getLeftImgFilename())
    print("Right img =", config.getRightImgFilename())
    print("Distance between projector =", config.getProjetorDist())
    print("Projected img width =", config.getProjectedImgWidth())
    print("Img width =", config.getImgWidth())
    print("Gamma =", config.getGamma())
    
    # Create ImageLoader object
    imgLoader = ImageLoader(config)
    
    # Create MaskGenerator object
    maskGen = MaskGenerator(imgLoader, config)
    
    # Create ImageProcessor object
    imgProcessor = ImageProcessor()
    
    leftBlend = imgProcessor.blendMask(imgLoader.getLeftOverlapImage(), 
                                       maskGen.getLeftMask())
    leftBlend = imgProcessor.gammaCorrection(leftBlend, config.getGamma())
    
    rightBlend = imgProcessor.blendMask(imgLoader.getRightOverlapImage(), 
                                        maskGen.getRightMask())
    rightBlend = imgProcessor.gammaCorrection(rightBlend, config.getGamma())

    leftStitch = imgProcessor.stitchImage(imgProcessor.gammaCorrection(imgLoader.getLeftNonOverlapImage(), config.getGamma()), 
                                          leftBlend)
    
    rightStitch = imgProcessor.stitchImage(rightBlend, 
                                           imgProcessor.gammaCorrection(imgLoader.getRightNonOverlapImage(), config.getGamma()))

#     cv2.imshow("leftNonOverlapImage", imgLoader.getLeftNonOverlapImage())
#     cv2.imshow("rightNonOverlapImage", imgLoader.getRightNonOverlapImage())
#     cv2.imshow("leftOverlapImage", imgLoader.getLeftOverlapImage())
#     cv2.imshow("rightOverlapImage", imgLoader.getRightOverlapImage())
#     cv2.imshow("leftBlend", leftBlend)
#     cv2.imshow("rightBlend", rightBlend)
    cv2.imshow("leftStitch", leftStitch)
    cv2.imshow("rightStitch", rightStitch)    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite("left_stitch.jpg", leftStitch)
    cv2.imwrite("right_stitch.jpg", rightStitch)
    