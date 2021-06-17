import kopf
from src import pinger
from src import k8s_api


class PingTestOperator:
    def __init__(self, pinger):
        self.pinger = pinger

    def process_pingtest_request(self, spec):
        hostname = spec.get("host")
        ping_count = spec.get("count")

        if self.__validate_spec_contents(hostname, ping_count):
            patch_body = self.__create_error_patch_body(
                "invalid spec provided, please check input yaml"
            )
        else:
            try:
                ping_response = self.pinger.ping_host(hostname, ping_count)
                patch_body = self.__create_pingtest_patch_body(ping_response)
            except Exception as e:
                patch_body = self.__create_error_patch_body(str(e))

        return patch_body

    def __validate_spec_contents(self, hostname, ping_count):
        return not hostname or not ping_count

    def __create_error_patch_body(self, error_message):
        patch_body = {"status": {"error": error_message}}
        return patch_body

    def __create_pingtest_patch_body(self, ping_response):

        pingtest_patch_body = {
            "status": {
                "packetsSent": ping_response.packets_sent,
                "packetsReceived": ping_response.packets_received,
                "packetLoss": ping_response.packet_loss,
                "packetResults": ping_response.packet_results,
                "roundTripMin": ping_response.round_trip_min_time,
                "roundTripMax": ping_response.round_trip_max_time,
                "roundTripAvg": ping_response.round_trip_average_time,
                "roundTripStdDev": ping_response.round_trip_standard_deviation_time,
            }
        }

        return pingtest_patch_body


@kopf.on.create("pingtests")
def create_fn(spec, name, namespace, **kwargs):
    operator = PingTestOperator(pinger.Pinger())
    patch_body = operator.process_pingtest_request(spec)

    k8s_api.update_pingtest_object(name, namespace, patch_body)
