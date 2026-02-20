import torch

def get_device():
    if torch.backends.mps.is_available() and torch.backends.mps.is_built():
        return torch.device("mps")

    if torch.cuda.is_available():   
        return torch.device("cuda")

    return torch.device("cpu")

DEVICE = get_device()
print(f"Running on: {DEVICE}")