import torch
from torch.utils.data import DataLoader
import transformers

def train_model(model, train_loader, val_loader, epochs=3, lr=3e-5, device="cpu"):
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
    model.to(device)

    for epoch in range(epochs):
        model.train()
        for batch in train_loader:
            inputs, labels = batch['input_ids'].to(device), batch['labels'].to(device)
            optimizer.zero_grad()
            outputs = model(inputs, labels=labels)
            loss = outputs.loss
            loss.backward()
            optimizer.step()
