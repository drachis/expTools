# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 11:59:36 2014

@author: toli
"""

import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMaya as OpenMaya

class DoublerNode(OpenMayaMPx.MPxNode):
    kPlugNodeId = OpenMaya.MTypeId(0x00047251)
    
    aInputA = OpenMaya.MObject();
    aInputB = OpenMaya.MObject();
    aOutput = OpenMaya.MObject();
    aPercent = OpenMaya.MObject();
    
    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)
        
    def compute(self, plug, data):
        if plug != DoublerNode.aOutput:
            return OpenMaya.MStatus.kUnknownParameter
        
        worldMatrixA = data.inputValue(DoublerNode.aInputA).asMatrix()
        worldMatrixB = data.inputValue(DoublerNode.aInputB).asMatrix()
        multi = data.inputValue(DoublerNode.aPercent).asFloat()
        
        #MTransformationMatrix
        mTMA = OpenMaya.MTransformationMatrix(worldMatrixA)
        mTMB = OpenMaya.MTransformationMatrix(worldMatrixB)
    
        #getting the translation datka from the world matrix        
        transA =  mTMA.getTranslation ( OpenMaya.MSpace.kTransform )
        transB =  mTMB.getTranslation ( OpenMaya.MSpace.kTransform )
        
        #setting the output
        hOutput = data.outputValue(DoublerNode.aOutput)
        resultTrans = OpenMaya.MFloatVector((transA.x +transB.x)*multi, 
                                        (transA.y +transB.y)*multi, 
                                        (transA.z +transB.z)*multi
                                        )
        hOutput.setMfFloatVector(resultTrans)
        
        data.setClean(plug)
         
        return OpenMaya.MStatus.kStatus
        
def creator():
    return OpenMayaMPx.asMPxPtr(DoublerNode())
    
#define new attributes here
def initialize():
    
    nAttr = OpenMaya.MFnNumericAttribute()
    nMAttr = OpenMaya.MFnMatrixAttribute()
    
    DoublerNode.aPercent = nAttr.create('percent', 'per', OpenMaya.MFnNumericData.kFloat, 0.5)
    nMAttr.setWritable(True)
    nMAttr.setSortable(True)
    nMAttr.setReadable(True)
    nAttr.setKeyable(True)
    
    DoublerNode.aInpuitB = nMAttr.create('inMatrixB', 'inB', OpenMaya.MFnMatrixAttribute.kDouble)
    nMAttr.setWritable(True)
    nMAttr.setSortable(True)
    nMAttr.setReadable(True)
    nAttr.setKeyable(True)
    
    DoublerNode.aInputA = nMAttr.create('inMatrixA', 'inA', OpenMaya.MFnMatrixAttribute.kDouble)
    nMAttr.setWritable(True)
    nMAttr.setSortable(True)
    nMAttr.setReadable(True)
    nAttr.setKeyable(True)
    
    DoublerNode.aOutput = nAttr.createPoint('outputTranslate', 'ot')
    nMAttr.setWritable(True)
    nMAttr.setSortable(True)
    nMAttr.setReadable(True)
    
    DoublerNode.addAttribute(DoublerNode.aPercent)
    DoublerNode.addAttribute(DoublerNode.aOutput)
    DoublerNode.addAttribute(DoublerNode.aInputB)
    DoublerNode.addAttribute(DoublerNode.aInputA)
    
    DoublerNode.attributeAffects(DoublerNode.aPercent, DoublerNode.aOutput)
    DoublerNode.attributeAffects(DoublerNode.aInputB, DoublerNode.aInputA)
    DoublerNode.attributeAffects(DoublerNode.aInputA, DoublerNode.aInputB)
    
def initializePlugin(obj):
    plugin = OpenMayaMPx.MPnPlugin(obj, 'Asim', '1.0', 'Any')
    try:
        plugin.registerNode()
    except:
        raise RuntimeError, 'Failed to register node'
    