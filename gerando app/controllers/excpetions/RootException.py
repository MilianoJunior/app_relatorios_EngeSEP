from kivy.base import (ExceptionManager, ExceptionHandler, EventLoopBase)
import sys

class RootException(Exception):
    pass

class AuthException(RootException):
    pass

class InterfaceException(RootException):
    pass

class CLPException(RootException):
    pass

class DBException(RootException):
    pass

class PDFException(RootException):
    pass