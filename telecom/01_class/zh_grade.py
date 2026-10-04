import json 
import math 

def main():
    with open("zh.json", "r") as f:
        data = json.load(f)

    hwPercent = data["homework"]["point"] / data["homework"]["max"] * 100
    socketPercent = data["socket"]["point"] / data["socket"]["max"] * 100
    katharaMax = data["kathara"]["max"]
    katharaMinPercent = data["kathara"]["min_percent"]

    gradeThresholds = {
        2: 50,
        3: 60,
        4: 75,
        5: 85,
    }

    for (grade, threshold) in gradeThresholds.items():
        neededKatharaPercent = 3 * threshold - hwPercent - socketPercent
        neededPoints = math.ceil(neededKatharaPercent / 100 * katharaMax)
        katharaMinPoints = math.ceil(katharaMinPercent * katharaMax)
        neededPoints = max(neededPoints, katharaMinPoints)

        if neededPoints > katharaMax:
            print(f"{grade}: Nope")
        else:
            print(f"{grade}: {neededPoints}")

if __name__ == "__main__":
    main()