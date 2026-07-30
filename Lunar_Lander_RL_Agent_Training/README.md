# 🚀 Lunar Lander Reinforcement Learning Agent using PPO

## 📌 Project Overview

This project demonstrates how to train an autonomous Lunar Lander agent using **Reinforcement Learning (RL)**. The agent is trained in the **Gymnasium LunarLander-v3** environment using the **Proximal Policy Optimization (PPO)** algorithm from the Stable-Baselines3 library.

The objective of the agent is to safely land a spacecraft on the designated landing pad while minimizing fuel usage and avoiding crashes. Through continuous interaction with the environment, the agent learns an optimal landing strategy by maximizing cumulative rewards.

---

## 🎯 Objectives

- Understand the fundamentals of Reinforcement Learning.
- Train an intelligent agent using the PPO algorithm.
- Evaluate the trained model's performance.
- Record and visualize the agent's gameplay.
- Analyze training results using reward metrics.

---

## 🧠 Reinforcement Learning

Reinforcement Learning is a machine learning paradigm where an agent learns by interacting with an environment. Instead of learning from labeled data, the agent receives rewards or penalties based on its actions and gradually learns the best policy to maximize long-term rewards.

### RL Components

- **Agent:** Lunar Lander
- **Environment:** Gymnasium LunarLander-v3
- **State Space:** 8-dimensional observation vector
- **Action Space:** 4 discrete actions
- **Reward:** Based on successful landing, stability, and fuel efficiency

---

## 🤖 PPO Algorithm

Proximal Policy Optimization (PPO) is a policy-gradient reinforcement learning algorithm developed by OpenAI. It provides stable and efficient learning by limiting large policy updates during training.

### Advantages

- Stable training
- Efficient learning
- Easy implementation
- High performance on continuous control tasks

---

## 🛠️ Technologies Used

- Python 3
- Gymnasium
- Stable-Baselines3
- PyTorch
- NumPy
- Matplotlib
- MoviePy
- Google Colab

---

## 📦 Installation

Install the required libraries before running the notebook.

```bash
pip install gymnasium[box2d]
pip install stable-baselines3[extra]
pip install moviepy
```

---

## 📈 Training Process

The agent is trained using PPO for **100,000 timesteps**.

Training includes:

- Environment creation
- Policy optimization
- Reward maximization
- Model saving
- Performance evaluation

---

## 📊 Evaluation

The trained model is evaluated over multiple episodes to calculate:

- Mean Reward
- Standard Deviation
- Landing Success

Higher average rewards indicate better policy learning.

---

## 🎥 Gameplay Recording

The trained agent's gameplay is recorded using the Gymnasium `RecordVideo` wrapper.

The recorded video demonstrates the agent's ability to land safely after training.

---

## 📸 Sample Output

Expected outputs include:

- Training logs
- Reward graphs
- Saved PPO model
- Gameplay video
- Evaluation statistics

---

## 📚 Learning Outcomes

After completing this project, you will understand:

- Reinforcement Learning fundamentals
- Markov Decision Process (MDP)
- Policy Gradient methods
- PPO algorithm
- Gymnasium environments
- Agent evaluation
- Reward optimization

---

## 🔮 Future Improvements

Possible enhancements include:

- Hyperparameter tuning
- Training for more timesteps
- Comparing PPO with DQN, A2C, and SAC
- TensorBoard visualization
- Custom reward shaping
- Deploying the trained model as a web application

---

## 👨‍💻 Author

**Name:** Sumant Kumar

**Project:** Lunar Lander Reinforcement Learning Agent using PPO

**Language:** Python

**Framework:** Stable-Baselines3

**Environment:** Gymnasium LunarLander-v3

---

## 📄 License

This project is intended for educational and academic purposes.
