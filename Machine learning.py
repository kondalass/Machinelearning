#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1
import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()#sorting the list
print("Sorted list is:",ages)
greatest=max(ages)#finding maximum and minimum ages from the list
smallest=min(ages)
ages.append(greatest)#adding max and min ages
ages.append(smallest)
ages.sort()
middle=statistics.median(ages)
l=len(ages)
summation=sum(ages)
average=summation/l#mean of the ages
difference=greatest-smallest#finding the range
print("Maximum age is:",greatest,)
print("Minimum age is:",smallest,)
print("List after adding min and max ages:",ages,)
print("Median age is:",middle)
print("Mean age is:",average)
print("The range is:",difference)


# In[2]:


#Question 2
dog={}#creating empty dictionaty,dog
#adding items to dog dictionary
dog['name']=""
dog['color']=""
dog['breed']=""
dog['legs']=""
dog['age']=""
print("The dog dictionary:",dog)
#creating empty dictionary,student
student={}
student['first_name']=""
student['last_name']=""
student['gender']=""
student['age']=""
student['marital status']=""
student['skills']=""
student['country']=""
student['city']=""
student['address']=""
length=len(student)
skills_value=(student['skills'])#get value of skills from dictionary
datatype=type(skills_value)
print("The student dictionary:",student)
print("length of student dictioanry is =",length)
print("Vakue of skills =",skills_value,"and data type is :",datatype)
student['skills']="programming","Networking"#adding 2 skill values
print("The List after adding 2 values for skills:",student)
the_keys=list(student.keys())#get dictionary keys
the_values=list(student.values())
print("The dictionary keys are:",the_keys)
print("The dictionary values are:",the_values)


# In[3]:


#Question 3
#creating brothers and sisters tuples
brothers=('Jackson','Nelson','John')
sisters=('Mary','Aggie')
siblings=brothers+sisters#joining the two tuples
l=len(siblings)
parents=('Harry','Nancy')#creat parent tuple
family_members=parents+siblings#joining parents and siblings tuple

print("Brothers tuple:",brothers)
print("Sisters tuple:",sisters)
print("Siblings tuple:",siblings)
print("Number of siblings is:",l)
print("Family mebers:",family_members)


# In[4]:


#Question 4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
l=len(it_companies)#get length of it_companies set
it_companies.add('Twitter')#adding twitter to the it_companies set
print("Length of the it_companies =",l)
print("Set after adding Twitter in it_companies",it_companies)
companies=['Turtle','Zalego','Tiktok','softonic']#creatig IT company set
it_companies.update(companies)#adding IT companies to the it_companies set
print("After inserting multiple IT companies:",it_companies)
it_companies.remove('Amazon')#removing amazon
print("After removing Amazon:",it_companies)
#Discard removes an element in a set and returns the remaining elements in the set.
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
A |= B#join Aand B
print("After joining A and B:",A)
A = {19, 22, 24, 20, 25, 26}
I=A.intersection(B)#intersecting A and B
print("A intersection B:",I)
A = {19, 22, 24, 20, 25, 26}
print("A Subset of B?",A.issubset(B))#check subset
A = {19, 22, 24, 20, 25, 26}
print("A disjoint B?:",A.isdisjoint(B))#check disjoint
A = {19, 22, 24, 20, 25, 26}
differ=A.symmetric_difference(B)#get symmetric difference
print("Symmetric difference =",differ)
cl1=A.clear()#clearing the set
cl2=B.clear()
print("Clear A:",cl1)
print("Clear B:",cl2)
convert=set(age)
#convert list to set and get their length 
print("Coverted set from list:",convert)
l=len(convert)
l_List=len(age)
print("Length of the List  =",l_List)
print("Length of the set  =",l)
print("Length of the List is greater compared to the Length of the Set")


# In[5]:


#Question 5
radius=30
pie=22/7
#claculating an area of a circle
_area_of_circle_=pie*radius*radius
_circum_of_circle_=pie*radius*2
take_radius=int(input("PLease enter the Radius = "))#prompting user input
area_of_circle=pie*take_radius*take_radius

print("Area of the circle is:",_area_of_circle_,)
print("Circumferece of the circle is:",_circum_of_circle_)
print("Area of the circle from user input is:",area_of_circle)


# In[6]:


#Question 6
#creating function to count number of unique words
def unique(state):
    print("Number of unique words  = ",len(state))#returns the number of unique words
statement="I am a teacher and I love to inspire and teach people"
s = set(statement.split(" "))#spliting words in th set
unique(s)


# In[7]:


#Question 7
#using tab escape character, \t for horizontal spacing between the words
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")


# In[8]:


#Question 8
radius = 10
area = 3.14 * radius ** 2
area=int(area)#formatting the area to interger
print("The area of a circle with radius",radius,"is",area,"meters square")#string formatting to include radius and its area


# In[9]:


#Question 9
weight_list=[]#creating an empty list
for weight in range(4):
    a=int(input("Enter the weights"))#requesting user input
    weight_list.append(a)
print("Lbs list:",weight_list)
#converting the Lbs to kilograms
kilograms=[]
for w in weight_list:
    kgs=(w/2.205)
    kilograms.append(kgs)
print("KGs list:",kilograms)


# In[10]:


#Question 10
import numpy as np  #importing important python libraries
import matplotlib.pyplot as plt  
import pandas as pd  
dataframe=pd.read_csv("dataset.csv")#reading the dataset
x= dataframe['Feature'].values  
y= dataframe['Class'].values 
#dividing data equally into training and testing data
from sklearn.model_selection import train_test_split  
features_tr, features_te, label_tr, label_te= train_test_split(x, y, random_state=0, train_size= 0.5 ) 
#reshaping the data feature and labes into 2D array
features_tr = np.array(features_tr).reshape(-1,1)
features_te = np.array(features_te).reshape(-1,1)
#Normalizing data
from sklearn.preprocessing import StandardScaler    
normalization= StandardScaler()    
features_tr= normalization.fit_transform(features_tr)    
features_te= normalization.transform(features_te)  
#fiting the training data into classifier model 
from sklearn.neighbors import KNeighborsClassifier  
model= KNeighborsClassifier(n_neighbors=3 )  
model.fit(features_tr, label_tr)
#Predicting the test set result  
predict_class= model.predict(features_te)  
print("Predicted Test Samples Output:",predict_class)

#creating a confusion matrix
from sklearn.metrics import confusion_matrix  
model_evaluation= confusion_matrix(label_te, predict_class) 
print("Confusion matrix:\n",model_evaluation)
#finding model accuracy
count=sum(sum(model_evaluation))
accuracy=(model_evaluation[0,0]+model_evaluation[1,1])/count
print ('Accuracy =: ', accuracy)
# finding model sensitivity
sense = model_evaluation[0,0]/(model_evaluation[0,0]+model_evaluation[0,1])
print('Sensitivity =: ', sense )
#finding model specificity
speci = model_evaluation[1,1]/(model_evaluation[1,0]+model_evaluation[1,1])
print('Specificity =: ', speci)


# In[ ]:




