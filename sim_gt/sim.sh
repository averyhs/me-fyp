#!/bin/zsh

python -m cellsium simulate \
    -t SimulationDuration=9.0 \
    -t SimulationOutputInterval=0.5 \
    -t GroundTruthOnlyCompleteCells=False \
    -t GroundTruthOnlyCompleteCellsInImages=False \
    -t NewCellCount=3 \
    -t NewCellRadiusFromCenter=20.0 \
    -t ChipmunkPlacementRadius=0.0001 \
    -t NewCellLength1Mean=3.5 \
    -t NewCellLength1Std=0.2 \
    -t NewCellLength2Mean=2.5 \
    -t NewCellLength2Std=0.15 \
    -t NewCellLengthAbsoluteMax=6 \
    -t NewCellLengthAbsoluteMin=1 \
    -t NewCellWidthMean=0.5 \
    -t NewCellWidthStd=0.1 \
    -t NewCellWidthAbsoluteMax=1.5 \
    -t NewCellWidthAbsoluteMin=0.1 \
    -t LuminanceBackground=0.35 \
    -t LuminanceCell=0.2 \
    -t Seed=9 \
    -o simulate \
    --Output GenericMaskOutput \
    -c mycomodel.py:Cell \
    -p