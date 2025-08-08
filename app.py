import math

def scrapyard_modifier(level: int) -> int:
    if level > 200:
        modifier = (level - 200) * 4 + 300
    else:
        modifier = level
        if level > 100:
            modifier = (level - 100) * 2 + 100
    return modifier - 1

def golden_scrap_cost(star_level: int, scrapyard_mul: int) -> int:
    cost = 100000 * (star_level - 10) + 250000

    # Multipliers of 1.3 at these star levels
    for lvl in [20, 30, 60, 80, 90, 100]:
        if star_level >= lvl:
            cost *= 1.3

    # Multipliers of 1.1 at these star levels
    for lvl in [150, 160, 170, 180, 190, 200, 210, 220, 230, 250, 300, 350, 400, 450, 500, 550]:
        if star_level >= lvl:
            cost *= 1.1

    return math.floor(cost * 100 / (scrapyard_mul + 100))

def magnet_cost(star_level: int, scrapyard_mul: int) -> int:
    cost = 250 * (star_level - 10) + 1000

    mults = [
        ([70, 75], 1.04),
        ([80, 85, 90, 94, 96], 1.06),
        ([98, 100, 105, 110, 120, 125, 130, 135, 140, 145, 150, 160, 180, 190, 200, 210, 220], 1.05),
        ([115], 1.03),
        ([230], 1.035),
        ([250], 1.1),
        ([270], 1.14),
        ([290], 1.15),
        ([300], 1.04),
        ([310, 330, 410, 430, 470, 610, 630, 650, 710, 810, 910, 1010, 1020, 1120, 1130], 1.1),
        ([350], 1.05),
        ([370], 1.1),
        ([390], 1.018),
        ([450], 1.06),
        ([490], 1.05),
        ([510, 530, 550, 570], 1.09),
        ([590, 670], 1.07),
        ([690], 1.05),
        ([1110, 1210], 1.3),
        ([1260, 1285], 1.18),
        ([1310, 1360], 1.36),
        ([1410, 1460], 1.37),
        ([1510], 1.3),
        ([1560], 1.269),
        ([1610, 1660], 1.1),
        ([1710], 1.3),
        ([1760], 1.269),
        ([1810], 1.1),
        ([12,13,14,15,16,17,18,19,20,21,22,23], 0.98)
    ]

    # Apply multiplier for each threshold crossed
    for levels, mult in mults:
        for lvl in levels:
            if star_level >= lvl:
                cost *= mult

    # Additional multiplier for star levels >= 1860
    if star_level >= 1860:
        cost *= math.pow(1.1, math.floor((star_level - 1810) / 50))

    return math.floor(cost * 100 / (scrapyard_mul + 100))

def fragment_cost(star_level: int, scrapyard_mul: int) -> int:
    cost = 4 + (star_level - 10)

    mult_1_05_levels = [60, 70, 75, 80, 85, 90, 94, 96, 98, 110, 115, 120, 125, 130, 140, 150, 160, 170, 180, 190, 200]
    for lvl in mult_1_05_levels:
        if star_level >= lvl:
            cost *= 1.05

    if star_level >= 100:
        cost *= 1.1

    if star_level >= 210:
        cost *= 1.3
    if star_level >= 260:
        cost *= 1.3
    if star_level >= 310:
        cost *= 1.4
    if star_level >= 410:
        cost *= 1.4
    if star_level >= 510:
        cost *= 1.4
    if star_level >= 610:
        cost *= 1.2
    if star_level >= 710:
        cost *= 1.1
    if star_level >= 810:
        cost *= 1.1
    if star_level >= 910:
        cost *= 1.1
    if star_level >= 1010:
        cost *= 1.1

    return math.floor(cost * 100 / (scrapyard_mul + 100))
