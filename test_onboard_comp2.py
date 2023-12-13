import pytest
import time

## Chalange figure out what the limits and the OB telemetry readigs are for:
#    1. Run the code and work out which assumptions are passing and which are failing. This would simulate
#       getting data from one of the modules on the satellite to find out if the system is wokring as we
#       as we would expect or not and note down which assumptions pass and which ones fail.
#    2. For the first pytest.assumption work out:
#           1. What it is measuring
#           2. What the limits are for the assumption
#           3. What the telemetry measurement is.
#    2. For the second pytest.assumption work out:
#           1. What it is measuring
#           2. What the limits are for the assumption
#           3. What the telemetry measurement is.


# Lets make some fake OB telemetry
ob_telemetry = {
    "current": 210,
    "voltage": 3.43
}

@pytest.mark.set1
def test_ob_limits(telemetry_limits):
    print("Querying the OB for its telemetry limits.")
    time.sleep(1)
    # Lets get the fake OB telemetry
    ob_tlm = ob_telemetry
    # Lets check to see fi the current is within limits.
    ob_min_curr_lim = telemetry_limits['obc']['min_current']
    ob_max_curr_lim = telemetry_limits['obc']['max_current']
    pytest.assume(ob_min_curr_lim <= ob_tlm['current'] <= ob_max_curr_lim, "Fail OB limit is out "
                  "of limits. Please work out what the limits for this should be and what the OB "
                  "current is.")
    # Lets check to see if the voltage is within limits
    ob_min_volt_lim = telemetry_limits['obc']['min_voltage']
    ob_max_volt_lim = telemetry_limits['obc']['max_voltage']
    pytest.assume(ob_min_volt_lim <= ob_tlm['voltage'] <= ob_max_volt_lim, "Fail OB limit is out of "
                  "limits. Please work out what the limits for this should be and what the OB voltage is.")

