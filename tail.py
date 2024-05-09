from pysimm import system, lmps, forcefield
from pysimm.apps.random_walk import random_walk

def monomer():
    s = system.read_mol('/home/ii/pysimm/pysimm/Examples/PES_185_50/topo/PES_185.mol')
    f = forcefield.Dreiding()
    s.apply_forcefield(f)
    
    c1 = s.particles[11]
    c2 = s.particles[50]
    c1.linker = 'head'
    c2.linker = 'tail'
        
            
    for b in c1.bonds:
        if b.a.elem == 'H' or b.b.elem == 'H':
            pb = b.a if b.b is c2 else b.b
            s.particles.remove(pb.tag, update=False)
            break
            
    s.remove_spare_bonding()
    
    s.pair_style = 'lj/cut'
    
    lmps.quick_min(s, min_style='fire')
    
    s.add_particle_bonding()
    
    return s