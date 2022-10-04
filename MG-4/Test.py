#Testfile for changing Parameters in the Workflow

import os, sys, yaml, subprocess

cmd = "sinfo | grep -P "alloc|mix" | grep -P "big" | awk '{print $6}'"

def NodeList():
    result = subprocess.run(cmd)

def change_config

    with open ('../simulation_config.yaml', 'w') as f:
        config_file = yaml.load(f)
        config_file['number_of_bins'] = n  



for n in range(NodeList.length()):



