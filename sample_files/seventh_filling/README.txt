To generate the pseudopotential:

1) I first obtain the Coulomb pseudo-potential for 35 flux quanta in the lowest Landau level:

/usr/local/DiagHam/build/FQHE/src/Programs/FQHEOnSphere/CoulombPseudopotentials -s 35 -l 0

2) Then a make a copy with V_1=V_3=V_5=1 only (to get the Laughlin state):

cp pseudopotential_coulomb_l_0_2s_35.dat pseudopotential_Laughlin_l_0_2s_35.dat

and edit the new file.

To generate the vec file:

3) I generate the complete spectrum for the Laughlin pseudopotential with the first eigenvector:

/usr/local/DiagHam/build/FQHE/src/Programs/FQHEOnSphere/FQHESphereFermionsTwoBodyGeneric -p 6 -l 35 --interaction-name Laughlin_l_0 --interaction-file pseudopotential_Laughlin_l_0_2s_35.dat --use-lapack -g --eigenstate -n 1

4) Alternatively, I can generate a set of vec files for different momentum sectors for the torus:

/usr/local/DiagHam/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsTwoBodyGeneric -p 6 -l 35 --interaction-name Laughlin_l_0 --interaction-file pseudopotential_Laughlin_l_0_2s_35.dat --use-lapack -g --eigenstate -n 1
