import xmltodict
#import xml.etree.ElementTree as ET
#from xml.dom import minidom
#from datetime import datetime

source = {'Garmin Connect': {'time_format': '%Y-%m-%dT%H:%M:%S.000Z'},
          'Strava.com Android': {'time_format': '%Y-%m-%dT%H:%M:%SZ'}}


class gpx(object):
    '''
        gpx interface

        gpx is an XML schema designed as a common GPS data format for software
        applications.
        This class has read() and write() methods for reading and writing xml
        string.


        from gpx doc:
            <gpx
            version="1.1 [1]"
            creator="xsd:string [1]">
                <metadata> metadataType </metadata> [0..1]
                <wpt> wptType </wpt> [0..*]
                <rte> rteType </rte> [0..*]
                <trk> trkType </trk> [0..*]
                <extensions> extensionsType </extensions> [0..1]
            </gpx>

        from gpx doc:
            <metadata>
                <name> xsd:string </name> [0..1]
                <desc> xsd:string </desc> [0..1]
                <author> personType </author> [0..1]
                <copyright> copyrightType </copyright> [0..1]
                <link> linkType </link> [0..*]
                <time> xsd:dateTime </time> [0..1]
                <keywords> xsd:string </keywords> [0..1]
                <bounds> boundsType </bounds> [0..1]
                <extensions> extensionsType </extensions> [0..1]
            </metadata>

        from gpx doc:
            <trk>
                <name> xsd:string </name> [0..1]
                <cmt> xsd:string </cmt> [0..1]
                <desc> xsd:string </desc> [0..1]
                <src> xsd:string </src> [0..1]
                <link> linkType </link> [0..*]
                <number> xsd:nonNegativeInteger </number> [0..1]
                <type> xsd:string </type> [0..1]
                <extensions> extensionsType </extensions> [0..1]
                <trkseg> trksegType </trkseg> [0..*]
            </trk>

        from gpx doc:
            <trkseg>
                <trkpt> wptType </trkpt> [0..*]
                <extensions> extensionsType </extensions> [0..1]
            </trkseg>
    '''

    def __repr__(self):
        pass

    class SourceCst(object):
        '''
        Depending on where the gpx file is coming / going, format differs.
        An instance of this class should be used for each gpx.read/write.
        '''
        def __init__(self, d):
            for k, v in d.items():
                setattr(self, k, v)

    @staticmethod
    def basic_parse(gpx):
        '''
        '''
        pass

    @staticmethod
    def read(gpx):
        '''
        Check if gpx file contain a valid activity.
        If so, returns an ordereddict defining the activity.

        in . gpx . path of gpx file
                 . type . string
        out . d . json dict
                . type . collections.OrederdDict


            >>> In [1]: a = gpx.read('run.gpx')

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
        '''
        with open(gpx, 'r') as f:
            parsed_gpx = xmltodict.parse(f.read())
            gpx.basic_parse(parsed_gpx)
            d = parsed_gpx['gpx']
        return d
