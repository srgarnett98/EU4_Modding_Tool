# %%
import numpy as np
import matplotlib.pyplot as plt

# %%

font = {
    1: [[0, 1, 0],
         [1, 1, 0],
         [0, 1, 0],
         [0, 1, 0],
         [1, 1, 1]],
    2: [[1, 1, 1],
         [0, 0, 1],
         [1, 1, 1],
         [1, 0, 0],
         [1, 1, 1]],
    3: [[1, 1, 1],
         [0, 0, 1],
         [0, 1, 1],
         [0, 0, 1],
         [1, 1, 1]],
    4: [[1, 0, 1],
         [1, 0, 1],
         [1, 1, 1],
         [0, 0, 1],
         [0, 0, 1]],
    5: [[1, 1, 1],
         [1, 0, 0],
         [1, 1, 1],
         [0, 0, 1],
         [1, 1, 1]],
    6: [[1, 1, 1],
         [1, 0, 0],
         [1, 1, 1],
         [1, 0, 1],
         [1, 1, 1]],
    7: [[1, 1, 1],
         [0, 0, 1],
         [0, 0, 1],
         [0, 0, 1],
         [0, 0, 1]],
    8: [[1, 1, 1],
         [1, 0, 1],
         [1, 1, 1],
         [1, 0, 1],
         [1, 1, 1]],
    9: [[1, 1, 1],
         [1, 0, 1],
         [1, 1, 1],
         [0, 0, 1],
         [1, 1, 1]],
    0: [[1, 1, 1],
         [1, 0, 1],
         [1, 0, 1],
         [1, 0, 1],
         [1, 1, 1]],
}

# %%

every_number = [np.zeros((5, 16))]*4942

for i in range(4942):
    digits: tuple[int, int, int, int] = (
        i//1000 % 10,
        i//100 % 10,
        i//10 % 10,
        i%10
    )
    
    this_number = np.zeros((5, 16))
    for j in range(5):
        started = False
        for k, digit in enumerate(digits):
            if digit != 0:
                started = True
            if started:
                this_number[j, k*4:k*4+3] = font[digit][j]
            
    every_number[i] = this_number
    
    
# %%


plt.figure()
plt.imshow(every_number[1234], vmin = 0, vmax = 1)
plt.show()

plt.figure()
plt.imshow(every_number[567], vmin = 0, vmax = 1)
plt.show()

plt.figure()
plt.imshow(every_number[890], vmin = 0, vmax = 1)
plt.show()
    
# %%

# to do: convolve over image, check match for each pixel with all 4921
