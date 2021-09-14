'''
For PBL 4 Project.
Created on: 07 Dec 2020
Author: Shaiful Nizam
File: ConfigReader.py
'''

from configparser import SafeConfigParser

class ConfigReader:
    def __init__(self):
        # initialize attributes
        self.configFilename = ""
        self.leftImgFilename = ""
        self.rightImgFilename = ""
        self.gamma = 0
        self.projectorDist = 0
        self.projetedImgWidth = 0
        self.imgWidth = 0
        self.blendingFactor = 0
        
    # This method will read the configuration file and initialize the local 
    # attributes' values.
    def read(self, configFilename):
        parser = SafeConfigParser()
        parser.read(configFilename)
        self.leftImgFilename = parser.get('img_src', 'left_img')
        self.rightImgFilename = parser.get('img_src','right_img')
        self.projectorDist = float(parser.get('measurements','projector_dist'))
        self.projetedImgWidth = float(parser.get('measurements','projected_img_width'))
        self.imgWidth = int(parser.get('constants','img_width'))
        self.gamma = float(parser.get('constants','gamma'))
        self.blendingFactor = float(parser.get('constants','blending_factor'))
        
    # Returns the left image filename
    def getLeftImgFilename(self):
        return self.leftImgFilename
        
    # Returns the right image filename
    def getRightImgFilename(self):
        return self.rightImgFilename
        
    # Returns the gamma value
    def getGamma(self):
        return self.gamma
    
    # Returns the distance between the projectors
    def getProjetorDist(self):
        return self.projectorDist
    
    # Returns the width of the projected image
    def getProjectedImgWidth(self):
        return self.projetedImgWidth
    
    # Returns the width of the image
    def getImgWidth(self):
        return self.imgWidth
    
    # Returns the value of the blending factor
    def getBlendingFactor(self):
        return self.blendingFactor
