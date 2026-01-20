# Credit Card Fraud Detection

Machine learning application for detecting fraudulent credit card transactions

## 📋 Overview

A web-based fraud detection system using logistic regression to analyze credit card transactions and identify potentially fraudulent activity in real-time.

**Developed by:**
- Mustafa Tayyip BAYRAM - [LinkedIn](https://www.linkedin.com/in/mutabay/)
- Furkan ÖCALAN - [LinkedIn](https://www.linkedin.com/in/furkan-ocalan-16186a174/)

![System Overview](https://user-images.githubusercontent.com/60510780/188311216-8c1e087d-ebac-4565-9d8d-87189d327ab3.png)

## 📂 Structure

- **[Analyze/](Analyze/)** - Core analysis engine and model
- **[Documents/](Documents/)** - Project reports and system diagrams
- **[apps/](apps/)** - Flask application modules
- **[uploads/](uploads/)** - Transaction file uploads
- **[ANALYSIS.ipynb](ANALYSIS.ipynb)** - Model training notebook
- **[fraud_test.txt](fraud_test.txt)** / **[non_fraud_test.txt](non_fraud_test.txt)** - Test datasets

## 🔬 Technical Implementation

### Dataset
- **Source**: [Kaggle Credit Card Fraud Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Type**: Credit card transaction records

### Model Architecture
- **Algorithm**: Logistic Regression
- **Performance Metrics**:
  - Accuracy: 97.6%
  - Recall: 89.6%

### Web Application Stack

| Component | Technology |
|-----------|------------|
| Backend Framework | Flask |
| Database | MySQL |
| Template System | Blueprint |

### Application Modules

- **Authentication**: User registration and login system
- **File Upload**: Transaction data file processing
- **Analysis Engine**: Real-time fraud detection
- **Dashboard**: Results visualization and reporting
- **Config**: Database configuration management

## 🚀 Installation & Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Model Setup
Download the trained model and place it in `Analyze/Models/` directory.  
*Model available in [ANALYSIS.ipynb](ANALYSIS.ipynb) or contact developers.*

### 3. Database Configuration
Update database credentials in `apps/config.py` (line 13)

### 4. Run Application
```bash
# Development mode
$env:FLASK_ENV="development"
$env:FLASK_DEBUG=1
$env:FLASK_APP=".\run.py"
flask run
```

## 📊 Application Screenshots

![Login Interface](https://user-images.githubusercontent.com/60510780/188311541-23073f97-e9c9-4f7f-a28f-23acbd4339b5.png)
![Dashboard](https://user-images.githubusercontent.com/60510780/188311560-3c72ad33-4ae6-4e6c-870d-03de13064e36.png)
![File Upload](https://user-images.githubusercontent.com/60510780/188311568-353600cc-3012-417d-a17a-8f291257a5a2.png)
![Analysis Results](https://user-images.githubusercontent.com/60510780/188311580-a7861455-d42e-4998-bdbd-dd27b7ae3cd7.png)
![Transaction Details](https://user-images.githubusercontent.com/60510780/188311589-5c002eea-6c80-4030-849e-c60c3c11a41d.png)
![Statistics View](https://user-images.githubusercontent.com/60510780/188311596-660bcf09-2533-4091-ade4-40020cd64bad.png)
![Detection Report](https://user-images.githubusercontent.com/60510780/188311599-f0c45358-5cd7-40d2-b862-8769031a3cad.png)

## 🛠️ Development Tools

| Purpose | Tool |
|---------|------|
| Version Control | GitHub |
| Project Management | Trello |
| Model Training | Google Colab with CUDA |

## ✨ Features

- Real-time fraud detection
- Batch transaction processing
- User authentication system
- Interactive dashboard
- High accuracy classification
- File-based data import
- Detailed analysis reports

## 📖 Documentation

Complete project reports and system diagrams are available in the [Documents](Documents/) folder.

## 🎯 Use Cases

- Credit card transaction monitoring
- Fraud pattern identification
- Risk assessment for financial institutions
- Real-time transaction validation

---

*Machine learning application for financial fraud detection*
