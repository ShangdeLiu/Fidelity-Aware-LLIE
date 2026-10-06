from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

low_path = "LOLdataset/eval15/low/1.png"
high_path = "LOLdataset/eval15/high/1.png"

low_image = Image.open(low_path)
high_image = Image.open(high_path)

print("Low-light image:", low_image.size)
print("Reference image:", high_image.size)

low_array = np.array(low_image).astype(np.float32) / 255.0
high_array = np.array(high_image).astype(np.float32) / 255.0
np.random.seed(0)

noise_std = 0.01
noise = np.random.normal(
    loc=0.0,
    scale=noise_std,
    size=low_array.shape
).astype(np.float32)

perturbed_array = np.clip(low_array + noise, 0.0, 1.0)
gamma = 0.4
enhanced_array = np.power(low_array, gamma)
perturbed_enhanced_array = np.power(perturbed_array, gamma)
stability_map = np.mean(
    np.abs(perturbed_enhanced_array - enhanced_array),
    axis=2
)
perturbed_image = Image.fromarray(
    np.uint8(np.clip(perturbed_array * 255.0, 0, 255))
)
error_map = np.mean(
    np.abs(enhanced_array - high_array),
    axis=2
)
correlation = np.corrcoef(
    stability_map.flatten(),
    error_map.flatten()
)[0, 1]

print("Sensitivity-Error Correlation:", correlation)
enhanced_image = Image.fromarray(
    np.uint8(np.clip(enhanced_array * 255.0, 0, 255))
)
brightness_map = np.mean(low_array, axis=2)
darkness_map = 1.0 - brightness_map

darkness_correlation = np.corrcoef(
    stability_map.flatten(),
    darkness_map.flatten()
)[0, 1]
error_darkness_correlation = np.corrcoef(
    error_map.flatten(),
    darkness_map.flatten()
)[0, 1]

print("Error-Darkness Correlation:", error_darkness_correlation)
print("Sensitivity-Darkness Correlation:", darkness_correlation)
plt.figure(figsize=(18, 8))

plt.subplot(2, 3, 1)
plt.imshow(low_image)
plt.title("Low-Light Input")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(perturbed_image)
plt.title("Perturbed Input")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(enhanced_image)
plt.title("Gamma Enhancement")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(high_image)
plt.title("Normal-Light Reference")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(error_map, cmap="hot")
plt.title("Reference Error Map")
plt.axis("off")

plt.subplot(2, 3, 6)
plt.imshow(stability_map, cmap="hot")
plt.title("Output Sensitivity Map")
plt.axis("off")

plt.tight_layout()
plt.show()