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

occupation(commercial_driver, 36000, high_risk).
occupation(student, 5000, low_risk).
occupation(engineer, 100000, low_risk).
occupation(cashier, 40000, low_risk).
occupation(trump_supporter, 32000, high_risk).

risk_requirement(low_risk, partial).
risk_requirement(low_risk, full).
risk_requirement(high_risk, full).

car_requirement(super_sport, traffic_insurance).
car_requirement(super_sport, engine_insurance).
car_requirement(super_sport, theft_insurance).

car_requirement(luxury, traffic_insurance).
car_requirement(luxury, theft_insurance).
car_requirement(luxury, glass_insurance).

car_requirement(noble, traffic_insurance).
car_requirement(noble, theft_insurance).

car_requirement(truck, traffic_insurance).
car_requirement(truck, engine_insurance).

car_requirement(compact, traffic_insurance).


illegal(AGE):- 
        AGE < 16.
very_young(AGE):- 
        AGE =< 18, \+ illegal(AGE).
young(AGE):- 
        AGE =< 21, \+ very_young(AGE).
old(AGE):- 
        AGE > 60.
experienced(AGE):- 
        \+ young(AGE), \+ old(AGE).

newbie(AGE, PREV_ACCIDENTS):- 
        (young(AGE); very_young(AGE)), PREV_ACCIDENTS =< 3.
careless(AGE, PREV_ACCIDENTS):- 
        \+ newbie(AGE, PREV_ACCIDENTS).
good(AGE, PREV_ACCIDENTS):- 
        \+ newbie(AGE, PREV_ACCIDENTS), PREV_ACCIDENTS =< 2.
well_done(AGE, PREV_ACCIDENTS):- 
        good(AGE, PREV_ACCIDENTS), PREV_ACCIDENTS =< 1.
well_rounded(AGE, PREV_ACCIDENTS):- 
        experienced(AGE), PREV_ACCIDENTS = 0.

can_afford(OCCUPATION, INSURANCE_ID):- 
        occupation(OCCUPATION, ANNUAL_INCOME, _), 
        insurance(INSURANCE_ID, _, _, _, COST, _),
        ANNUAL_INCOME / 2 >= COST.

high_risk(AGE, PREV_ACCIDENTS):-
        newbie(AGE, PREV_ACCIDENTS);
        careless(AGE, PREV_ACCIDENTS).

combined_risk_requirement(RISK, COVERAGE, AGE, PREV_ACCIDENTS):-
        \+ high_risk(AGE, PREV_ACCIDENTS); risk_requirement(RISK, COVERAGE).

required_minimum(OCCUPATION, AGE, PREV_ACCIDENTS, CAR_MODEL, INSURANCE_ID):-
        occupation(OCCUPATION, _, RISK), 
        insurance(INSURANCE_ID, INSURANCE_TYPE, COVERAGE, _, _, _),
        car_model(CAR_MODEL, CLASS),
        (INSURANCE_TYPE \= traffic_insurance; 
         combined_risk_requirement(RISK, COVERAGE, AGE, PREV_ACCIDENTS)),
        car_requirement(CLASS, INSURANCE_TYPE).

pick(OCCUPATION, AGE, PREV_ACCIDENTS, CAR_MODEL, 
     INSURANCE_ID, INSURANCE_TYPE, INSURANCE_COVERAGE, 
     INSURANCE_DURATION, INSURANCE_PRICE, INSURANCE_PRICE_RANGE):-
     \+ illegal(AGE),
     required_minimum(OCCUPATION, AGE, PREV_ACCIDENTS, CAR_MODEL, INSURANCE_ID),
     (high_risk(AGE, PREV_ACCIDENTS); can_afford(OCCUPATION, INSURANCE_ID)),
     insurance(INSURANCE_ID, INSURANCE_TYPE, INSURANCE_COVERAGE, 
               INSURANCE_DURATION, INSURANCE_PRICE, INSURANCE_PRICE_RANGE).

