insurance(1, glass_insurance, full, 5, 12000, cheap).
insurance(2, theft_insurance, full, 5, 12000, cheap).
insurance(3, engine_insurance, partial, 6, 20000, medium).
insurance(4, engine_insurance, full, 4, 32000, expensive).
insurance(5, traffic_insurance, partial, 3, 30000, expensive).
insurance(6, traffic_insurance, full, 2, 25000, medium).
insurance(7, traffic_insurance, full, 1, 10000, cheap).
insurance(8, traffic_insurance, partial, 2, 9000, cheap).
insurance(9, traffic_insurance, full, 7, 50000, expensive).

car_model(corvette_c, super_sport).
car_model(mecedes_benz_e, luxury).
car_model(bmw_e, luxury).
car_model(toyota_camry, noble).
car_model(honda_accord, noble).
car_model(ford_f, truck).
car_model(toyota_corolla, compact).

occupation(commercial_driver, 36000, ).

illegal(AGE):- AGE < 16.
very_young(AGE):- AGE =< 18, \+ illegal(AGE).
young(AGE):- AGE =< 21, \+ very_young(AGE).
old(AGE):- AGE > 60.
experienced(AGE):- \+ young(AGE), \+ old(AGE).

newbie(AGE, PREV_ACCIDENTS):- (young(AGE); very_young(AGE)), PREV_ACCIDENTS =< 3.
careless(AGE, PREV_ACCIDENTS):- \+ newbie(AGE, PREV_ACCIDENTS).
good(AGE, PREV_ACCIDENTS):- \+ newbie(AGE, PREV_ACCIDENTS), PREV_ACCIDENTS =< 2.
well_done(AGE, PREV_ACCIDENTS):- good(AGE, PREV_ACCIDENTS), PREV_ACCIDENTS =< 1.
well_rounded(AGE, PREV_ACCIDENTS):- experienced(AGE), PREV_ACCIDENTS = 0.


can_afford(OCCUPATION, INSURANCE):- occupation(OCCUPATION, ANNUAL_INCOME, _, _).

