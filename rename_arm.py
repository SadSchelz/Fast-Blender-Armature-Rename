import bpy  

ob = bpy.context.object
if ob.type == "ARMATURE":
    for bone in ob.data.bones:
        if str(bone.name)[:2] == "r_" or str(bone.name)[:1] == "R_":
            bone.name = f"{str(bone.name)[2:]}.R"
        elif str(bone.name)[:2] == "l_" or str(bone.name)[:1] == "L_":
            bone.name = f"{str(bone.name)[2:]}.L"
