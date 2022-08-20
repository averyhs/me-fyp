from cellsium.model import assemble_cell, SimulatedCell, h_to_s, RodShaped
from cellsium.simulation.simulator import Timestep
from cellsium.model.agent import (
    Copyable,
    IdCounter,
    InitializeWithParameters,
    Representable,
    WithLineage,
    WithLineageHistory,
    WithRandomSequences,
    WithTemporalLineage,
)
from typing import Any, Iterable, Mapping, Optional
from random import randint
from math import cos, sin
from cmath import pi

class MycoCellModel(SimulatedCell):
    @staticmethod
    def random_sequences(sequence):
        return dict(elongation_rate=sequence.normal(0.5, 0.09))  # µm·h⁻¹ (mean & std?)

    def birth(self, parent=None, ts=None) -> None:
        self.elongation_rate = next(self.random.elongation_rate)
        self.division_time = h_to_s(3)

    def grow(self, ts) -> None:
        self.length += self.elongation_rate * ts.hours

        if ts.time > (self.birth_time + self.division_time):
            offspring_a, offspring_b = self.divide(ts)
            offspring_a.length = offspring_b.length = self.length / 2
    
    def divide(self, ts: Timestep) -> Iterable["SimulatedCell"]:
        """
        Called when a cell should divide, creates the daughter cells.
        :param ts: Timestep
        :return: None
        """

        # My division behavior
        # --------------------
        division_angle = randint(-45,45) * pi/180
        x, y = self.position
        alpha = self.angle
        length = self.length

        offspring_a, offspring_b = self.copy(), self.copy()

        offspring_a.position = [float(x-(length/4)*cos(alpha+division_angle)), float(y-(length/4)*sin(alpha+division_angle))]
        offspring_b.position = [float(x+(length/4)*cos(alpha)), float(y+(length/4)*sin(alpha))]
        offspring_a.angle = self.angle
        offspring_b.angle = self.angle + division_angle
        # --------------------

        if isinstance(self, WithLineage):
            offspring_a.parent_id = offspring_b.parent_id = self.id_

        if isinstance(self, WithLineageHistory):
            offspring_a.lineage_history = self.lineage_history[:] + [self.id_]
            offspring_b.lineage_history = self.lineage_history[:] + [self.id_]

        if isinstance(self, WithTemporalLineage):
            now = ts.simulation.time
            offspring_b.birth_time = offspring_a.birth_time = now

        ts.simulator.add(offspring_a)
        ts.simulator.add(offspring_b)

        offspring_a.birth(parent=self, ts=ts)
        offspring_b.birth(parent=self, ts=ts)

        ts.simulator.remove(self)

        return offspring_a, offspring_b



Cell = assemble_cell(MycoCellModel, RodShaped)