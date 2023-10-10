from project.managing_app import ManagingApp

app = ManagingApp()

print(app.register_user( 'Tisha', 'Reenie', '7246506' ))

print(app.register_user( 'Bernard', 'Remy', 'CDYHVSR68661'))

print(app.register_user( 'Mack', 'Cindi', '7246506'))

print(app.upload_vehicle('PassengerCar', 'Chevrolet', 'Volt', 'CWP8032'))

print(app.upload_vehicle( 'PassengerCar', 'Volkswagen', 'e-Up!', 'COUN199728'))

print(app.upload_vehicle('PassengerCar', 'Mercedes-Benz', 'EQS', '5UNM315'))

print(app.upload_vehicle('CargoVan', 'Ford', 'e-Transit', '726QOA'))

print(app.upload_vehicle('CargoVan', 'BrightDrop', 'Zevo400', 'SC39690'))

print(app.upload_vehicle('EcoTruck', 'Mercedes-Benz', 'eActros', 'SC39690'))

print(app.upload_vehicle('PassengerCar', 'Tesla', 'CyberTruck', '726QOA'))

print(app.allow_route('SOF', 'PLD', 144))

print(app.allow_route('BUR', 'VAR', 87))

print(app.allow_route('BUR', 'VAR', 87))

print(app.allow_route('SOF', 'PLD', 184))

print(app.allow_route('BUR', 'VAR', 86.999))

print(app.make_trip('CDYHVSR68661', '5UNM315', 3, False))

print(app.make_trip('7246506', 'CWP8032', 1, True))

print(app.make_trip('7246506', 'COUN199728', 1, False))

print(app.make_trip('CDYHVSR68661', 'CWP8032', 3, False))

print(app.make_trip('CDYHVSR68661', '5UNM315', 2, False))

print(app.repair_vehicles(2))

print(app.repair_vehicles(20))

print(app.users_report())