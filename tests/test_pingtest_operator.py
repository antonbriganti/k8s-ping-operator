import unittest
import unittest.mock
from src.pingtest_operator import PingTestOperator
from src.pinger import PingResponse


class TestPingTestOperator(unittest.TestCase):
    def test_operator_catches_malformed_spec_and_returns_error_message(self):
        test_spec = {"host": "google.com"}
        expected_response = {
            "status": {"error": "invalid spec provided, please check input yaml"}
        }

        mocked_pinger = unittest.mock.MagicMock()
        pingtest_operator = PingTestOperator(mocked_pinger)
        actual_response = pingtest_operator.process_pingtest_request(test_spec)

        self.assertEqual(expected_response, actual_response)

    def test_operator_catches_bad_host_and_returns_error_message(self):
        test_spec = {"host": "google.comm", "count": 5}
        expected_response = {
            "status": {"error": "The name 'google.comm' cannot be resolved"}
        }

        mocked_pinger = unittest.mock.Mock(side_effect=KeyError())
        mocked_pinger.ping_host = unittest.mock.Mock(
            side_effect=Exception("The name 'google.comm' cannot be resolved")
        )
        pingtest_operator = PingTestOperator(mocked_pinger)
        actual_response = pingtest_operator.process_pingtest_request(test_spec)

        self.assertEqual(expected_response, actual_response)

    def test_operator_creates_patch_body_for_valid_spec(self):
        test_spec = {"host": "google.com", "count": 5}
        expected_response = {
            "status": {
                "packetsSent": 2,
                "packetsReceived": 2,
                "packetLoss": 0,
                "packetResults": [
                    {"packetNumber": 0, "from": "1.1.1.1", "time": 5, "bytesSent": 64},
                    {"packetNumber": 1, "from": "1.1.1.1", "time": 5, "bytesSent": 64},
                ],
                "roundTripMin": 5,
                "roundTripMax": 5,
                "roundTripAvg": 5,
                "roundTripStdDev": 0.0,
            }
        }

        mocked_pinger = unittest.mock.Mock()
        mocked_pinger.ping_host = unittest.mock.Mock(
            return_value=PingResponse("1.1.1.1", 64, 2, 2, 0, [5, 5], 5, 5, 5)
        )

        pingtest_operator = PingTestOperator(mocked_pinger)
        actual_response = pingtest_operator.process_pingtest_request(test_spec)
        
        self.assertEqual(expected_response, actual_response)
