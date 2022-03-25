import sys
# in order to read from different parts of this repository
sys.path.insert(0, '../../common/reading-data')
from readCsv import readCsvFile

def run():
    trainingHeader, trainingData = readCsvFile('train.csv')
    testHeader, testData = readCsvFile('test.csv')
    print('hello world')

run()