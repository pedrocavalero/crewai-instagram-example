#!/usr/bin/env python
from linkedin.crew import LinkedInCrew
import datetime


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        "current_date": datetime.datetime.now().strftime("%Y-%m-%d"),
        "LinkedIn_description": "International Jobs for Brazilian Software Developers",  # input("Enter the page description here: "),
        "topic_of_the_week": "Best way for Brazilians to get an international developer job",  # input("Enter the topic of the week here: "),
    }
    LinkedInCrew().crew().kickoff(inputs=inputs)
