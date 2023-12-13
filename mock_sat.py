import re


class MockSat(object):
    def __init__(self):
        self.welcome_message()
        self.ai = MockAi()
        self.ob = MockOb()
        self.pd = MockPd()
        self.sam = MockSam()
        self.strt = MockStrt()

    def welcome_message(self):
        banner = """
              _
           .-T |   _
           | | |  / |   Welcome to the Spire Testing Console
           | | | / /`|  ID: Candidate
        _  | | |/ / /   Network: Local
        \`\| '.' / /    Key Signature: aaFGTnbh87H
         \ \`-. '--|    
          \    '   |    Logging to ElasticSearch: www.spire.com
           \  .`  /     Logging to file: My_file
            |    |      CDH: 4.2
            |    |      API Versions: 3.5
                 """
        print(banner)

class MockAi(object):
    class Btp(object):
        def ping(self):
            return {"reply_time_ms": 0, "success": True}

        def shell(self, command):
            return {"error_code": 0, "stdout": "", "truncated": False}

    def __init__(self):
        self.btp = self.Btp()
        self.ethernet = {"boots": 0, "enable": 0, "error": 0, "flags": 0, "type": 2}
        self.channels = 1
        self.store_size = 4500

    def get_eth(self):
        return self.ethernet

    def set_eth(self, enable, boots):
        self.ethernet.update({"enable": enable, "boots": boots})

    def get_channels(self):
        return {"channels": self.channels, "error": 0, "flags": 0, "success": True, "type": 2}

    def set_channels(self, channel):
        self.channels = channel

    def get_store_status(self):
        return {"backend": 0, "count": 340, "error": 0, "seq": 339, "size": self.store_size, "type": 2}

    def set_store_size(self, type, size):
        self.store_size = size

    def reboot(self):
        self.ethernet["boots"] = max(0, self.ethernet["boots"] - 1)


class MockOb(object):
    def __init__(self):
        self.bootcount = 0

    def ping(self):
        return {"reply_time_ms": 0, "success": True}

    def shell(self, command, timeout=0):
        if command == "cat /proc/cmdline":
            res = (
                "console=ttyO2,115200n8 ubi.mtd=20 ubi.mtd=30 ubi.mtd=41 "
                "root=ubi{ubi} ro rootfstype=ubifs\n".format(
                    ubi="0_0" if 10 < self.bootcount < 20 else "2_0"
                )
            )
        elif "reset-bootcount.py" in command:
            self.bootcount = int(command.split()[2])
            res = ""
        else:
            res = ""
        return {"error_code": 0, "exit_code": 0, "stdout": res}

    def reboot(self):
        self.bootcount += 1


class MockPd(object):
    def __init__(self):
        self.hk_dict = {
            "ADCS": {"state": "on"},
            "AI": {"state": "on"},
            "OB": {"state": "on"},
            "STRT": {"state": "on"},
            "UHF_1": {"state": "on"},
            "UHF_2": {"state": "off"},
            "PD": {"fsm_state": "FULL"},
        }

    def hk(self):
        return self.hk_dict

    def enable_manual_mode(self, time, cutoff_v):
        self.hk_dict["PD"]["fsm_state"] = "MANUAL"

    def disable_manual_mode(self):
        self.hk_dict["PD"]["fsm_state"] = "FULL"

    def set_active_radio(self, radio):
        self.hk_dict["UHF_1"]["state"] = "on" if radio == "rdf_pri" else "off"
        self.hk_dict["UHF_2"]["state"] = "on" if radio == "rdf_sec" else "off"

    def switch_off(self, subsystem):
        self.hk_dict[subsystem]["state"] = "off"

    def switch_on(self, subsystem):
        self.hk_dict[subsystem]["state"] = "on"

    def ping(self):
        return {"reply_time_ms": 0, "success": True}


class MockSam(object):
    def ping(self):
        pass


class MockStrt(object):
    def __init__(self):
        self.config_ant = "pod"

    def ping(self):
        return {"pong": 0}

    def shell(self, command):
        if command == 'readlink -en "/var/microg/repo/air/gnss/tools/mfg/configs/current_config"':
            res = "/var/microg/repo/air/gnss/tools/mfg/configs/test_{self.config_ant}.config".format(
                self=self
            )
        elif "ln -sf" in command:
            pattern = re.compile(
                r"cd /var/microg/repo/air/gnss/tools/mfg/configs && "
                r"ln -sf /var/microg/repo/air/gnss/tools/mfg/configs/test_([a-z]+)\.config current_config"
            )
            m = pattern.match(command)
            self.config_ant = m.groups()[0]
            res = ""
        else:
            res = ""

        return {
            "error_code": 0,
            "result": res,
            "return_code": 0,
        }



    
