#!/bin/zsh

python -m cellsium simulate \
    -t SimulationDuration=6.0 \
    -t SimulationOutputInterval=0.5 \
    -t GroundTruthOnlyCompleteCells=False \
    -t GroundTruthOnlyCompleteCellsInImages=False \
    -t ChipmunkPlacementRadius=0.0 \
    -t NewCellLength1Mean=9 \
    -t NewCellLength1Std=1.3 \
    -t NewCellLength2Mean=2.5 \
    -t NewCellLength2Std=0.15 \
    -t NewCellLengthAbsoluteMax=15 \
    -t NewCellLengthAbsoluteMin=1 \
    -t NewCellWidthMean=0.5 \
    -t NewCellWidthStd=0.1 \
    -t NewCellWidthAbsoluteMax=1.5 \
    -t NewCellWidthAbsoluteMin=0.1 \
    -t LuminanceBackground=0.35 \
    -t LuminanceCell=0.2 \
    -o simulate \
    --Output GenericMaskOutput \
    -c mycomodel.py:Cell \
    -p