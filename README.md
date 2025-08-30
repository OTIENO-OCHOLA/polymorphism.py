# polymorphism.pyclass ElectronicDevice

    """Base class for all electronic devices"""
    
    def __init__(self, brand, model, power_source):
        self.brand = brand
        self.model = model
        self.power_source = power_source
        self.is_powered_on = False
    
    def power_on(self):
        """Power on the device"""
        if not self.is_powered_on:
            self.is_powered_on = True
            return f"{self.brand} {self.model} is now powered on!"
        return f"{self.brand} {self.model} is already on."
    
    def power_off(self):
        """Power off the device"""
        if self.is_powered_on:
            self.is_powered_on = False
            return f"{self.brand} {self.model} is now powered off."
        return f"{self.brand} {self.model} is already off."
    
    def get_info(self):
        """Get device information"""
        return f"Brand: {self.brand}, Model: {self.model}, Power Source: {self.power_source}"

class Smartphone(ElectronicDevice):
    """Smartphone class that inherits from ElectronicDevice"""

    def __init__(self, brand, model, storage_gb, os, screen_size, battery_mah):
        super().__init__(brand, model, "Battery")
        self.storage_gb = storage_gb
        self.os = os
        self.screen_size = screen_size
        self.battery_mah = battery_mah
        self.installed_apps = []
        self.current_volume = 50  # Volume level from 0 to 100
    
    def install_app(self, app_name):
        """Install a new application"""
        if app_name not in self.installed_apps:
            self.installed_apps.append(app_name)
            return f"Installed {app_name} successfully!"
        return f"{app_name} is already installed."
    
    def uninstall_app(self, app_name):
        """Uninstall an application"""
        if app_name in self.installed_apps:
            self.installed_apps.remove(app_name)
            return f"Uninstalled {app_name} successfully!"
        return f"{app_name} is not installed."
    
    def set_volume(self, level):
        """Set volume level (0-100)"""
        if 0 <= level <= 100:
            self.current_volume = level
            return f"Volume set to {level}%"
        return "Volume level must be between 0 and 100"
    
    def make_call(self, number):
        """Make a phone call"""
        if self.is_powered_on:
            return f"📞 Calling {number}..."
        return "Cannot make call - phone is powered off"
    
    def get_info(self):
        """Override base method to include smartphone-specific info"""
        base_info = super().get_info()
        return (f"{base_info}, OS: {self.os}, Storage: {self.storage_gb}GB, "
                f"Screen: {self.screen_size}\", Battery: {self.battery_mah}mAh")

        class Animal:
    """Base class for all animals"""
    
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat
    
    def move(self):
        """Base move method - to be overridden by subclasses"""
        return "The animal moves."
    
    def speak(self):
        """Base speak method - to be overridden by subclasses"""
        return "The animal makes a sound."
    
    def describe(self):
        """Describe the animal"""
        return f"I am a {self.name} living in {self.habitat}."

class Bird(Animal):
    """Bird class that inherits from Animal"""

    def __init__(self, name, habitat, wingspan):
        super().__init__(name, habitat)
        self.wingspan = wingspan
    
    def move(self):
        """Birds fly!"""
        return "🦅 Flying through the sky!"
    
    def speak(self):
        """Birds chirp or sing"""
        return "🐦 Chirp chirp!"
    
    def build_nest(self):
        """Bird-specific behavior"""
        return "🏠 Building a nest for eggs!"

class Fish(Animal):
    """Fish class that inherits from Animal"""

    def __init__(self, name, habitat, fin_count):
        super().__init__(name, habitat)
        self.fin_count = fin_count
    
    def move(self):
        """Fish swim!"""
        return "🐠 Swimming through the water!"
    
    def speak(self):
        """Fish make bubble sounds"""
        return "🐟 Blub blub!"
    
    def blow_bubbles(self):
        """Fish-specific behavior"""
        return "💨 Blowing bubbles!"

class Mammal(Animal):
    """Mammal class that inherits from Animal"""

    def __init__(self, name, habitat, leg_count):
        super().__init__(name, habitat)
        self.leg_count = leg_count
    
    def move(self):
        """Mammals walk or run"""
        return "🐾 Walking on the ground!"
    
    def speak(self):
        """Mammals make various sounds"""
        return "🐕 Woof! (or other mammal sound)"
    
    def give_birth(self):
        """Mammal-specific behavior"""
        return "👶 Giving birth to live young!"

# Demonstration of polymorphism

def demonstrate_movement(animals):
    """Demonstrate polymorphism by calling move() on different animals"""
    print("\n🎭 Polymorphism Demonstration:")
    print("=" * 40)
    for animal in animals:
        print(f"{animal.name}: {animal.move()}")

# Create some smartphone objects

print("📱 Smartphone Examples:")
print("=" * 40)

iphone = Smartphone("Apple", "iPhone 15", 256, "iOS", 6.1, 3349)
samsung = Smartphone("Samsung", "Galaxy S23", 512, "Android", 6.8, 3900)

print(iphone.get_info())
print(iphone.power_on())
print(iphone.install_app("WhatsApp"))
print(iphone.make_call("555-1234"))
print(iphone.set_volume(75))

print("\n" + samsung.get_info())
print(samsung.install_app("Instagram"))
print(samsung.install_app("Twitter"))

# Create animal objects and demonstrate polymorphism

print("\n🐾 Animal Examples:")
print("=" * 40)

eagle = Bird("Eagle", "Mountains", 2.1)
salmon = Fish("Salmon", "Rivers", 7)
dog = Mammal("Dog", "Homes", 4)

animals = [eagle, salmon, dog]

for animal in animals:
    print(f"\n{animal.describe()}")
    print(f"Movement: {animal.move()}")
    print(f"Sound: {animal.speak()}")

# Special behaviors

print(f"\n{eagle.name}: {eagle.build_nest()}")
print(f"{salmon.name}: {salmon.blow_bubbles()}")
print(f"{dog.name}: {dog.give_birth()}")

# Demonstrate polymorphism

demonstrate_movement(animals)

# Additional polymorphism example with different movement contexts

print("\n\n🚗 Vehicle Polymorphism Example:")
print("=" * 40)

class Vehicle:
    def move(self):
        return "This vehicle moves"

class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road!"

class Airplane(Vehicle):
    def move(self):
        return "✈️ Flying through the air!"

class Boat(Vehicle):
    def move(self):
        return "⛵ Sailing on water!"

class Bicycle(Vehicle):
    def move(self):
        return "🚴 Pedaling on the path!"

# Create vehicles and demonstrate polymorphism

vehicles = [Car(), Airplane(), Boat(), Bicycle()]

for i, vehicle in enumerate(vehicles, 1):
    print(f"Vehicle {i}: {vehicle.move()}")
