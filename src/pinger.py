import statistics
from icmplib import ping


class PingResponse:
    def __init__(
        self,
        host_ip_address,
        ping_packet_size,
        packets_sent,
        packets_received,
        packet_loss,
        round_trip_times,
        round_trip_min_time,
        round_trip_max_time,
        round_trip_average_time,
    ):

        self.packets_sent = packets_sent
        self.packets_received = packets_received
        self.packet_loss = packet_loss
        self.packet_results = [
            {
                "packetNumber": packet_number,
                "from": host_ip_address,
                "time": round_trip_times[packet_number],
                "bytesSent": ping_packet_size,
            }
            for packet_number in range(len(round_trip_times))
        ]
        self.round_trip_min_time = round_trip_min_time
        self.round_trip_max_time = round_trip_max_time
        self.round_trip_average_time = round_trip_average_time
        self.round_trip_standard_deviation_time = statistics.stdev(round_trip_times)


class Pinger:
    def ping_host(self, hostname, ping_count):
        ping_packet_size = 64
        ping_result = ping(hostname, count=ping_count, payload_size=ping_packet_size)

        return PingResponse(
            ping_result.address,
            ping_packet_size,
            ping_result.packets_sent,
            ping_result.packets_received,
            ping_result.packet_loss,
            ping_result.rtts,
            ping_result.min_rtt,
            ping_result.max_rtt,
            ping_result.avg_rtt,
        )
