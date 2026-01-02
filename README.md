# BERT (Bidirectional Encoder Representations from Transformers) 
   #### Encoder: 
    BERT employs an encoder-only architecture.
   
   #### Decoder: 
   GPT employs a decoder-only architecture. GPT, or a generative pre-trained transformer, is a type of large language model (LLM) that utilizes deep learning to produce human-like text. Neural networks are trained on massive datasets containing text and code, enabling them to understand and generate coherent and contextually relevant responses. As a key component in the field of generative AI, GPT pushes the boundaries of what's possible with AI, enabling machines to produce creative and human-quality content.
![image](https://github.com/user-attachments/assets/009c62dd-cefa-4288-b85b-9f97740f2c81)

##### What is Hagging face? 
Hugging Face is a platform for machine learning and data science that lets users build, train, and share AI models.

##### Transformers: 
It is a hugging face library developed by Hugging Face.  
Transformers provides thousands of pretrained models to perform tasks on different modalities such as text, vision, and audio.Transformers library provides a convenient way to perform transfer learning for a variety of natural language processing (NLP) and even multimodal tasks.
   ###### BertTokenizer 
   - BertTokenizer is a class from the transformers library
   - This class is used to convert input text into token IDs that a BERT model can process.
   ###### BertModel
   - BertModel is a class from the transformers library by Hugging Face. It represents the pre-trained BERT model architecture, which can be used for a variety of tasks like text classification, token classification, question answering, and more.
# BERT (Bidirectional Encoder Representations from Transformers) and similar models are excellent examples of transfer learning in natural language processing (NLP).

### Vertex AI
- Vertex AI in express mode is the fastest way to start building generative AI applications on Google Cloud. Signing up in express mode is quick and easy, and it doesn't require entering any billing information.


https://github.com/user-attachments/assets/0a9e97e4-d007-4abc-9bc7-9f25733524ce


# 🏦 AI-Powered Bank Complaint Classification System

An intelligent complaint management system that uses BERT (Bidirectional Encoder Representations from Transformers) to automatically classify and categorize customer complaints in the banking sector. This project leverages transfer learning and natural language processing to streamline complaint handling and improve customer service efficiency.

## 🌟 Overview

This application combines state-of-the-art NLP technology with a user-friendly web interface to automatically classify banking complaints into predefined categories. Built with Flask and powered by BERT, the system can understand context and sentiment in customer complaints, enabling faster response times and better service delivery.

## 🎯 Features

- **BERT-Based Classification**: Uses pre-trained BERT model for accurate text classification
- **Transfer Learning**: Leverages Hugging Face's transformers library for efficient model training
- **Web Interface**: Clean, intuitive Flask-based web application
- **Real-time Processing**: Instant complaint classification and categorization
- **Vertex AI Integration**: Enhanced AI capabilities using Google Cloud's Vertex AI
- **Model Persistence**: Trained model saved for quick deployment and inference

## 🏗️ Architecture

### BERT Model
The system uses BERT (Bidirectional Encoder Representations from Transformers), an encoder-only architecture that reads text bidirectionally to understand context better than traditional sequential models.

**Key Advantages:**
- Bidirectional context understanding
- Pre-trained on large text corpus
- Fine-tuned for banking complaint classification
- Transfer learning capabilities for domain-specific tasks

### Technology Stack
- **Backend**: Python, Flask
- **ML Framework**: PyTorch
- **NLP**: Hugging Face Transformers (BertTokenizer, BertModel)
- **AI Platform**: Google Cloud Vertex AI
- **Frontend**: HTML templates

## 📁 Project Structure

```
Bank-Project/
├── app.py                 # Flask web application
├── model.py              # BERT model architecture and training logic
├── vertexai.py           # Vertex AI integration
├── main_nb.ipynb         # Jupyter notebook for experimentation
├── AIComplaintHub.pth    # Trained model weights
├── requirements.txt      # Project dependencies
├── templates/            # HTML templates for web interface
└── README.md            # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip package manager
- Google Cloud account (for Vertex AI features)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/SanguleAKB/Bank-Project.git
cd Bank-Project
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Running the Application

1. **Start the Flask server**
```bash
python app.py
```

2. **Access the application**
Open your browser and navigate to `http://localhost:5000`

3. **Submit a complaint**
Enter your complaint text in the web interface and receive instant classification results

## 🔧 Configuration

### Vertex AI Setup

To use Vertex AI features in express mode:

1. Sign up for Google Cloud Platform
2. Enable Vertex AI API
3. Configure credentials in `vertexai.py`
4. No billing information required for express mode

### Model Training

To retrain the model with your own data:

1. Prepare your labeled complaint dataset
2. Open `main_nb.ipynb` in Jupyter Notebook
3. Follow the training pipeline
4. Save the model as `AIComplaintHub.pth`

## 📊 Model Details

### BERT Components

**BertTokenizer**: Converts raw text into token IDs that the BERT model can process
- Handles text preprocessing
- Manages special tokens ([CLS], [SEP])
- Creates attention masks

**BertModel**: Pre-trained transformer architecture
- 12 transformer layers (BERT-base)
- 768 hidden dimensions
- Attention mechanism for context understanding
- Fine-tuned for complaint classification

### Transfer Learning Approach

The project uses transfer learning by:
1. Starting with pre-trained BERT weights
2. Adding a classification layer on top
3. Fine-tuning on banking complaint data
4. Achieving high accuracy with limited training data

## 🎓 Use Cases

- **Customer Service**: Automatic routing of complaints to relevant departments
- **Priority Management**: Identifying urgent complaints requiring immediate attention
- **Trend Analysis**: Understanding common complaint categories
- **Response Automation**: Generating appropriate responses based on complaint type
- **Quality Assurance**: Monitoring complaint resolution effectiveness

## 📈 Performance

The model achieves high accuracy in classifying complaints into categories such as:
- Account management issues
- Transaction disputes
- Card-related problems
- Loan inquiries
- Service quality complaints
- Technical issues

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Key Concepts

### What is Transfer Learning?
Transfer learning allows us to use knowledge from pre-trained models (like BERT) and adapt them to specific tasks (complaint classification) with minimal training data and computational resources.

### What is Hugging Face?
Hugging Face is a platform providing pre-trained models and tools for NLP tasks. The Transformers library offers easy access to models like BERT, GPT, and many others.

### BERT vs GPT
- **BERT**: Encoder-only architecture, reads text bidirectionally, best for classification tasks
- **GPT**: Decoder-only architecture, generates text sequentially, best for text generation

## 🔍 Future Enhancements

- [ ] Multi-language support
- [ ] Sentiment analysis integration
- [ ] Real-time dashboard for complaint analytics
- [ ] Email integration for automatic complaint ingestion
- [ ] Mobile application
- [ ] Advanced reporting and visualization

## 📄 License

This project is available for educational and commercial use.

## 👤 Author

**Sangule AKB**
- GitHub: [@SanguleAKB](https://github.com/SanguleAKB)

## 🙏 Acknowledgments

- Hugging Face for the Transformers library
- Google Cloud for Vertex AI platform
- BERT paper authors for the groundbreaking architecture
- Open-source community for various tools and libraries

## 📞 Support

For questions, issues, or suggestions:
- Open an issue on GitHub
- Contact through GitHub profile

---

**Note**: This project demonstrates the application of modern NLP techniques in solving real-world business problems. It showcases the power of transfer learning and pre-trained models in achieving high performance with minimal resources.
