from triangulation import RX8Node, TriangulationRX8

# [MILITECH MESSAGE]
location_1 = RX8Node(
    int(input("\n[MILITECH RX8 MESSAGE LOG]: ENTER [X] COORDINATE OF FIRST LOCATION (SET 0 AS DEFAULT): ")), 
    int(input("[MILITECH RX8 MESSAGE LOG]: ENTER [Y] COORDINATE OF FIRST LOCATION (SET 0 AS DEFAULT): ")),
    )

location_2 = RX8Node(
    int(input("\n[MILITECH RX8 MESSAGE LOG]: ENTER [X] COORDINATE OF SECOND LOCATION: ")), 
    int(input("[MILITECH RX8 MESSAGE LOG]: ENTER [Y] COORDINATE OF SECOND LOCATION: ")),
    ) 

# [MILITECH MESSAGE]
r1 = int(input("\n[MILITECH RX8 MESSAGE LOG]: ENTER LENGHT TO THE TARGET FROM FIRST LOCATION (IN METERS): "))
r2 = int(input("[MILITECH RX8 MESSAGE LOG]: ENTER LENGHT TO THE TARGET FROM SECOND LOCATION (IN METERS): "))


rx8 = TriangulationRX8()
trx8_possible_locations = rx8(location_1, location_2, r1, r2)

print("\n[MILITECH RX8 MESSAGE LOG]: INDIRECT LOCATIONS OF THE TARGET")
for idx, point in enumerate(trx8_possible_locations, start=1):
    x, y = point
    print(f"[MILITECH RX8 MESSAGE LOG]: {idx} POSITION OG THE TARGET: [X: {round(x, 2)}, Y: {round(y, 2)}]")

