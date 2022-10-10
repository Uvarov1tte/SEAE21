import sensors_main
import unittest
from unittest.mock import Mock, call, patch # needed for the example integration test case
import sys # needed for setting the command line parameters for test cases

# Unit tests implemented with Python's built-in unittest
# need to be classes, so here we use TestSensors class
# for the tests.
class TestSensors(unittest.TestCase):    
    @patch('builtins.print')
    def test_check_limits_integration2(self, mock_print):
        # set command line parameters, since they are where main gets the
        # min and max temperature settings (8 and 16), then call the function with the command line args
        sys.argv = ["sensors_main.py", "8", "16"]
        sensors_main.main()
        # check the last line called
        mock_print.assert_called_with([25.0, -4.2, -13.9, 4.5])

if __name__ == '__main__':
    unittest.main() 