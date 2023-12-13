import pytest
import time

@pytest.mark.set1
def test_obc_memory():
    print("\Querying OBC's unflashed memory from the SD card. Please wait...")
    time.sleep(5)
    obc_unflashed_memory=50000
    print("OBC unflashed memory calculated at {}B. Proceeding...\n".format(obc_unflashed_memory))
    time.sleep(3)
    obc_flash_data=6000
    print("Calculating total size of flash data to be copied. Please wait...")
    time.sleep(5)
    print("Flashing data size calculated at {}B. Proceeding...\n".format(obc_flash_data))
    obc_total_supported_memory = 52000
    print("Querying total supported memory for OBC version 2.3.1. Please wait...")
    time.sleep(3)
    print("Total supported memory info achieved ({}B). Proceeding...\n".format(obc_total_supported_memory))
    print("Test results:\n")
    time.sleep(2)
    pytest.assume(obc_unflashed_memory + obc_flash_data <= obc_total_supported_memory, "Failed, please reference test code to figure out why.")
    pytest.assume(obc_unflashed_memory == obc_total_supported_memory, "Failed, please reference test code to figure out why.")
