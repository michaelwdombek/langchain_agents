from dataclasses import dataclass
from typing import Protocol


@dataclass
class HIVEMIND(Protocol):
    """
    Protocol for the HIVEMIND tier classes
        Tier 1: CENTRAL_HUB - understands the overall problem and decomposes it into tasks
        Tier 2: STRATEGIC_SYNAPSES - controls the working of one tasks
        Tier 3: OPERATIVE_CLUSTERS - does the working
    """

    @staticmethod
    def goal() -> str:
        """
        Returns:
            str: A part of the System prompt that describes the goal of the specific tier
        """
        ...

    @staticmethod
    def structure() -> str:
        """
        Returns:
            str: A part of the System prompt that describes the structure of the HIVEMIND and the task of
                    specific tier in it
        """
        ...

    @staticmethod
    def flow() -> str:
        """
        Returns:
            str: A part of the System prompt that describes the operational flow of the specific tier
        """
        ...

    @staticmethod
    def objective() -> str:
        """
        Returns:
            str: A part of the System prompt that describes the objective of the specific tier
        """
        ...

