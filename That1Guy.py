def createbar(rangelen: int, duck: str): # generator function to create loading bar
    lastprint = ""
    toprint = ""
    for i in range(rangelen):
        currentpercent = math.ceil(len(duck) * (i / rangelen))
        if not lastprint == duck[:currentpercent]:
            toprint = duck[len(lastprint):currentpercent]
            lastprint = duck[:currentpercent]
        elif (i == rangelen - 1 and duck[:currentpercent] != duck) or (duck[:currentpercent] == duck):
            toprint = duck
        yield toprint
