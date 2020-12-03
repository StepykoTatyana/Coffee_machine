class CoffeeMachine:
    def __init__(self):
        self.water_def = 400
        self.milk_def = 540
        self.coffee_beans_def = 120
        self.cups_def = 9
        self.money_def = 550
        self.lack = ''

    def action(self, actions):
        def default():
            print()
            print(f"""The coffee machine has:
        {self.water_def} of water
        {self.milk_def} of milk
        {self.coffee_beans_def} of coffee beans
        {self.cups_def} of disposable cups
        ${self.money_def} of money""")

        def buy(water, milk, coffee_beans, money, cups=1):
            self.water_def = self.water_def - water
            self.milk_def = self.milk_def - milk
            self.coffee_beans_def = self.coffee_beans_def - coffee_beans
            self.cups_def = self.cups_def - cups
            self.money_def = self.money_def + money

        def check():
            if self.water_def - water_coffee >= 0 and self.coffee_beans_def - coffee_beans_coffee >= 0 \
                    and self.milk_def - milk_coffee >= 0 and self.cups_def - 1 >= 0:
                print("I have enough resources, making you a coffee!")
                buy(water_coffee, milk_coffee, coffee_beans_coffee, money_coffee)
            else:
                if self.water_def - water_coffee < 0:
                    self.lack = "water"
                if self.milk_def - milk_coffee < 0:
                    self.lack = "milk"
                if self.coffee_beans_def - coffee_beans_coffee < 0:
                    self.lack = "coffee beans"
                if self.cups_def - 1 < 0:
                    self.lack = "cup"
                print(f"Sorry, not enough {self.lack}!")

        def fill():
            print()
            self.water_def = self.water_def + int(input("Write how many ml of water do you want to add: "))
            self.milk_def = self.milk_def + int(input("Write how many ml of milk do you want to add: "))
            self.coffee_beans_def = self.coffee_beans_def + int(
                input("Write how many grams of coffee beans do you want to add: "))
            self.cups_def = self.cups_def + int(input("Write how many disposable cups of coffee do you want to add: "))

        def take():
            print()
            print(f"I gave you ${self.money_def}")
            self.money_def = 0
            print()

        if actions == "buy":
            print()
            coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
            if coffee_type == '1':  # espresso
                water_coffee = 250
                coffee_beans_coffee = 16
                milk_coffee = 0
                money_coffee = 4
                check()
            if coffee_type == '2':  # a latte
                water_coffee = 350
                milk_coffee = 75
                coffee_beans_coffee = 20
                money_coffee = 7
                check()
            if coffee_type == '3':  # a cappuccino
                water_coffee = 200
                milk_coffee = 100
                coffee_beans_coffee = 12
                money_coffee = 6
                check()
        if actions == 'fill':
            fill()
        if actions == 'take':
            take()
        if actions == 'remaining':
            default()


my = CoffeeMachine()
act = input("Write action (buy, fill, take, remaining, exit): ")
while act != 'exit':
    my.action(act)
    print()
    act = input("Write action (buy, fill, take, remaining, exit): ")
    continue
