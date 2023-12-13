### Notes for completing the challenges


https://github.com/matt-spire/mfg-interview/assets/139474836/e7f649cc-a897-405a-ae72-92894d7e2501


- You can either:
    - Clone this repo on to a linux distribution (Ubuntu 20.x will be fine) and install pytest locally using python2
      - Please use these commands to do so:

            pip install pytest==2.9.1
            pip install pytest-assume==1.2

    - Open this repo in codespaces (simpler) where the dev envrionment will be automatically created.
      - Instructions for getting started with codespaces:

            Create your own branch of the repo

            Click the <>code button at the top of the repo

            Select the codespaces tab

            Create a codespace in your branch



<small> **The repo that’s been shared with you, contains all the files you will need to complete the tasks. You will not require any further packages to be installed to complete the tasks** </small>

## Please commit your changes / answers to your own branch to be discussed during on-site visit.

##################################################################

The py files named `test_onboard_comp, test_onboard_comp2, test_power_unit, test_power_unit2, test_power_unit3 and test_power_unit4` are tests utilizing some pytest capabilities.

Run each of them separately and find the reason for failure, if there is a failure at all.

Commands to be run:

py.test -rs -v -s -k test_power_unit.py

py.test -rs -v -s -k test_power_unit2.py

py.test -rs -v -s -k test_power_unit3.py

py.test -rs -v -s -k test_power_unit4.py

py.test -rs -v -s -k test_onboard_comp.py

Open the file `test_onboard_comp2.py` and read the instructions before you run:

py.test -rs -v -s -k test_onboard_comp2.py

##################################################################

The file `mock_sat.py` contains a simple satellite class. Please review the file to have an idea of what the functions are doing and work through the following:

- Create a sample object of that class

- Making use of the satellite's MockAi class, what is the difference between `Btp.ping()` and `btp.ping()` functions? Are they both working as expected? If not, why?

- What is the value for the `MockAi()` channels variable? Can you set it to a different number? Is it mutable?

- Write a function that will evaluate the result of the `get_store_status()` function in the `MockAi()` class and increase the "error" output if the difference between the seq and the count is more than 1

- Create a handle of the `MockOb()` and call the `ob.bootcount()` function. Is it working? If not, why? How would you make it return the value we want?

- Make a call of the MockOb's shell function by running `shell("cat /proc/cmdline")`. What is the value of the "root" field? How would you make it print out "ubi0_0" instead?

- Use the shell function to reset the bootcount and re-run the `shell("cat /proc/cmdline")` command. Does that change the "root" value? How would you make it work, i.e. when the bootcount is reset, make the "root" value in the `shell("cat /proc/cmdline")` print out the correct value.

##################################################################
