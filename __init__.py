bl_info = {
    "name": "Compositing Node Automatisation Tools",
    "author": "Oleg",
    "version": (1, 0),
    "blender": (3, 4, 0),
    "category": "Compositing",
    "description": "Addon adds usefull tools to automate compositor node creation and editing"
}

import bpy

from . import operators

main_modules = [
    operators
]

print(__name__)

def cleanse_modules():
    """search for your plugin modules in blender python sys.modules and remove them"""

    import sys

    all_modules = sys.modules 
    all_modules = dict(sorted(all_modules.items(),key= lambda x:x[0])) #sort them
   
    for k,v in all_modules.items():
        if k.startswith(__name__):
            del sys.modules[k]

    return None 

def register():
    for m in main_modules:
        m.register()
    return None 

def unregister():
    for m in reversed(main_modules):
        m.unregister()

    cleanse_modules()
    return None 

if __name__ == '__main__':
    register()