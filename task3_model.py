class SmartThermostatAgent:
    def __init__(self, target_temperature):
        self.target_temp = target_temperature
        self.previous_action = None
        self.temperature_history = []
    
    def sense_environment(self, current_temp):
        self.temperature_history.append(current_temp)
        return current_temp
    
    def make_decision(self, current_temp):
        # Get the last action from memory
        last_action = self.previous_action
        
        # Check if temperature is within comfortable range
        comfortable_range = 1.0  # 1 degree tolerance
        lower_bound = self.target_temp - comfortable_range
        upper_bound = self.target_temp + comfortable_range
        
        # Decision logic with memory consideration
        if current_temp < lower_bound:
            if last_action != "Heating activated":
                action = "Heating activated"
            else:
                action = "Maintain heating"
        
        elif current_temp > upper_bound:
            if last_action != "Cooling activated":
                action = "Cooling activated"
            else:
                action = "Maintain cooling"
        
        else:
            if last_action in ["Heating activated", "Cooling activated"]:
                action = "System standby"
            else:
                action = "No action needed"
        
        # Update memory
        self.previous_action = action
        return action

# Simulation environment
room_conditions = {
    "Living Area": [19, 20, 21, 22, 21, 20],
    "Bed Chamber": [23, 24, 23, 22, 23, 24],
    "Kitchen Space": [25, 24, 25, 26, 25, 24],
    "Washroom": [20, 19, 18, 19, 20, 21]
}

preferred_temperature = 22
controller = SmartThermostatAgent(preferred_temperature)

print("Smart Thermostat System - Model Based Agent")
print("=" * 50)

for room_name, temp_readings in room_conditions.items():
    print(f"\n{room_name}:")
    for reading in temp_readings:
        decision = controller.make_decision(reading)
        print(f"  Temperature: {reading}°C  {decision}")