import bpy

from . import main
from . import utils

classes = []
classes += main.classes
classes += utils.classes

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
            bpy.utils.unregister_class(cls)