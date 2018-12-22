#!/usr/bin/python

import os
import sys
import pip
import venv
import logging

import requirements

def prepare_environment():
	logging.info("Preparing environment...")
	env_builder = venv.EnvBuilder(
		system_site_packages=False,
		clear=True,
		symlinks=False,
		with_pip=True
	)
	env_builder.create(requirements.VENV_PATH)


def install_packages():
	logging.info("Installing packages...")
	os.system(requirements.VENV_PATH + "/bin/pip install --upgrade pip")
	
	if ("-dev" in sys.argv):
		logging.info("...including dev packages...")
		package_list = requirements.PACKAGES + requirements.DEV_PACKAGES
		
	else:
		package_list = requirements.PACKAGES
		
	os.system(
		(requirements.VENV_PATH + "/bin/pip install {}")
		.format(" ".join(package_list))
	)
	

if (__name__ == "__main__"):
	logging.basicConfig(format="# %(message)s", level=logging.INFO)
	if (sys.version_info < requirements.PYTHON_VERSION):
		logging.info(
			"You need to use python {} or newer to setup this environment"
			.format(".".join(map(str,PYTHON_VERSION)))
		)
		sys.exit(-1)
	
	prepare_environment()
	install_packages()
	
	if ("-activate" in sys.argv):
		logging.info("Activating environment with bash...")
		os.system('/bin/bash --rcfile flask/bin/activate')
	
	else:
		logging.info(
			"Environment ready, use `source {}/bin/activate` to activate it."
			.format(requirements.VENV_PATH)
		)