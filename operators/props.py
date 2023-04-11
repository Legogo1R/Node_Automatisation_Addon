import bpy

from bpy.props import (
		StringProperty,
		EnumProperty,
        BoolProperty,
        PointerProperty,
        )


class NA_Addon_Props(bpy.types.PropertyGroup):
        
	all_viewlayers_bool: BoolProperty(
        name="All Viewlayers",
		description="",
		default=True)
    
	rlayer_node_bool : BoolProperty(
        name="RLayer Node",
		description="",
		default=True  
	)

	output_node_bool : BoolProperty(
		name="Output Node",
		description="",
		default=True
        )
	
	viewlayers_enum : EnumProperty(
		name="Enum",
		description='',
		items=[
		('all_viewlayers', "All Viewlayers", ""),
		('selected_viewlayers', "Selected Viewlayers", ""),
		('current_viewlayer', "Current Viewlayer", ""),
		]		
	)

	scenes_enum : EnumProperty(
		name="Enum",
		description='',
		items=[
		('all_scenes', "All Scenes", ""),
		('selected_scenes', "Selected Scenes", ""),
		]		
	)


# Classes to register
classes = [
    NA_Addon_Props
]
