import xmltodict

def getGPXDictFromJson(gpx):
    ''' 
    return json dict from gpx file

    in . gpx . path of gpx file
             . type . string
    out . d . json dict
            . type . collections.OrederdDict


        >>> In [1]: a = get_activity('run.gpx')

        >>> In [2]: a.keys()
            Out[2]:
            [u'@version',
             u'@creator',
             u'@xsi:schemaLocation',
             u'@xmlns',
             u'@xmlns:gpxtpx',
             u'@xmlns:gpxx',
             u'@xmlns:xsi',
             u'metadata',
             u'trk']

     cf ./gpx.py for details

    '''
    with open(gpx, 'r') as f:
        parsed_gpx = xmltodict.parse(f.read())
        d = parsed_gpx['gpx']
    return d

def GetActivityDictFromJson(gpx):
    ''' 
    return activity dict from gpx dict

    in . d . json dict
           . type . collections.OrederdDict
    in . gpx . path of gpx file
             . type . string
    '''
    d = GetActivityFromJson(gpx)
    try:
        a = gpx.read(gpx)
        return a
    except Exception as e:
        print(str(e))
        return dict()
