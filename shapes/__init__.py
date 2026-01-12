# -----------------------------------------------------------
# DEMONSTRATING RELATIVE IMPORTS (INSIDE PACKAGE)
# -----------------------------------------------------------
# We use '.' to refer to the current package level.
# This allows 'circle' and 'rectangle' to be imported relative
# to the location of this __init__.py file.

from .circle import Circle
from .rectangle import Rectangle

# -----------------------------------------------------------
# EXPOSING CLASSES WITH __all__
# -----------------------------------------------------------
# This list defines what is imported when running:
# from shapes import *

__all__ = ['Circle', 'Rectangle']




