FlightStream lets you control Microsoft Flight Simulator from a Stream Deck, and see live data from Microsoft Flight Simulator on the Stream Deck.

It uses https://pypi.org/project/SimConnect/ and https://pypi.org/project/streamdeck/

This is an initial release; work in progress.

Presently only works for StreamDeck XL. Only tested with 747-800, but should work with most aircraft.

The UI is based around stages of flight, with pages listed down the left hand side:

* HOME shows the flight level set in the autopilot, altitude, throttle lever position, ground speed, true airspeed, whether the autopilot is on, minutes to the next waypoint, and distance to the next waypoint in kilometers, minutes to the final destination and touchdown vertical velocity. It also allows you to speed-up and slow-down the sim.

* GRND provides functions useful while on the ground: battery on, APU Start, turn on or off guidance ribbons, request ground services for power, fuel, catering, luggage, stairs, jetways and push back.

* VIEWS provides quick access to to the different types of views: Pilot, External, Drone. It also gives one-click access to several instrument views, cockpit views, and external views.

* TO / LAND lets you see the position of the flaps, spoilers, altitude, throttle, ground speed and true airspeed. It allows you to toggle LOC, APPR, Landing Gear, FLCH, HDG, taxi lights and landing lights. It also lets you increase or decrease flaps, change target flight level by 5000, 1000 or 100 and change target heading by 90, 10 or 1 degree.


## To run:

1. Add a profile to your Stream Deck with no buttons set, and make that profile active. Or exit the Stream Deck app.

2. Run Microsoft Flight Simulator

3. Run FlightStream
