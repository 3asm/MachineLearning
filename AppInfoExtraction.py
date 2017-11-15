from Characteristics import Characteristics
import pandas as pd
import os
import numpy

class AppInfoExtraction:
    apps = []
    malware_index = []
    c = Characteristics()  # Create the structure for characteristics

    def read_list_app(self, appDir, malwareList):

        malware = pd.read_csv(malwareList, sep=',')                         #inspect the .csv file understanding which file is effectively a malware
        for filename in os.listdir(appDir):                                 #scanning the dataset
            app = []
            #feature1=[]
            #feature2=[]
            with open(appDir + filename) as f:                              #inpecting each file within the dataset
                if (malware['sha256'].str.contains(filename).any()):        #It's a MALWARE!!!
                    self.malware_index.append(1)
                else:
                    self.malware_index.append(0)  #Good App

                for line in f.read().splitlines():
                    arguments = line.split("::")
                    if (len(line)>0):
                         app.append(arguments[1])


                self.apps.append(app)

