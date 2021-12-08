from Crops import Crop

if __name__ == "__main__":
    wheat = Crop("wheat", 2.0, 3.6)
    soy = Crop("soy beans", 20.0, 14)
    print(wheat.getSellPerMinute())
    print(soy.getSellPerMinute())