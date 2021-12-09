from Crops import Crop

if __name__ == "__main__":
    wheat = Crop("wheat", 2.0, 3.6)
    mais = Crop("mais", 5, 7)
    soy = Crop("soy beans", 20.0, 10.8)
    sugar_cane= Crop("sugar cane", 30, 14)
    carrot = Crop("carrot", 10, 7.2)
    indigo = Crop("indigo", 120, 25)
    pumpkin = Crop("pumpkin", 180, 32)

    array = []
    array.append(wheat.toDict())
    array.append(mais.toDict())
    array.append(carrot.toDict())
    array.append(soy.toDict())
    array.append(sugar_cane.toDict())
    array.append(indigo.toDict())
    array.append(pumpkin.toDict())
    
    value = "time"

    array = wheat.sort(array, value)
    for i in range(0, len(array)):
        print(array[i]["name"] + " - " + str(array[i][value]))
