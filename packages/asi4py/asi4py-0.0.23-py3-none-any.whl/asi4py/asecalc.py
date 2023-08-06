from ase.calculators.calculator import Calculator, all_changes
from .pyasi import ASIlib
from ase import units

"""
# FHI-AIMS conversion constants
bohr    = 0.52917721
hartree = 27.2113845
hartree_over_bohr = 51.42206426
bohr_over_hartree = 0.019446905
"""
bohr    = units.Bohr
hartree = units.Hartree


class ASI_ASE_calculator(Calculator):
  '''
    ASI ASI calc
  '''
  implemented_properties = ['energy', 'free_energy', 'forces', 'charges', 'stress']
  supported_changes = {}

  def __init__(self, lib_file_name, init_func, mpi_comm, atoms, work_dir='asi.temp', logfile='asi.log'):
    Calculator.__init__(self)
    self.atoms = atoms.copy()
    self.asi = ASIlib(lib_file_name, init_func, mpi_comm, atoms, work_dir, logfile)
    self.asi.init()
    self.DM_init_callback = None

  def todict(self):
      d = {'type': 'calculator',
           'name': 'ASI wrapper'}
      return d

  def calculate(self, atoms=None, properties=['energy'],
                system_changes=all_changes):
      bad = [change for change in system_changes
             if change not in self.supported_changes]

      # First time calculate() is called, system_changes will be
      # all_changes.  After that, only positions and cell may change.
      if self.atoms is not None and any(bad):
          raise PropertyNotImplementedError(
              'Cannot change {} through ASI API.  '
              .format(bad if len(bad) > 1 else bad[0]))
      
      #print("calculate:", properties)

      self.atoms = atoms.copy()
      self.asi.atoms = atoms
      self.asi.set_geometry()
      results = {}
      self.asi.run()
      results['free_energy'] = results['energy'] = self.asi.total_energy * hartree
      
      if 'forces' in properties:
        if self.asi.total_forces is not None:
          results['forces'] = self.asi.total_forces * (hartree / bohr)

      if 'stress' in properties:
        if self.asi.stress is not None:
          results['stress'] = self.asi.stress

      # Charges computation breaks total_energy on subsequent SCF calculations in AIMS:  results['charges'] = self.asi.atomic_charges

      self.results.update(results)

  def close(self):
      self.asi.close()

  def __del__(self):
      self.close()
