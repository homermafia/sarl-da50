import os
import sys


from vm.Kernel import Kernel
import time

import uuid

from vm.builtin.skill.SreDynamicSkillProvider import SreDynamicSkillProvider

# start_time = time.time()

args = sys.argv
agent_path = args[1]
parameters = () if len(args) == 2 else args[2:]

agent_directory = os.path.split(agent_path)[0]
agent_name = os.path.splitext(os.path.basename(agent_path))[0]

sys.path.append(agent_directory)

agent_module = __import__(agent_name)
agent_class = getattr(agent_module, agent_name)

kernel = Kernel()
kernel.start(agent_class, *parameters)

# print("time elapsed : {:.2f}s".format(time.time() - start_time))