variable a index Al_LowCutoff Al_HighCutoff Al_MedCutoff
label loop1
shell cd ./$a
shell lmp -i run.in.Al
shell cd ..
next a
jump SELF loop1
print "Done!"