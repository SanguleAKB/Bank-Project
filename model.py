import torch
from transformers import BertTokenizer, BertModel
from torch import nn

# Load BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained("google-bert/bert-base-uncased")
bert_model = BertModel.from_pretrained("google-bert/bert-base-uncased")
bert_model.eval() 

# Define the model architecture 
class FeedForwordNN(nn.Module): 
    def __init__(self, input_dim=768, output_dim=5):  
        super(FeedForwordNN, self).__init__()
        self.fc1 = nn.Linear(input_dim, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, output_dim)
        self.relu = nn.ReLU()

    def forward(self, X):
        X = self.fc1(X)
        X = self.relu(X)
        X = self.fc2(X)
        X = self.relu(X)
        X = self.fc3(X) 
        return X

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the pre-trained model
try:
    model = FeedForwordNN(input_dim=768, output_dim=5)  
    model.load_state_dict(torch.load("AIComplaintHub.pth"))
    model.to(device)
    model.eval()  
    print("Model loaded successfully.")
except FileNotFoundError:
    print("Error: 'AIComplaintHub.pth' not found. Check the file path.")
except RuntimeError as e:
    print(f"Error loading state_dict: {e}. Ensure the model architecture matches the saved file.")

# Function to classify a new complaint
def classify_new_complaint(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        bert_outputs = bert_model(**inputs)
        embedding = bert_outputs.last_hidden_state[:, 0, :] 
        embedding = embedding.to(device)
        output = model(embedding)
        prediction = torch.argmax(output, dim=1).item()
    categories = ['credit_card', 'retail_banking', 'credit_reporting', 'mortgages_and_loans', 'debt_collection']
    return categories[prediction]

