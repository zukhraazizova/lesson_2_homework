from smartphone import Smartphone


catalog =[
    Smartphone("samsung","s25","+712345678"),
    Smartphone("iphone","17pro","+78906543"),
    Smartphone("xioami","13","+789065432")
]

for smartphone in catalog: 
    print(smartphone.brand, "-", smartphone.model, ".", smartphone.phone)
