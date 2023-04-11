import bpy

from . import main_ops
from . import utils
from . import ui_ops
from . import props

classes = []
classes += main_ops.classes
classes += utils.classes
classes += ui_ops.classes
classes += props.classes

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.na = bpy.props.PointerProperty(type=props.NA_Addon_Props)

def unregister():
    for cls in reversed(classes):
            bpy.utils.unregister_class(cls)

    del bpy.types.Scene.na