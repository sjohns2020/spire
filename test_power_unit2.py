import pytest
import time
from pprint import pprint

@pytest.mark.set1
def test_pdu_battery_voltage(telemetry_limit):
    """
    Compare the PDU battery voltage to the EPS and LEMBAT voltage to make sure they are all within X
    tolerance of each other
    """
    print("\n\nTelemetry Limits:\n\n")
    pprint(telemetry_limits)
    pdu_battery_voltage = 6800
    eps_battery_voltage = 200
    lembat_battery_voltage = 400
    print("\nCalculating the difference between PDU and EPS battery voltages. Please wait...\n")
    time.sleep(3)
    print("Calculating the difference between PDU and LEMBAT battery voltages. Please wait...\n")
    time.sleep(3)
    pytest.assume(abs(pdu_battery_voltage - eps_battery_voltage) == 100, "Difference between PDU battery "
                    "voltage and EPS battery voltage was {diff}mV, should be no more than 100mv."
                    "\nPDU battery voltage: {pdu}mV\nEPS battery voltage: {eps}mV\n"
                    .format(diff=abs(pdu_battery_voltage - eps_battery_voltage),
                            pdu=pdu_battery_voltage,
                            eps=eps_battery_voltage))
    pytest.assume(abs(pdu_battery_voltage - lembat_battery_voltage) == 100, "Difference between PDU "
                    "battery voltage and LEMBAT battery voltage was {diff}mV, should be no more than 100mV."
                    "\nPDU battery voltage: {pdu}mV\nLEMBATT battery voltage: {eps}mV\n"
                    .format(diff=abs(pdu_battery_voltage - lembat_battery_voltage),
                            pdu=pdu_battery_voltage,
                            eps=lembat_battery_voltage))
