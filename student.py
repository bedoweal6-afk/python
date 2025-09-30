import pandas as pd
import numpy as np         
import matplotlib.pyplot as plt 
import seaborn as sns     
from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv('student_performance_dataset.csv')
print(df.head())
df = df.drop('Student_ID', axis=1)
df = pd.get_dummies(df, columns=['Gender', 'Parental_Education_Level', 'Internet_Access_at_Home', 'Extracurricular_Activities'], drop_first=True)
df = df.drop('Pass_Fail', axis=1)
print(df.head())
plt.figure(figsize=(8, 5))
sns.histplot(df['Final_Exam_Score'], kde=True, bins=15, color='skyblue')
plt.title('Distribution of Final Exam Score')
plt.xlabel('Final Exam Score')
plt.ylabel('Count')
plt.show()
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Study_Hours_per_Week', y='Final_Exam_Score', data=df, alpha=0.7, color='green')
plt.title('Study Hours per Week vs. Final Exam Score')
plt.xlabel('Study Hours per Week')
plt.ylabel('Final Exam Score')
plt.show()
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Past_Exam_Scores', y='Final_Exam_Score', data=df, alpha=0.7, color='purple')
plt.title('Past Exam Scores vs. Final Exam Score')
plt.xlabel('Past Exam Scores')
plt.ylabel('Final Exam Score')
plt.show()
X = df.drop('Final_Exam_Score', axis=1)
y = df['Final_Exam_Score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)*100
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R²): {r2:.2f}")