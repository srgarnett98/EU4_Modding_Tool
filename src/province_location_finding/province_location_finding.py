# %%
from typing import Sequence
import numpy as np
import matplotlib.pyplot as plt

# %%

font = {
    1: np.array([[0, 1, 0], [1, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]]),
    2: np.array([[1, 1, 1], [0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 1]]),
    3: np.array([[1, 1, 1], [0, 0, 1], [0, 1, 1], [0, 0, 1], [1, 1, 1]]),
    4: np.array([[1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]]),
    5: np.array([[1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1]]),
    6: np.array([[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1]]),
    7: np.array([[1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]]),
    8: np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]]),
    9: np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]]),
    0: np.array([[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]]),
}

font_sums = {key: np.sum(value)*(765) for key, value in font.items()}

# %%

every_number = [np.zeros((5, 16))] * 4942

for i in range(4942):
    digits: list[int] = [
        i // 1000 % 10,
        i // 100 % 10,
        i // 10 % 10,
        i % 10,
    ]

    this_number = np.zeros((5, 16))
    for j in range(5):
        started = False
        for k, digit in enumerate(digits):
            if digit != 0:
                started = True
            if started:
                this_number[j, k * 4 : k * 4 + 3] = font[digit][j]

    every_number[i] = this_number

every_number_sum = [np.sum(x) * (255 * 3) for x in every_number]
every_number_sum = np.array(every_number_sum)
# %%


plt.figure()
plt.imshow(every_number[1234], vmin=0, vmax=1)
plt.show()

plt.figure()
plt.imshow(every_number[567], vmin=0, vmax=1)
plt.show()

plt.figure()
plt.imshow(every_number[890], vmin=0, vmax=1)
plt.show()
# %%

# to do: convolve over image, check match for each pixel with all 4921
from PIL import Image

province_map = Image.open("province_ID_map.png")
np_province_map = np.array(province_map)
sum_province_map = np.sum(np_province_map, axis=2)

print(np.shape(np_province_map))
print(np_province_map[0, 0, :])

print(np.max(np_province_map, axis=(0, 1)))
# %%

def remove_overlaps(digit_hits: list[int]):
    sum_equivilents = [font_sums[digit] for digit in digit_hits]
    return digit_hits[np.argmax(sum_equivilents)]

def digits_to_int(digits: Sequence[int | None])->int:
    if digits[4] is not None:
        return -1
    elif digits[3] is None:
        return -1
    else:
        int_no = 0
        if digits[0] is not None:
            int_no += digits[0]*1000
        if digits[1] is not None:
            int_no += digits[1]*100
        if digits[2] is not None:
            int_no += digits[2]*10
        if digits[3] is not None:
            int_no += digits[3]
        return int_no

def check_points(digit_masks, digit_mask_sums, done_list, region_to_check) -> int:
    if np.max(region_to_check) < 764:
        return -1

    digits: Sequence[int | None] = [None]*5
    for i in range(5):
        subregion = region_to_check[:, i*4:i*4+3]
        digit_hits: list[int] = []
        for key, mask in font.items():
            convolve = np.multiply(mask, subregion)
            convolve_sum = np.sum(convolve)
            if convolve_sum == font_sums[key]:
                digit_hits.append(key)
        if len(digit_hits) > 0:
            digits[i] = remove_overlaps(digit_hits)
        
    return digits_to_int(digits)


# %%
matches = [(0, 0)] * 4942
matches = np.array(matches)
done_list = []
for i, row in enumerate(np_province_map[:-5]):
    print(i)
    for j, point in enumerate(row[:-16]):
        matched_no = check_points(
            every_number,
            every_number_sum,
            done_list,
            sum_province_map[i : i + 5, j : j + 20],
        )
        if matched_no > 0:
            done_list.append(matched_no)
            matches[matched_no] = (i, j)

# %%

matched_no = check_points(
            every_number,
            every_number_sum,
            done_list,
            sum_province_map[63 : 63 + 5, 532 : 532 + 16],
        )
print(matched_no)
# %%

print(matches[101])
# %%
n_plotted = 0
for i, number_match in enumerate(matches):
    if number_match[0] != 0 and n_plotted < 100:
        print("number found")
        print(i)
        print("at posittion")
        print(number_match)
        plt.figure()
        plt.imshow(
            np_province_map[
                number_match[0] - 50 : number_match[0] + 50,
                number_match[1] - 50 : number_match[1] + 50,
                :,
            ]
        )
        plt.show()
        n_plotted += 1
# %%
