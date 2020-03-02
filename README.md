# Click Through Rate Prediction

### Objective : 
To find how likely the user clicks the search result based on various attributes

## Data Download:  https://www.kaggle.com/c/expedia-personalized-sort/data
After downloading the dataset, place `train.csv` and `test.csv` inside `datasets/data`

### Runtime tested on: 
Python 3.7.4

### Instructions
`pip install -r requirements.txt` <br/>
`cd src` <br/>
`python data_preprocessing.py` <br/>
 `python model.py`
 
 ### References
 1. Rendle, S. (2010). [Factorization Machines](https://www.csie.ntu.edu.tw/~b97053/paper/Rendle2010FM.pdf)
 2. YuChin Juan, Yong Zhuang, and Wei-Sheng Chin (2016). [Field-aware Factorization Machines for CTR Prediction](https://www.andrew.cmu.edu/user/yongzhua/conferences/ffm.pdf)