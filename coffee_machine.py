class CoffeeMachine:
    '''Coffee machine software'''
    options={'espresso':{'water':[50,'ml'],'coffee':[18,'g'],'money':[-1.5,'$']},
             'latte':{'water':[200,'ml'],'milk':[150,'ml'],'coffee':[24,'g'],'money':[-2.5,'$']},
             'cappuccino':{'water':[250,'ml'],'milk':[100,'ml'],'coffee':[24,'g'],'money':[-3.0,'$']}}

    def __init__(self):
        self.resources={'water':[0,'ml'],'milk':[0,'ml'],'coffee':[0,'g'],'money':[0.0,'$']}
        self.on=True

    def run(self):
        while self.on:
            prompt=input('What would you like? (espresso/latte/cappuccino):')
            coffee_machine.resolve_request(prompt)
    
    def fill(self):
        self.resources['water'][0]+=2000
        self.resources['coffee'][0]+=300
        self.resources['milk'][0]+=1000

    def show_report(self):
        for name,res_data in self.resources.items():
            print(f'{name}: {res_data[0]}{res_data[1]}')

    def check_resources(self,chosen_drink):
        depl_resources=[]
        for resource in CoffeeMachine.options[chosen_drink]:
            if self.resources[resource][0]<CoffeeMachine.options[chosen_drink][resource][0]:
                depl_resources.append(resource)
        if depl_resources:
            print(f'Sorry, there\'s not enough {",".join(depl_resources)}')
            return False
        return True
    
    def process_payment(self,chosen_drink):
        coins={'quarters':0,'dimes':0,'nickles':0,'pennies':0}
        for coin in coins:
            amount='-'
            while not amount.isnumeric():
                amount=input(f'Insert {coin}: ')
            coins[coin]=int(amount)
        inserted_sum=coins['quarters']*0.25+coins['dimes']*0.1+coins['nickles']*0.05+coins['pennies']*0.01
        if inserted_sum<-CoffeeMachine.options[chosen_drink]['money'][0]:
            print('Sorry, that\'s not enough money. Money refunded.')
            return False
        elif inserted_sum>-CoffeeMachine.options[chosen_drink]['money'][0]:
            print(f'Here is ${inserted_sum+CoffeeMachine.options[chosen_drink]["money"][0]:.2f} dollars in change.')
        self.resources['money'][0]-=CoffeeMachine.options[chosen_drink]["money"][0]
        return True
    
    def prepare_coffee(self,chosen_drink):
        for resource in CoffeeMachine.options[chosen_drink]:
            if resource!='money':
                self.resources[resource][0]-=CoffeeMachine.options[chosen_drink][resource][0]
        print(f'Here is your {chosen_drink}, enjoy! ☕')


    def resolve_request(self,prompt):
        '''Translates prompt request to action, and performs it'''
        if prompt=='off':
            print('Shutting off... goodbye!')
            self.on=False
        elif prompt=='report':
            self.show_report()
        elif prompt=='fill':
            self.fill()
            print('Recources replenished!')
            self.show_report()
        elif prompt in CoffeeMachine.options:
            is_enough_res=self.check_resources(prompt)
            if is_enough_res:
                payment_successful=self.process_payment(prompt)
                if payment_successful:
                    self.prepare_coffee(prompt)



coffee_machine=CoffeeMachine()
coffee_machine.run()