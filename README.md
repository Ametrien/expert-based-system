## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is a basic expert system that can identify an alien by its features. 
The system consists of knowledge base and inference engine. 
Knowledge base contains information about different types of aliens.
Inference engine evaluates the information provided by user and finds out who the alien in their mind was.
This expert-based system provides both intermediary and final results.
The first question is asked randomly, then the system eliminates questions that would not narrow 
the list of suspects down. System only asks questions that bring you closer to the answer.
For instance, if the first random question was about hair and user answered 'red', the system
will at first say that the alien belongs to the red hair family. The next question will be about 
religion, because all the other parameters of red haired aliens are the same. The system will then
justify its choice.
	
## Technologies
Project is created with:
* Python version: 3.8

## Setup
To run this project, run 'main.py'. 
When asked a question, have a look at the database, determine which alien 
is on your mind and enter a few characterictics of them. 
In the end of the interrogation you will get an answer.
Do not leave user input fields empty.
