import csv

# returns a tuple of (header, data) from the given csv file
def readCsvFile(filePath):
    file = open(filePath)
    csvReader = csv.reader(file)
    # a 1-d list of variable names
    header = next(csvReader)
    # a 2-d list of points - each element in the outer list should have the same number of elements as the header
    data = []
    for row in csvReader:
        # validation of each data point is done based on the header
        # a malformed header will then cause issues upon the rest of the read
        if len(row) == len(header):
            data.append(row)
    return (header, data)
