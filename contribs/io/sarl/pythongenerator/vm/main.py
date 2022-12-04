from vm.AgentWithEvent.agentWithEvent import AgentWithEvent
from vm.GuardedAgent.guardedAgent import GuardedAgent
from vm.HelloWorld.helloWorld import HelloWorldAgent
from vm.Kernel import Kernel
#from contribs.io.sarl.pythongenerator.vm.HelloWorld.helloWorld import HelloWorldAgent
from vm.LoggingAgent.LoggingAgent import LoggingAgent

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

kernel = Kernel()
kernel.start(HelloWorldAgent)