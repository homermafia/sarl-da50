from contribs.io.sarl.pythongenerator.vm.GuardedAgent.guardedAgent import GuardedAgent
from contribs.io.sarl.pythongenerator.vm.Kernel import Kernel
#from contribs.io.sarl.pythongenerator.vm.HelloWorld.helloWorld import HelloWorldAgent
from contribs.io.sarl.pythongenerator.vm.LoggingAgent.LoggingAgent import LoggingAgent

import uuid

from contribs.io.sarl.pythongenerator.vm.builtin.skill.SreDynamicSkillProvider import SreDynamicSkillProvider

### HelloWorld
# helloWorld = HelloWorldAgent
# eventsList = helloWorld.__guard_io_sarl_core_Initialize__(helloWorld,1)
# eventsList[0](helloWorld,1)

#dynamicSkillProvider = SreDynamicSkillProvider()

### HelloWorld with the loggingSkill
#loggingAgent = LoggingAgent(None, uuid.uuid4(), dynamicSkillProvider)
#myAgentEvents = loggingAgent.__guard_io_sarl_core_Initialize__(1)
#myAgentEvents[0](1)

### GuardedAgent
#guardedAgent = GuardedAgent(None, uuid.uuid4(), dynamicSkillProvider)
#myAgentEvents1 = guardedAgent.__guard_io_sarl_core_Initialize__(2)
#myAgentEvents1[0](2)

kernel = Kernel()
kernel.start(LoggingAgent)
