import sys
import os
import logging
import subprocess

from .config import VENV_PATH
from .requirements import REQUIRED_PYTHON_VERSION, REQUIRED_PACKAGES, DEV_REQUIRED_PACKAGES

def check_python_version():
	if sys.version_info < REQUIRED_PYTHON_VERSION:
		version_string = ".".join(map(str, REQUIRED_PYTHON_VERSION))
		logging.error(
            "You have to use python {version} or newer in this environment"
            .format(version=version_string)
        )
		exit(-1)


def check_virtual_environment():
	binary_valid = sys.executable.endswith(VENV_PATH + "bin/python") \
		or sys.executable.endswith(VENV_PATH + "bin/python3")
	env_valid = os.getenv("__PYVENV_LAUNCHER__", None) is not None

	if not binary_valid or not env_valid:
		logging.error(
			"You have to use virtual environment. " \
			"Use '-setup_env' to make setup or activate it"
		)
		exit(-1)


def check_python_runtime(require_virtual):
	check_python_version()
	if require_virtual:
		check_virtual_environment()


def check_installed_packages(required_packages = REQUIRED_PACKAGES):
	reqs = subprocess.check_output([sys.executable, "-m", "pip", "freeze"])
	installed_packages = [r.decode().split("==")[0].lower() for r in reqs.split()]

	required_packages = [p.split("==")[0].lower() for p in required_packages]
	missing_packages = [required for required in required_packages if required not in installed_packages]

	if len(missing_packages) > 0:
		logging.error(
			"There are missing packages:\n{}"
			.format("\n".join(map(str, missing_packages)))
		)
		exit(-1)


def check_environment(require_virtual, dev_enabled):
	check_python_runtime(require_virtual)

	if dev_enabled:
		required_packages = REQUIRED_PACKAGES + DEV_REQUIRED_PACKAGES
		
	else:
		required_packages = REQUIRED_PACKAGES

	check_installed_packages(required_packages)

	logging.info("Environment valid...")
