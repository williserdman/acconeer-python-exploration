import sys

from ..module_info import ModuleFamily, ModuleInfo
from ..utils import multi_sensor_wrap
from .plotting import PGUpdater
from .processing import Processor, get_processing_config, get_sensor_config


_multi_sensor_wrap = multi_sensor_wrap(sys.modules[__name__])

module_info = ModuleInfo(
    "sparse_speed",
    "Speed (sparse)",
    _multi_sensor_wrap,
    ModuleFamily.EXAMPLE,
    _multi_sensor_wrap.get_sensor_config,
    _multi_sensor_wrap.Processor,
    True,
    None,
)
