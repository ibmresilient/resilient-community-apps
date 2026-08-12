import sys

if sys.version_info >= (3, 8):
    import importlib.metadata

    try:
        __version__ = importlib.metadata.version(__name__)
    except importlib.metadata.PackageNotFoundError:
        pass

else:
    import pkg_resources
    try:
        __version__ = pkg_resources.get_distribution(__name__).version
    except pkg_resources.DistributionNotFound:
        pass