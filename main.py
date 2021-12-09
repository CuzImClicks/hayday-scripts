from Crops import Crop

if __name__ == "__main__":
    wheat = Crop("wheat", 2.0, 3.6)
    mais = Crop("mais", 5, 7)
    carrot = Crop("carrot", 10, 7.2)
    soy = Crop("soy beans", 20.0, 10.8)
    sugar_cane= Crop("sugar cane", 30, 14)
    indigo = Crop("indigo", 120, 25)

    print(wheat.getSellPerMinute())
    print(soy.getSellPerMinute())
    print(mais.getSellPerMinute())
    print(sugar_cane.getSellPerMinute())
    print(carrot.getSellPerMinute())
    print(indigo.getSellPerMinute())