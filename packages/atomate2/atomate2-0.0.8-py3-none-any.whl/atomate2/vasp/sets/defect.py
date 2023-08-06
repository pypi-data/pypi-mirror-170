"""Module defining VASP input set generators for defect calculations."""

from __future__ import annotations

from dataclasses import dataclass

from pymatgen.core import Structure
from pymatgen.io.vasp import Outcar, Vasprun

from atomate2.vasp.sets.base import VaspInputGenerator


@dataclass
class AtomicRelaxSetGenerator(VaspInputGenerator):
    """Class to generate VASP atom-only relaxation input sets."""

    use_structure_charge: bool = True

    def get_incar_updates(
        self,
        structure: Structure,
        prev_incar: dict = None,
        bandgap: float = 0,
        vasprun: Vasprun = None,
        outcar: Outcar = None,
    ) -> dict:
        """
        Get updates to the INCAR for a relaxation job.

        Parameters
        ----------
        structure
            A structure.
        prev_incar
            An incar from a previous calculation.
        bandgap
            The band gap.
        vasprun
            A vasprun from a previous calculation.
        outcar
            An outcar from a previous calculation.

        Returns
        -------
        dict
            A dictionary of updates to apply.
        """
        return {
            "IBRION": 2,
            "ISIF": 2,
            "EDIFFG": -0.05,
            "LREAL": False,
            "NSW": 99,
            "LCHARG": False,
            "ENCUT": 500,
            "LAECHG": False,
            "NELMIN": 6,
        }
