##greet + search insurance + goodbye
* greet
  - utter_greet
* query_insurance
  - action_query_insurance
* goodbye
  - utter_goodbye

## search insurance
* query_insurance
  - action_query_insurance

## greet+ search insurance
* greet
  - utter_greet
* query_insurance
  - action_query_insurance

## search insurance with price range = cheap 1
* greet
  - utter_greet
* query_insurance_with_price{"price_range":"cheap"}
  - action_query_insurance_with_price

## search insurance with price range = cheap 2
* greet
  - utter_greet
* query_insurance_with_price{"price_range":"cheap"}
  - action_query_insurance_with_price
* goodbye
  - utter_goodbye

## search insurance with price range = cheap 3 
* query_insurance_with_price{"price_range":"cheap"}
  - action_query_insurance_with_price

## search insurance with price range = cheap 4
* greet
  - utter_greet
* query_insurance_with_price{"price_range":"cheap"}
  - action_query_insurance_with_price
* goodbye
  -  utter_goodbye

## search insurance with price range = medium
* greet
  - utter_greet
* query_insurance_with_price{"price_range":"medium"}
  - action_query_insurance_with_price
* goodbye
  - utter_goodbye

## search insurance with price range = expensive
* greet
  - utter_greet
* query_insurance_with_price{"price_range":"expensive"}
  - action_query_insurance_with_price
* goodbye
  - utter_goodbye


## search insurance with price range = expensive 2
* query_insurance_with_price{"price_range":"expensive"}
  - action_query_insurance_with_price

## search insurance with price range = expensive 3
* query_insurance_with_price{"price_range":"expensive"}
  - action_query_insurance_with_price
* goodbye
  - utter_goodbye

## search with name
* greet
  - utter_greet
* query_insurance_with_name{"car_insurance":"glass insurance"}
  - action_query_insurance_with_name
* goodbye
  - utter_goodbye

## search with name
* query_insurance_with_name{"car_insurance":"theft insurance"}
  - action_query_insurance_with_name


## search with nam 2e
* query_insurance_with_name{"car_insurance":"engine insurance"}
  - action_query_insurance_with_name

## search with nam 3
* query_insurance_with_name{"car_insurance":"traffic insurance"}
  - action_query_insurance_with_name



## buy_insurance 1
* greet
  - utter_greet
* buy_insurance
  - utter_ask_name
* inform{"car_insurance": "glass insurance"}
  - utter_ask_duration
* inform{"duration": "3 years"}
  - utter_ask_coverage
* inform{"coverage": "full"}
  - action_show_order
  - utter_ask_confirm_order
* affirm
  - action_buy_insurance

## buy_insurance 2
* greet
  - utter_greet
* buy_insurance
  - utter_ask_name
* inform{"car_insurance": "robber insurance"}
  - utter_ask_duration
* inform{"duration": "5 years"}
  - utter_ask_coverage
* inform{"coverage": "full"}
  - action_show_order
* affirm
  - action_buy_insurance

## buy_insurance 3
* greet
  - utter_greet
* buy_insurance
  - utter_ask_name
* inform{"car_insurance": "glass insurance"}
  - utter_ask_duration
* inform{"duration": "10 years"}
  - utter_ask_coverage
* inform{"coverage": "partial"}
  - action_show_order
* affirm
  - action_buy_insurance

## buy_insurance 4
* greet
  - utter_greet
* buy_insurance
  - utter_ask_name
* inform{"car_insurance": "engine insurance"}
  - utter_ask_duration
* inform{"duration": "5 years"}
  - utter_ask_coverage
* inform{"coverage": "full"}
  - action_show_order
* affirm
  - action_buy_insurance

## buy_insurance 5 fail
* greet
  - utter_greet
* buy_insurance
  - utter_ask_name
* inform{"car_insurance": "engine insurance"}
  - utter_ask_duration
* inform{"duration": "3 years"}
  - utter_ask_coverage
* inform{"coverage": "partial"}
  - action_show_order
* deny
  - utter_fail

## buy_insurance 6 fail
* greet
  - utter_greet
* buy_insurance
  - utter_ask_name
* inform{"car_insurance": "glass insurance"}
  - utter_ask_duration
* inform{"duration": "10 years"}
  - utter_ask_coverage
* inform{"coverage": "full"}
  - action_show_order
* deny
  - utter_fail

## buy_insurance 7 restart
* greet
  - utter_greet
* buy_insurance
  - utter_ask_name
* inform{"car_insurance": "glass insurance"}
  - utter_ask_duration
* inform{"duration": "10 years"}
  - utter_ask_coverage
* inform{"coverage": "full"}
  - action_show_order
* restart
  - utter_restart

## claim 1
* make_claim
  - utter_ask_id
* inform{"iid": "iid 02"}
  - utter_ask_what_happen
* inform{"description": "My car is broken"}
  - action_make_claim

## claim 2
* make_claim
  - utter_ask_id
* inform{"iid": "iid 01"}
  - utter_ask_what_happen
* inform{"description": "My car glass is broken"}
  - action_make_claim

## claim 3
* make_claim
  - utter_ask_id
* inform{"iid": "iid 03"}
  - utter_ask_what_happen
* inform{"description": "I hit a tree"}
  - action_make_claim

## claim 4
* make_claim
  - utter_ask_id
* inform{"iid": "iid 01"}
  - utter_ask_what_happen
* inform{"description": "My engine doesn't work"}
  - action_make_claim

## claim 5
* make_claim
  - utter_ask_id
* inform{"iid": "insurance id 032"}
  - utter_ask_what_happen
* inform{"description": "My engine is broken"}
  - action_make_claim

## claim 6
* make_claim
  - utter_ask_id
* inform{"iid": "iid 05"}
  - utter_ask_what_happen
* inform{"description": "My car was stolen"}
  - action_make_claim

## claim 7
* make_claim
  - utter_ask_id
* inform{"iid": "iid 05"}
  - utter_ask_what_happen
* inform{"description": "My car is crashed"}
  - action_make_claim

## claim 8
* make_claim
  - utter_ask_id
* inform{"iid": "iid 09"}
  - utter_ask_what_happen
* inform{"description": "My car was damaged"}
  - action_make_claim

## set uid 1
* set_uid
  - action_set_uid{"uid": "uid 1"}

## set uid 2
* set_uid
  - action_set_uid{"uid": "uid 2"}

## set uid 3
* set_uid
  - action_set_uid{"uid": "uid 30"}

## set uid 4
* set_uid
  - action_set_uid{"uid": "uid 3"}

## set uid 5
* set_uid
  - action_set_uid{"uid": "uid 8"}



## Hello
* greet
- utter_greet

## Bye
* goodbye
- utter_goodbye

## what can i do
* ask_what_can_i_do
  - utter_what_can_i_do
