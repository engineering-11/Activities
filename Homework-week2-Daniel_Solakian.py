#!/usr/bin/env python
# coding: utf-8

# 1.a Assume an average human mass of 70kg. What is the activity (Bq) of that person?

# Humans have radioisotopes in them, the γ radition producer is K-40 Carbon is negligible
# 
#     Finding the percentage of Potassium in humans, with M_0= 70 kg
#     
#     .4% *70 kg = 0.28 kg
#     
#     Natural abundance of radioisotope K-40 is .012% respectively, and use stoichiometry to determine number of atoms 
#         
#     .28 kg * 1000g/1 kg* 1 mol/39.098 g * 6.0223*10^23 atoms/1mol = 4.3*10^24 atoms
#         N = 4.3 * 10^24 atoms * .00012 = 5.18 * 10^20 atoms K-40
#         
# t(1/2) for K-40 = 1.248 * 10^9 yr
# 
#     Find the decay constant λ = ln(2)/ t(1/2)
#     
#     λ= 5.55 * 10^-10 /yr
#     
#     Activity of humans is ΔN/Δt = λN = (5.18 * 10^20) * (5.55*10^-10) = 2.8749*10^11 decay/year
#     
#     Convert decay/year => second 
#     
#     2.8749*10^11 decay/year * 1 yr / 31536000 s = 9116.25 Bq
#     
#     The branching ratio of k-40 is 10.66% gamma radiation, so a portion of the total activity.
#     
#     .1066 * 9116.25 = 971.79 Bq

# 1b. How radioactive am I?
#     
#     Using specific activity, and m = 55 kg
#     
#     Specific activity = λN/m
#     
#     Determine N, number of γ emitting radioisotopes in me (k-40)
#     
#     .4% * 55 kg = .22 kg
#     
#     .22 kg => atoms (from part 1a.) = 3.388679728 * 10^24 atoms 
#     
#     3.388679728 * 10^24 atoms * .00012 = 4.066416 * 10 ^ 20 k-40 atoms
#     
#     λ = 5.55 * 10^-10 /year 
#     λ in seconds = 5.55 * 10^-10 /year * 1 yr / 31536000 s = 1.7599 * 10^-17 /s
#     
# Specific activity 
#     
#     A = (λ * N)/m = (1.7599 * 10^-17 /s * 4.066416 * 10 ^ 20 k-40 atoms)/55 kg = 130.12  bq/kg
#     
#     130.12 bq/kg * 55 kg = 7162.77 bq for a 55 kg "me"

# References:
#     
#     https://en.wikipedia.org/wiki/Composition_of_the_human_body
#         
#     Lecture 2 slides for eq
#     
#     Chris and Ali helped :^)

# 2. Activity of a 120 g banana

# 2a. The components that contribute to the activity of a banana are the elements that have some natural abundance of radioisotopes. The elements are potassium, carbon, and hydrogen. 
# 
#     However, the only components that will contribute significantly to the activity of the banana is the potassium and its natural abundance of potassium 40 (K-40).
#     
#     Trace amounts of radioactive C-14 and tritium occur naturally and are negligible in the calculation.

# 2b. Activity just from gamma radiation
# 
#     m = 120 g
#     
#     m_k = 358 mg/100 g => .358/100 g; .385/100 = x /120 => .4296 g K in a banana of 120 g
#     
#     m_k = .4296 g K 
#     
# Number of K-40 atoms in a banana 
#     
#     N = .4296 g * 1 mol/39.098 g * 6.0223*10^23 atoms/1mol = 6.61717 * 10^21 K atoms
#     
#     K-40 is .012% of K (natural abundance)
#     
#     .00012 * 6.61717 * 10^21 K atoms = 7.9406 * 10^17 k-40 atoms = N_k
#     
# Activity of Banana 
#     activity = λN = 7.9406 * 10^17 atoms * 5.55 * 10^-10 /yr = 440703343.7 decays/year
#     
#     440703343.7 decays/ year to decays/sec => 13.98 Bq
#     
# Gamma Activity from total for K-40 is 10.66%
#     
#     13.98 Bq * .1066 = 1.49 Bq

# Activity from electrons is the β- decay from K-40
#     
#     The percentage of the β- decay in k-40 is 89.27%
#     
#     Total activity is 13.98 Bq
#     
#     .8927 * 13.98 = 12.479946 Bq for β- decay from branching ratios

# 2d. Total activity of banana found above 
#     13.98 Bq

# 2e. Purchasing a banana, the the peel blocks the beta decays, so only gammas are exposed.
#     
#     The typical group of bananas bought at a store is 8 bananas. 
#     
#     Gamma activity * 8 medium bananas = 1.49 * 8 = 11.92 Bq for 8 medium sized bananas

# 2f. Eating the banana, you are exposed to the total activity of the banana:
#     assuming the mass and activity of the peel is negligble, and only one is eaten at a time, the activity is...
#     13.98 Bq.

# References
#     https://www.ptable.com/
#         
#     Lecture 2 slides
#     
#     https://en.wikipedia.org/wiki/Banana#Nutrition
#     
#     IAEA Nuclear Data Section
