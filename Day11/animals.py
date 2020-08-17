class Animal:
    noise = 'RRRRR'
    color = 'blue'

    def make_noise(self):
        print(f'{self} makes {self.noise}')

    def show_color(self):
        print(f'{self} is {self.color}')


    def get_noise():        
        return self.noise

    def set_noise(self, new_noise):
            self.noise = new_noise

    def get_color():
        return self.color

    def set_color(self, new_color):
            self.color = new_color

class Wolf(Animal):
    noise = 'grrrr'
    color = 'gray'
