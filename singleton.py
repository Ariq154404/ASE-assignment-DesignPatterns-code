class X_Ray_Machine(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not X_Ray_Machine.__instance:
            X_Ray_Machine.__instance = object.__new__(cls)
        return X_Ray_Machine.__instance

    def __init__(self, start_time, intensity):
        self.start_time = start_time
        self.intensity = intensity

s1 = X_Ray_Machine("5:03:51", 9)
s2 = X_Ray_Machine("5:05:31", 5)

print(s1)
print(s2)
print("Both s1 and s2 are the same instances")
print(s1 == s2)
print("Intensity of S1 is",s1.intensity)
print("Intensity of S2 is",s2.intensity)