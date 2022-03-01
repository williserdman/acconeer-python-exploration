from acconeer.exptool.a111.algo import ModuleFamily, ModuleInfo

from ._processor import Processor, get_processing_config, get_sensor_config
from .ui import PGUpdater


module_info = ModuleInfo(
    key="iq_sleep_breathing",
    label="Sleep breathing (IQ)",
    pg_updater=PGUpdater,
    processing_config_class=get_processing_config,
    module_family=ModuleFamily.EXAMPLE,
    sensor_config_class=get_sensor_config,
    processor=Processor,
    multi_sensor=False,
    docs_url=(
        "https://acconeer-python-exploration.readthedocs.io/"
        + "en/latest/processing/sleep_breathing.html"
    ),
)
