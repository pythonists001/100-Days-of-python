nato = {
    "A": "Alfa",
    "B":"Bravo",
    "C":"Charlie",
    "D":"Delta",
    "E":"Echo",
    "F":"Foxtrot",
    "G":"Golf",
    "H":"Hotel",
    "I":"India",
    "J":"Juliett",
    "K":"Kilo",
    "L":"Lima",
    "M":"Mike",
    "N":"November",
    "O":"Oscar",
    "P":"Papa",
    "Q":"Quebec",
    "R":"Romeo",
    "S":"Sierra",
    "T":"Tango",
    "U":"Uniform",
    "V":"Victor",
    "W":"Whiskey",
    "X":"X-ray",
    "Y":"Yankee",
    "Z":"Zulu",
}

name = "ARVIND SINGH"
f = []
for _ in name:
    if _ in nato.keys():
        f.append(nato[_])
print(f)
# list(map(bark, ['hello', 'hey', 'hi']))
# ['HELLO!', 'HEY!', 'HI!']