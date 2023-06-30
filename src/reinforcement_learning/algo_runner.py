"""
Main script in charge of running the training
"""

#from q_learning import QTable  # type: ignore


def main(episode_number: int = 200):
    """
    Algorithm 1 pseudo-code: cf. page 7

    Simulations default values: cf. page 9
    """

    state_list: list = []
    # type: ignore
    # HERE: initialize_Q()
    #hfs_q_table = QTable()

    for episode in range(episode_number):  # type: ignore
        # HERE: initialization

        for state in state_list:  # type: ignore
            # HERE: Arrival time update as end time of previous stage

            #for workpiece in workpiece_list:  # type: ignore
                """
                HERE:

                1- choose action (next machine) based on Q
                2- perform action
                    (pass workpiece to the next chosen machine -> ie update
                    state with next stage)
                3- observe new state s' and receive reward:
                    state == tuple (stage, workpiece)
                    "receiving reward" = update Q(state, action)
                """

            # HERE: sort workpieces by end times
            # for proper arrival time at next stage
            # in ascending order
