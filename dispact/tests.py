#from django.test import TestCase
from unittest import TestCase
import mock
from gpx import Gpx

# Create your tests here.

class GpxTest(TestCase):

    @mock.patch.object(Gpx, 'read')
    def test_gpx_read(self, mock_read):
        Gpx.read('tic')
        Gpx.read('tac')
        Gpx.read('toe')
        self.assertEqual(1,1)
        expected = [(('tic',),), (('tac',),),(('toe',),)]
        self.assertEqual(mock_read.call_args_list, expected)
        
if __name__ == '__main__':
    import unittest
    unittest.main()
