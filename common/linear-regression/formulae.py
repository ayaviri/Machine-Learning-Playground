# this is a growing library of the formulae i accumulate 
# in this way, each formula implementation is only done once

# tags: r, product-moment coefficient, bivariate correlation 
def pearsonCorrelationCoefficient(xValues, xMean, yValues, yMean):
    # will not validate means of both variables, but will validate length of both lists
    if len(xValues) == len(yValues):
        raise AttributeError("The two datasets are not of the same length")

    numeratorSum = 0
    # TODO: follow these two links to implement this formula
    # https://www.youtube.com/watch?v=GhrxgbQnEEU
    # https://www.google.com/search?q=pearson%27s+correlation+coefficient&oq=pearson%27s+&aqs=chrome.2.0i433i512j69i57j0i131i433i512j0i433i512j0i512l6.3340j0j7&sourceid=chrome&ie=UTF-8
    for index in range(len(xValues)):
        print('hello world')
    return 0