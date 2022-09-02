import sdf
# ----------------------------------------
# operations that can be used to merge sdf
# this is used to start with something but
# one should be able to extend it
# ---------------------------------------


operations_2d = {
    '∪':  {'name': 'union', 'func': sdf.d2.union},
    '∩':  {'name': 'intersection', 'func': sdf.d2.intersection},
    'b':  {'name': 'blend','func': sdf.d2.blend},
    '~∪': {'name': 'negate_union','func': lambda s1,s2: sdf.d2.negate(sdf.d2.union(s1, s2))},
    '~∩': {'name': 'negate_intersection','func': lambda s1,s2: sdf.d2.negate(sdf.d2.intersection(s1, s2))},
    '-':  {'name': 'difference', 'func': sdf.d2.difference},
}

operations_3d = {
    '∪':  {'name': 'union', 'func': sdf.d3.union},
    '∩':  {'name': 'intersection', 'func': sdf.d3.intersection},
    'b':  {'name': 'blend','func': sdf.d3.blend},
    '~∪': {'name': 'negate_union','func': lambda s1,s2: sdf.d3.negate(sdf.d3.union(s1, s2))},
    '~∩': {'name': 'negate_intersection','func': lambda s1,s2: sdf.d3.negate(sdf.d3.intersection(s1, s2))},
    '-':  {'name': 'difference', 'func': sdf.d3.difference},
}