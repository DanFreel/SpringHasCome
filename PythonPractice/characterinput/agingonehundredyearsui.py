class AgingOneHundredYearsUI(object):

    def __init__(self, name="", age=-1):
        self.name = name
        self.age = age

    def output_results(self, future_date):
        print('Hi {}. You will be 100 years old in year {}'.format(self.name, future_date))

    def prompt_name(self):
        self.name = input('Please input your name: ')

    def prompt_age(self):
        self.age = int(input('And now your age: '))
