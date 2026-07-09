import torch
import torch.nn as nn
#sample geen expression data: 8 samples, 16 genes
data = torch.rand(8,16)
print(data.shape)
print(data)

class Autoencoder(nn.Module):
    def __init__(self):
        super().__init__()

        self.encoder = nn.Sequential(
            nn.Linear(16,8),
            nn.Linear(8,3)
            
            )
        self.decoder = nn.Sequential(
            nn.Linear(3,8),
            nn.Linear(8,16)
        )
    def forward(self, x):
        compressed = self.encoder(x)
        decompress = self.decoder(compressed)
        return decompress

model = Autoencoder()
print(model)