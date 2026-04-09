import maya.cmds as mc
import maya.mel as ml

def ConfigureCtrlForJnt(jnt, ctrlName):
    ctrlGrpName = ctrlName + "_grp"
    mc.group(ctrlName, n=ctrlGrpName)

    mc.matchTransform(ctrlGrpName, jnt)
    mc.orientConstraint(ctrlName, jnt)    

    return ctrlName, ctrlGrpName

# make the plus shaped controller, this will be used for the ikfk blend
def CreatePlusController(namePrefix, size):
    # use the ml.eval() to make the plus shaped curve
    # scale the controller to the size
    # freeze transformation
    # lock and hide the translate, scale, and rotation, and visibility of the controller


def CreateCircleControllerForJnt(jnt, namePrefix, radius=10):
    ctrlName = f"ac_{namePrefix}_{jnt}"  
    mc.circle(n=ctrlName, r = radius, nr=(1,0,0))
    return ConfigureCtrlForJnt(jnt, ctrlName)


def CreateBoxControllerForJnt(jnt, namePrefix, size=10):
    ctrlName = f"ac_{namePrefix}_{jnt}"
    ml.eval(f"curve -n {ctrlName} -d 1 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15;")
    mc.setAttr(f"{ctrlName}.scale", size, size, size, type="double3")

    # this is the same as freeze transformation command in maya
    mc.makeIdentity(ctrlName, apply=True)
    return ConfigureCtrlForJnt(jnt, ctrlName)