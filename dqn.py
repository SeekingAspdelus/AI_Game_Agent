'''
Author: Tianle Zhu
Date: 2022-11-20 16:56:22
LastEditTime: 2022-12-10 14:53:33
LastEditors: Tianle Zhu
FilePath: \AI_Game_Agent\dqn.py
'''
import torch as T
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import agents

class DeepQNetwork(nn.Module):
    def __init__(self, lr, input_dims, fc1_dims, fc2_dims, n_actions):
        super(DeepQNetwork, self).__init__()
        self.input_dims = input_dims
        self.fc1_dims = fc1_dims
        self.fc2_dims = fc2_dims
        self.n_actions = n_actions
        self.fc1 = nn.Linear(self.input_dims, self.fc1_dims)
        self.fc2 = nn.Linear(self.fc1_dims, self.fc2_dims)
        self.fc3 = nn.Linear(self.fc2_dims, self.n_actions)

        self.optimizer = optim.Adam(self.parameters(), lr=lr)
        self.loss = nn.MSELoss()
        self.device = T.device('cuda:0' if T.cuda.is_available() else 'cpu')
        self.to(self.device)
        
    def forward(self, state):
        x = F.relu(self.fc1(state))
        x = F.relu(self.fc2(x))
        actions = self.fc3(x)
        return actions
    
class DQNAgent(agents.QlearningAgent):
    def __init__(self, name, money, color, game, gamma=0.9, epsilon=1.0, lr=0.001, input_dims=16, batch_size=30, n_actions = 10, max_mem_size=100000, eps_end=0.05, eps_dec=5e-4):
        super().__init__(name,money,color,game)
        self.gamma = gamma
        self.epsilon = epsilon
        self.eps_min = eps_end
        self.eps_dec = eps_dec
        self.lr = lr
        self.action_space = [i for i in range(n_actions)]
        self.mem_size = max_mem_size
        self.batch_size = batch_size
        self.mem_cntr = 0
        self.iter_cntr = 0
        #self.replace_target = 100

        self.Q_eval = DeepQNetwork(lr, n_actions=n_actions,
                                   input_dims=input_dims,
                                   fc1_dims=16, fc2_dims=12)
        self.state_memory = np.zeros((self.mem_size, input_dims),
                                     dtype=np.float32)
        self.new_state_memory = np.zeros((self.mem_size, input_dims),
                                         dtype=np.float32)
        self.action_memory = np.zeros(self.mem_size, dtype=np.int32)
        self.reward_memory = np.zeros(self.mem_size, dtype=np.float32)
        self.terminal_memory = np.zeros(self.mem_size, dtype=np.bool)

    def store_transition(self, state, reward,action, terminal, state_):
        index = self.mem_cntr % self.mem_size
        self.state_memory[index] = state
        self.new_state_memory[index] = state_
        self.reward_memory[index] = reward
        self.action_memory[index] = action
        self.terminal_memory[index] = terminal

        self.mem_cntr += 1
    
    def get_available_action(self, observation):
        available_action = self.get_action()
        if np.random.random() > self.epsilon:
            state = T.tensor(observation).to(self.Q_eval.device)
            actions = self.Q_eval.forward(state)
            sorted_actions = T.argsort(actions)
            for action_idx in sorted_actions:
                action = self.game.action_ls[action_idx.item()]
                if action in available_action:
                    return action_idx
        else:
            action = np.random.choice(available_action)
            action_idx = self.convertAction(action)

        return action_idx

    def learn(self):
        if self.mem_cntr < self.batch_size:
            return

        self.Q_eval.optimizer.zero_grad()

        max_mem = min(self.mem_cntr, self.mem_size)

        batch = np.random.choice(max_mem, self.batch_size, replace=False)
        batch_index = np.arange(self.batch_size, dtype=np.int32)

        state_batch = T.tensor(self.state_memory[batch]).to(self.Q_eval.device)
        new_state_batch = T.tensor(
                self.new_state_memory[batch]).to(self.Q_eval.device)
        action_batch = self.action_memory[batch]
        reward_batch = T.tensor(
                self.reward_memory[batch]).to(self.Q_eval.device)
        terminal_batch = T.tensor(
                self.terminal_memory[batch]).to(self.Q_eval.device)

        q_eval = self.Q_eval.forward(state_batch)[batch_index, action_batch]
        q_next = self.Q_eval.forward(new_state_batch)
        q_next[terminal_batch] = 0.0
        
        
        q_target = reward_batch + self.gamma*T.max(q_next, dim=1)[0]

        loss = self.Q_eval.loss(q_target, q_eval).to(self.Q_eval.device)
        loss.backward()
        self.Q_eval.optimizer.step()

        self.iter_cntr += 1
        self.epsilon = self.epsilon - self.eps_dec \
            if self.epsilon > self.eps_min else self.eps_min
            
    def my_turn(self):
        state = self.get_state()
        state = np.array(state,dtype=np.float32)
        action_idx = self.get_available_action(state)
        action = self.game.action_ls[action_idx]
        #print(action_idx,action.name)
        reward = self.computeReward(action)
        action.invest(self)
        if self.verbose:
            print("{agent_name} invested in {investment_name}".format(agent_name=self.name, investment_name=action.name))
        nextState = self.get_state()
        self.store_transition(state,reward,action_idx,0.0,nextState)
        self.learn()
        return
    
    def saveWeights(self, filepath):
        if ".pth" in filepath or ".pt" in filepath:
            T.save(self.Q_eval.state_dict(), filepath)
        else:
            print("invalid save path")
            
    def loadWeights(self, filepath):
        if ".pth" in filepath or ".pt" in filepath:
            self.Q_eval.load_state_dict(T.load(filepath))
        else:
            print("invalid save path")