from ...core.object_base import OpenSCADObject, OpenSCADConstant
from ... import import_scad
from pathlib import Path

importFile = Path(__file__).absolute().parent.parent.parent / 'libs' / 'BOSL2' / 'modular_hose.scad'
_ = import_scad(f'{importFile}', use_not_include=False)

_small_end = OpenSCADConstant('_small_end')
_big_end = OpenSCADConstant('_big_end')
_hose_waist = OpenSCADConstant('_hose_waist')

class modular_hose(OpenSCADObject):
    def __init__(self, size=None, type=None, clearance=None, waist_len=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("modular_hose" ,{"size" : size, "type" : type, "clearance" : clearance, "waist_len" : waist_len, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class modular_hose(OpenSCADObject):
    def __init__(self, size=None, type=None, clearance=None, waist_len=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("modular_hose" ,{"size" : size, "type" : type, "clearance" : clearance, "waist_len" : waist_len, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class modular_hose_radius(OpenSCADObject):
    def __init__(self, size=None, outer=None, **kwargs):
       super().__init__("modular_hose_radius" ,{"size" : size, "outer" : outer, **kwargs})

