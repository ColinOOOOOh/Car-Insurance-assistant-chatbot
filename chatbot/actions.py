from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests
from rasa_core.events import AllSlotsReset
class ActionQueryInsurance(Action):
    def name(self) -> Text:
        return "action_query_insurance"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        r = requests.post('http://0.0.0.0:5000/chat_bot', json={"message": "query_insurance", "attribute": "-"})
        return_str = "You may be interested in the following: *"
        ret_str = r.json()['car_insurance']
        ret_list = []
        for i in range(len(ret_str)):
            if ret_str[i]['name'] in ret_list:
                continue
            else:
                ret_list.append(ret_str[i]['name'])
                return_str += str(ret_str[i]['name']) +'*'
        dispatcher.utter_message(return_str)
        return []

class ActionQueryInsuranceWithPrice(Action):
    def name(self) -> Text:
        return "action_query_insurance_with_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        price_range = tracker.get_slot("price_range")
        print(price_range,' price_range')
        r = requests.post('http://0.0.0.0:5000/chat_bot', json={ "message": "query_insurance_with_price","attribute": price_range})
        return_str = "We have :*"
        ret_str = r.json()['car_insurance']
        ret_list = []
        for i in range(len(ret_str)):
            if ret_str[i]['name'] in ret_list:
                continue
            else:
                ret_list.append(ret_str[i]['name'])
                return_str += str(ret_str[i]['name']) +'*'
        dispatcher.utter_message(return_str)
        return []

class ActionQueryInsuranceWithName(Action):
    def name(self) -> Text:
         return "action_query_insurance_with_name"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
         name = tracker.get_slot("car_insurance")
         print("car_insurance: ", name)
         r = requests.post('http://0.0.0.0:5000/chat_bot', json={"message": "query_insurance_with_name", "attribute": name})
         return_str = ""
         print(r.json())
         for k, v in r.json().items():
             return_str += str(v[0]['description']) 
         dispatcher.utter_message(return_str)
         return []

class ActionBuyInsurance(Action):
    def name(self) -> Text:
        return "action_buy_insurance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        name = tracker.get_slot("car_insurance")
        coverage = tracker.get_slot("coverage")
        duration = tracker.get_slot("duration")
        uid = tracker.get_slot("uid")
        print(uid, "uid",  name, ' name', coverage, 'coverage', duration, ' duration')
        r = requests.post('http://0.0.0.0:5000/buy_ins', json={"uid": uid, "name": name, "coverage": coverage,"duration": duration})
        return_str = "Order success! *You insurance id is : "
        for k, v in r.json().items():
            return_str += str(v)
        dispatcher.utter_message(return_str)
        return []

class ActionShowOrder(Action):
    def name(self) -> Text:
        return "action_show_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        name = tracker.get_slot("car_insurance")
        coverage = tracker.get_slot("coverage")
        duration = tracker.get_slot("duration")
        r = requests.post('http://0.0.0.0:5000/get_price', json={"name": name, "coverage": coverage,"duration": duration})
        return_str =  'Here is your order:*       insurance name: ' + str(name) +  '* coverage: ' + str(coverage) + '* duration: ' + str(duration)
        for k, v in r.json().items():
            
            if str(v) == 'none':
                return_str = "Sorry. We do have this insurance. Please say 'restart' to restart the process"
            else:
                return_str += " "
                return_str += str(k)
                return_str += ": "
                return_str += str(v) + " dollars *"
                return_str += "To confirm your order, say yes. To cancel, please say no."
        print(return_str)
        dispatcher.utter_message(return_str)
        return []

class ActionMakeClaim(Action):
    def name(self) -> Text:
        return "action_make_claim"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        iid_tmp = tracker.get_slot("iid")
        _, iid = iid_tmp.split(" ")
        uid = tracker.get_slot("uid")
        description = tracker.get_slot("description")
        r = requests.post('http://0.0.0.0:5000/order', json={"iid": iid, "uid": uid, "description": description})
        return_str = "We received your claim. Thank you. * Your claim tracking id is:    "       
        for k, v in r.json().items():
            return_str += str(v)
        dispatcher.utter_message(return_str)
        return []

class ActionSetUid(Action):
    def name(self)-> Text:
        return "action_set_uid"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        uid = tracker.get_slot("uid")
        _, uid1 = uid.split(" ")
        print(uid1)
        return [SlotSet("uid", uid1)]

