from datetime import datetime, timedelta
from rasa_sdk import Action


def text_date_to_int(text_date):
    if text_date == "mañana":
        return 1
    if text_date == "ayer":
        return -1
    if text_date == "hoy":
        return 0


weekday_mapping = [
    "lunes",
    "martes",
    "miércoles",
    "jueves",
    "viernes",
    "sábado",
    "domingo"
]


def weekday_to_text(weekday: int):
    return weekday_mapping[weekday]


def display_date_support_error(text_date):
    return f"""El sistema actualmente no puede procesar 
la consulta de la fecha para {text_date}"""


class ActionQueryTime(Action):
    def name(self):
        return "action_query_time"

    def run(self, dispatcher, tracker, domain):
        fecha = datetime.now()
        hora = fecha.strftime("%H:%M:%S")
        dispatcher.utter_message("Son las " + hora)
        return []
    
    
class ActionQueryDate(Action):
    def name(self):
        return "action_query_date"
    
    def run(self, dispatcher, tracker, domain):
        text_date = tracker.get_slot("fecha") or "hoy"
        int_date = text_date_to_int(text_date)
        if int_date is not None: 
            delta = timedelta(days=int_date)
            current_date = datetime.now()
            target_date = current_date + delta
            dispatcher.utter_message(
                text=target_date.strftime("Es %A %d de %B de %Y")
            )
        else:
            dispatcher.utter_message(
                display_date_support_error(text_date)
            )
        
        return []
                        

class ActionQueryWeekday(Action):
    def name(self):
        return "action_query_weekday"
    
    def run(self, dispatcher, tracker, domain):
        text_date = tracker.get_slot("fecha") or "hoy"
        int_date = text_date_to_int(text_date)
        if int_date is not None: 
            delta = timedelta(days=int_date)
            current_date = datetime.now()
            target_date = current_date + delta
            dispatcher.utter_message(
                text=weekday_to_text(target_date.weekday())
            )
        else:
            dispatcher.utter_message(
                text=display_date_support_error(text_date)
            )
        return []
    
    