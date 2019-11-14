# Copyright (c) 2016-2019 Adam Karpierz
# Licensed under the zlib/libpng License
# https://opensource.org/licenses/zlib/

__all__ = ('__title__', '__summary__', '__uri__', '__version_info__',
           '__version__', '__author__', '__maintainer__', '__email__',
           '__copyright__', '__license__')

__title__        = "libusb"
__summary__      = "Python binding for the libusb C library (ctypes/cffi-based libusb)."
__uri__          = "https://pypi.org/project/libusb/"
__version_info__ = type("version_info", (), dict(serial=5, # 11312
                        major=1, minor=0, micro=22, releaselevel="beta"))
__version__      = "{0.major}.{0.minor}.{0.micro}{1}{2}".format(__version_info__,
                   dict(final="", alpha="a", beta="b", rc="rc")[__version_info__.releaselevel],
                   "" if __version_info__.releaselevel == "final" else __version_info__.serial)
__author__       = "Adam Karpierz"
__maintainer__   = "Adam Karpierz"
__email__        = "adam@karpierz.net"
__copyright__    = "Copyright (c) 2016-2019, {0}".format(__author__)
__license__      = "zlib/libpng License ; {0}".format(
                   "https://opensource.org/licenses/zlib/")
