import csv
from enum import Enum

# an enum for the names of file from which data is read
class FileName(Enum):
    TRAIN = 'train.csv'
    TEST = 'test.csv'

class DataRead: 
    def __init__(self):
        self.trainingData = None
        self.testData = None
        self.trainingHeader = None

class DataRead:

    def __init__(self):
        self.trainingData = None
        self.testData = None
        self.trainingHeader = None
        self.testHeader = None

    def getTrainingData(self):
        self.__getDataHelper(self.trainingData, self.trainingHeader, FileName.TRAIN.value)
        return self.trainingData

    def getTestData(self):
        self.__getDataHelper(self.testData, self.testHeader, FileName.TEST.value)
        return self.testData

    def getTrainingHeader(self):
        self.__getHeaderHelper(self.trainingData, self.trainingHeader, FileName.TRAIN.value)
        return self.trainingHeader

    def getTestHeader(self):
        self.__getHeaderHelper(self.testData, self.testHeader, FileName.TEST.value)
        return self.testHeader

    # reads the ENTIRE csv file and populates both the header and the data fields of this instance for a particular data type (training/test) 
    def __getDataHelper(self, dataType, headerType, fileName):
        print(self.trainingHeader)
        print(self.trainingData)
        print(headerType)
        print(dataType)
        if dataType is None:
            print('populating rows in data helper')
            dataFile = open(fileName)
            csvReader = csv.reader(dataFile)
            headerType = next(csvReader)
            rows = []
            for row in csvReader:
                # this behavior is specific to the data we're working with, we're ensuring that the tuple has two values
                if len(row) == 2:
                    rows.append(row)
            dataType = rows

    def __getHeaderHelper(self, dataType, headerType, fileName):
        if headerType is None:
            print('populating header in header helper')
            dataFile = open(fileName)
            csvReader = csv.reader(dataFile)
            headerType = next(csvReader)
            if dataType is None:
                print('populating rows in header helper')
                rows = []
                for row in csvReader:
                    # again, this behavior is specific to the data we're working with, we're ensuring that the tuple has two values
                    if len(row) == 2:
                        rows.append(row)
                dataType = rows

# FIXME: arguments are passed by assignment, not by reference, meaning that this needs to be reworked. 