import sys
import geopy.distance

pointA = (float(sys.argv[1]), float(sys.argv[2]))
pointB = (float(sys.argv[3]), float(sys.argv[4]))

print("Point A: ")
print(pointA)
print("Point B: ")
print(pointB)

NSdiff = abs(pointA[0]-pointB[0])
EWdiff = abs(pointA[1]-pointB[1])



coords_1 = pointA
coords_2 = pointB

#total distance, latitude distance, longitude difference
distance = geopy.distance.geodesic(coords_1, coords_2).km*1000
NSdistance = geopy.distance.geodesic(coords_1, (coords_2[0],coords_1[1])).km*1000
EWdistance = geopy.distance.geodesic(coords_1, (coords_1[0], coords_2[1])).km*1000

print("\nmeters apart: ")
print(distance)
print()

#finding points needed when assuming each is about .55 meter apart
points_needed = int(distance/.55)

NS_rel_points = []
EW_rel_points = []

for i in range(points_needed):
    NS_rel_points.append(NSdistance*i/points_needed)
    EW_rel_points.append(EWdistance*i/points_needed)

#generate csv below
with open("goToTarget.csv",'w') as f:
    for i in range(points_needed):
        f.write(str(NS_rel_points[i]) + ", " + str(EW_rel_points[i])+"\n")









