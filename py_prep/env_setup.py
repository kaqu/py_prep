import os
import sys
import pip
import venv
import logging
import subprocess

from .config import VENV_PATH
from .requirements import REQUIRED_PYTHON_VERSION, REQUIRED_PACKAGES, DEV_REQUIRED_PACKAGES

def initialize_environment():
	import venv

	logging.info("Initializing environment...")
	env_builder = venv.EnvBuilder(
        system_site_packages=False,
        clear=True,
        symlinks=False,
        with_pip=True
    )
	env_builder.create(VENV_PATH)
	logging.info(
        "Virtual environment initialized, use `source {venv_path}bin/activate` to activate it."
        .format(venv_path=VENV_PATH)
    )

def install_packages(dev_enabled):
	logging.info("Installing packages...")

	if dev_enabled:
		logging.info("Including dev packages...")
		required_packages = REQUIRED_PACKAGES + DEV_REQUIRED_PACKAGES
		
	else:
		required_packages = REQUIRED_PACKAGES

	result = os.system(
		("pip install {}")
		.format(" ".join(required_packages))
	)

	if (result != 0):
		logging.error("Failed to install packages...")
		exit(result)
