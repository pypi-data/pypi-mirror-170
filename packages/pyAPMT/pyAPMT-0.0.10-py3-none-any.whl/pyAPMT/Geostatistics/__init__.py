# -*- coding: utf-8 -*-
"""

Geostatistical Module

"""

# Author: Sebastian Avalos <sebastian.avalos@apmodtech.com>
#         Advanced Predictive Modeling Technology
#         www.apmodtech.com/pyAPMT/
#         September-2022
#
# License: MIT License


# All submodules and packages
from . import Contact_Analysis
from . import Drill_Holes
from . import Probability_plots
from . import Slides_2D
from . import Nearest_Neighbor
from . import Variogram_Maps3D
from . import Capping_Analysis
from . import AdjustVarMod3D


from .Contact_Analysis import PlotContacs
from .Drill_Holes import DrillHoles
from .Probability_plots import ProbabilityPlot
from .Slides_2D import Plot2DSlides
from .Nearest_Neighbor import ComputeNearestNeighbor
from .Variogram_Maps3D import ComputeVariogramMaps3D
from .Capping_Analysis import ComputeCappingAnalysis
from .AdjustVarMod3D import AutomaticVariogramModel3D


__all__ = ['Contact_Analysis', 'PlotContacs', 'Drill_Holes', 'DrillHoles', \
           'Probability_plots', 'ProbabilityPlot', 'Slides_2D', 'Plot2DSlides',\
           'Nearest_Neighbor', 'ComputeNearestNeighbor',\
           'Variogram_Maps3D', 'ComputeVariogramMaps3D'\
           'Capping_Analysis', 'ComputeCappingAnalysis',\
           'Capping_Analysis', 'AutomaticVariogramModel3D']