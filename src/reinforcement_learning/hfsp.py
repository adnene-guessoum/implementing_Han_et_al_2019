"""
	Set up the Hybrid flow shop environment to interact with as per
	specifications in Han et al 2019 (cf. paper section 4 MDP framework for
	HFSP.
"""

import numpy as np


class Hfsp:
    """
    Don't know what it looks like yet...

    Do I really need a class ?

    probably needs:

    workpieces, stages, machines (ie. actions)

    returns what's needed for runner.py:
            actions list (machines per stages),
            states ((stage, machine) tuples),
            whatever else...

    """

    def __init__(self, number_stages, number_machines_per_stages):
        return self

    def hfsp_setup(self):
        return actions, states
