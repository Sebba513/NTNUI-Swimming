import random
# format of set: description:total_distance:sets:reps:distance:intensity:stroke:starting_time:equipment

warm_up = [["400m valgfri innsvømming", 400, 1, 1, 400, 2, "valgfri"], ["3 • 200 valgfri innsvømming", 600, 1, 3, 200, 2, "valgfri"]]

main_set = [["12 • 100m best i snitt", 1200, 1, 12, 100, 6, "crawl"]]

cool_down = [["200m utsvømming", 200, 1, 1, 200, 1, "valgfri"]]

def generate_program(distance, intensity):

    warm = random.randint(0, len(warm_up))
    main = random.randint(0, len(main_set))
    cool = random.randint(0, len(cool_down))



for i, j, k in zip(warm_up, main_set, cool_down):
    print(i[0],k[0],j[0])