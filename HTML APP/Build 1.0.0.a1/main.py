import eel
import pyowm
owm = pyowm.OWM("8bdd33f2a79072c140b1e6d317f98af0")

@eel.expose
def get_weather_icon(place):
	#owm = pyowm.OWM("8bdd33f2a79072c140b1e6d317f98af0")
	mgr = owm.weather_manager()

	observation = mgr.weather_at_place(place)
	w = observation.weather

	weat = w.status


	print(weat)
	print(place)
	if weat == 'Mist':
		return "https://image.flaticon.com/icons/svg/578/578116.svg"
	elif weat == 'Clear':
		return "https://image.flaticon.com/icons/svg/578/578153.svg"
	elif weat == 'Clouds':
		return "https://image.flaticon.com/icons/svg/578/578116.svg" #Clouds
	elif weat == 'Rain':
		return "https://image.flaticon.com/icons/svg/578/578132.svg"
@eel.expose
def get_weather(place):

	mgr = owm.weather_manager()

	observation = mgr.weather_at_place(place)
	w = observation.weather
	weath = w.status
	temp = w.temperature('celsius')['temp']

	return "В " + place + " сейчас " + str(temp) + " градусов"


eel.init("webs")
eel.start("main.html", size=(800, 700))
