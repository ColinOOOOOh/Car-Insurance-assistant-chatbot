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
        r = requests.post('http://3.15.234.46:5000/chat_bot', json={"sender": "chatbot", "message": "query_insurance", "attribute": "-"})
        for k, v in r.json().items():
                print(k, ' k', v, 'v')

        #dispatcher.utter_message(r)
        return []

class ActionQueryInsuranceWithPrice(Action):
    def name(self) -> Text:
        return "action_query_insurance_with_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        price_range = tracker.get_slot("price_range")
        print(price_range,' price_range')
        r = requests.post('http://3.15.234.46:5000/chat_bot', json={"sender": "chatbot", "message": "query_insurance_with_price","attribute": "cheap"})
        for k, v in r.json().items():
            print(k, ' k', v, 'v')


        dispatcher.utter_message("We heve : 1. glass insurance ")
        return []

class ActionQueryInsuranceWithName(Action):
    def name(self) -> Text:
         return "action_query_insurance_with_price"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
         name = tracker.get_slot("name")
         print("name: ", name)
         r = requests.post('http://3.15.234.46:5000/query_with_name', json={"name": name})
         for k, v in r.json().items():
             print(k, ' k', v, 'v')
         dispatcher.utter_message("name")
         return []

class ActionBuyInsurance(Action):
    def name(self) -> Text:
        return "action_buy_insurance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        name = tracker.get_slot("name")
        coverage = tracker.get_slot("coverage")
        duration = tracker.get_slot("duration")
        uid = tracker.get_slot("uid")
        print(uid, "uid",  name, ' name', coverage, 'coverage', duration, ' duration')
        r = requests.post('http://3.15.234.46:5000/buy_ins', json={"uid": uid, "name": name, "coverage": coverage,"duration": duration})
        return_str = "Order success! You insurance id is : "
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
        name = tracker.get_slot("name")
        coverage = tracker.get_slot("coverage")
        duration = tracker.get_slot("duration")
        r = requests.post('http://3.15.234.46:5000/get_price', json={"name": name, "coverage": coverage,"duration": duration})
        return_str =  'Here is your order:       insurance name: ' + str(name) +  '\n coverage: ' + str(coverage) + '\n duration: ' + str(duration)
        for k, v in r.json().items():
            
            if str(v) == 'none':
                return_str = "Sorry. We do have this insurance. Please say 'restart' to restart the process"
            else:
                return_str += " "
                return_str += str(k)
                return_str += ": "
                return_str += str(v)
                return_str += "\n  To confirm your order, say yes. To cancel, please say no."
        print(return_str)
        dispatcher.utter_message(return_str)
        return []

class ActionMakeClaim(Action):
    def name(self) -> Text:
        return "action_make_claim"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        iid = tracker.get_slot("iid")
        description = tracker.get_slot("description")
        r = requests.post('http://3.15.234.46:5000/order', json={"iid": iid, "description": description})
        return_str = "We received your claim. Thank you.        Your claim tracking id is:    "       
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
