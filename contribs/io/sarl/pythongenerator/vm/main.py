import os
import sys


from vm.Kernel import Kernel
import time

import uuid

from vm.builtin.skill.SreDynamicSkillProvider import SreDynamicSkillProvider

### HelloWorld
# helloWorld = HelloWorldAgent
# eventsList = helloWorld.__guard_io_sarl_core_Initialize__(helloWorld,1)
# eventsList[0](helloWorld,1)

# loggingAgent = LoggingAgent
# myAgentEvents = loggingAgent.__guard_io_sarl_core_Initialize__(loggingAgent,1)
# myAgentEvents[0](loggingAgent,1)

### GuardedAgent
# guardedAgent = GuardedAgent
# myAgentEvents = guardedAgent.__guard_io_sarl_core_Initialize__(guardedAgent,2)
# myAgentEvents[0](guardedAgent,2)

### AgentWithEvent
#agentWithEvent = AgentWithEvent()
#myAgentEvents = agentWithEvent.__guard_io_sarl_core_Initialize__(agentWithEvent)
#myAgentEvents[0](agentWithEvent)

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