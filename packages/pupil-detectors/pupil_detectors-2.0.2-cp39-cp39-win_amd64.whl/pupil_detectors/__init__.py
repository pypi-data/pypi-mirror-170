

""""""# start delvewheel patch
def _delvewheel_init_patch_1_0_1():
    import os
    import sys
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'pupil_detectors.libs'))
    if sys.version_info[:2] >= (3, 8) and not os.path.exists(os.path.join(sys.base_prefix, 'conda-meta')) or sys.version_info[:2] >= (3, 10):
        os.add_dll_directory(libs_dir)
    else:
        from ctypes import WinDLL
        with open(os.path.join(libs_dir, '.load-order-pupil_detectors-2.0.2')) as file:
            load_order = file.read().split()
        for lib in load_order:
            WinDLL(os.path.join(libs_dir, lib))


_delvewheel_init_patch_1_0_1()
del _delvewheel_init_patch_1_0_1
# end delvewheel patch

try:
    from importlib.metadata import PackageNotFoundError, version
except ImportError:
    from importlib_metadata import PackageNotFoundError, version

try:
    __version__ = version("pupil_detectors")
except PackageNotFoundError:
    # package is not installed
    pass

from .detector_2d import Detector2D
from .detector_base import DetectorBase
from .roi import Roi

__all__ = ["__version__", "DetectorBase", "Detector2D", "Roi"]
