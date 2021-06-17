import unittest
from src.pinger import PingResponse


class TestPingResponse(unittest.TestCase):
    def test_pingresponse_correctly_transforms_packet_results(self):
        expected_packet_results = [
            {
                "packetNumber": 0,
                "from": "1.1.1.1",
                "time": 5,
                "bytesSent": 64,
            },
            {
                "packetNumber": 1,
                "from": "1.1.1.1",
                "time": 5,
                "bytesSent": 64,
            },
        ]

        ping_response = PingResponse("1.1.1.1", 64, 2, 2, 0, [5, 5], 5, 5, 5)

        self.assertEqual(expected_packet_results, ping_response.packet_results)
