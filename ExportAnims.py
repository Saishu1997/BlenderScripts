import bpy
import os
import re

# CHANGE THIS TO YOUR DESIRED EXPORT DIRECTORY
export_path = "C:\YourFileName"

# Get the armature object
armature = bpy.data.objects.get("Armature")  # Change if yours has a different name
if not armature:
    raise Exception("Armature not found!")

# Select armature and meshes
bpy.ops.object.select_all(action='DESELECT')
armature.select_set(True)
bpy.context.view_layer.objects.active = armature

for child in armature.children:
    if child.type == 'MESH':
        child.select_set(True)

for action in bpy.data.actions:
    armature.animation_data_create()
    armature.animation_data.action = action
    action.use_fake_user = True

    
    safe_name = re.sub(r'[<>:"/\\|?*\n\r\t]', '_', action.name)
    fbx_name = f"{safe_name}.fbx"
    fbx_path = os.path.join(export_path, fbx_name)

    bpy.ops.export_scene.fbx(
        filepath=fbx_path,
        use_selection=True,
        object_types={'ARMATURE', 'MESH'},
        apply_unit_scale=True,
        apply_scale_options='FBX_SCALE_ALL',
        mesh_smooth_type='FACE',
        bake_anim=True,
        bake_anim_use_all_bones=True,
        bake_anim_use_nla_strips=False,
        bake_anim_use_all_actions=False,
        bake_anim_force_startend_keying=True,
        add_leaf_bones=False,
        primary_bone_axis='Y',
            )

    print(f"Exported: {fbx_name}")

print("\n Exported all Files!")
