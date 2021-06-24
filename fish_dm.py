#source ~/.bashrc
#conda activate tf2
#python ~/1-THESE/4-sample_code/7-PILCO/PILCO/fish_dm.py

from dm_control import suite
from dm_control import viewer
import numpy as np

env = suite.load(domain_name="fish", task_name="swim")
action_spec = env.action_spec()

# Define a uniform random policy.
def random_policy(time_step):
  del time_step  # Unused.
  return np.random.uniform(low=action_spec.minimum,
                           high=action_spec.maximum,
                           size=action_spec.shape)

# Launch the viewer application.
viewer.launch(env, policy=random_policy)
# from dm_control import suite
# import numpy as np
# from dm_control import viewer
# # Load one task:
# env = suite.load(domain_name="fish", task_name="swim")
# # Iterate over a task set:
# for domain_name, task_name in suite.BENCHMARKING:
#   env = suite.load(domain_name, task_name)
# print(env)
# viewer.launch(env)
# # Step through an episode and print out reward, discount and observation.
# action_spec = env.action_spec()
# time_step = env.reset()
# while not time_step.last():
#     action = np.random.uniform(action_spec.minimum,
#                              action_spec.maximum,
#                              size=action_spec.shape)
#     time_step = env.step(action)
#     print(time_step.reward, time_step.discount, time_step.observation)
