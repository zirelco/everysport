#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import everysport
import logging
import os


#Getting the Everysport APIKEY from the system environment. 
APIKEY = os.environ['EVERYSPORT_APIKEY'] 


class TestResults(unittest.TestCase):

    def setUp(self):        
        self.api = everysport.Api(APIKEY)  


    def test_results_allsvenskan(self):
        
        results = self.api.get_results(everysport.ALLSVENSKAN)

        logging.debug(results)

        self.assertTrue(len(results) > 0)

    


if __name__ == '__main__': 
    logging.basicConfig(filename='results.log',
                            level=logging.DEBUG, 
                            filemode="w")
    unittest.main()
