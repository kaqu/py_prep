import sys
import os
import logging

from .config import VENV_PATH
from .env_check import check_python_runtime, check_environment
from .env_setup import initialize_environment, install_packages

def rerun_activated(argv):
    logging.info("Rerunning with activated venv...")
    args = set(argv[1:])
    if "-init" in args:
        args.remove("-init")
        args.add("-install")

    return os.system(
        "/bin/bash -c 'source {venv_path}bin/activate\npython -m env_setup {args}'"
        .format(venv_path=VENV_PATH, args=", ".join(args))
    )


def main(argv):    
    logging.basicConfig(format="[%(levelname)s] %(message)s", level=logging.INFO)

    require_virtual = "-no-venv" not in argv
    dev_enabled = "-dev" in argv
    initialize =  "-init" in argv
    install = initialize or "-install" in argv
    check = "-check" in argv

    if initialize and require_virtual:
        initialize_environment()
        result = rerun_activated(argv)
        exit(result)
    
    check_python_runtime(require_virtual)

    if install:
        install_packages(dev_enabled)

    if check:
        check_environment(require_virtual, dev_enabled)
	