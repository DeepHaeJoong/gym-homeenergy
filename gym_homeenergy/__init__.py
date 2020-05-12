from gym.envs.registration import register

register(
    id='homeenergy-v0',
    entry_point='gym_homeenergy.envs:homeenergyEnv',
)
register(
    id='homeenergy-extrahard-v0',
    entry_point='gym_homeenergy.envs:homeenergyExtraHardEnv',
)
