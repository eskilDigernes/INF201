from torchvision import datasets, transforms
import numpy as np

def get_mnist():
    return datasets.MNIST(root='./data', train=True, transform=transforms.ToTensor(), download=True)

def return_image(image_index, mnist_dataset):
    # Get the image and its corresponding label
    image, label = mnist_dataset[image_index]

    # Now, you have the image as a PyTorch tensor.
    # You can access its data as a matrix using .detach().numpy()
    image_matrix = image[0].detach().numpy()  # Grayscale image, so we select the first channel (index 0)

    return image_matrix.reshape(image_matrix.size), image_matrix, label

def read_from_file(name="image_19961.txt"):
        x = np.zeros(28 * 28)
        with open(name) as file:
                for i, line in enumerate(file):
                    # split and convert values to floats
                    x[i * 28 : (i+1)*28] = [float(value) for value in line.strip().split()]

# Choose an index to select one of the images
image_index = 19961
mnist_dataset = get_mnist()
x, image, label = return_image(image_index, mnist_dataset) # This here reads image {image_index} from the mnist dataset.
x_file = read_from_file() # In case you were not able to install torchvision, you can use this read_from_file function

print(f"Image {image_index} shows the number {label}")
print(f"The pixels of this image (collected in a vector) are \n {x}")
