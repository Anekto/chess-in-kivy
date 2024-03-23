import torch
from torch import nn
from torch.optim import Adam
import random

import shared_state

# Define a simple model
class MyModel(nn.Module):
    def __init__(self):
        super().__init__()

        self.piece_to_index = {
            "___": 0,  # Empty square
            "wT ": 1,
            "wL ": 2,
            "wS ": 3,
            "wK ": 4,
            "wKK": 5,
            "wS ": 6,
            "wL ": 7,
            "wT ": 8,
            "wB ": 9,
            "sT ": 10,
            "sL ": 11,
            "sS ": 12,
            "sK ": 13,
            "sKK": 14,
            "sS ": 15,
            "sL ": 16,
            "sT ": 17,
            "sB ": 18
        }

        self.input_size = 8 * 8 * 19
        self.hidden_size = 8 * 8 * 19
        self.output_size = 8 * 8
        # Define model layers here (e.g., linear, convolutional, etc.)
        self.linear1 = nn.Linear(self.input_size, self.hidden_size)  # Example layer
        self.linear2 = nn.Linear(self.hidden_size, self.output_size)

    def forward(self, x):
        x = x.view(-1, self.input_size)  # Flatten input
        x = self.linear1(x)
        x = torch.relu(x)
        x = self.linear2(x)
        return x


    def make_move(self, board_state):
        # 1. Convert board state to tensor (as you've done)
        board_tensor = torch.zeros(8, 8, 19)  # 8x8 board, channel for each piece

        #print(board_tensor)

        # Creates a board state filled with 1s ?
        for row in range(1, 8):  # Start from row 1 to skip the first row
            for col in range(7):
                piece = board_state[row][col]  # Extract first characters for piece
                piece_index = self.piece_to_index[piece]
                
                board_tensor[row - 1, col, piece_index] = 1  # Adjust row index for tensor


        # output model and output forward with tensor are the same values
        output = model(board_tensor)
        output_tensor = model.forward(board_tensor)

        # 3. Process output based on your model's purpose
        #    For example, if it predicts move probabilities:
        move_probabilities = torch.softmax(output, dim=1)  # Convert to probabilities
        best_move_index = torch.argmax(move_probabilities)
        # ... (use best_move_index to make the move on the board)


        ### PRINTING THE PROBABILITIES TO FIND OUT WHATS HAPPENING

        #print("\n Best move index", best_move_index, "\n model output", output)
        #print("\n move probabilities", move_probabilities," output forward", output_tensor)

        return best_move_index


    
    def save_model(self, model):

        torch.save(model, 'torch/my_model_2.pt')  # Adjust path and filename


    def bot_move(self, board_state, pos1):
        pos2 = [None, None]

        board_tensor = torch.ones(8, 8, 19)  # 8x8 board, channel for each piece
        
        # Creates a board state filled with 1s ?
        for row in range(1, 8):  # Start from row 1 to skip the first row
            for col in range(7):

                if row == pos1[0] and col == pos1[1]:

                    piece = board_state[row][col]  # Extract first characters for piece
                    piece_index = self.piece_to_index[piece]
                
                    board_tensor[row - 1, col, piece_index] = 1
                else:

                    piece = board_state[row][col]  # Extract first characters for piece
                    piece_index = self.piece_to_index[piece]
                
                    board_tensor[row - 1, col, piece_index] = 0  # Adjust row index for tensor

        output = model(board_tensor)

        move_probabilities = torch.softmax(output, dim=1)  # Convert to probabilities
        best_move_index = torch.argmax(move_probabilities)
        
        
        
        #print("Best move index:", best_move_index, "\nMove probabilities:", move_probabilities)



        pos2[0] = random.randint(1,8)
        pos2[1] = random.randint(1,8)

        return pos2

# Load the model from a file
try:
    model = torch.load('torch/my_model_2.pt')
    print("Loading model ...")
except:
    model = MyModel()

shared_state.model = model
#need to check every move for probabilty of good move


# Call this function for each turn
#while game_is_not_finished:
#    make_move(shared_state.state)
