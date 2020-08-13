'''Wrapper for vrmusbcam2.h

Generated with:
/usr/bin/ctypesgen.py -llibvrmusbcam2.so -lvrmusbcam2.dll vrmusbcam2.h vrmusbcam2l.h vrmusbcam2props.h -o vrmusbcamapi.py

Do not modify this file.
'''

__docformat__ = 'restructuredtext'

# Begin preamble

import ctypes
import os
import sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64, )
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types


class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]


def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):

        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x

        p.from_param = classmethod(from_param)

    return p


class UserString:
    def __init__(self, seq):
        if isinstance(seq, str):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data)

    def __long__(self):
        return int(self.data)

    def __float__(self):
        return float(self.data)

    def __complex__(self):
        return complex(self.data)

    def __hash__(self):
        return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, str):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))

    def __radd__(self, other):
        if isinstance(other, str):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1:]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1:]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, str):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub) + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, str):
            self.data += other
        else:
            self.data += str(other)
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)), ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.


def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str) and
            type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class


class _variadic_function(object):
    def __init__(self, func, restype, argtypes):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path
import re
import sys
import glob
import platform
import ctypes
import ctypes.util


def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []


class LibraryLoader(object):
    def __init__(self):
        self.other_dirs = []

    def load_library(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self, path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError as e:
            raise ImportError(e)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # FIXME / TODO return '.' and os.path.dirname(__file__)
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path:
                yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                    "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir, name)

    def getdirs(self, libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path(
            "DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")
        dirs.append(os.path.dirname(__file__))

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(
                os.path.join(os.environ['RESOURCEPATH'], '..', 'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix


class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH",  # HPUX
                     "LIBPATH",  # OS/2, AIX
                     "LIBRARY_PATH",  # BE/OS
                     ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")
        directories.append(os.path.dirname(__file__))

        try:
            directories.extend([dir.strip()
                                for dir in open('/etc/ld.so.conf')])
        except IOError:
            pass

        unix_lib_dirs_list = ['/lib', '/usr/lib', '/lib64', '/usr/lib64']
        if sys.platform.startswith('linux'):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            bitage = platform.architecture()[0]
            if bitage.startswith('32'):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ['/lib/i386-linux-gnu',
                                       '/usr/lib/i386-linux-gnu']
            elif bitage.startswith('64'):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ['/lib/x86_64-linux-gnu',
                                       '/usr/lib/x86_64-linux-gnu']
            else:
                # guess...
                unix_lib_dirs_list += glob.glob('/lib/*linux-gnu')
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result:
            yield result

        path = ctypes.util.find_library(libname)
        if path:
            yield os.path.join("/lib", path)

# Windows


class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try:
            return getattr(self.cdll, name)
        except AttributeError:
            try:
                return getattr(self.windll, name)
            except AttributeError:
                raise


class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs


load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries

# _libs["libvrmusbcam2.so"] = load_library("libvrmusbcam2.so")
_libs["libvrmusbcam2.so"] = load_library("vrmusbcam2.dll")

# 2 libraries
# End libraries

# No modules

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 46
VRmBYTE = c_ubyte

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 47
VRmWORD = c_uint

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 48
VRmDWORD = c_uint

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 49
VRmBOOL = c_uint

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 50
VRmSTRING = String

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 56


class struct__VRmSizeI(Structure):
    pass


struct__VRmSizeI.__slots__ = [
    'm_width',
    'm_height',
]
struct__VRmSizeI._fields_ = [
    ('m_width', c_int),
    ('m_height', c_int),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 56
VRmSizeI = struct__VRmSizeI

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 62


class struct__VRmPointI(Structure):
    pass


struct__VRmPointI.__slots__ = [
    'm_x',
    'm_y',
]
struct__VRmPointI._fields_ = [
    ('m_x', c_int),
    ('m_y', c_int),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 62
VRmPointI = struct__VRmPointI

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 70


class struct__VRmRectI(Structure):
    pass


struct__VRmRectI.__slots__ = [
    'm_left',
    'm_top',
    'm_width',
    'm_height',
]
struct__VRmRectI._fields_ = [
    ('m_left', c_int),
    ('m_top', c_int),
    ('m_width', c_int),
    ('m_height', c_int),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 70
VRmRectI = struct__VRmRectI

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 85
enum__VRmRetVal = c_int

VRM_FAILED = 0  # /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 85

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 85
VRM_SUCCESS = 1

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 85
VRmRetVal = enum__VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 102
enum__VRmErrorCode = c_int

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 102
VRM_ERROR_CODE_SUCCESS = 0

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 102
VRM_ERROR_CODE_FUNCTION_CALL_TIMEOUT = 262147

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 102
VRM_ERROR_CODE_GENERIC_ERROR = 2147500037

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 102
VRM_ERROR_CODE_TRIGGER_TIMEOUT = 2147745793

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 102
VRM_ERROR_CODE_TRIGGER_STALL = 2147745794

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 102
VRM_ERROR_CODE_TRANSFER_TIMEOUT = 2147745796

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 102
VRmErrorCode = enum__VRmErrorCode

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 109
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetLastError'):
    VRmUsbCamGetLastError = _libs['libvrmusbcam2.so'].VRmUsbCamGetLastError
    VRmUsbCamGetLastError.argtypes = []
    VRmUsbCamGetLastError.restype = VRmSTRING

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 115
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetLastErrorCode'):
    VRmUsbCamGetLastErrorCode = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetLastErrorCode
    VRmUsbCamGetLastErrorCode.argtypes = []
    VRmUsbCamGetLastErrorCode.restype = c_int

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 118
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamClearLastError'):
    VRmUsbCamClearLastError = _libs['libvrmusbcam2.so'].VRmUsbCamClearLastError
    VRmUsbCamClearLastError.argtypes = []
    VRmUsbCamClearLastError.restype = None

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 123
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamLastErrorWasTriggerTimeout'):
    VRmUsbCamLastErrorWasTriggerTimeout = _libs[
        'libvrmusbcam2.so'].VRmUsbCamLastErrorWasTriggerTimeout
    VRmUsbCamLastErrorWasTriggerTimeout.argtypes = []
    VRmUsbCamLastErrorWasTriggerTimeout.restype = VRmBOOL

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 128
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamLastErrorWasTriggerStall'):
    VRmUsbCamLastErrorWasTriggerStall = _libs[
        'libvrmusbcam2.so'].VRmUsbCamLastErrorWasTriggerStall
    VRmUsbCamLastErrorWasTriggerStall.argtypes = []
    VRmUsbCamLastErrorWasTriggerStall.restype = VRmBOOL

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 144
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamEnableLogging'):
    VRmUsbCamEnableLogging = _libs['libvrmusbcam2.so'].VRmUsbCamEnableLogging
    VRmUsbCamEnableLogging.argtypes = []
    VRmUsbCamEnableLogging.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 161
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamEnableLoggingEx'):
    VRmUsbCamEnableLoggingEx = _libs[
        'libvrmusbcam2.so'].VRmUsbCamEnableLoggingEx
    VRmUsbCamEnableLoggingEx.argtypes = [VRmSTRING]
    VRmUsbCamEnableLoggingEx.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 166
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetVersion'):
    VRmUsbCamGetVersion = _libs['libvrmusbcam2.so'].VRmUsbCamGetVersion
    VRmUsbCamGetVersion.argtypes = [POINTER(VRmDWORD)]
    VRmUsbCamGetVersion.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 176
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamCleanup'):
    VRmUsbCamCleanup = _libs['libvrmusbcam2.so'].VRmUsbCamCleanup
    VRmUsbCamCleanup.argtypes = []
    VRmUsbCamCleanup.restype = None

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 189


class struct_VRmUsbCamDeviceInternal(Structure):
    pass

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 189
VRmUsbCamDevice = POINTER(struct_VRmUsbCamDeviceInternal)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 209


class struct__VRmDeviceKey(Structure):
    pass


struct__VRmDeviceKey.__slots__ = [
    'm_serial',
    'mp_manufacturer_str',
    'mp_product_str',
    'm_busy',
    'mp_private',
]
struct__VRmDeviceKey._fields_ = [
    ('m_serial', VRmDWORD),
    ('mp_manufacturer_str', VRmSTRING),
    ('mp_product_str', VRmSTRING),
    ('m_busy', VRmBOOL),
    ('mp_private', POINTER(None)),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 209
VRmDeviceKey = struct__VRmDeviceKey

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 215
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamUpdateDeviceKeyList'):
    VRmUsbCamUpdateDeviceKeyList = _libs[
        'libvrmusbcam2.so'].VRmUsbCamUpdateDeviceKeyList
    VRmUsbCamUpdateDeviceKeyList.argtypes = []
    VRmUsbCamUpdateDeviceKeyList.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 225
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamUpdateDeviceKeyListEx'):
    VRmUsbCamUpdateDeviceKeyListEx = _libs[
        'libvrmusbcam2.so'].VRmUsbCamUpdateDeviceKeyListEx
    VRmUsbCamUpdateDeviceKeyListEx.argtypes = [VRmBOOL, VRmBOOL, VRmBOOL]
    VRmUsbCamUpdateDeviceKeyListEx.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 229
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamResetDeviceKeyList'):
    VRmUsbCamResetDeviceKeyList = _libs[
        'libvrmusbcam2.so'].VRmUsbCamResetDeviceKeyList
    VRmUsbCamResetDeviceKeyList.argtypes = []
    VRmUsbCamResetDeviceKeyList.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 232
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetDeviceKeyListSize'):
    VRmUsbCamGetDeviceKeyListSize = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetDeviceKeyListSize
    VRmUsbCamGetDeviceKeyListSize.argtypes = [POINTER(VRmDWORD)]
    VRmUsbCamGetDeviceKeyListSize.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 237
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetDeviceKeyListEntry'):
    VRmUsbCamGetDeviceKeyListEntry = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetDeviceKeyListEntry
    VRmUsbCamGetDeviceKeyListEntry.argtypes = [
        VRmDWORD, POINTER(POINTER(VRmDeviceKey))
    ]
    VRmUsbCamGetDeviceKeyListEntry.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 240
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetVendorId'):
    VRmUsbCamGetVendorId = _libs['libvrmusbcam2.so'].VRmUsbCamGetVendorId
    VRmUsbCamGetVendorId.argtypes = [POINTER(VRmDeviceKey), POINTER(VRmWORD)]
    VRmUsbCamGetVendorId.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 243
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetProductId'):
    VRmUsbCamGetProductId = _libs['libvrmusbcam2.so'].VRmUsbCamGetProductId
    VRmUsbCamGetProductId.argtypes = [POINTER(VRmDeviceKey), POINTER(VRmWORD)]
    VRmUsbCamGetProductId.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 246
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetGroupId'):
    VRmUsbCamGetGroupId = _libs['libvrmusbcam2.so'].VRmUsbCamGetGroupId
    VRmUsbCamGetGroupId.argtypes = [POINTER(VRmDeviceKey), POINTER(VRmWORD)]
    VRmUsbCamGetGroupId.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 250
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetSerialString'):
    VRmUsbCamGetSerialString = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetSerialString
    VRmUsbCamGetSerialString.argtypes = [
        POINTER(VRmDeviceKey), POINTER(VRmSTRING)
    ]
    VRmUsbCamGetSerialString.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 254
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetIpAddress'):
    VRmUsbCamGetIpAddress = _libs['libvrmusbcam2.so'].VRmUsbCamGetIpAddress
    VRmUsbCamGetIpAddress.argtypes = [
        POINTER(VRmDeviceKey), POINTER(VRmSTRING)
    ]
    VRmUsbCamGetIpAddress.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 259
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetLocalIpAddress'):
    VRmUsbCamGetLocalIpAddress = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetLocalIpAddress
    VRmUsbCamGetLocalIpAddress.argtypes = [
        POINTER(VRmDeviceKey), POINTER(VRmSTRING)
    ]
    VRmUsbCamGetLocalIpAddress.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 263
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamCompareDeviceKeys'):
    VRmUsbCamCompareDeviceKeys = _libs[
        'libvrmusbcam2.so'].VRmUsbCamCompareDeviceKeys
    VRmUsbCamCompareDeviceKeys.argtypes = [
        POINTER(VRmDeviceKey), POINTER(VRmDeviceKey), POINTER(VRmBOOL)
    ]
    VRmUsbCamCompareDeviceKeys.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 266
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamFreeDeviceKey'):
    VRmUsbCamFreeDeviceKey = _libs['libvrmusbcam2.so'].VRmUsbCamFreeDeviceKey
    VRmUsbCamFreeDeviceKey.argtypes = [POINTER(POINTER(VRmDeviceKey))]
    VRmUsbCamFreeDeviceKey.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 271
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamOpenDevice'):
    VRmUsbCamOpenDevice = _libs['libvrmusbcam2.so'].VRmUsbCamOpenDevice
    VRmUsbCamOpenDevice.argtypes = [
        POINTER(VRmDeviceKey), POINTER(VRmUsbCamDevice)
    ]
    VRmUsbCamOpenDevice.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 275
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetDeviceKey'):
    VRmUsbCamGetDeviceKey = _libs['libvrmusbcam2.so'].VRmUsbCamGetDeviceKey
    VRmUsbCamGetDeviceKey.argtypes = [
        VRmUsbCamDevice, POINTER(POINTER(VRmDeviceKey))
    ]
    VRmUsbCamGetDeviceKey.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 278
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamCloseDevice'):
    VRmUsbCamCloseDevice = _libs['libvrmusbcam2.so'].VRmUsbCamCloseDevice
    VRmUsbCamCloseDevice.argtypes = [VRmUsbCamDevice]
    VRmUsbCamCloseDevice.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 296


class struct__VRmUserData(Structure):
    pass


struct__VRmUserData.__slots__ = [
    'm_length',
    'mp_data',
    'mp_private',
]
struct__VRmUserData._fields_ = [
    ('m_length', VRmDWORD),
    ('mp_data', POINTER(VRmBYTE)),
    ('mp_private', POINTER(None)),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 296
VRmUserData = struct__VRmUserData

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 301
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamLoadUserData'):
    VRmUsbCamLoadUserData = _libs['libvrmusbcam2.so'].VRmUsbCamLoadUserData
    VRmUsbCamLoadUserData.argtypes = [
        VRmUsbCamDevice, POINTER(POINTER(VRmUserData))
    ]
    VRmUsbCamLoadUserData.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 306
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSaveUserData'):
    VRmUsbCamSaveUserData = _libs['libvrmusbcam2.so'].VRmUsbCamSaveUserData
    VRmUsbCamSaveUserData.argtypes = [VRmUsbCamDevice, POINTER(VRmUserData)]
    VRmUsbCamSaveUserData.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 310
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamNewUserData'):
    VRmUsbCamNewUserData = _libs['libvrmusbcam2.so'].VRmUsbCamNewUserData
    VRmUsbCamNewUserData.argtypes = [POINTER(POINTER(VRmUserData)), VRmDWORD]
    VRmUsbCamNewUserData.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 313
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamFreeUserData'):
    VRmUsbCamFreeUserData = _libs['libvrmusbcam2.so'].VRmUsbCamFreeUserData
    VRmUsbCamFreeUserData.argtypes = [POINTER(POINTER(VRmUserData))]
    VRmUsbCamFreeUserData.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 322
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamRestartTimer'):
    VRmUsbCamRestartTimer = _libs['libvrmusbcam2.so'].VRmUsbCamRestartTimer
    VRmUsbCamRestartTimer.argtypes = []
    VRmUsbCamRestartTimer.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 325
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetCurrentTime'):
    VRmUsbCamGetCurrentTime = _libs['libvrmusbcam2.so'].VRmUsbCamGetCurrentTime
    VRmUsbCamGetCurrentTime.argtypes = [POINTER(c_double)]
    VRmUsbCamGetCurrentTime.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 378
enum__VRmColorFormat = c_int

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 378
VRM_ARGB_4X8 = 0

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 378
VRM_BGR_3X8 = (VRM_ARGB_4X8 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 378
VRM_RGB_565 = (VRM_BGR_3X8 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 378
VRM_YUYV_4X8 = (VRM_RGB_565 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 378
VRM_GRAY_8 = (VRM_YUYV_4X8 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 378
VRM_BAYER_GBRG_8 = (VRM_GRAY_8 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 378
VRM_BAYER_BGGR_8 = (VRM_BAYER_GBRG_8 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 378
VRM_BAYER_RGGB_8 = (VRM_BAYER_BGGR_8 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 378
VRM_BAYER_GRBG_8 = (VRM_BAYER_RGGB_8 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 378
VRM_GRAY_10 = (VRM_BAYER_GRBG_8 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 378
VRM_BAYER_GBRG_10 = (VRM_GRAY_10 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 378
VRM_BAYER_BGGR_10 = (VRM_BAYER_GBRG_10 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 378
VRM_BAYER_RGGB_10 = (VRM_BAYER_BGGR_10 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 378
VRM_BAYER_GRBG_10 = (VRM_BAYER_RGGB_10 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 378
VRM_GRAY_16 = (VRM_BAYER_GRBG_10 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 378
VRM_BGR_3X16 = (VRM_GRAY_16 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 378
VRM_BAYER_GBRG_16 = (VRM_BGR_3X16 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 378
VRM_BAYER_BGGR_16 = (VRM_BAYER_GBRG_16 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 378
VRM_BAYER_RGGB_16 = (VRM_BAYER_BGGR_16 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 378
VRM_BAYER_GRBG_16 = (VRM_BAYER_RGGB_16 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 378
VRM_UYVY_4X8 = (VRM_BAYER_GRBG_16 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 378
VRmColorFormat = enum__VRmColorFormat

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 426
enum__VRmImageModifier = c_int

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 426
VRM_STANDARD = 0

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 426
VRM_VERTICAL_MIRRORED = (1 << 0)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 426
VRM_HORIZONTAL_MIRRORED = (1 << 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 426
VRM_INTERLACED_FIELD0 = (1 << 2)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 426
VRM_INTERLACED_FIELD1 = (1 << 3)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 426
VRM_INTERLACED_FIELD01 = (1 << 4)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 426
VRM_INTERLACED_FRAME = (1 << 5)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 426
VRM_CORRECTION_LUT_1CHANNEL_8 = (1 << 6)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 426
VRM_CORRECTION_LUT_1CHANNEL_10 = (1 << 7)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 426
VRM_CORRECTION_LUT_4CHANNEL_8 = (1 << 8)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 426
VRM_CORRECTION_LUT_4CHANNEL_10 = (1 << 9)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 426
VRM_USER_ROI = (1 << 10)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 426
VRM_SUBSAMPLED = (1 << 11)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 426
VRM_RUN_LENGTH_ENCODED = (1 << 12)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 426
VRM_ALAW_COMPRESSED = (1 << 13)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 426
VRM_ORDER_TFF = (1 << 14)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 426
VRM_ORDER_BFF = (1 << 15)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 426
VRM_CORRECTION_LUT_1CHANNEL_16 = (1 << 16)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 426
VRmImageModifier = enum__VRmImageModifier

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 439


class struct__VRmImageFormat(Structure):
    pass


struct__VRmImageFormat.__slots__ = [
    'm_width',
    'm_height',
    'm_color_format',
    'm_image_modifier',
]
struct__VRmImageFormat._fields_ = [
    ('m_width', VRmDWORD),
    ('m_height', VRmDWORD),
    ('m_color_format', VRmColorFormat),
    ('m_image_modifier', c_int),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 439
VRmImageFormat = struct__VRmImageFormat

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 454


class struct__VRmImage(Structure):
    pass


struct__VRmImage.__slots__ = [
    'm_image_format',
    'mp_buffer',
    'm_pitch',
    'm_time_stamp',
    'mp_private',
]
struct__VRmImage._fields_ = [
    ('m_image_format', VRmImageFormat),
    ('mp_buffer', POINTER(VRmBYTE)),
    ('m_pitch', VRmDWORD),
    ('m_time_stamp', c_double),
    ('mp_private', POINTER(None)),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 454
VRmImage = struct__VRmImage

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 458
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamNewImage'):
    VRmUsbCamNewImage = _libs['libvrmusbcam2.so'].VRmUsbCamNewImage
    VRmUsbCamNewImage.argtypes = [POINTER(POINTER(VRmImage)), VRmImageFormat]
    VRmUsbCamNewImage.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 462
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamCopyImage'):
    VRmUsbCamCopyImage = _libs['libvrmusbcam2.so'].VRmUsbCamCopyImage
    VRmUsbCamCopyImage.argtypes = [
        POINTER(POINTER(VRmImage)), POINTER(VRmImage)
    ]
    VRmUsbCamCopyImage.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 467
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamCropImage'):
    VRmUsbCamCropImage = _libs['libvrmusbcam2.so'].VRmUsbCamCropImage
    VRmUsbCamCropImage.argtypes = [
        POINTER(POINTER(VRmImage)), POINTER(VRmImage), POINTER(VRmRectI)
    ]
    VRmUsbCamCropImage.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 471
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetImage'):
    VRmUsbCamSetImage = _libs['libvrmusbcam2.so'].VRmUsbCamSetImage
    VRmUsbCamSetImage.argtypes = [
        POINTER(POINTER(VRmImage)), VRmImageFormat, POINTER(VRmBYTE), VRmDWORD
    ]
    VRmUsbCamSetImage.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 476
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetImageEx'):
    VRmUsbCamSetImageEx = _libs['libvrmusbcam2.so'].VRmUsbCamSetImageEx
    VRmUsbCamSetImageEx.argtypes = [POINTER(POINTER(VRmImage)), VRmImageFormat,
                                    POINTER(VRmBYTE), VRmDWORD, VRmDWORD]
    VRmUsbCamSetImageEx.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 479
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetFrameCounter'):
    VRmUsbCamGetFrameCounter = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetFrameCounter
    VRmUsbCamGetFrameCounter.argtypes = [POINTER(VRmImage), POINTER(VRmDWORD)]
    VRmUsbCamGetFrameCounter.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 483
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetImageFooter'):
    VRmUsbCamGetImageFooter = _libs['libvrmusbcam2.so'].VRmUsbCamGetImageFooter
    VRmUsbCamGetImageFooter.argtypes = [
        POINTER(VRmImage), POINTER(POINTER(None)), POINTER(VRmDWORD)
    ]
    VRmUsbCamGetImageFooter.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 486
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetImageBufferSize'):
    VRmUsbCamGetImageBufferSize = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetImageBufferSize
    VRmUsbCamGetImageBufferSize.argtypes = [
        POINTER(VRmImage), POINTER(VRmDWORD)
    ]
    VRmUsbCamGetImageBufferSize.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 495
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetImageBufferSize'):
    VRmUsbCamSetImageBufferSize = _libs[
        'libvrmusbcam2.so'].VRmUsbCamSetImageBufferSize
    VRmUsbCamSetImageBufferSize.argtypes = [POINTER(VRmImage), VRmDWORD]
    VRmUsbCamSetImageBufferSize.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 498
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetImageSensorPort'):
    VRmUsbCamGetImageSensorPort = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetImageSensorPort
    VRmUsbCamGetImageSensorPort.argtypes = [
        POINTER(VRmImage), POINTER(VRmDWORD)
    ]
    VRmUsbCamGetImageSensorPort.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 501
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamFreeImage'):
    VRmUsbCamFreeImage = _libs['libvrmusbcam2.so'].VRmUsbCamFreeImage
    VRmUsbCamFreeImage.argtypes = [POINTER(POINTER(VRmImage))]
    VRmUsbCamFreeImage.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 504
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetTargetFormatListSize'):
    VRmUsbCamGetTargetFormatListSize = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetTargetFormatListSize
    VRmUsbCamGetTargetFormatListSize.argtypes = [
        POINTER(VRmImageFormat), POINTER(VRmDWORD)
    ]
    VRmUsbCamGetTargetFormatListSize.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 507
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetTargetFormatListEntry'):
    VRmUsbCamGetTargetFormatListEntry = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetTargetFormatListEntry
    VRmUsbCamGetTargetFormatListEntry.argtypes = [
        POINTER(VRmImageFormat), VRmDWORD, POINTER(VRmImageFormat)
    ]
    VRmUsbCamGetTargetFormatListEntry.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 515
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamConvertImage'):
    VRmUsbCamConvertImage = _libs['libvrmusbcam2.so'].VRmUsbCamConvertImage
    VRmUsbCamConvertImage.argtypes = [POINTER(VRmImage), POINTER(VRmImage)]
    VRmUsbCamConvertImage.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 518
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetStringFromColorFormat'):
    VRmUsbCamGetStringFromColorFormat = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetStringFromColorFormat
    VRmUsbCamGetStringFromColorFormat.argtypes = [
        VRmColorFormat, POINTER(VRmSTRING)
    ]
    VRmUsbCamGetStringFromColorFormat.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 521
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetPixelDepthFromColorFormat'):
    VRmUsbCamGetPixelDepthFromColorFormat = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetPixelDepthFromColorFormat
    VRmUsbCamGetPixelDepthFromColorFormat.argtypes = [
        VRmColorFormat, POINTER(VRmDWORD)
    ]
    VRmUsbCamGetPixelDepthFromColorFormat.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 525
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamCompareImageFormats'):
    VRmUsbCamCompareImageFormats = _libs[
        'libvrmusbcam2.so'].VRmUsbCamCompareImageFormats
    VRmUsbCamCompareImageFormats.argtypes = [
        POINTER(VRmImageFormat), POINTER(VRmImageFormat), POINTER(VRmBOOL)
    ]
    VRmUsbCamCompareImageFormats.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 528
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetImageLut'):
    VRmUsbCamGetImageLut = _libs['libvrmusbcam2.so'].VRmUsbCamGetImageLut
    VRmUsbCamGetImageLut.argtypes = [
        POINTER(VRmImage), POINTER(POINTER(VRmBYTE)), POINTER(VRmDWORD)
    ]
    VRmUsbCamGetImageLut.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 541
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetSensorPortListSize'):
    VRmUsbCamGetSensorPortListSize = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetSensorPortListSize
    VRmUsbCamGetSensorPortListSize.argtypes = [
        VRmUsbCamDevice, POINTER(VRmDWORD)
    ]
    VRmUsbCamGetSensorPortListSize.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 544
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetSensorPortListEntry'):
    VRmUsbCamGetSensorPortListEntry = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetSensorPortListEntry
    VRmUsbCamGetSensorPortListEntry.argtypes = [
        VRmUsbCamDevice, VRmDWORD, POINTER(VRmDWORD)
    ]
    VRmUsbCamGetSensorPortListEntry.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 548
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetSourceFormatEx'):
    VRmUsbCamGetSourceFormatEx = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetSourceFormatEx
    VRmUsbCamGetSourceFormatEx.argtypes = [
        VRmUsbCamDevice, VRmDWORD, POINTER(VRmImageFormat)
    ]
    VRmUsbCamGetSourceFormatEx.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 552
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetSourceFormatDescription'):
    VRmUsbCamGetSourceFormatDescription = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetSourceFormatDescription
    VRmUsbCamGetSourceFormatDescription.argtypes = [
        VRmUsbCamDevice, VRmDWORD, POINTER(VRmSTRING)
    ]
    VRmUsbCamGetSourceFormatDescription.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 555
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamFindSensorPortListIndex'):
    VRmUsbCamFindSensorPortListIndex = _libs[
        'libvrmusbcam2.so'].VRmUsbCamFindSensorPortListIndex
    VRmUsbCamFindSensorPortListIndex.argtypes = [
        VRmUsbCamDevice, VRmDWORD, POINTER(VRmDWORD)
    ]
    VRmUsbCamFindSensorPortListIndex.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 559
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetTargetFormatListSizeEx2'):
    VRmUsbCamGetTargetFormatListSizeEx2 = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetTargetFormatListSizeEx2
    VRmUsbCamGetTargetFormatListSizeEx2.argtypes = [
        VRmUsbCamDevice, VRmDWORD, POINTER(VRmDWORD)
    ]
    VRmUsbCamGetTargetFormatListSizeEx2.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 562
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetTargetFormatListEntryEx2'):
    VRmUsbCamGetTargetFormatListEntryEx2 = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetTargetFormatListEntryEx2
    VRmUsbCamGetTargetFormatListEntryEx2.argtypes = [
        VRmUsbCamDevice, VRmDWORD, VRmDWORD, POINTER(VRmImageFormat)
    ]
    VRmUsbCamGetTargetFormatListEntryEx2.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 566
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamStart'):
    VRmUsbCamStart = _libs['libvrmusbcam2.so'].VRmUsbCamStart
    VRmUsbCamStart.argtypes = [VRmUsbCamDevice]
    VRmUsbCamStart.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 570
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamStop'):
    VRmUsbCamStop = _libs['libvrmusbcam2.so'].VRmUsbCamStop
    VRmUsbCamStop.argtypes = [VRmUsbCamDevice]
    VRmUsbCamStop.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 573
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetRunning'):
    VRmUsbCamGetRunning = _libs['libvrmusbcam2.so'].VRmUsbCamGetRunning
    VRmUsbCamGetRunning.argtypes = [VRmUsbCamDevice, POINTER(VRmBOOL)]
    VRmUsbCamGetRunning.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 576
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamResetFrameCounter'):
    VRmUsbCamResetFrameCounter = _libs[
        'libvrmusbcam2.so'].VRmUsbCamResetFrameCounter
    VRmUsbCamResetFrameCounter.argtypes = [VRmUsbCamDevice]
    VRmUsbCamResetFrameCounter.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 583
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamIsNextImageReadyEx'):
    VRmUsbCamIsNextImageReadyEx = _libs[
        'libvrmusbcam2.so'].VRmUsbCamIsNextImageReadyEx
    VRmUsbCamIsNextImageReadyEx.argtypes = [
        VRmUsbCamDevice, VRmDWORD, POINTER(VRmBOOL)
    ]
    VRmUsbCamIsNextImageReadyEx.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 592
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamLockNextImageEx2'):
    VRmUsbCamLockNextImageEx2 = _libs[
        'libvrmusbcam2.so'].VRmUsbCamLockNextImageEx2
    VRmUsbCamLockNextImageEx2.argtypes = [VRmUsbCamDevice, VRmDWORD,
                                          POINTER(POINTER(VRmImage)),
                                          POINTER(VRmDWORD), c_int]
    VRmUsbCamLockNextImageEx2.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 597
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamLockNextImageEx'):
    VRmUsbCamLockNextImageEx = _libs[
        'libvrmusbcam2.so'].VRmUsbCamLockNextImageEx
    VRmUsbCamLockNextImageEx.argtypes = [
        VRmUsbCamDevice, VRmDWORD, POINTER(POINTER(VRmImage)),
        POINTER(VRmDWORD)
    ]
    VRmUsbCamLockNextImageEx.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 605
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamUnlockNextImage'):
    VRmUsbCamUnlockNextImage = _libs[
        'libvrmusbcam2.so'].VRmUsbCamUnlockNextImage
    VRmUsbCamUnlockNextImage.argtypes = [
        VRmUsbCamDevice, POINTER(POINTER(VRmImage))
    ]
    VRmUsbCamUnlockNextImage.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 610
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSoftTrigger'):
    VRmUsbCamSoftTrigger = _libs['libvrmusbcam2.so'].VRmUsbCamSoftTrigger
    VRmUsbCamSoftTrigger.argtypes = [VRmUsbCamDevice]
    VRmUsbCamSoftTrigger.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 614
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetDeviceLut'):
    VRmUsbCamGetDeviceLut = _libs['libvrmusbcam2.so'].VRmUsbCamGetDeviceLut
    VRmUsbCamGetDeviceLut.argtypes = [VRmUsbCamDevice, VRmDWORD,
                                      POINTER(POINTER(VRmBYTE)),
                                      POINTER(VRmDWORD), POINTER(VRmDWORD)]
    VRmUsbCamGetDeviceLut.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 630
enum__VRmUserLutFormat = c_int

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 630
VRM_USER_LUT_NONE = 0

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 630
VRM_USER_LUT_8_TO_16 = (VRM_USER_LUT_NONE + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 630
VRM_USER_LUT_10_TO_16 = (VRM_USER_LUT_8_TO_16 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 630
VRM_USER_LUT_16_TO_16 = (VRM_USER_LUT_10_TO_16 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 630
VRM_USER_LUT_END = (VRM_USER_LUT_16_TO_16 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 630
VRmUserLutFormat = enum__VRmUserLutFormat

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 640
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetUserLut'):
    VRmUsbCamGetUserLut = _libs['libvrmusbcam2.so'].VRmUsbCamGetUserLut
    VRmUsbCamGetUserLut.argtypes = [
        VRmUsbCamDevice, VRmDWORD, VRmDWORD, VRmUserLutFormat,
        POINTER(POINTER(VRmWORD))
    ]
    VRmUsbCamGetUserLut.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 646
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamFreeUserLut'):
    VRmUsbCamFreeUserLut = _libs['libvrmusbcam2.so'].VRmUsbCamFreeUserLut
    VRmUsbCamFreeUserLut.argtypes = [POINTER(POINTER(VRmWORD))]
    VRmUsbCamFreeUserLut.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 656
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetUserLut'):
    VRmUsbCamSetUserLut = _libs['libvrmusbcam2.so'].VRmUsbCamSetUserLut
    VRmUsbCamSetUserLut.argtypes = [
        VRmUsbCamDevice, VRmDWORD, VRmDWORD, VRmUserLutFormat, POINTER(VRmWORD)
    ]
    VRmUsbCamSetUserLut.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 664
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamUserLutCommit'):
    VRmUsbCamUserLutCommit = _libs['libvrmusbcam2.so'].VRmUsbCamUserLutCommit
    VRmUsbCamUserLutCommit.argtypes = [VRmUsbCamDevice, VRmDWORD]
    VRmUsbCamUserLutCommit.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 674
enum__VRmEventReturnType = c_int

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 674
VRM_EVENT_ERROR = 0

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 674
VRM_EVENT_TIMEOUT = 1

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 674
VRM_EVENT_SUCCESS = 2

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 674
VRmEventReturnType = enum__VRmEventReturnType

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 676
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamWaitForStrobe'):
    VRmUsbCamWaitForStrobe = _libs['libvrmusbcam2.so'].VRmUsbCamWaitForStrobe
    VRmUsbCamWaitForStrobe.argtypes = [
        VRmUsbCamDevice, c_int, POINTER(VRmEventReturnType)
    ]
    VRmUsbCamWaitForStrobe.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 692
VRmUsbCamConfigID = c_uint

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 696
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamLoadConfig'):
    VRmUsbCamLoadConfig = _libs['libvrmusbcam2.so'].VRmUsbCamLoadConfig
    VRmUsbCamLoadConfig.argtypes = [VRmUsbCamDevice, VRmUsbCamConfigID]
    VRmUsbCamLoadConfig.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 701
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSaveConfig'):
    VRmUsbCamSaveConfig = _libs['libvrmusbcam2.so'].VRmUsbCamSaveConfig
    VRmUsbCamSaveConfig.argtypes = [VRmUsbCamDevice, VRmUsbCamConfigID]
    VRmUsbCamSaveConfig.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 704
if hasattr(_libs['libvrmusbcam2.so'],
           'VRmUsbCamSaveConfigRequiresFirmwareCompression'):
    VRmUsbCamSaveConfigRequiresFirmwareCompression = _libs[
        'libvrmusbcam2.so'].VRmUsbCamSaveConfigRequiresFirmwareCompression
    VRmUsbCamSaveConfigRequiresFirmwareCompression.argtypes = [
        VRmUsbCamDevice, VRmUsbCamConfigID, POINTER(VRmBOOL)
    ]
    VRmUsbCamSaveConfigRequiresFirmwareCompression.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 707
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamDeleteConfig'):
    VRmUsbCamDeleteConfig = _libs['libvrmusbcam2.so'].VRmUsbCamDeleteConfig
    VRmUsbCamDeleteConfig.argtypes = [VRmUsbCamDevice, VRmUsbCamConfigID]
    VRmUsbCamDeleteConfig.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 711
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetConfigData'):
    VRmUsbCamGetConfigData = _libs['libvrmusbcam2.so'].VRmUsbCamGetConfigData
    VRmUsbCamGetConfigData.argtypes = [
        VRmUsbCamDevice, POINTER(POINTER(VRmUserData))
    ]
    VRmUsbCamGetConfigData.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 715
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetConfigData'):
    VRmUsbCamSetConfigData = _libs['libvrmusbcam2.so'].VRmUsbCamSetConfigData
    VRmUsbCamSetConfigData.argtypes = [VRmUsbCamDevice, POINTER(VRmUserData)]
    VRmUsbCamSetConfigData.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 720
if hasattr(_libs['libvrmusbcam2.so'],
           'VRmUsbCamConfigIncludesUnsupportedValues'):
    VRmUsbCamConfigIncludesUnsupportedValues = _libs[
        'libvrmusbcam2.so'].VRmUsbCamConfigIncludesUnsupportedValues
    VRmUsbCamConfigIncludesUnsupportedValues.argtypes = [
        VRmUsbCamDevice, POINTER(VRmBOOL)
    ]
    VRmUsbCamConfigIncludesUnsupportedValues.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
enum__VRmPropId = c_int

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_EXPOSURE_TIME_F = 4097

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_AUTO_EXPOSURE_B = 4099

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_AUTO_EXPOSURE_MAX_F = (VRM_PROPID_CAM_AUTO_EXPOSURE_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_SIGNAL_SOURCE_E = 4105

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_SIGNAL_SOURCE_UNKNOWN = 269025280

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_SIGNAL_SOURCE_SVIDEO = (
    VRM_PROPID_CAM_SIGNAL_SOURCE_UNKNOWN + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_SIGNAL_SOURCE_COMPOSITE = (
    VRM_PROPID_CAM_SIGNAL_SOURCE_SVIDEO + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_SIGNAL_SOURCE_YC = (VRM_PROPID_CAM_SIGNAL_SOURCE_COMPOSITE + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_FRAMERATE_MAX_F = 4106

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_EXPOSURE_TIME1_F = (VRM_PROPID_CAM_FRAMERATE_MAX_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_EXPOSURE_OFFSET0_ODD_LINE_F = 4108

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_EXPOSURE_OFFSET1_ODD_LINE_F = (
    VRM_PROPID_CAM_EXPOSURE_OFFSET0_ODD_LINE_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_ACQUISITION_RATE_MAX_F = 4110

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_AUTO_EXPOSURE_TARGET_LUMA_I = 4111

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_HBLANK_DURATION_I = 4112

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_VBLANK_DURATION_I = (VRM_PROPID_CAM_HBLANK_DURATION_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_TRG2EXP_TIME_F = (VRM_PROPID_CAM_VBLANK_DURATION_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_EXP2VS_TIME_F = 4116

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_ROW_TIME_F = (VRM_PROPID_CAM_EXP2VS_TIME_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_GAIN_RED_I = 4128

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_GAIN_GREEN_I = (VRM_PROPID_CAM_GAIN_RED_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_GAIN_BLUE_I = (VRM_PROPID_CAM_GAIN_GREEN_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_GAIN_MONOCHROME_I = (VRM_PROPID_CAM_GAIN_BLUE_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_AUTO_GAIN_B = (VRM_PROPID_CAM_GAIN_MONOCHROME_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_AUTO_GAIN_MAX_I = (VRM_PROPID_CAM_AUTO_GAIN_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_OFFSET_RED_I = (VRM_PROPID_CAM_AUTO_GAIN_MAX_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_OFFSET_GREEN_I = (VRM_PROPID_CAM_OFFSET_RED_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_OFFSET_BLUE_I = (VRM_PROPID_CAM_OFFSET_GREEN_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_BRIGHTNESS_I = (VRM_PROPID_CAM_OFFSET_BLUE_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_CONTRAST_I = (VRM_PROPID_CAM_BRIGHTNESS_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_SATURATION_I = (VRM_PROPID_CAM_CONTRAST_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_HUE_I = (VRM_PROPID_CAM_SATURATION_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_ANTI_BLOOMING_B = 4144

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_ANTI_BLOOMING_VOLTAGE_F = (VRM_PROPID_CAM_ANTI_BLOOMING_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_DARK_OFFSET_B = (VRM_PROPID_CAM_ANTI_BLOOMING_VOLTAGE_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_DARK_OFFSET_VOLTAGE_F = (VRM_PROPID_CAM_DARK_OFFSET_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_SENSOR_SIZE_I = 4160

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_MONOCHROME_MODE_B = 4162

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_GLOBAL_SHUTTER_B = (VRM_PROPID_CAM_MONOCHROME_MODE_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_VIDEO_STANDARD_E = 4164

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_VIDEO_STANDARD_UNKNOWN = 272891904

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_VIDEO_STANDARD_PAL = (VRM_PROPID_CAM_VIDEO_STANDARD_UNKNOWN + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_VIDEO_STANDARD_NTSC = (VRM_PROPID_CAM_VIDEO_STANDARD_PAL + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_DEVICE_TYPE_E = 4165

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_DEVICE_TYPE_CMOS = 272957440

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_DEVICE_TYPE_CCD = (VRM_PROPID_CAM_DEVICE_TYPE_CMOS + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_DEVICE_TYPE_AVC = (VRM_PROPID_CAM_DEVICE_TYPE_CCD + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_READOUT_FLIP_H_B = 4166

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_READOUT_FLIP_V_B = (VRM_PROPID_CAM_READOUT_FLIP_H_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_HIGH_DYNAMIC_MODE_B = 4176

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_HIDYN_KNEE_COUNT_I = (VRM_PROPID_CAM_HIGH_DYNAMIC_MODE_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_HIDYN_AUTO_RATIO_B = (VRM_PROPID_CAM_HIDYN_KNEE_COUNT_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_HIDYN_AUTO_RATIO1_I = (VRM_PROPID_CAM_HIDYN_AUTO_RATIO_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_HIDYN_AUTO_RATIO2_I = (VRM_PROPID_CAM_HIDYN_AUTO_RATIO1_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_HIDYN_AUTO_RATIO3_I = (VRM_PROPID_CAM_HIDYN_AUTO_RATIO2_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_HIDYN_AUTO_RATIO4_I = (VRM_PROPID_CAM_HIDYN_AUTO_RATIO3_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_HIDYN_EXPOSURE_KNEE1_F = (
    VRM_PROPID_CAM_HIDYN_AUTO_RATIO4_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_HIDYN_EXPOSURE_KNEE2_F = (
    VRM_PROPID_CAM_HIDYN_EXPOSURE_KNEE1_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_HIDYN_EXPOSURE_KNEE3_F = (
    VRM_PROPID_CAM_HIDYN_EXPOSURE_KNEE2_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_HIDYN_EXPOSURE_KNEE4_F = (
    VRM_PROPID_CAM_HIDYN_EXPOSURE_KNEE3_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_HIDYN_STEP_VOLTAGE1_F = (
    VRM_PROPID_CAM_HIDYN_EXPOSURE_KNEE4_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_HIDYN_STEP_VOLTAGE2_F = (
    VRM_PROPID_CAM_HIDYN_STEP_VOLTAGE1_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_HIDYN_STEP_VOLTAGE3_F = (
    VRM_PROPID_CAM_HIDYN_STEP_VOLTAGE2_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_HIDYN_STEP_VOLTAGE4_F = (
    VRM_PROPID_CAM_HIDYN_STEP_VOLTAGE3_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_TEMPERATURE_F = 4192

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_HIDYN_STEP_VOLTAGE1_RAW_I = (VRM_PROPID_CAM_TEMPERATURE_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_HIDYN_STEP_VOLTAGE2_RAW_I = (
    VRM_PROPID_CAM_HIDYN_STEP_VOLTAGE1_RAW_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_HIDYN_STEP_VOLTAGE3_RAW_I = (
    VRM_PROPID_CAM_HIDYN_STEP_VOLTAGE2_RAW_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_HIDYN_STEP_VOLTAGE4_RAW_I = (
    VRM_PROPID_CAM_HIDYN_STEP_VOLTAGE3_RAW_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_VREF1_ADJUST_I = 4208

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_AUTO_BLACKLEVEL_B = (VRM_PROPID_CAM_VREF1_ADJUST_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_BLACKLEVEL_ADJUST_I = (VRM_PROPID_CAM_AUTO_BLACKLEVEL_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_VREF1_VOLTAGE_F = 4224

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_VREF2_VOLTAGE_F = (VRM_PROPID_CAM_VREF1_VOLTAGE_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_VREF3_VOLTAGE_F = (VRM_PROPID_CAM_VREF2_VOLTAGE_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_VREF4_VOLTAGE_F = (VRM_PROPID_CAM_VREF3_VOLTAGE_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_VLN1_VOLTAGE_F = 4240

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_VLN2_VOLTAGE_F = (VRM_PROPID_CAM_VLN1_VOLTAGE_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_VLP_VOLTAGE_F = 4256

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_VRST_PIX_VOLTAGE_F = 4272

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_RESET_LEVEL_ADJ_I = 5376

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_PIXEL_BIAS_ADJ_I = (VRM_PROPID_CAM_RESET_LEVEL_ADJ_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_VBLANK_DURATION_PIXELS_I = (VRM_PROPID_CAM_PIXEL_BIAS_ADJ_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_GAIN_DOUBLING_B = 5632

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_AUTO_EXPOSURE_BRIGHT_THRESHOLD_I = 5889

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_AUTO_EXPOSURE_BRIGHT_PERCENTAGE_F = (
    VRM_PROPID_CAM_AUTO_EXPOSURE_BRIGHT_THRESHOLD_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_CMOSIS_EXPOSURE_TIME_ALTERNATING_B = 6656

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_CMOSIS_ADC_GAIN_I = (
    VRM_PROPID_CAM_CMOSIS_EXPOSURE_TIME_ALTERNATING_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_CMOSIS_VRAMP1_I = (VRM_PROPID_CAM_CMOSIS_ADC_GAIN_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_CMOSIS_VRAMP2_I = (VRM_PROPID_CAM_CMOSIS_VRAMP1_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_CMOSIS_TEMP_RAW_I = (VRM_PROPID_CAM_CMOSIS_VRAMP2_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_MSARE1_GAIN_F = 6912

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_MSARE1_REFERENCE_VOLTAGE_F = (VRM_PROPID_CAM_MSARE1_GAIN_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_EMBEDDED_SENSOR_REGISTER_LINES_ENABLE_B = 7168

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_EMBEDDED_AE_STATISTICS_LINES_ENABLE_B = 7169

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_DEVICE_HARDWARE_REVISION_I = 8192

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_DEVICE_FIRMWARE_REVISION_I = (
    VRM_PROPID_DEVICE_HARDWARE_REVISION_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_DEVICE_NV_MEM_TOTAL_I = (VRM_PROPID_DEVICE_FIRMWARE_REVISION_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_DEVICE_NV_MEM_FREE_I = (VRM_PROPID_DEVICE_NV_MEM_TOTAL_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_DEVICE_NV_MEM_FILESYS_FORMAT_B = (
    VRM_PROPID_DEVICE_NV_MEM_FREE_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_DEVICE_FIRMWARE_COMPRESSED_B = (
    VRM_PROPID_DEVICE_NV_MEM_FILESYS_FORMAT_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_DEVICE_USB_HIGH_SPEED_B = (
    VRM_PROPID_DEVICE_FIRMWARE_COMPRESSED_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_DEVICE_USB_STARTUP_HIGH_SPEED_B = (
    VRM_PROPID_DEVICE_USB_HIGH_SPEED_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_DEVICE_STATUS_LED_B = (
    VRM_PROPID_DEVICE_USB_STARTUP_HIGH_SPEED_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_PIXEL_CLOCK_F = 8448

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_REFERENCE_FREQ_ADJ_I = (VRM_PROPID_CAM_PIXEL_CLOCK_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_AUTO_PIXEL_CLOCK_B = (VRM_PROPID_CAM_REFERENCE_FREQ_ADJ_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_ALLOW_OVERCLOCKING_B = (VRM_PROPID_CAM_AUTO_PIXEL_CLOCK_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_ILLUMINATION_INTENSITY_F = 8464

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_TRIGGER_POLARITY_E = 8480

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_TRIGGER_POLARITY_POS_EDGE = 555745280

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_TRIGGER_POLARITY_NEG_EDGE = (
    VRM_PROPID_CAM_TRIGGER_POLARITY_POS_EDGE + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_TRIGGER_POLARITY_POS_LEVEL = (
    VRM_PROPID_CAM_TRIGGER_POLARITY_NEG_EDGE + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_TRIGGER_POLARITY_NEG_LEVEL = (
    VRM_PROPID_CAM_TRIGGER_POLARITY_POS_LEVEL + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_TRIGGER_DELAY_F = 8481

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_INTERNAL_TRIGGER_RATE_F = 8483

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_TRIGGER_BURST_COUNT_I = (
    VRM_PROPID_CAM_INTERNAL_TRIGGER_RATE_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_TRIGGER_EXPOSURE_REDUCTION_I = 8487

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_LAST_EXTERNAL_TRIGGER_TIMESTAMP_D = 8490

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_TRIGGER_MSARE1_RRO_BURST_COUNT_I = 8492

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_TRIGGER_MSARE1_RRO_DELAY_F = (
    VRM_PROPID_CAM_TRIGGER_MSARE1_RRO_BURST_COUNT_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_STROBE_POLARITY_E = 8496

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_STROBE_POLARITY_DISABLED = 556793856

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_STROBE_POLARITY_POS = (
    VRM_PROPID_CAM_STROBE_POLARITY_DISABLED + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_STROBE_POLARITY_NEG = (VRM_PROPID_CAM_STROBE_POLARITY_POS + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_STROBE_DELAY_F = 8497

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_STROBE_WIDTH_F = (VRM_PROPID_CAM_STROBE_DELAY_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_STROBE_ILLUMINATION_B = (VRM_PROPID_CAM_STROBE_WIDTH_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_STROBE_BURST_COUNT_I = (
    VRM_PROPID_CAM_STROBE_ILLUMINATION_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CAM_STROBE_OUT_REDUCTION_I = 8505

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_SOURCE_FORMAT_E = 12288

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_SOURCE_FORMAT_8BIT_RAW = 805306368

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_SOURCE_FORMAT_16BIT_RAW = (
    VRM_PROPID_GRAB_SOURCE_FORMAT_8BIT_RAW + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_SOURCE_FORMAT_8BIT_RLE = (
    VRM_PROPID_GRAB_SOURCE_FORMAT_16BIT_RAW + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_READOUT_ORIGIN_POINT_I = 12289

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_HOST_RINGBUFFER_SIZE_I = (
    VRM_PROPID_GRAB_READOUT_ORIGIN_POINT_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_FRAMERATE_AVERAGE_F = (
    VRM_PROPID_GRAB_HOST_RINGBUFFER_SIZE_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_FRAMERATE_ESTIMATED_F = (
    VRM_PROPID_GRAB_FRAMERATE_AVERAGE_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_HOST_RINGBUFFER_IMAGES_READY_I = (
    VRM_PROPID_GRAB_FRAMERATE_ESTIMATED_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_CONFIG_E = 12294

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_CONFIG_FACTORY_DEFAULTS = 805699584

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_CONFIG_USER_DEFAULTS = (
    VRM_PROPID_GRAB_CONFIG_FACTORY_DEFAULTS + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_CONFIG_2 = (VRM_PROPID_GRAB_CONFIG_USER_DEFAULTS + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_CONFIG_3 = (VRM_PROPID_GRAB_CONFIG_2 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_CONFIG_4 = (VRM_PROPID_GRAB_CONFIG_3 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_CONFIG_5 = (VRM_PROPID_GRAB_CONFIG_4 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_CONFIG_6 = (VRM_PROPID_GRAB_CONFIG_5 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_CONFIG_7 = (VRM_PROPID_GRAB_CONFIG_6 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_CONFIG_8 = (VRM_PROPID_GRAB_CONFIG_7 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_CONFIG_9 = (VRM_PROPID_GRAB_CONFIG_8 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_CONFIG_DESCRIPTION_S = 12295

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_DATARATE_AVERAGE_I = (VRM_PROPID_GRAB_CONFIG_DESCRIPTION_S + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_SYNC_FREERUN_JITTER_F = (
    VRM_PROPID_GRAB_DATARATE_AVERAGE_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_USER_ROI_RECT_I = 12304

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_DEVICE_RINGBUFFER_IMAGES_READY_I = (
    VRM_PROPID_GRAB_USER_ROI_RECT_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_DEVICE_RINGBUFFER_SIZE_I = (
    VRM_PROPID_GRAB_DEVICE_RINGBUFFER_IMAGES_READY_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_DEVICE_RAMGRAB_MODE_E = 12308

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_DEVICE_RAMGRAB_MODE_BUFFERING = 806617088

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_DEVICE_RAMGRAB_MODE_BUFFERING_DT = (
    VRM_PROPID_GRAB_DEVICE_RAMGRAB_MODE_BUFFERING + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_DEVICE_RAMGRAB_MODE_LOW_LATENCY = (
    VRM_PROPID_GRAB_DEVICE_RAMGRAB_MODE_BUFFERING_DT + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_DEVICE_RAMGRAB_MODE_LOW_LATENCY_DT = (
    VRM_PROPID_GRAB_DEVICE_RAMGRAB_MODE_LOW_LATENCY + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_DEVICE_MULTIFRAME_COUNT_I = 12345

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_FPGA_GLOBAL_LUT_DISABLE_B = (
    VRM_PROPID_GRAB_DEVICE_MULTIFRAME_COUNT_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_MODE_E = 12416

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_MODE_FREERUNNING = 813694976

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_MODE_TRIGGERED_EXT = (VRM_PROPID_GRAB_MODE_FREERUNNING + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_MODE_TRIGGERED_SOFT = (VRM_PROPID_GRAB_MODE_TRIGGERED_EXT + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_MODE_TRIGGERED_SOFT_EXT = (
    VRM_PROPID_GRAB_MODE_TRIGGERED_SOFT + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_MODE_FREERUNNING_SEQUENTIAL = (
    VRM_PROPID_GRAB_MODE_TRIGGERED_SOFT_EXT + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_MODE_SYNCHRONIZED_FREERUNNING = (
    VRM_PROPID_GRAB_MODE_FREERUNNING_SEQUENTIAL + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_MODE_TRIGGERED_INTERNAL = (
    VRM_PROPID_GRAB_MODE_SYNCHRONIZED_FREERUNNING + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_TRIGGER_TIMEOUT_F = 12417

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_SENSOR_PROPS_SELECT_E = 12432

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_SENSOR_PROPS_SELECT_1 = 814743553

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_SENSOR_PROPS_SELECT_2 = (
    VRM_PROPID_GRAB_SENSOR_PROPS_SELECT_1 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_SENSOR_PROPS_SELECT_3 = (
    VRM_PROPID_GRAB_SENSOR_PROPS_SELECT_2 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_SENSOR_PROPS_SELECT_4 = (
    VRM_PROPID_GRAB_SENSOR_PROPS_SELECT_3 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_SENSOR_PROPS_SELECT_5 = (
    VRM_PROPID_GRAB_SENSOR_PROPS_SELECT_4 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_SENSOR_PROPS_SELECT_6 = (
    VRM_PROPID_GRAB_SENSOR_PROPS_SELECT_5 + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_SENSOR_ENABLE_1_B = 12433

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_SENSOR_ENABLE_2_B = (VRM_PROPID_GRAB_SENSOR_ENABLE_1_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_SENSOR_ENABLE_3_B = (VRM_PROPID_GRAB_SENSOR_ENABLE_2_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_SENSOR_ENABLE_4_B = (VRM_PROPID_GRAB_SENSOR_ENABLE_3_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_SENSOR_ENABLE_5_B = (VRM_PROPID_GRAB_SENSOR_ENABLE_4_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_SENSOR_ENABLE_6_B = (VRM_PROPID_GRAB_SENSOR_ENABLE_5_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_AVC_FIELD_SELECT_E = 12448

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_AVC_FIELD_SELECT_TOP = 815792128

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_AVC_FIELD_SELECT_BOTTOM = (
    VRM_PROPID_GRAB_AVC_FIELD_SELECT_TOP + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_AVC_FIELD_REDUCTION_E = 12449

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_AVC_FIELD_REDUCTION_OFF = 815857664

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_AVC_FIELD_REDUCTION_ON = (
    VRM_PROPID_GRAB_AVC_FIELD_REDUCTION_OFF + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_AVC_READOUT_E = 12450

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_AVC_READOUT_FIELD = 815923200

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_AVC_READOUT_FRAME = (VRM_PROPID_GRAB_AVC_READOUT_FIELD + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_AVC_READOUT_PROGRESSIVE_FRAME = (
    VRM_PROPID_GRAB_AVC_READOUT_FRAME + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_YUV_BYTE_ORDER_E = 12453

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_YUV_BYTE_ORDER_YUYV = 816119808

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_GRAB_YUV_BYTE_ORDER_UYVY = (VRM_PROPID_GRAB_YUV_BYTE_ORDER_YUYV + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_FILTER_MASTER_GAMMA_F = 12544

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_FILTER_MASTER_LUMINANCE_I = (VRM_PROPID_FILTER_MASTER_GAMMA_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_FILTER_MASTER_CONTRAST_F = (
    VRM_PROPID_FILTER_MASTER_LUMINANCE_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_FILTER_MASTER_BLACKLEVEL_I = (
    VRM_PROPID_FILTER_MASTER_CONTRAST_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_FILTER_ALAW_COMPENSATION_B = 12552

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_FILTER_RED_GAMMA_F = 12560

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_FILTER_RED_LUMINANCE_I = (VRM_PROPID_FILTER_RED_GAMMA_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_FILTER_RED_CONTRAST_F = (VRM_PROPID_FILTER_RED_LUMINANCE_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_FILTER_GREEN_GAMMA_F = 12576

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_FILTER_GREEN_LUMINANCE_I = (VRM_PROPID_FILTER_GREEN_GAMMA_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_FILTER_GREEN_CONTRAST_F = (VRM_PROPID_FILTER_GREEN_LUMINANCE_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_FILTER_BLUE_GAMMA_F = 12592

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_FILTER_BLUE_LUMINANCE_I = (VRM_PROPID_FILTER_BLUE_GAMMA_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_FILTER_BLUE_CONTRAST_F = (VRM_PROPID_FILTER_BLUE_LUMINANCE_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_PLUGIN_AUTO_EXPOSURE_B = 12800

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_PLUGIN_AUTO_EXPOSURE_MAX_F = (VRM_PROPID_PLUGIN_AUTO_EXPOSURE_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_PLUGIN_AUTO_EXPOSURE_TARGET_MEAN_VALUE_I = (
    VRM_PROPID_PLUGIN_AUTO_EXPOSURE_MAX_F + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_PLUGIN_AUTO_EXPOSURE_TARGET_MEAN_VALUE_TOLERANCE_I = (
    VRM_PROPID_PLUGIN_AUTO_EXPOSURE_TARGET_MEAN_VALUE_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_PLUGIN_AUTO_EXPOSURE_ROI_RECT_I = (
    VRM_PROPID_PLUGIN_AUTO_EXPOSURE_TARGET_MEAN_VALUE_TOLERANCE_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_PLUGIN_AUTO_RESET_LEVEL_B = 12816

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_PLUGIN_AUTO_WHITE_BALANCE_FILTER_B = 12832

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_PLUGIN_AUTO_WHITE_BALANCE_GAINS_B = (
    VRM_PROPID_PLUGIN_AUTO_WHITE_BALANCE_FILTER_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_PLUGIN_AUTO_WHITE_BALANCE_ROI_RECT_I = (
    VRM_PROPID_PLUGIN_AUTO_WHITE_BALANCE_GAINS_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_PLUGIN_AUTO_CHANNEL_BALANCE_FILTER_B = 12840

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_PLUGIN_IMAGE_PROCESSING_B = 13568

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CONVERTER_BAYER_HQ_B = 16384

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CONVERTER_FLIP_H_B = (VRM_PROPID_CONVERTER_BAYER_HQ_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CONVERTER_FLIP_V_B = (VRM_PROPID_CONVERTER_FLIP_H_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_CONVERTER_PREFER_GRAY_OUTPUT_B = (VRM_PROPID_CONVERTER_FLIP_V_B + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_IMAGEPROC_DPM_B = 16640

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_ETHCAM_SERVER_RINGBUFFER_SIZE_I = 20736

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_ETHCAM_SERVER_MTU_I = (
    VRM_PROPID_ETHCAM_SERVER_RINGBUFFER_SIZE_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_DAV_WAIT_FOR_STROBE_E = 22784

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_DAV_WAIT_FOR_STROBE_DISABLE = 1493172225

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_DAV_WAIT_FOR_STROBE_EDGE_RISING = (
    VRM_PROPID_DAV_WAIT_FOR_STROBE_DISABLE + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRM_PROPID_DAV_WAIT_FOR_STROBE_EDGE_FALLING = (
    VRM_PROPID_DAV_WAIT_FOR_STROBE_EDGE_RISING + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2props.h: 314
VRmPropId = enum__VRmPropId

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 746
enum__VRmPropType = c_int

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 746
VRM_PROP_TYPE_BOOL = 1

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 746
VRM_PROP_TYPE_INT = (VRM_PROP_TYPE_BOOL + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 746
VRM_PROP_TYPE_FLOAT = (VRM_PROP_TYPE_INT + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 746
VRM_PROP_TYPE_STRING = (VRM_PROP_TYPE_FLOAT + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 746
VRM_PROP_TYPE_ENUM = (VRM_PROP_TYPE_STRING + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 746
VRM_PROP_TYPE_SIZE_I = (VRM_PROP_TYPE_ENUM + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 746
VRM_PROP_TYPE_POINT_I = (VRM_PROP_TYPE_SIZE_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 746
VRM_PROP_TYPE_RECT_I = (VRM_PROP_TYPE_POINT_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 746
VRM_PROP_TYPE_DOUBLE = (VRM_PROP_TYPE_RECT_I + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 746
VRmPropType = enum__VRmPropType

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 756


class struct__VRmPropInfo(Structure):
    pass


struct__VRmPropInfo.__slots__ = [
    'm_id',
    'm_type',
    'm_id_string',
    'm_description',
    'm_writeable',
]
struct__VRmPropInfo._fields_ = [
    ('m_id', VRmPropId),
    ('m_type', VRmPropType),
    ('m_id_string', VRmSTRING),
    ('m_description', VRmSTRING),
    ('m_writeable', VRmBOOL),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 756
VRmPropInfo = struct__VRmPropInfo

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 765


class struct__VRmPropAttribsB(Structure):
    pass


struct__VRmPropAttribsB.__slots__ = [
    'm_default',
    'm_min',
    'm_max',
    'm_step',
]
struct__VRmPropAttribsB._fields_ = [
    ('m_default', VRmBOOL),
    ('m_min', VRmBOOL),
    ('m_max', VRmBOOL),
    ('m_step', VRmBOOL),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 765
VRmPropAttribsB = struct__VRmPropAttribsB

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 775


class struct__VRmPropAttribsI(Structure):
    pass


struct__VRmPropAttribsI.__slots__ = [
    'm_default',
    'm_min',
    'm_max',
    'm_step',
]
struct__VRmPropAttribsI._fields_ = [
    ('m_default', c_int),
    ('m_min', c_int),
    ('m_max', c_int),
    ('m_step', c_int),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 775
VRmPropAttribsI = struct__VRmPropAttribsI

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 785


class struct__VRmPropAttribsF(Structure):
    pass


struct__VRmPropAttribsF.__slots__ = [
    'm_default',
    'm_min',
    'm_max',
    'm_step',
]
struct__VRmPropAttribsF._fields_ = [
    ('m_default', c_float),
    ('m_min', c_float),
    ('m_max', c_float),
    ('m_step', c_float),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 785
VRmPropAttribsF = struct__VRmPropAttribsF

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 795


class struct__VRmPropAttribsD(Structure):
    pass


struct__VRmPropAttribsD.__slots__ = [
    'm_default',
    'm_min',
    'm_max',
    'm_step',
]
struct__VRmPropAttribsD._fields_ = [
    ('m_default', c_double),
    ('m_min', c_double),
    ('m_max', c_double),
    ('m_step', c_double),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 795
VRmPropAttribsD = struct__VRmPropAttribsD

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 806


class struct__VRmPropAttribsS(Structure):
    pass


struct__VRmPropAttribsS.__slots__ = [
    'm_default',
    'm_min',
    'm_max',
    'm_step',
]
struct__VRmPropAttribsS._fields_ = [
    ('m_default', VRmSTRING),
    ('m_min', VRmSTRING),
    ('m_max', VRmSTRING),
    ('m_step', VRmSTRING),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 806
VRmPropAttribsS = struct__VRmPropAttribsS

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 816


class struct__VRmPropAttribsE(Structure):
    pass


struct__VRmPropAttribsE.__slots__ = [
    'm_default',
    'm_min',
    'm_max',
    'm_step',
]
struct__VRmPropAttribsE._fields_ = [
    ('m_default', VRmPropId),
    ('m_min', VRmPropId),
    ('m_max', VRmPropId),
    ('m_step', VRmPropId),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 816
VRmPropAttribsE = struct__VRmPropAttribsE

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 826


class struct__VRmPropAttribsSizeI(Structure):
    pass


struct__VRmPropAttribsSizeI.__slots__ = [
    'm_default',
    'm_min',
    'm_max',
    'm_step',
]
struct__VRmPropAttribsSizeI._fields_ = [
    ('m_default', VRmSizeI),
    ('m_min', VRmSizeI),
    ('m_max', VRmSizeI),
    ('m_step', VRmSizeI),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 826
VRmPropAttribsSizeI = struct__VRmPropAttribsSizeI

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 836


class struct__VRmPropAttribsPointI(Structure):
    pass


struct__VRmPropAttribsPointI.__slots__ = [
    'm_default',
    'm_min',
    'm_max',
    'm_step',
]
struct__VRmPropAttribsPointI._fields_ = [
    ('m_default', VRmPointI),
    ('m_min', VRmPointI),
    ('m_max', VRmPointI),
    ('m_step', VRmPointI),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 836
VRmPropAttribsPointI = struct__VRmPropAttribsPointI

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 846


class struct__VRmPropAttribsRectI(Structure):
    pass


struct__VRmPropAttribsRectI.__slots__ = [
    'm_default',
    'm_min',
    'm_max',
    'm_step',
]
struct__VRmPropAttribsRectI._fields_ = [
    ('m_default', VRmRectI),
    ('m_min', VRmRectI),
    ('m_max', VRmRectI),
    ('m_step', VRmRectI),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 846
VRmPropAttribsRectI = struct__VRmPropAttribsRectI

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 850
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetPropertyListSize'):
    VRmUsbCamGetPropertyListSize = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetPropertyListSize
    VRmUsbCamGetPropertyListSize.argtypes = [
        VRmUsbCamDevice, POINTER(VRmDWORD)
    ]
    VRmUsbCamGetPropertyListSize.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 853
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetPropertyListEntry'):
    VRmUsbCamGetPropertyListEntry = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetPropertyListEntry
    VRmUsbCamGetPropertyListEntry.argtypes = [
        VRmUsbCamDevice, VRmDWORD, POINTER(VRmPropId)
    ]
    VRmUsbCamGetPropertyListEntry.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 856
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetPropertyInfo'):
    VRmUsbCamGetPropertyInfo = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetPropertyInfo
    VRmUsbCamGetPropertyInfo.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(VRmPropInfo)
    ]
    VRmUsbCamGetPropertyInfo.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 859
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetPropertySupported'):
    VRmUsbCamGetPropertySupported = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetPropertySupported
    VRmUsbCamGetPropertySupported.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(VRmBOOL)
    ]
    VRmUsbCamGetPropertySupported.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 863
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetPropertyValueB'):
    VRmUsbCamGetPropertyValueB = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetPropertyValueB
    VRmUsbCamGetPropertyValueB.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(VRmBOOL)
    ]
    VRmUsbCamGetPropertyValueB.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 864
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetPropertyValueB'):
    VRmUsbCamSetPropertyValueB = _libs[
        'libvrmusbcam2.so'].VRmUsbCamSetPropertyValueB
    VRmUsbCamSetPropertyValueB.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(VRmBOOL)
    ]
    VRmUsbCamSetPropertyValueB.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 865
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetPropertyAttribsB'):
    VRmUsbCamGetPropertyAttribsB = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetPropertyAttribsB
    VRmUsbCamGetPropertyAttribsB.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(VRmPropAttribsB)
    ]
    VRmUsbCamGetPropertyAttribsB.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 870
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetPropertyValueI'):
    VRmUsbCamGetPropertyValueI = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetPropertyValueI
    VRmUsbCamGetPropertyValueI.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(c_int)
    ]
    VRmUsbCamGetPropertyValueI.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 871
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetPropertyValueI'):
    VRmUsbCamSetPropertyValueI = _libs[
        'libvrmusbcam2.so'].VRmUsbCamSetPropertyValueI
    VRmUsbCamSetPropertyValueI.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(c_int)
    ]
    VRmUsbCamSetPropertyValueI.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 872
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetPropertyAttribsI'):
    VRmUsbCamGetPropertyAttribsI = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetPropertyAttribsI
    VRmUsbCamGetPropertyAttribsI.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(VRmPropAttribsI)
    ]
    VRmUsbCamGetPropertyAttribsI.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 877
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetPropertyValueF'):
    VRmUsbCamGetPropertyValueF = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetPropertyValueF
    VRmUsbCamGetPropertyValueF.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(c_float)
    ]
    VRmUsbCamGetPropertyValueF.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 878
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetPropertyValueF'):
    VRmUsbCamSetPropertyValueF = _libs[
        'libvrmusbcam2.so'].VRmUsbCamSetPropertyValueF
    VRmUsbCamSetPropertyValueF.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(c_float)
    ]
    VRmUsbCamSetPropertyValueF.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 879
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetPropertyAttribsF'):
    VRmUsbCamGetPropertyAttribsF = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetPropertyAttribsF
    VRmUsbCamGetPropertyAttribsF.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(VRmPropAttribsF)
    ]
    VRmUsbCamGetPropertyAttribsF.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 884
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetPropertyValueD'):
    VRmUsbCamGetPropertyValueD = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetPropertyValueD
    VRmUsbCamGetPropertyValueD.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(c_double)
    ]
    VRmUsbCamGetPropertyValueD.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 885
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetPropertyValueD'):
    VRmUsbCamSetPropertyValueD = _libs[
        'libvrmusbcam2.so'].VRmUsbCamSetPropertyValueD
    VRmUsbCamSetPropertyValueD.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(c_double)
    ]
    VRmUsbCamSetPropertyValueD.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 886
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetPropertyAttribsD'):
    VRmUsbCamGetPropertyAttribsD = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetPropertyAttribsD
    VRmUsbCamGetPropertyAttribsD.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(VRmPropAttribsD)
    ]
    VRmUsbCamGetPropertyAttribsD.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 892
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetPropertyValueS'):
    VRmUsbCamGetPropertyValueS = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetPropertyValueS
    VRmUsbCamGetPropertyValueS.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(VRmSTRING)
    ]
    VRmUsbCamGetPropertyValueS.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 893
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetPropertyValueS'):
    VRmUsbCamSetPropertyValueS = _libs[
        'libvrmusbcam2.so'].VRmUsbCamSetPropertyValueS
    VRmUsbCamSetPropertyValueS.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(VRmSTRING)
    ]
    VRmUsbCamSetPropertyValueS.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 894
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetPropertyAttribsS'):
    VRmUsbCamGetPropertyAttribsS = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetPropertyAttribsS
    VRmUsbCamGetPropertyAttribsS.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(VRmPropAttribsS)
    ]
    VRmUsbCamGetPropertyAttribsS.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 899
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetPropertyValueE'):
    VRmUsbCamGetPropertyValueE = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetPropertyValueE
    VRmUsbCamGetPropertyValueE.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(VRmPropId)
    ]
    VRmUsbCamGetPropertyValueE.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 900
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetPropertyValueE'):
    VRmUsbCamSetPropertyValueE = _libs[
        'libvrmusbcam2.so'].VRmUsbCamSetPropertyValueE
    VRmUsbCamSetPropertyValueE.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(VRmPropId)
    ]
    VRmUsbCamSetPropertyValueE.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 901
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetPropertyAttribsE'):
    VRmUsbCamGetPropertyAttribsE = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetPropertyAttribsE
    VRmUsbCamGetPropertyAttribsE.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(VRmPropAttribsE)
    ]
    VRmUsbCamGetPropertyAttribsE.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 906
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetPropertyValueSizeI'):
    VRmUsbCamGetPropertyValueSizeI = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetPropertyValueSizeI
    VRmUsbCamGetPropertyValueSizeI.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(VRmSizeI)
    ]
    VRmUsbCamGetPropertyValueSizeI.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 907
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetPropertyValueSizeI'):
    VRmUsbCamSetPropertyValueSizeI = _libs[
        'libvrmusbcam2.so'].VRmUsbCamSetPropertyValueSizeI
    VRmUsbCamSetPropertyValueSizeI.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(VRmSizeI)
    ]
    VRmUsbCamSetPropertyValueSizeI.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 908
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetPropertyAttribsSizeI'):
    VRmUsbCamGetPropertyAttribsSizeI = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetPropertyAttribsSizeI
    VRmUsbCamGetPropertyAttribsSizeI.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(VRmPropAttribsSizeI)
    ]
    VRmUsbCamGetPropertyAttribsSizeI.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 913
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetPropertyValuePointI'):
    VRmUsbCamGetPropertyValuePointI = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetPropertyValuePointI
    VRmUsbCamGetPropertyValuePointI.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(VRmPointI)
    ]
    VRmUsbCamGetPropertyValuePointI.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 914
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetPropertyValuePointI'):
    VRmUsbCamSetPropertyValuePointI = _libs[
        'libvrmusbcam2.so'].VRmUsbCamSetPropertyValuePointI
    VRmUsbCamSetPropertyValuePointI.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(VRmPointI)
    ]
    VRmUsbCamSetPropertyValuePointI.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 915
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetPropertyAttribsPointI'):
    VRmUsbCamGetPropertyAttribsPointI = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetPropertyAttribsPointI
    VRmUsbCamGetPropertyAttribsPointI.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(VRmPropAttribsPointI)
    ]
    VRmUsbCamGetPropertyAttribsPointI.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 920
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetPropertyValueRectI'):
    VRmUsbCamGetPropertyValueRectI = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetPropertyValueRectI
    VRmUsbCamGetPropertyValueRectI.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(VRmRectI)
    ]
    VRmUsbCamGetPropertyValueRectI.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 921
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetPropertyValueRectI'):
    VRmUsbCamSetPropertyValueRectI = _libs[
        'libvrmusbcam2.so'].VRmUsbCamSetPropertyValueRectI
    VRmUsbCamSetPropertyValueRectI.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(VRmRectI)
    ]
    VRmUsbCamSetPropertyValueRectI.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 922
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetPropertyAttribsRectI'):
    VRmUsbCamGetPropertyAttribsRectI = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetPropertyAttribsRectI
    VRmUsbCamGetPropertyAttribsRectI.argtypes = [
        VRmUsbCamDevice, VRmPropId, POINTER(VRmPropAttribsRectI)
    ]
    VRmUsbCamGetPropertyAttribsRectI.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 931
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSavePNG'):
    VRmUsbCamSavePNG = _libs['libvrmusbcam2.so'].VRmUsbCamSavePNG
    VRmUsbCamSavePNG.argtypes = [VRmSTRING, POINTER(VRmImage), c_int]
    VRmUsbCamSavePNG.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 933
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamLoadPNG'):
    VRmUsbCamLoadPNG = _libs['libvrmusbcam2.so'].VRmUsbCamLoadPNG
    VRmUsbCamLoadPNG.argtypes = [VRmSTRING, POINTER(POINTER(VRmImage))]
    VRmUsbCamLoadPNG.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 953
enum__VRmStaticCallbackType = c_int

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 953
VRM_STATIC_CALLBACK_TYPE_DEVICE_CHANGE = 1

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 953
VRM_STATIC_CALLBACK_TYPE_CMEM_ALLOCATION_CHANGE = 2

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 953
VRmStaticCallbackType = enum__VRmStaticCallbackType

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 963
enum__VRmDeviceChangeType = c_int

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 963
VRM_DEVICE_CHANGE_TYPE_ARRIVAL = 1

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 963
VRM_DEVICE_CHANGE_TYPE_REMOVECOMPLETE = 2

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 963
VRM_DEVICE_CHANGE_TYPE_BUSY = 3

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 963
VRmDeviceChangeType = enum__VRmDeviceChangeType

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 975


class struct__VRmStaticCallbackCMemAllocationChangeParams(Structure):
    pass


struct__VRmStaticCallbackCMemAllocationChangeParams.__slots__ = [
    'm_allocate',
    'mp_virtual',
    'mp_physical',
    'm_size',
]
struct__VRmStaticCallbackCMemAllocationChangeParams._fields_ = [
    ('m_allocate', VRmBOOL),
    ('mp_virtual', POINTER(None)),
    ('mp_physical', POINTER(None)),
    ('m_size', VRmDWORD),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 975
VRmStaticCallbackCMemAllocationChangeParams = struct__VRmStaticCallbackCMemAllocationChangeParams

VRmStaticCallback = CFUNCTYPE(
    UNCHECKED(None), VRmStaticCallbackType, POINTER(None), POINTER(None)
)  # /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 978

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 988
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamRegisterStaticCallback'):
    VRmUsbCamRegisterStaticCallback = _libs[
        'libvrmusbcam2.so'].VRmUsbCamRegisterStaticCallback
    VRmUsbCamRegisterStaticCallback.argtypes = [
        VRmStaticCallback, POINTER(None)
    ]
    VRmUsbCamRegisterStaticCallback.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 991
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamUnregisterStaticCallback'):
    VRmUsbCamUnregisterStaticCallback = _libs[
        'libvrmusbcam2.so'].VRmUsbCamUnregisterStaticCallback
    VRmUsbCamUnregisterStaticCallback.argtypes = [VRmStaticCallback]
    VRmUsbCamUnregisterStaticCallback.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 1000
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamRegisterStaticCallbackEx'):
    VRmUsbCamRegisterStaticCallbackEx = _libs[
        'libvrmusbcam2.so'].VRmUsbCamRegisterStaticCallbackEx
    VRmUsbCamRegisterStaticCallbackEx.argtypes = [
        VRmStaticCallback, POINTER(None)
    ]
    VRmUsbCamRegisterStaticCallbackEx.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 1004
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamUnregisterStaticCallbackEx'):
    VRmUsbCamUnregisterStaticCallbackEx = _libs[
        'libvrmusbcam2.so'].VRmUsbCamUnregisterStaticCallbackEx
    VRmUsbCamUnregisterStaticCallbackEx.argtypes = [
        VRmStaticCallback, POINTER(None)
    ]
    VRmUsbCamUnregisterStaticCallbackEx.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 1036
enum__VRmDeviceCallbackType = c_int

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 1036
VRM_DEVICE_CALLBACK_TYPE_LUT_CHANGED = 1

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 1036
VRM_DEVICE_CALLBACK_TYPE_SOURCE_FORMAT_CHANGED = 2

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 1036
VRM_DEVICE_CALLBACK_TYPE_PROPERTY_VALUE_CHANGED = 3

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 1036
VRM_DEVICE_CALLBACK_TYPE_PROPERTY_LIST_CHANGED = 4

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 1036
VRM_DEVICE_CALLBACK_TYPE_SOURCE_FORMAT_LIST_CHANGED = 5

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 1036
VRM_DEVICE_CALLBACK_TYPE_TARGET_FORMAT_LIST_CHANGED = 6

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 1036
VRM_DEVICE_CALLBACK_TYPE_PROPERTY_INFO_CHANGED = 7

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 1036
VRM_DEVICE_CALLBACK_TYPE_PROPERTY_ATTRIBS_CHANGED = 8

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 1036
VRmDeviceCallbackType = enum__VRmDeviceCallbackType

VRmDeviceCallback = CFUNCTYPE(
    UNCHECKED(None), VRmUsbCamDevice, VRmDeviceCallbackType, POINTER(None),
    POINTER(None)
)  # /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 1039

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 1056
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamRegisterDeviceCallbackEx'):
    VRmUsbCamRegisterDeviceCallbackEx = _libs[
        'libvrmusbcam2.so'].VRmUsbCamRegisterDeviceCallbackEx
    VRmUsbCamRegisterDeviceCallbackEx.argtypes = [
        VRmUsbCamDevice, VRmDeviceCallback, POINTER(None)
    ]
    VRmUsbCamRegisterDeviceCallbackEx.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 1060
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamUnregisterDeviceCallbackEx'):
    VRmUsbCamUnregisterDeviceCallbackEx = _libs[
        'libvrmusbcam2.so'].VRmUsbCamUnregisterDeviceCallbackEx
    VRmUsbCamUnregisterDeviceCallbackEx.argtypes = [
        VRmUsbCamDevice, VRmDeviceCallback, POINTER(None)
    ]
    VRmUsbCamUnregisterDeviceCallbackEx.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 1067
if hasattr(_libs['libvrmusbcam2.so'], 'VRmCreateVMLIBKey'):
    VRmCreateVMLIBKey = _libs['libvrmusbcam2.so'].VRmCreateVMLIBKey
    VRmCreateVMLIBKey.argtypes = [POINTER(VRmDWORD)]
    VRmCreateVMLIBKey.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 1068
if hasattr(_libs['libvrmusbcam2.so'], 'VRmCreateVMLIBKeyDsp'):
    VRmCreateVMLIBKeyDsp = _libs['libvrmusbcam2.so'].VRmCreateVMLIBKeyDsp
    VRmCreateVMLIBKeyDsp.argtypes = [POINTER(VRmDWORD)]
    VRmCreateVMLIBKeyDsp.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 43
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamLastErrorWasTransferTimeout'):
    VRmUsbCamLastErrorWasTransferTimeout = _libs[
        'libvrmusbcam2.so'].VRmUsbCamLastErrorWasTransferTimeout
    VRmUsbCamLastErrorWasTransferTimeout.argtypes = []
    VRmUsbCamLastErrorWasTransferTimeout.restype = VRmBOOL

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 50
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetSourceFormat'):
    VRmUsbCamSetSourceFormat = _libs[
        'libvrmusbcam2.so'].VRmUsbCamSetSourceFormat
    VRmUsbCamSetSourceFormat.argtypes = [VRmUsbCamDevice, VRmImageFormat]
    VRmUsbCamSetSourceFormat.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 57
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetBayerHQ'):
    VRmUsbCamSetBayerHQ = _libs['libvrmusbcam2.so'].VRmUsbCamSetBayerHQ
    VRmUsbCamSetBayerHQ.argtypes = [VRmBOOL]
    VRmUsbCamSetBayerHQ.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 60
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetBayerHQ'):
    VRmUsbCamGetBayerHQ = _libs['libvrmusbcam2.so'].VRmUsbCamGetBayerHQ
    VRmUsbCamGetBayerHQ.argtypes = [POINTER(VRmBOOL)]
    VRmUsbCamGetBayerHQ.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 67
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamUpdateSourceFormatList'):
    VRmUsbCamUpdateSourceFormatList = _libs[
        'libvrmusbcam2.so'].VRmUsbCamUpdateSourceFormatList
    VRmUsbCamUpdateSourceFormatList.argtypes = [VRmUsbCamDevice]
    VRmUsbCamUpdateSourceFormatList.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 70
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetSourceFormatListSize'):
    VRmUsbCamGetSourceFormatListSize = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetSourceFormatListSize
    VRmUsbCamGetSourceFormatListSize.argtypes = [
        VRmUsbCamDevice, POINTER(VRmDWORD)
    ]
    VRmUsbCamGetSourceFormatListSize.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 73
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetSourceFormatListEntry'):
    VRmUsbCamGetSourceFormatListEntry = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetSourceFormatListEntry
    VRmUsbCamGetSourceFormatListEntry.argtypes = [
        VRmUsbCamDevice, VRmDWORD, POINTER(VRmImageFormat)
    ]
    VRmUsbCamGetSourceFormatListEntry.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 76
if hasattr(_libs['libvrmusbcam2.so'],
           'VRmUsbCamGetSourceFormatListEntryDescription'):
    VRmUsbCamGetSourceFormatListEntryDescription = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetSourceFormatListEntryDescription
    VRmUsbCamGetSourceFormatListEntryDescription.argtypes = [
        VRmUsbCamDevice, VRmDWORD, POINTER(POINTER(c_char))
    ]
    VRmUsbCamGetSourceFormatListEntryDescription.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 81
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetSourceFormatIndex'):
    VRmUsbCamSetSourceFormatIndex = _libs[
        'libvrmusbcam2.so'].VRmUsbCamSetSourceFormatIndex
    VRmUsbCamSetSourceFormatIndex.argtypes = [VRmUsbCamDevice, VRmDWORD]
    VRmUsbCamSetSourceFormatIndex.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 84
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetSourceFormatIndex'):
    VRmUsbCamGetSourceFormatIndex = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetSourceFormatIndex
    VRmUsbCamGetSourceFormatIndex.argtypes = [
        VRmUsbCamDevice, POINTER(VRmDWORD)
    ]
    VRmUsbCamGetSourceFormatIndex.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 87
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetSourceFormat'):
    VRmUsbCamGetSourceFormat = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetSourceFormat
    VRmUsbCamGetSourceFormat.argtypes = [
        VRmUsbCamDevice, POINTER(VRmImageFormat)
    ]
    VRmUsbCamGetSourceFormat.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 90
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamIsUserROIFormat'):
    VRmUsbCamIsUserROIFormat = _libs[
        'libvrmusbcam2.so'].VRmUsbCamIsUserROIFormat
    VRmUsbCamIsUserROIFormat.argtypes = [
        VRmUsbCamDevice, VRmDWORD, POINTER(VRmBOOL)
    ]
    VRmUsbCamIsUserROIFormat.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 93
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetQueueSize'):
    VRmUsbCamSetQueueSize = _libs['libvrmusbcam2.so'].VRmUsbCamSetQueueSize
    VRmUsbCamSetQueueSize.argtypes = [VRmUsbCamDevice, VRmDWORD]
    VRmUsbCamSetQueueSize.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 95
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetQueueSize'):
    VRmUsbCamGetQueueSize = _libs['libvrmusbcam2.so'].VRmUsbCamGetQueueSize
    VRmUsbCamGetQueueSize.argtypes = [VRmUsbCamDevice, POINTER(VRmDWORD)]
    VRmUsbCamGetQueueSize.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 98
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetEstimatedFps'):
    VRmUsbCamGetEstimatedFps = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetEstimatedFps
    VRmUsbCamGetEstimatedFps.argtypes = [VRmUsbCamDevice, POINTER(c_double)]
    VRmUsbCamGetEstimatedFps.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 102
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetTargetFormatListSizeEx'):
    VRmUsbCamGetTargetFormatListSizeEx = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetTargetFormatListSizeEx
    VRmUsbCamGetTargetFormatListSizeEx.argtypes = [
        VRmUsbCamDevice, POINTER(VRmDWORD)
    ]
    VRmUsbCamGetTargetFormatListSizeEx.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 106
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetTargetFormatListEntryEx'):
    VRmUsbCamGetTargetFormatListEntryEx = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetTargetFormatListEntryEx
    VRmUsbCamGetTargetFormatListEntryEx.argtypes = [
        VRmUsbCamDevice, VRmDWORD, POINTER(VRmImageFormat)
    ]
    VRmUsbCamGetTargetFormatListEntryEx.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 111
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamIsNextImageReady'):
    VRmUsbCamIsNextImageReady = _libs[
        'libvrmusbcam2.so'].VRmUsbCamIsNextImageReady
    VRmUsbCamIsNextImageReady.argtypes = [VRmUsbCamDevice, POINTER(VRmBOOL)]
    VRmUsbCamIsNextImageReady.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 116
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamLockNextImage'):
    VRmUsbCamLockNextImage = _libs['libvrmusbcam2.so'].VRmUsbCamLockNextImage
    VRmUsbCamLockNextImage.argtypes = [
        VRmUsbCamDevice, POINTER(POINTER(VRmImage)), POINTER(VRmBOOL)
    ]
    VRmUsbCamLockNextImage.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 129
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamReloadFactorySettings'):
    VRmUsbCamReloadFactorySettings = _libs[
        'libvrmusbcam2.so'].VRmUsbCamReloadFactorySettings
    VRmUsbCamReloadFactorySettings.argtypes = [VRmUsbCamDevice]
    VRmUsbCamReloadFactorySettings.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 136
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamReloadUserSettings'):
    VRmUsbCamReloadUserSettings = _libs[
        'libvrmusbcam2.so'].VRmUsbCamReloadUserSettings
    VRmUsbCamReloadUserSettings.argtypes = [VRmUsbCamDevice]
    VRmUsbCamReloadUserSettings.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 139
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSaveUserSettings'):
    VRmUsbCamSaveUserSettings = _libs[
        'libvrmusbcam2.so'].VRmUsbCamSaveUserSettings
    VRmUsbCamSaveUserSettings.argtypes = [VRmUsbCamDevice]
    VRmUsbCamSaveUserSettings.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 142
if hasattr(_libs['libvrmusbcam2.so'],
           'VRmUsbCamIsFirmwareCompressionRequired'):
    VRmUsbCamIsFirmwareCompressionRequired = _libs[
        'libvrmusbcam2.so'].VRmUsbCamIsFirmwareCompressionRequired
    VRmUsbCamIsFirmwareCompressionRequired.argtypes = [
        VRmUsbCamDevice, POINTER(VRmBOOL)
    ]
    VRmUsbCamIsFirmwareCompressionRequired.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 159
enum__VRmTriggerMode = c_int

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 159
VRM_TRIGGERMODE_NONE = 0

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 159
VRM_TRIGGERMODE_SNAPSHOT_EXT = 1

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 159
VRM_TRIGGERMODE_SNAPSHOT_SOFT = 2

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 159
VRM_TRIGGERMODE_SNAPSHOT_EXT_SOFT = 3

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 159
VRmTriggerMode = enum__VRmTriggerMode

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 169
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetTriggerMode'):
    VRmUsbCamSetTriggerMode = _libs['libvrmusbcam2.so'].VRmUsbCamSetTriggerMode
    VRmUsbCamSetTriggerMode.argtypes = [VRmUsbCamDevice, VRmTriggerMode]
    VRmUsbCamSetTriggerMode.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 172
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetTriggerMode'):
    VRmUsbCamGetTriggerMode = _libs['libvrmusbcam2.so'].VRmUsbCamGetTriggerMode
    VRmUsbCamGetTriggerMode.argtypes = [
        VRmUsbCamDevice, POINTER(VRmTriggerMode)
    ]
    VRmUsbCamGetTriggerMode.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 177
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetTriggerTimeout'):
    VRmUsbCamSetTriggerTimeout = _libs[
        'libvrmusbcam2.so'].VRmUsbCamSetTriggerTimeout
    VRmUsbCamSetTriggerTimeout.argtypes = [VRmUsbCamDevice, c_float]
    VRmUsbCamSetTriggerTimeout.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 180
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetTriggerTimeout'):
    VRmUsbCamGetTriggerTimeout = _libs[
        'libvrmusbcam2.so'].VRmUsbCamGetTriggerTimeout
    VRmUsbCamGetTriggerTimeout.argtypes = [VRmUsbCamDevice, POINTER(c_float)]
    VRmUsbCamGetTriggerTimeout.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 192


class struct__VRmTriggerStats(Structure):
    pass


struct__VRmTriggerStats.__slots__ = [
    'm_caught_count',
    'm_dropped_count',
    'm_time_stamp',
]
struct__VRmTriggerStats._fields_ = [
    ('m_caught_count', VRmWORD),
    ('m_dropped_count', VRmWORD),
    ('m_time_stamp', c_double),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 192
VRmTriggerStats = struct__VRmTriggerStats

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 196
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamReadTriggerStats'):
    VRmUsbCamReadTriggerStats = _libs[
        'libvrmusbcam2.so'].VRmUsbCamReadTriggerStats
    VRmUsbCamReadTriggerStats.argtypes = [
        VRmUsbCamDevice, POINTER(VRmTriggerStats)
    ]
    VRmUsbCamReadTriggerStats.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 215
enum__VRmFeatures = c_int

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 215
VRM_SETTINGS1_SUPPORTED = (1 << 0)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 215
VRM_SETTINGS2_SUPPORTED = (1 << 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 215
VRM_SETTINGS3_SUPPORTED = (1 << 2)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 215
VRM_SETTINGS4_SUPPORTED = (1 << 3)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 215
VRM_SETTINGS5_SUPPORTED = (1 << 4)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 215
VRM_SETTINGS6_SUPPORTED = (1 << 5)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 215
VRM_SETTINGS7_SUPPORTED = (1 << 6)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 215
VRM_SETTINGS8_SUPPORTED = (1 << 7)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 215
VRM_SETTINGS9_SUPPORTED = (1 << 8)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 215
VRM_EXT_TRIGGER_SUPPORTED = (1 << 16)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 215
VRM_SOFT_TRIGGER_SUPPORTED = (1 << 17)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 215
VRmFeatures = enum__VRmFeatures

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 219
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetFeatures'):
    VRmUsbCamGetFeatures = _libs['libvrmusbcam2.so'].VRmUsbCamGetFeatures
    VRmUsbCamGetFeatures.argtypes = [VRmUsbCamDevice, POINTER(c_int)]
    VRmUsbCamGetFeatures.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 252


class struct__VRmSettings1(Structure):
    pass


struct__VRmSettings1.__slots__ = [
    'm_roi_left',
    'm_roi_top',
    'm_roi_width',
    'm_roi_height',
    'm_sensor_width',
    'm_sensor_height',
    'm_exposure_time_ms',
    'm_pixel_clock_mhz',
    'm_red_gain',
    'm_green_gain',
    'm_blue_gain',
    'm_reset_level',
    'm_pixel_bias_voltage',
]
struct__VRmSettings1._fields_ = [
    ('m_roi_left', VRmWORD),
    ('m_roi_top', VRmWORD),
    ('m_roi_width', VRmWORD),
    ('m_roi_height', VRmWORD),
    ('m_sensor_width', VRmWORD),
    ('m_sensor_height', VRmWORD),
    ('m_exposure_time_ms', c_double),
    ('m_pixel_clock_mhz', c_double),
    ('m_red_gain', VRmBYTE),
    ('m_green_gain', VRmBYTE),
    ('m_blue_gain', VRmBYTE),
    ('m_reset_level', VRmBYTE),
    ('m_pixel_bias_voltage', VRmBYTE),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 252
VRmSettings1 = struct__VRmSettings1

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 254
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetSettings1'):
    VRmUsbCamSetSettings1 = _libs['libvrmusbcam2.so'].VRmUsbCamSetSettings1
    VRmUsbCamSetSettings1.argtypes = [VRmUsbCamDevice, POINTER(VRmSettings1)]
    VRmUsbCamSetSettings1.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 255
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetSettings1'):
    VRmUsbCamGetSettings1 = _libs['libvrmusbcam2.so'].VRmUsbCamGetSettings1
    VRmUsbCamGetSettings1.argtypes = [VRmUsbCamDevice, POINTER(VRmSettings1)]
    VRmUsbCamGetSettings1.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 262


class struct__VRmSettings2(Structure):
    pass


struct__VRmSettings2.__slots__ = ['m_illumination_intensity', ]
struct__VRmSettings2._fields_ = [('m_illumination_intensity', c_double), ]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 262
VRmSettings2 = struct__VRmSettings2

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 264
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetSettings2'):
    VRmUsbCamSetSettings2 = _libs['libvrmusbcam2.so'].VRmUsbCamSetSettings2
    VRmUsbCamSetSettings2.argtypes = [VRmUsbCamDevice, POINTER(VRmSettings2)]
    VRmUsbCamSetSettings2.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 265
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetSettings2'):
    VRmUsbCamGetSettings2 = _libs['libvrmusbcam2.so'].VRmUsbCamGetSettings2
    VRmUsbCamGetSettings2.argtypes = [VRmUsbCamDevice, POINTER(VRmSettings2)]
    VRmUsbCamGetSettings2.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 279


class struct__VRmSettings3(Structure):
    pass


struct__VRmSettings3.__slots__ = [
    'm_gamma',
    'm_luminance',
    'm_contrast',
]
struct__VRmSettings3._fields_ = [
    ('m_gamma', c_float),
    ('m_luminance', c_short),
    ('m_contrast', c_float),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 279
VRmSettings3 = struct__VRmSettings3

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 281
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetSettings3'):
    VRmUsbCamSetSettings3 = _libs['libvrmusbcam2.so'].VRmUsbCamSetSettings3
    VRmUsbCamSetSettings3.argtypes = [VRmUsbCamDevice, POINTER(VRmSettings3)]
    VRmUsbCamSetSettings3.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 282
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetSettings3'):
    VRmUsbCamGetSettings3 = _libs['libvrmusbcam2.so'].VRmUsbCamGetSettings3
    VRmUsbCamGetSettings3.argtypes = [VRmUsbCamDevice, POINTER(VRmSettings3)]
    VRmUsbCamGetSettings3.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 289
enum__VRmAVCInput = c_int

VRM_SVIDEO = 0  # /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 289

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 289
VRM_COMPOSITE = (VRM_SVIDEO + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 289
VRM_YC = (VRM_COMPOSITE + 1)

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 289
VRmAVCInput = enum__VRmAVCInput

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 304


class struct__VRmSettings4(Structure):
    pass


struct__VRmSettings4.__slots__ = [
    'm_luminance_brightness',
    'm_luminance_contrast',
    'm_chrominance_saturation',
    'm_chrominance_hue',
    'm_format',
]
struct__VRmSettings4._fields_ = [
    ('m_luminance_brightness', VRmBYTE),
    ('m_luminance_contrast', VRmBYTE),
    ('m_chrominance_saturation', VRmBYTE),
    ('m_chrominance_hue', c_char),
    ('m_format', VRmAVCInput),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 304
VRmSettings4 = struct__VRmSettings4

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 306
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetSettings4'):
    VRmUsbCamSetSettings4 = _libs['libvrmusbcam2.so'].VRmUsbCamSetSettings4
    VRmUsbCamSetSettings4.argtypes = [VRmUsbCamDevice, POINTER(VRmSettings4)]
    VRmUsbCamSetSettings4.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 307
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetSettings4'):
    VRmUsbCamGetSettings4 = _libs['libvrmusbcam2.so'].VRmUsbCamGetSettings4
    VRmUsbCamGetSettings4.argtypes = [VRmUsbCamDevice, POINTER(VRmSettings4)]
    VRmUsbCamGetSettings4.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 344


class struct__VRmSettings5(Structure):
    pass


struct__VRmSettings5.__slots__ = [
    'm_roi_left',
    'm_roi_top',
    'm_roi_width',
    'm_roi_height',
    'm_vblank_lines',
    'm_sensor_width',
    'm_sensor_height',
    'm_exposure_time_ms',
    'm_pixel_clock_mhz',
    'm_adapt_readout_to_exposure',
    'm_red_gain',
    'm_green_gain',
    'm_blue_gain',
    'm_vrst_low_voltage',
]
struct__VRmSettings5._fields_ = [
    ('m_roi_left', VRmWORD),
    ('m_roi_top', VRmWORD),
    ('m_roi_width', VRmWORD),
    ('m_roi_height', VRmWORD),
    ('m_vblank_lines', VRmBYTE),
    ('m_sensor_width', VRmWORD),
    ('m_sensor_height', VRmWORD),
    ('m_exposure_time_ms', c_double),
    ('m_pixel_clock_mhz', c_double),
    ('m_adapt_readout_to_exposure', VRmBOOL),
    ('m_red_gain', VRmBYTE),
    ('m_green_gain', VRmBYTE),
    ('m_blue_gain', VRmBYTE),
    ('m_vrst_low_voltage', c_double),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 344
VRmSettings5 = struct__VRmSettings5

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 346
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetSettings5'):
    VRmUsbCamSetSettings5 = _libs['libvrmusbcam2.so'].VRmUsbCamSetSettings5
    VRmUsbCamSetSettings5.argtypes = [VRmUsbCamDevice, POINTER(VRmSettings5)]
    VRmUsbCamSetSettings5.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 347
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetSettings5'):
    VRmUsbCamGetSettings5 = _libs['libvrmusbcam2.so'].VRmUsbCamGetSettings5
    VRmUsbCamGetSettings5.argtypes = [VRmUsbCamDevice, POINTER(VRmSettings5)]
    VRmUsbCamGetSettings5.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 355
enum__VRmTriggerPolarity = c_int

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 355
VRM_TRIGGERPOLARITY_POS_EDGE = 0

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 355
VRM_TRIGGERPOLARITY_NEG_EDGE = 1

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 355
VRM_TRIGGERPOLARITY_POS_LEVEL = 2

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 355
VRM_TRIGGERPOLARITY_NEG_LEVEL = 3

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 355
VRmTriggerPolarity = enum__VRmTriggerPolarity

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 367


class struct__VRmSettings6(Structure):
    pass


struct__VRmSettings6.__slots__ = [
    'm_polarity',
    'm_delay_ms',
]
struct__VRmSettings6._fields_ = [
    ('m_polarity', VRmTriggerPolarity),
    ('m_delay_ms', c_double),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 367
VRmSettings6 = struct__VRmSettings6

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 369
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetSettings6'):
    VRmUsbCamSetSettings6 = _libs['libvrmusbcam2.so'].VRmUsbCamSetSettings6
    VRmUsbCamSetSettings6.argtypes = [VRmUsbCamDevice, POINTER(VRmSettings6)]
    VRmUsbCamSetSettings6.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 370
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetSettings6'):
    VRmUsbCamGetSettings6 = _libs['libvrmusbcam2.so'].VRmUsbCamGetSettings6
    VRmUsbCamGetSettings6.argtypes = [VRmUsbCamDevice, POINTER(VRmSettings6)]
    VRmUsbCamGetSettings6.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 382


class struct__VRmSettings7(Structure):
    pass


struct__VRmSettings7.__slots__ = ['m_vblank_lines', ]
struct__VRmSettings7._fields_ = [('m_vblank_lines', VRmBYTE), ]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 382
VRmSettings7 = struct__VRmSettings7

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 384
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetSettings7'):
    VRmUsbCamSetSettings7 = _libs['libvrmusbcam2.so'].VRmUsbCamSetSettings7
    VRmUsbCamSetSettings7.argtypes = [VRmUsbCamDevice, POINTER(VRmSettings7)]
    VRmUsbCamSetSettings7.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 385
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetSettings7'):
    VRmUsbCamGetSettings7 = _libs['libvrmusbcam2.so'].VRmUsbCamGetSettings7
    VRmUsbCamGetSettings7.argtypes = [VRmUsbCamDevice, POINTER(VRmSettings7)]
    VRmUsbCamGetSettings7.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 416


class struct__VRmSettings8(Structure):
    pass


struct__VRmSettings8.__slots__ = [
    'm_roi_left',
    'm_roi_top',
    'm_roi_width',
    'm_roi_height',
    'm_vblank_lines',
    'm_sensor_width',
    'm_sensor_height',
    'm_exposure_time_ms',
    'm_pixel_clock_mhz',
    'm_red_gain',
    'm_green_gain',
    'm_blue_gain',
]
struct__VRmSettings8._fields_ = [
    ('m_roi_left', VRmWORD),
    ('m_roi_top', VRmWORD),
    ('m_roi_width', VRmWORD),
    ('m_roi_height', VRmWORD),
    ('m_vblank_lines', VRmWORD),
    ('m_sensor_width', VRmWORD),
    ('m_sensor_height', VRmWORD),
    ('m_exposure_time_ms', c_double),
    ('m_pixel_clock_mhz', c_double),
    ('m_red_gain', c_float),
    ('m_green_gain', c_float),
    ('m_blue_gain', c_float),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 416
VRmSettings8 = struct__VRmSettings8

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 418
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetSettings8'):
    VRmUsbCamSetSettings8 = _libs['libvrmusbcam2.so'].VRmUsbCamSetSettings8
    VRmUsbCamSetSettings8.argtypes = [VRmUsbCamDevice, POINTER(VRmSettings8)]
    VRmUsbCamSetSettings8.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 419
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetSettings8'):
    VRmUsbCamGetSettings8 = _libs['libvrmusbcam2.so'].VRmUsbCamGetSettings8
    VRmUsbCamGetSettings8.argtypes = [VRmUsbCamDevice, POINTER(VRmSettings8)]
    VRmUsbCamGetSettings8.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 426
enum__VRmShutterPolarity = c_int

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 426
VRM_SHUTTERPOLARITY_DISABLED = 0

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 426
VRM_SHUTTERPOLARITY_POS = 1

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 426
VRM_SHUTTERPOLARITY_NEG = 2

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 426
VRmShutterPolarity = enum__VRmShutterPolarity

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 438


class struct__VRmSettings9(Structure):
    pass


struct__VRmSettings9.__slots__ = [
    'm_polarity',
    'm_delay_ms',
    'm_pulse_width_ms',
]
struct__VRmSettings9._fields_ = [
    ('m_polarity', VRmShutterPolarity),
    ('m_delay_ms', c_float),
    ('m_pulse_width_ms', c_float),
]

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 438
VRmSettings9 = struct__VRmSettings9

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 440
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamSetSettings9'):
    VRmUsbCamSetSettings9 = _libs['libvrmusbcam2.so'].VRmUsbCamSetSettings9
    VRmUsbCamSetSettings9.argtypes = [VRmUsbCamDevice, POINTER(VRmSettings9)]
    VRmUsbCamSetSettings9.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 441
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamGetSettings9'):
    VRmUsbCamGetSettings9 = _libs['libvrmusbcam2.so'].VRmUsbCamGetSettings9
    VRmUsbCamGetSettings9.argtypes = [VRmUsbCamDevice, POINTER(VRmSettings9)]
    VRmUsbCamGetSettings9.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 451
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamUserDataBytesFree'):
    VRmUsbCamUserDataBytesFree = _libs[
        'libvrmusbcam2.so'].VRmUsbCamUserDataBytesFree
    VRmUsbCamUserDataBytesFree.argtypes = [VRmUsbCamDevice, POINTER(VRmDWORD)]
    VRmUsbCamUserDataBytesFree.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 455
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamRegisterDeviceCallback'):
    VRmUsbCamRegisterDeviceCallback = _libs[
        'libvrmusbcam2.so'].VRmUsbCamRegisterDeviceCallback
    VRmUsbCamRegisterDeviceCallback.argtypes = [
        VRmUsbCamDevice, VRmDeviceCallback, POINTER(None)
    ]
    VRmUsbCamRegisterDeviceCallback.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 458
if hasattr(_libs['libvrmusbcam2.so'], 'VRmUsbCamUnregisterDeviceCallback'):
    VRmUsbCamUnregisterDeviceCallback = _libs[
        'libvrmusbcam2.so'].VRmUsbCamUnregisterDeviceCallback
    VRmUsbCamUnregisterDeviceCallback.argtypes = [
        VRmUsbCamDevice, VRmDeviceCallback
    ]
    VRmUsbCamUnregisterDeviceCallback.restype = VRmRetVal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 14
try:
    VRMUSBCAM_VERSION = 3500
except:
    pass

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 489
try:
    VRM_IMAGE_BUFFER_SIZE_MAX = 4294967295
except:
    pass

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 161
try:
    VRM_TRIGGERMODE_REPEATED_SNAPSHOT = VRM_TRIGGERMODE_SNAPSHOT_EXT
except:
    pass

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 56
_VRmSizeI = struct__VRmSizeI

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 62
_VRmPointI = struct__VRmPointI

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 70
_VRmRectI = struct__VRmRectI

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 189
VRmUsbCamDeviceInternal = struct_VRmUsbCamDeviceInternal

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 209
_VRmDeviceKey = struct__VRmDeviceKey

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 296
_VRmUserData = struct__VRmUserData

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 439
_VRmImageFormat = struct__VRmImageFormat

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 454
_VRmImage = struct__VRmImage

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 756
_VRmPropInfo = struct__VRmPropInfo

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 765
_VRmPropAttribsB = struct__VRmPropAttribsB

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 775
_VRmPropAttribsI = struct__VRmPropAttribsI

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 785
_VRmPropAttribsF = struct__VRmPropAttribsF

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 795
_VRmPropAttribsD = struct__VRmPropAttribsD

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 806
_VRmPropAttribsS = struct__VRmPropAttribsS

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 816
_VRmPropAttribsE = struct__VRmPropAttribsE

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 826
_VRmPropAttribsSizeI = struct__VRmPropAttribsSizeI

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 836
_VRmPropAttribsPointI = struct__VRmPropAttribsPointI

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 846
_VRmPropAttribsRectI = struct__VRmPropAttribsRectI

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2.h: 975
_VRmStaticCallbackCMemAllocationChangeParams = struct__VRmStaticCallbackCMemAllocationChangeParams

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 192
_VRmTriggerStats = struct__VRmTriggerStats

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 252
_VRmSettings1 = struct__VRmSettings1

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 262
_VRmSettings2 = struct__VRmSettings2

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 279
_VRmSettings3 = struct__VRmSettings3

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 304
_VRmSettings4 = struct__VRmSettings4

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 344
_VRmSettings5 = struct__VRmSettings5

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 367
_VRmSettings6 = struct__VRmSettings6

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 382
_VRmSettings7 = struct__VRmSettings7

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 416
_VRmSettings8 = struct__VRmSettings8

# /home/cg/3Python/beamprofiler/beamprofiler/libraries/vrmagic/vrmusbcam2l.h: 438
_VRmSettings9 = struct__VRmSettings9

# No inserted files
