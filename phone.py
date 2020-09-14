class Phone():
    def __init__(self, phone_number):
        self.number = phone_number

    def call(self, other_number):
        print("Calling {} from {}".format(other_number, self.number))
        # print(f"Calling {other_number} from {self.number}")

    def text(self, other_number, msg):
        print("Sending text to {} from {}".fromat(other_number, self.number))
        print(msg)

    def open_app(self, app_name):
        print("Opening {} on device".format(app_name))


class IPhone(Phone):
    def __init__(self, phone_number):
        super().__init__(phone_number)
        self.fingerprint = None

    def set_fingerprint(self, new_fingerprint):
        self.fingerprint = new_fingerprint

    def unlock(self, fingerprint=None):
        if (fingerprint == None and self.fingerprint == None):
            print("Phone is unlocked because no fingerprint is currently set")

        if (fingerprint == self.fingerprint):
            print("Phone is unlocked")
        else:
            print("Phone locked. Fingerprint does not match.")


ilyhashems_iphone = IPhone(1111111111)
print("ilyhashem's number is {}".format(ilyhashems_iphone.number))

ilyhashems_iphone.set_fingerprint("password")

print(ilyhashems_iphone.fingerprint)

ilyhashems_iphone.unlock("password123")

ilyhashems_iphone.call(2222222222)

ilyhashems_iphone.open_app("Tik Tok")
