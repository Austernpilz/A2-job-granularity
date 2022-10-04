#Testfile for changing Parameters in the Workflow

import subprocess
import pandas as pd
import numpy as np 

cmd = ["bash", "-c", "sinfo -N | grep -P \"alloc|mix\" | grep -P big | awk '{print $1}'"]
def NodeList():
    result = subprocess.run(cmd)


def change_config

    with open ('../simulation_config.yaml', 'w') as f:
        config_file = yaml.load(f)
        config_file['number_of_bins'] = n  



for n in range(NodeList.length()):


subprocess.run(["bash", "-c", "sinfo | grep -P \"alloc|mix\" | grep -P big | awk '{print $6}'"])


