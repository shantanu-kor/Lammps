variable t equal 0.0
label loop1
variable a loop 20
variable t equal $t+100
print "Temperature is $t"
label loop2
variable b index "Morse_Shifted_GirifalcoWeizer_1959HighCutoff_Ni__MO_381861218831_004" "Morse_Shifted_GirifalcoWeizer_1959LowCutoff_Ni__MO_322509103239_004" "Morse_Shifted_GirifalcoWeizer_1959MedCutoff_Ni__MO_758825945924_004"
variable c index "HighCutoff" "LowCutoff" "MedCutoff"
units metal
boundary p p p
atom_style atomic
lattice custom 3.5238 a1 1.0 0.0 0.0 a2 0.0 1.0 0.0 a3 0.0 0.0 1.0 basis 0.25 0.25 0.25 basis 0.25 0.75 0.75 basis 0.75 0.25 0.75 basis 0.75 0.75 0.25
region 1 sphere 20.0 20.0 20.0 5.0
region 2 block 0.0 40.0 0.0 40.0 0.0 40.0
create_box 1 2
mass 1 58.6934
create_atoms 1 region 1
group 1 type 1
pair_style kim $b
pair_coeff * * Ni
neighbor 2.5 bin
neigh_modify every 1 delay 1
dump 1 all atom 100 dump.Ni_$t_$c
compute 1 1 pe/atom
compute 2 1 ke/atom
compute ape 1 reduce ave c_1
compute ake 1 reduce ave c_2
thermo_style custom step temp c_ape c_ake
thermo 100
fix 1 1 nvt temp $t $t 0.01 fixedpoint 20.0 20.0 20.0
timestep 0.001
run 20000
write_data Ni_$t_$c.data
clear
next b
next c
jump SELF loop2
clear
next a
jump SELF loop1
variable a delete
print "Done!"