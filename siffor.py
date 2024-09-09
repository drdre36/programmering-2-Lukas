class Elev:
    def __init__(self, namn, alder, godkand):
        self.namn = namn 
        self.alder = alder 
        self.glad = godkand 

elev1 = Elev("Anna", 16, True)
elev2 = Elev("Erik", 17, False)

print(f"{elev1.namn} är {elev1.alder} år och glad: {elev1.glad}")
print(f"{elev2.namn} är {elev2.alder} år och glad: {elev2.glad}")
