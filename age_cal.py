#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
import datetime

now=datetime.datetime.now()
year=input("what is your birth year")
print ("your birth year is");year
print ("current year");now.year
Age=now.year-int(year)
print ("your age is");Age
Calc=100-Age
finalcalc=now.year+Calc
print ("Your will turn 100 year old in year ");finalcalc


