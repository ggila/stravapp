import xmltodict

def get_activity(gpx):
    ''' 
    open activity from file gpx
    in . gpx . path of gpx file
             . type . string
    out . a . activity.json
            . type . collections.OrederdDict
    '''
    with open(gpx, 'r') as f:
        a = xmltodict.parse(f.read())
    return a

#def
