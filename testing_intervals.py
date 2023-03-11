# pin 1 short
onOffVariationsTestPin1 = [
    [True] * 5,
    [False] * 8,
    [True] * 3,
    [False] * 3,
    [True] * 9,
    [False] * 13,
    [True] * 14,
    [False] * 3,
    [True] * 10,
    [False] * 3,
    [True] * 4,
    [False] * 3,
]
flat_onOffVariationsTestS1 = sum(onOffVariationsTestPin1, [])

# pin 2 long
shortOnOffVariationsTestPin2 = [
    [True] * 20,
    [False] * 3,
    [True] * 10,
    [False] * 3,
    [True] * 5,
    [False] * 3,
    [True] * 14,
    [False] * 3,
    [True] * 10,
    [False] * 3,
    [True] * 4,
    [False] * 3,
]
flat_onOffVariationsTestS2 = sum(shortOnOffVariationsTestPin2, [])
