# Single-Service-Queue-Simulation
Queue Simulation involving customers visiting one server. Provides average waiting time and percentage of customers who waited less than a specified time.

# Data to edit:
- opening_time/closing_time = 24hr time converted in seconds (e.g 10pm = 2200 x 60 x 60)
- wait_cap = (in seconds) generates percentage of customers who waited less than this duration for service.
- arrival_time = randint(x,y) where gap between arrivals is randomly selected between x seconds and y seconds.
- completion_time = randint(x,y) where duration of service is randomly selected between x seconds and y seconds.
