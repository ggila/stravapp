import xmltodict
#import xml.etree.ElementTree as ET
#from xml.dom import minidom
#from datetime import datetime

'''
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

source = {'Garmin Connect': {'time_format': '%Y-%m-%dT%H:%M:%S.000Z'},
          'Strava.com Android': {'time_format': '%Y-%m-%dT%H:%M:%SZ'}}


class Gpx(object):
    '''
        gpx interface

        gpx is an XML schema designed as a common GPS data format for software
        applications.
        This class has read() and write() methods for reading and writing xml
        string.
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

    @classmethod
    def read(cls, gpx):
        '''
        Check if gpx file contains a valid activity.
        If so, returns a dict defining the activity.

            >>> In [2]: a = Gpx.read('valid_run.gpx')
            
            >>> In [3]: a.keys()
                Out[3]: ['date', 'tracks', 'name']

            >>> In [4]: {k:type(a[k]) for k in a.keys()}
                Out[4]: {'date': unicode, 'name': unicode, 'tracks': list}
                
            >>> In [5]: a['tracks'][0].keys()
                Out[5]: ['lat', 'hr', 'ele', 'lon', 'delta']

        '''
        with open(gpx, 'r') as f:
            parsed_gpx = xmltodict.parse(f.read())
        cls._basic_parse(parsed_gpx)
        d = cls._set_activity_dict(parsed_gpx['gpx'])
        return d

    @classmethod
    def _basic_parse(cls, gpx_dict):
        gpx = gpx_dict['gpx']
        cls._check_creator(gpx['@creator'])

    @staticmethod
    def _check_creator(creator):
        if creator not in source:
            raise ValueError('xml file creator {} is not known'
                             .format(creator))

    @classmethod
    def _set_activity_dict(cls, gpx):
        d = {
            'name': gpx['trk']['name'],
            'date': gpx['metadata']['time'],
            'tracks': cls._format_tracks(
                gpx['trk']['trkseg']['trkpt']),
        } 
        return d

    @classmethod
    def _format_tracks(cls, trkpt):
        tracks = list()
        for trk in trkpt:
            track = {
                    'delta': trk['time'], 
                    'lon': trk['@lon'],
                    'lat': trk['@lat'],
                    'ele': trk['ele'],
                    'hr': -1,
            }
            track.update(cls._check_extensions(trk))
            tracks.append(track)
        return tracks

    @staticmethod
    def _check_extensions(trk):
        ext = dict()
        return ext
