import sys
import torch
import torch.nn as nn


class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, n_layers):
        super(RNN,self).__init__()
        self.hidden_size = hidden_size
        self.n_layers = n_layers
        
        self.rnn = nn.RNN(input_size, hidden_size, n_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
    
    def forward(self, input):
        batch_size = input.size(0)
        
        hidden = self.initHidden(batch_size)
        
        out, hidden = self.rnn(input, hidden)
        
        out = out.contiguous().view(-1, self.hidden_size)
        out = self.fc(out)
        
        return out, hidden
    
    def initHidden(self, batch_size):
        return torch.zeros(self.n_layers, batch_size, self.hidden_size)

rnn = torch.load('shakespeare-rnn-generation.pt')

def predict(model, character):
    model
    character = np.array([[char2int[c] for c in character]])
    character = one_hot_encode(character, dict_size, character.shape[1], 1)

    character = torch.from_numpy(character)
    
    out, hidden = model(character)
    out
    prob = nn.functional.softmax(out[-1], dim=0).data
    char_ind = torch.max(prob, dim=0)[1].item()

    return int2char[char_ind], hidden


def sample(model, out_len, start):
    model
    model.eval() # eval mode
    start = start.lower()
    chars = [ch for ch in start]
    size = out_len - len(chars)
    for ii in range(size):
        char, h = predict(model, chars)
        # if char == '-':
        #     char="\n"
        chars.append(char)

    return ''.join(chars)

if __name__ == '__main__':
    sample(rnn, sys.argv[1], sys.argv[2])