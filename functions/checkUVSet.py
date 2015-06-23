from maya import cmds


def getList(typestr):
    return cmds.ls(type=typestr)
    

def searchUVSet(mesh_list, multiple_UV_set, not_UV_set):    
    # get mesh list    
    for mesh in mesh_list:
        uvset_list = cmds.polyUVSet(mesh, query=True, allUVSets=True)
        uvset_count = len(uvset_list)
        if uvset_count == 1:
            continue
        # Multiple UVSet
        elif uvset_count > 1:
            uvname_list = []
            for uvset_name in uvset_list:
                uvname_list.append(uvset_name)
            multiple_UV_set.update({mesh: uvname_list})
        # Not has UVSet
        elif uvset_count == 0:
            not_UV_set.append(mesh)

# Main Function
def run():
    multiple_UV_set = {}
    not_UV_set = []
    
    mesh_list = getList("mesh")
    searchUVSet(mesh_list, multiple_UV_set, not_UV_set)
    
    return multiple_UV_set, not_UV_set