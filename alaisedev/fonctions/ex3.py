# étudiez et executez le code suivant pour le comprendre
# modifiez ensuite la fonction imbriquée pour qu'on puisse changer la température d'une station
# et qu'un subscriber puisse définir une température à partir de laquelle il est notifié

def create_weather_station(localisation):
    observers = []
    localisation = localisation
    current_temperature = None

    def subscribe(observer_name, threshold_temp):
        observers.append({
            'name': observer_name,
            'threshold': threshold_temp,
        })
    def change_temp(new_temp):
        nonlocal current_temperature
        old_temp = current_temperature
        current_temperature = new_temp
        print(f"\n{localisation} : température changée de {old_temp}°C à {new_temp}°C")
        notified_observers = []
        for observer in observers:
            if current_temperature >= observer['threshold']:
                print(f"{localisation} : notification envoyée à {observer['name']} (seuil: {observer['threshold']}°C)")
                notified_observers.append(observer['name'])

        if notified_observers:
            print(f"Observateurs notifiés: {', '.join(notified_observers)}")
        else:
            print("Aucun observateur notifié")

    def notify():
        for observer in observers:
            print(f"{localisation} : envoi d'un message à {observer} pour lui indiquer la température")
    return subscribe, notify, change_temp

"""
quimper_subscribe, quimper_notify = create_weather_station("quimper")
quimper_subscribe("olivier")
quimper_subscribe("pierre")
quimper_notify()
"""

quimper_subscribe, quimper_unsubscribe, quimper_change_temp = create_weather_station("quimper")
quimper_subscribe("olivier", 30)
quimper_subscribe("pierre", 27)
quimper_subscribe("marie", 29)
quimper_change_temp(24)
# notifications envoyées
quimper_change_temp(30)
# notifications envoyées
quimper_change_temp(32)
# notifications envoyées
