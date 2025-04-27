class Engine:
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.running = False
    
    def start(self):
        if not self.running:
            self.running = True
            return f"Engine started. {self.horsepower}hp {self.fuel_type} engine is running."
        return "Engine is already running."
    
    def stop(self):
        if self.running:
            self.running = False
            return "Engine stopped."
        return "Engine is already stopped."
    
    def get_specs(self):
        return f"{self.horsepower}hp {self.fuel_type} engine"


class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition: Car has-an Engine
    
    def start_car(self):
        return f"{self.make} {self.model}: {self.engine.start()}"
    
    def stop_car(self):
        return f"{self.make} {self.model}: {self.engine.stop()}"
    
    def get_car_info(self):
        return f"{self.make} {self.model} with {self.engine.get_specs()}"


# Create an Engine object
v8_engine = Engine(300, "Gasoline")

# Create a Car with the engine
sports_car = Car("Ferrari", "F430", v8_engine)

# Access Engine methods through Car
print(sports_car.get_car_info())
print(sports_car.start_car())
print(sports_car.stop_car())

# Create another Engine and Car
diesel_engine = Engine(180, "Diesel")
truck = Car("Ford", "F-150", diesel_engine)

# Use the second car
print("\n" + truck.get_car_info())
print(truck.start_car())

# Both cars share the same engine type but have different engine instances
print("\nBoth cars have the Engine type but different engine instances:")
print(f"sports_car.engine is truck.engine: {sports_car.engine is truck.engine}")
print(f"type(sports_car.engine) is type(truck.engine): {type(sports_car.engine) is type(truck.engine)}")
