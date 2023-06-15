
import os
import platform
from pathlib import Path
from typing import Union

from .__init__ import package_name


class Utils:
    @staticmethod
    def get_config_dir() -> Path:
        """
        Return a platform-specific root directory for user configuration settings.
        """
        return {
            'Windows': Path(os.path.expandvars('%LOCALAPPDATA%')),
            'Darwin': Path.home().joinpath('Library').joinpath('Application Support'),
            'Linux': Path.home().joinpath('.config')
            }[platform.system()].joinpath(package_name)

    @staticmethod
    def get_resource_path(filename: Union[str, Path]) -> Path:
        """
        Return a package resource and create it in the process if it doesn't exists
        already.
        """
        config_dir = Utils.get_config_dir()
        config_dir.mkdir(parents=True, exist_ok=True)
        resource = config_dir.joinpath(filename)
        resource.touch(exist_ok=True)
        return resource
