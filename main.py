'''
Authors: Amy Zhao, Katrina Delos Reyes, Astha Singhal, Shruti Sharma

This program intends to understand if there is a bias amongst people when it comes to terror attacks. It tries to see how strongly people responded 
to a terror attack in Eastern country vs one in a Western country. 

A terror attack chosen for western country: ___________________
A terror attach chosen for eastern country: ___________________
They are of equal magnitude and (POSIBLY) from the same terror group

We hypothesize that there is a greater bias for western countries. Based on the tweets after a terror attack, we understand the general sentiment/emotion
from the tweets using an LSTM. We normalize the data by accounting for number of users in that region. A more negative sentiment would imply thta it brought 
a greater set of emotions // could make that a shortcoming

NOTE: WE COULD JUST USE AN SVM and just think of a list of words expected from a group that cares like "thoughts, prayers, regards, family" - the group 
with greater % of such words would care more

- It first finds all tweets in the first 24 hours of a terror attack. 
- Passes tweets through LSTM (or SVM) to understand the sentiment


Data visualization using
- bar chart comparing number of tweets in general
	- (or) bubble choropleth thing
- maybe a timeline showing changes in emotions over hours - would need a model to understan % of emotion
- 


Shortcomings
- not enough data
- only comparing two attacks
	- could be an issue with other national events going on to distract people from it
- 
''' 
