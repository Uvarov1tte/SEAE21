import sensors_main
import unittest
from unittest.mock import Mock, call, patch # needed for the example integration test case
import sys # needed for setting the command line parameters for test cases

# Unit tests implemented with Python's built-in unittest
# need to be classes, so here we use TestSensors class
# for the tests.
class TestSensors(unittest.TestCase):
    ###############################
    # Examples of unit test cases #
    ###############################

    # The test case test_check_limits1 that tests the check_limits
    # with correct inputs (lower limit 18 and higher limit 22) and
    # expects the method to return True, since the limits are
    # correct.
    def test_check_limits1(self):
        limits = [18, 22]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result, True)
    
    # The test case test_check_limits2 that tests the check_limits
    # with incorrect inputs (lower limit 22 and higher limit 18) and
    # expects the method to return False, since the limits are
    # incorrect.
    def test_check_limits2(self):
        limits = [22, 18]
        result = sensors_main.check_limits(limits)
        self.assertFalse(result, False)

    # The test case test_check_limits3 that tests the check_limits
    # with incorrect inputs that are equal (lower limit 18 and higher
    # limit 18) and expects the method to return False, since the
    # limits are incorrect. 
    def test_check_limits3(self):
        limits = [18, 18]
        result = sensors_main.check_limits(limits)
        self.assertFalse(result, False)

    # The test case test_check_limits1 that tests the check_limits
    # with correct inputs (lower limit 8 and higher limit 16) and
    # expects the method to return True, since the limits are
    # correct.
    def test_check_limits4(self):
        limits = [8, 16]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result, True)

    # The test case test_read_sensors0 that tests whether function
    # read_sensors return any sensor readings.
    def test_read_Sensors(self):
        result=sensors_main.read_sensors()
        self.assertNotEqual(result, "")

    # The test case test_read_sensors that tests whether function
    # read_sensors return 4 sensor readings.
    def test_read_sensors(self):
        result = len(sensors_main.read_sensors())
        self.assertEqual(result, 4)

    # The test case test_read_sensors2 that tests whether function
    # read_sensors return 5 result for each sensor reading.
    def test_read_sensors2(self):
        sensors_reading = sensors_main.read_sensors()
        for sensor in sensors_reading:
            num_of_result= len(sensor)
        self.assertNotEqual(num_of_result, 5)
    # possible change if it is allowed to change the code in sensors_main.py

    #######################################
    # Example of an integration test case #
    #######################################

    # The test case test_check_limits_integration1 that tests
    # the check_limits from main.

    # Redirect console output to sys.stdout in order to
    # check it from the test cases (here, from the example
    # integration test case). Notice the use of mock_print
    # as a parameter of the test case function.
    @patch('builtins.print')
    def test_check_limits_integration1(self, mock_print):
        # set command line parameters, since they are where main gets the
        # min and max temperature settings
        sys.argv = [["sensors_main.py"], [22], [18]]

        # call main with the command line parameters set up
        sensors_main.main()

        # check that the console output is the expected error message
        mock_print.assert_called_with("Error: Incorrect command line arguments.")

        # If you want to see what is in mock_print, you can use the following
        # (requires that there is import sys as this module has because this
        # test case sets the command line arguments that are in sys.argv)
        #
        # sys.stdout.write(str(mock_print.call_args) + "\n")
        # sys.stdout.write(str(mock_print.call_args_list) + "\n")
    
    @patch('builtins.print')
    def test_check_limits_integration2(self, mock_print):
        # set command line parameters, since they are where main gets the
        # min and max temperature settings (18 and 22), then call the function with the command line args
        with patch.object(sys,'argv', ["sensors_main.py", 18, 22]):
            sensors_main.main()
        # sys.argv = ["sensors_main.py", 18, 22]
        # sensors_main.main()
        # set up for the test call below
        mock = Mock(return_value=None)
        # mock([21.2, 18.2, 18.2, 22.2])
        # mock([-5.0, -4.2, -3.9, -4.5])
        # mock([1.2, 0.0, 0.5, -0.8, -1.0])
        # mock([25.0, -4.2, -13.9, 4.5])
        sensors_readings = [[21.2, 18.2, 18.2, 22.2], [-5.0, -4.2, -3.9, -4.5], [1.2, 0.0, 0.5, -0.8, -1.0], [25.0, -4.2, -13.9, 4.5]]
        i = 0
        calls = []
        while i<4:
            for sensor in sensors_readings:
                mock(sensor)
                calls.append(call(sensor))
                i+=1
        # calls = [call([21.2, 18.2, 18.2, 22.2]), call([-5.0, -4.2, -3.9, -4.5]), call([1.2, 0.0, 0.5, -0.8, -1.0]), call([25.0, -4.2, -13.9, 4.5])]

        # check that the console output is the expected calls (sensor readings lists)
        mock_print.assert_has_calls(calls, any_order=False)

        # see what is in mock_print
        sys.stdout.write(str(mock_print.call_args_list) + "\n")

if __name__ == '__main__':
    unittest.main()