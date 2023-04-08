from .operators.main import NODE_OT_simple_node_setup

bl_info = {
    "name": "Compositing Node Automatisation Tools",
    "author": "Oleg",
    "version": (1, 0),
    "blender": (3, 4, 0),
    "category": "Compositing",
    "description": "Addon adds usefull tools to automate compositor node creation and editing"
}

import bpy

classes = [
    NODE_OT_simple_node_setup,
]

def register():
    for cl in classes:
        bpy.utils.register_class(cl)

def unregister():
    for cl in classes:
        bpy.utils.unregister_class(cl)

if __name__ == '__main__':
    register()