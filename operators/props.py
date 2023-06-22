import bpy

from bpy.props import (
		IntProperty,
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
		('current_scene', "Current Scene", ""),
		]		
	)

	scene_list_index : IntProperty(
		name="Index of scene_list",
		default=0
	)

	viewlayer_list_index : IntProperty(
		name="Index of viewlayer_list",
		default=0
	)


class ListItem(bpy.types.PropertyGroup):

	name : StringProperty(
        name='Name',
	 	default=''
		)
	

# Classes to register
classes = [
    NA_Addon_Props,
    ListItem
]
