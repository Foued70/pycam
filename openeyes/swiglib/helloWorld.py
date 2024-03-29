# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.36
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _helloWorld
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


class PySwigIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PySwigIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PySwigIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _helloWorld.delete_PySwigIterator
    __del__ = lambda self : None;
    def value(*args): return _helloWorld.PySwigIterator_value(*args)
    def incr(*args): return _helloWorld.PySwigIterator_incr(*args)
    def decr(*args): return _helloWorld.PySwigIterator_decr(*args)
    def distance(*args): return _helloWorld.PySwigIterator_distance(*args)
    def equal(*args): return _helloWorld.PySwigIterator_equal(*args)
    def copy(*args): return _helloWorld.PySwigIterator_copy(*args)
    def next(*args): return _helloWorld.PySwigIterator_next(*args)
    def previous(*args): return _helloWorld.PySwigIterator_previous(*args)
    def advance(*args): return _helloWorld.PySwigIterator_advance(*args)
    def __eq__(*args): return _helloWorld.PySwigIterator___eq__(*args)
    def __ne__(*args): return _helloWorld.PySwigIterator___ne__(*args)
    def __iadd__(*args): return _helloWorld.PySwigIterator___iadd__(*args)
    def __isub__(*args): return _helloWorld.PySwigIterator___isub__(*args)
    def __add__(*args): return _helloWorld.PySwigIterator___add__(*args)
    def __sub__(*args): return _helloWorld.PySwigIterator___sub__(*args)
    def __iter__(self): return self
PySwigIterator_swigregister = _helloWorld.PySwigIterator_swigregister
PySwigIterator_swigregister(PySwigIterator)

AUTHOR = _helloWorld.AUTHOR

def printString(*args):
  """printString()"""
  return _helloWorld.printString(*args)

def printLine(*args):
  """printLine(string s)"""
  return _helloWorld.printLine(*args)

def simpleProcess(*args):
  """simpleProcess()"""
  return _helloWorld.simpleProcess(*args)

def commaOp(*args):
  """commaOp()"""
  return _helloWorld.commaOp(*args)

def booltest(*args):
  """booltest()"""
  return _helloWorld.booltest(*args)

def wait4in(*args):
  """wait4in()"""
  return _helloWorld.wait4in(*args)

def factorial(*args):
  """factorial(int num) -> int"""
  return _helloWorld.factorial(*args)

def getName(*args):
  """getName() -> string"""
  return _helloWorld.getName(*args)

def runAll(*args):
  """runAll(int ?, string ?)"""
  return _helloWorld.runAll(*args)

cvar = _helloWorld.cvar
yearMade = cvar.yearMade

def add(*args):
  """
    add(int x1, int x2, int x3=0, int x4=0) -> int
    add(int x1, int x2, int x3=0) -> int
    add(int x1, int x2) -> int
    """
  return _helloWorld.add(*args)

