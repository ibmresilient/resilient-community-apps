# Install PyPi dependencies for master build/test or if dev_deps is false
if [[ $MASTER_BUILD -eq 0 || $DEV_DEPS -eq 1 ]]; then
	pip install resilient-circuits
	pip install pytest-resilient-circuits
	pip install resilient-lib
	exit 0
fi

# else - install these dependencies from Artifactory
pip install resilient -i $ARTIFACTORY_PYPI_INDEX
pip install resilient-circuits -i $ARTIFACTORY_PYPI_INDEX
pip install resilient-lib -i $ARTIFACTORY_PYPI_INDEX
pip install pytest-resilient-circuits -i $ARTIFACTORY_PYPI_INDEX


