import unittest
from alerter import *

class TestAlerter(unittest.TestCase):
          
    def test_failure_count(self):
        #checks count of failures 
        self.assertEqual(alert_failure_count, 1) 

if __name__ == '__main__':
    alert_failure_count= alert_in_celcius(400, network_alert_stub)
    alert_failure_count= alert_in_celcius(303.6,network_alert_stub)
    unittest.main()
