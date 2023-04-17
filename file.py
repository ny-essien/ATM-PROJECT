class filemark(object):


    def display(self,value):
        return value

    def display_options(self,options):
        for i in range(len(options)):
            print(f"{i + 1}.  {self.display(options[i])}")


    def display_dict(self, value):
        for i, op in enumerate(value):
            print(f"{i + 1}. {value[op]}")


    def enter_pin(self):

        while True:

            print("Enter Pin: ")
            self.request_pin = input()

            if self.request_pin:
                if len(self.request_pin) < 4 or len(self.request_pin) > 4:
                    print("Invalid Pin")

                else:
                    return self.request_pin
            break






