import os
import logging
import base64
from pathlib import Path

import pydantic
import ti

logger = logging.getLogger(__name__)

class Settings(pydantic.BaseSettings):
    logging_conf: pydantic.FilePath = Path(ti.package_directory).joinpath("logging.toml").resolve()
    vt_api_key: str
    
    class Config:
        env_file = 'env'
        case_sensitive = False
