import gpx

def GetActivityDictFromFile(gpx):
    ''' 
    return activity dict from gpx dict

    out . a . activity
            . dict
    '''
    a = gpx.read(gpx)
    return a
