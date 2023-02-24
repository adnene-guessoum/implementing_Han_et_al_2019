"""
    TODO: re-enable pylint too manu argument rule

    Model for simple q-learning algorithm implementation in HFS context

    Han, Wei, Fang Guo, and Xichao Su. 2019. "A Reinforcement Learning Method
    for a Hybrid Flow-Shop Scheduling Problem" Algorithms 12, no. 11: 222.
    https://doi.org/10.3390/a12110222

"""

import numpy as np
import pandas as pd


class QTable:
    """
    cf. page 9 for default values
    """

    def __init__(
        self,
        actions: list,
        initial_epsilon: float,
        episode_number: int,
        exploration_decay: float,
        learning_rate: float = 0.1,
        discount_factor: float = 0.9,
    ):  # pylint: disable=too-many-arguments
        self.actions = actions
        self.alpha = learning_rate
        self.gamma = discount_factor

        # cf equation (12): exploration_decay is beta
        self.epsilon = initial_epsilon - (exploration_decay * episode_number)

        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)

    def action_selection(self, observation):
        """
        Choosing next machine as per the q_table and the exploration
        exploitation trade-off.
        """
        if np.random.uniform() < self.epsilon:
            q_lookup = self.q_table.loc[observation, :]

            # random machine choice in case of equal value
            selected_action = np.random.choice(
                q_lookup[q_lookup == np.max(q_lookup)].index
            )

        else:
            selected_action = np.random.choice(self.actions)

        return selected_action

    def update_q_table(self, state, action, reward, next_state):
        """
        Updating the q-table after allocation to next stage and received
        reward.
        """
        prediction = self.q_table.loc[state, action]

        # "goal" state in paper designates terminal state of an episode.
        # last machine choice in last stage for last workpiece. ie, "terminal".
        if next_state is not None:
            target = (
                reward + self.gamma * self.q_table.loc[next_state, :].max()
            )
        else:
            target = reward

        self.q_table.loc[state, action] += self.alpha * (target - prediction)
