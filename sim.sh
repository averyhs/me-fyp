#!/bin/zsh

python -m cellsium simulate \
    -t SimulationDuration=6.0 \
    -t SimulationOutputInterval=0.5 \
    -t GroundTruthOnlyCompleteCells=False \
    -t GroundTruthOnlyCompleteCellsInImages=False \
    -t ChipmunkPlacementRadius=0.0 \
    -t NewCellBendOverallLower=-0.2 \
    -t NewCellBendOverallUpper=0.2 \
    -t NewCellLength1Mean=2.5 \
    -t NewCellLength1Std=0.15 \
    -t NewCellLength2Mean=10 \
    -t NewCellLength2Std=3 \
    -t NewCellLengthAbsoluteMax=15 \
    -t NewCellLengthAbsoluteMin=1 \
    -t NewCellWidthMean=0.5 \
    -t NewCellWidthStd=0.1 \
    -t NewCellWidthAbsoluteMax=1.5 \
    -t NewCellWidthAbsoluteMin=0.1 \
    -o simulate \
    --Output GenericMaskOutput \
    -c mycomodel.py:Cell \
    -p