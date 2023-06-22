import bpy

from . import main_ops
from . import utils
from . import ui_ops
from . import props

classes = []
classes += utils.classes
classes += main_ops.classes
classes += ui_ops.classes
classes += props.classes


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.na = bpy.props.PointerProperty(type=props.NA_Addon_Props)
    bpy.types.Scene.scene_list = bpy.props.CollectionProperty(type=props.ListItem)
    bpy.types.Scene.viewlayer_list = bpy.props.CollectionProperty(type=props.ListItem)
    

def unregister():
    for cls in reversed(classes):
            bpy.utils.unregister_class(cls)

    del bpy.types.Scene.na
    del bpy.types.Scene.scene_list
    del bpy.types.Scene.viewlayer_list
