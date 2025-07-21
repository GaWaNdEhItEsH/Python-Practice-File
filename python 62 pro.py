# Multilevel Inheritance

print("Hello World")

class Dad:
    basketball = 1

class Son(Dad):
    dance = 1
    # basketball = 5
    def is_dance(self):
        return f"Yes I dance {self.dance} no of time."

class Grandson(Son):
    dance = 6
    gitar = 3

    # def is_dance(self):
    #     return f"Good dancer ! I can dance {self.dance} no of times"

cherry = Dad()
larry = Son()
goli = Grandson()

# print(goli.is_dance())
# print(goli.basketball)
# print(cherry.gitar)
# print(goli.gitar)


# electronic device
# pocket gadget
# phone





class ElectronicDevice:
    no_of_device = 5

    # def __init__(self,inch_32,inch_40,mixer,mob_phone,freeze):
    #     self.tv32 = inch_32
    #     self.tv40 = inch_40
    #     self.grinder = mixer
    #     self.phone = mob_phone
    #     self.refrigerator = freeze

    def device_size(self):
        return f"Device size are bigger and smaller and {self.no_of_device} no of device are electronic device."

class PocketGadget(ElectronicDevice):
    no_of_gadget = 3

    def gadget_size(self):
        return f"Gadget size are pocket friendly and there are {self.no_of_gadget} no. of gadget."

class Phone(PocketGadget):
    no_of_phone = 1

    def mobile_phone(self):
        return f"This android mobile phone are economical and value for money and {self.no_of_phone} are available"

samsung = ElectronicDevice()
hanselectronic = PocketGadget()
parimobile = Phone()

print(parimobile.no_of_phone)
print(parimobile.device_size())
print(parimobile.mobile_phone())
print(hanselectronic.no_of_device)
#print(samsung.no_of_gadget)  It gives error

