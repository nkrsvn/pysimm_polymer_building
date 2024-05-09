from pysimm import system, lmps, forcefield
from pysimm.apps.random_walk import random_walk
from midle import monomer as monomerM
from tail import monomer as monomerT
from head import monomer as monomerH
from pysimm.apps.random_walk import copolymer

def run(test=False):
    # we'll create a pe monomer from the pysimm.models database
    chainM = monomerM()
    chainH = monomerH()
    chainT = monomerT()

    chainM.pair_style = 'lj'
    chainH.pair_style = 'lj'
    chainT.pair_style = 'lj'
    
    f = forcefield.Dreiding()
    chainM.apply_charges(f, charges='gasteiger')
    chainH.apply_charges(f, charges='gasteiger')
    chainT.apply_charges(f, charges='gasteiger')      

    print('Building polymer chain 1...')
    monochain = copolymer([chainT, chainM, chainH], 50, pattern=[1, 48, 1], forcefield=f)
    monochain.apply_charges(f, charges='gasteiger')
    monochain.write_xyz('monochain.xyz')
    monochain.write_yaml('monochain.yaml')
    monochain.write_lammps('monochain.lmps')
    monochain.write_chemdoodle_json('monochain.json')
    
#    print('Replicating polymer chain...')
#    uniform_polymer = system.replicate(monochain, 5, density=0.3, rand=True)     
#    uniform_polymer.write_xyz('uniform_polymer.xyz')
#    uniform_polymer.write_yaml('uniform_polymer.yaml')
#    uniform_polymer.write_lammps('uniform_polymer.lmps')
#    uniform_polymer.write_chemdoodle_json('uniform_polymer.json')
    
if __name__ == '__main__':
    run()