#
# Central Hub is the entry point that organizes all high level tasks of the LLM interaction
#
from dataclasses import dataclass, field
from typing import Dict
from json import load as json_load


def load_central_hub_config(default_config_json_path: str = "config/central_hub_defaults.json") -> Dict[str, str]:
    """
    loads the central hub configuration json, default is config/central_hub_defaults.json
    Args:
        default_config_json_path (str, optional): path to the central hub configuration json. Defaults to "config/central_hub_defaults.json".

    Returns:
        Dict[str, str]: the central hub configuration
    """
    with open(default_config_json_path, "r") as f:
        return json_load(f)


CENTRAL_HUB_DEFAULT_CONFIG = load_central_hub_config()


@dataclass
class CentralHub:
    central_prompt: str = field(default=None)

    def __post_init__(self):
        if self.central_prompt is None:
            self.central_prompt = f"{self.goal()}\n{self.structure()}\n{self.flow()}\n{self.objective()}"

    @staticmethod
    def goal() -> str:
        return CENTRAL_HUB_DEFAULT_CONFIG["goal"]

    @staticmethod
    def structure() -> str:
        return CENTRAL_HUB_DEFAULT_CONFIG["structure"]


    @staticmethod
    def flow() -> str:
        return CENTRAL_HUB_DEFAULT_CONFIG["flow"]

    @staticmethod
    def objective() -> str:
        return CENTRAL_HUB_DEFAULT_CONFIG["objective"]

