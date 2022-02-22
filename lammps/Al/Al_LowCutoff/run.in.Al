variable lattice_spacing equal 3.80

label loop1
variable a loop 10
print "Lattice_spacing is ${lattice_spacing}"

units metal
boundary f f f
atom_style atomic

lattice fcc ${lattice_spacing} origin 0 0 0
region r1 block 0 8 0 8 0 8 units lattice side in
create_box 1 r1
#if "$a == 1" then "create_box 1 region$a"
#if "$a > 1" then "delete_atoms group 1" &
#"change_box 1 boundary p p f units lattice" &
#"reset_timestep 0"
mass 1 26.98
create_atoms 1 region r1
group 1 type 1
pair_style kim Morse_Shifted_GirifalcoWeizer_1959LowCutoff_Al__MO_411898953661_004
pair_coeff * * Al
neighbor 2.5 bin
neigh_modify every 1 delay 1
timestep 0.001
dump 1 all atom 100 dump.Al_${lattice_spacing}
thermo 100
thermo_style custom step temp press pe ke etotal
fix 1 all nvt temp 0.0001 0.0001 0.01
run 10000
unfix 1
clear
variable lattice_spacing equal ${lattice_spacing}+0.05
next a
jump SELF loop1
variable a delete
print "done..."