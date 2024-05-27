import os
from PIL import Image
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms

class EarRingLoader(Dataset):
    def __init__(self, main_dir, transform=None):
        self.main_dir = main_dir
        self.transform = transform
        self.all_imgs = os.listdir(main_dir)
        self.all_imgs = [f for f in self.all_imgs if os.path.isfile(os.path.join(main_dir, f))]

    def __len__(self):
        return len(self.all_imgs)

    def __getitem__(self, idx):
        img_loc = os.path.join(self.main_dir, self.all_imgs[idx])
        image = Image.open(img_loc)
        if self.transform is not None:
            tensor_image = self.transform(image)
        return tensor_image



# # Create a data loader
# image_loader = DataLoader(custom_dataset, batch_size=32, shuffle=True)

# # Iterate over the data loader
# for image_batch in image_loader:
#     # Perform operations on image_batch
#     pass
