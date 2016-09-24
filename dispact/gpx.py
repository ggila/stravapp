import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime

class gpx(object):
    '''
        gpx interface

        gpx is an XML schema designed as a common GPS data format for software applications.
        This class has read() and write() methods for reading and writing xml string.


        from gps 1.1 doc:
            <gpx
            version="1.1 [1]"
            creator="xsd:string [1]"> 
                <metadata> metadataType </metadata> [0..1] 
                <wpt> wptType </wpt> [0..*] 
                <rte> rteType </rte> [0..*] 
                <trk> trkType </trk> [0..*] 
                <extensions> extensionsType </extensions> [0..1] 
            </gpx>
        from gps 1.1 doc:
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

        from gps 1.1 doc:
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

        from gps 1.1 doc:
            <trkseg> 
                <trkpt> wptType </trkpt> [0..*] 
                <extensions> extensionsType </extensions> [0..1] 
            </trkseg>
    '''

    def __repr__(self):
        pass

    @staticmethod
    def read(gpx):
        pass

    @staticmethod
    def _readTime(meta, time_format):
        '''
        Return datetime from metadata xml element
        '''
        time = meta.find('time'.format(gpx._xml_namespace)).text
        return datetime.strptime(time, time_format)

    @staticmethod
    def _readDeltaTime(time, t0, time_format):
        return datetime.strptime(time, time_format) - t0

    @staticmethod
    def _addAttr(ptDict, pTag, attr, func):
            tag = pTag.find(attr)
            if tag is not None:
                ptDict[attr] = func(tag.text)

    @staticmethod
    def _readTrkPt(pt, t0, tf):
        '''setup track points list from trkseg xml element'''
        ptDict = {k: float(v) for k, v in pt.attrib.items()}  # get lon and lat
        for attr, func in (('ele', float),
                           ('time', lambda t: gpx._readDeltaTime(t, t0, tf)),):
            gpx._addAttr(ptDict, pt, attr, func)
        extensions = pt.find('extensions')
        if extensions is not None:
            for attr, func in (('hr', int),
                               ('cad', int),
                               ('atemp', int),):
                gpx._addAttr(ptDict, extensions[0], attr, func)
        return ptDict
