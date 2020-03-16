# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:19:34 2020

@author: sundooedu
"""
#%%
import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range(100):
    env.render()
    env.step(env.action_space.sample())
#%%
import gym
env = gym.make("MountainCar-v0")
env.reset()

done = False
while not done:
    action = 2  # always go right!
    actioin = env.action_space.sample()
    env.step(action)
    env.render()
#%%
import gym
env = gym.make("CartPole-v0")

def basic_policy(obs):
    angle = obs[2]
    return 0 if angle < 0 else 1

#summary
import numpy as np
np.mean(totals), np.std(totals), np.min(totals), np.max(totals)

totals =[]
for episode in range(500):
    episode_rewards=0
    obs = env.reset()    
    for step in range(1000):
        action = basic_policy(obs)
        obs,reward,done,info=env.step(action)
        episode_rewards+=reward
        if done:
            break
        totals.append(episode_rewards)  
        
model = Sequential()
model.add(Dense(24, input_shape=(observation_space,), activation="relu"))
model.add(Dense(24, activation="relu"))
model.add(Dense(self.action_space, activation="linear"))
model.compile(loss="mse", optimizer=Adam(lr=0.001))
model.summary()        