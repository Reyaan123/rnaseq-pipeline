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

criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
x=1
while x<101:
    output = model(data)          # step 1
    loss = criterion(output, data) # step 2
    optimizer.zero_grad()          # clear old gradients
    loss.backward()                # step 3
    optimizer.step()               # step 4
    if x%10 == 0:
        print(f"Epoch {x}, Loss: {loss.item():.4f}")
    x=x+1

with torch.no_grad():
    modencoder = model.encoder(data)
    print (modencoder)