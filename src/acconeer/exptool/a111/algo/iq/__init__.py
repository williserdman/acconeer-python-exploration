import sys

from ..module_info import ModuleFamily, ModuleInfo
from .plotting import PGUpdater
from .processing import Processor, get_processing_config, get_sensor_config


module_info = ModuleInfo(
    "iq",
    "IQ",
    sys.modules[__name__],
    ModuleFamily.SERVICE,
    get_sensor_config,
    Processor,
    True,
    "https://acconeer-python-exploration.readthedocs.io/en/latest/services/iq.html",
)
