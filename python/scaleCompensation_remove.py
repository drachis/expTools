#set the scale compensation for the joints in the scene to false
import pymel.core as pm
sel = pm.ls(type='joint')
objs = []
for bone in sel:
    pm.setAttr("{}.{}".format(bone.name(), "segmentScaleCompensate") ,False)
pm.warning("Removed scale compensation on " + str(len(sel)) + " joints")
