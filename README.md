# Credit-Card-Fraudulent-Detection

<br>


### Mustafa Tayyip BAYRAM   
### Furkan ÖCALAN  

<br>

![image](https://user-images.githubusercontent.com/60510780/188311216-8c1e087d-ebac-4565-9d8d-87189d327ab3.png)

<hr>



## Specification about what we used and achieved.

***************
### Data

- [creditcard.csv](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

***************

### Model Training

- Architecture
    - Logistic Regression

- Inference Results
    - Accuracy: 0.976
    - Recall: 0.896

***************

### Application  

| Idx | Tool-Framework |
| ------ | ------ |
| Web | Flask |
| DBMS | MySQL |
| Template Management | Blueprint |

- Authentication
    - Login-register implementations.
- File
    - Processes from file uploading to analyze.
- Home
    - Processes from analyze to end of the application.
- Templates
    - Files required for rendering purpose.
- config
    - Database connection credentials.

***************
### Helper Tools 

| Idx | Tool-Framework |
| ------ | ------ |
| VCS | Github |
| Scrum Tool | Trello |
| Model Training | Google Collab & CUDA |

***************
### Project Reports

Under the Documents folder, report and diagrams are accessible.

***************

Notebooks used to train the model for this application can be found [here](ANALYSIS.ipynb).

<hr>

## Steps followed to setup the project

1. Initialise the application by downloading dependencies  by entering the following command in terminal, after getting into the project directory:

```(bash)
pip install -r requirements.txt
```

2. Get the model and put it Analyze/Models directory. [You can get it from notebook or contact us.]
3. Change database credentials according to your database. [apps/config.py line:13]
4. Start the application
```(bash)
$env:FLASK_ENV="development"    # [Use it only during the development stage.]
$env:FLASK_DEBUG=1              # [Use it only during the development stage.]
$env:FLASK_APP = ".\run.py"
flask run
```

<hr>

<br>

 
## Screenshots of the application

![image](https://user-images.githubusercontent.com/60510780/188311541-23073f97-e9c9-4f7f-a28f-23acbd4339b5.png)
![image](https://user-images.githubusercontent.com/60510780/188311560-3c72ad33-4ae6-4e6c-870d-03de13064e36.png)
![image](https://user-images.githubusercontent.com/60510780/188311568-353600cc-3012-417d-a17a-8f291257a5a2.png)
![image](https://user-images.githubusercontent.com/60510780/188311580-a7861455-d42e-4998-bdbd-dd27b7ae3cd7.png)
![image](https://user-images.githubusercontent.com/60510780/188311589-5c002eea-6c80-4030-849e-c60c3c11a41d.png)
![image](https://user-images.githubusercontent.com/60510780/188311596-660bcf09-2533-4091-ade4-40020cd64bad.png)
![image](https://user-images.githubusercontent.com/60510780/188311599-f0c45358-5cd7-40d2-b862-8769031a3cad.png)

<hr>


To Contact Us::
- Mustafa Tayyip BAYRAM
    - [LinkedIn](https://www.linkedin.com/in/mutabay/)
- Furkan ÖCALAN
    - [LinkedIn](https://www.linkedin.com/in/furkan-ocalan-16186a174/)



