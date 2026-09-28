# Problem Statement

## Problem

College students sometimes need help in a subject or programming topic, but they may not know which other student has that skill. Messages in different groups can also become difficult to track.

## Proposed solution

The Student Help Exchange System is a small command-line Python program that stores student profiles and skills. A student can create a help request and search for another student who has the required skill.

## Objectives

- make student-to-student academic help easier to organize
- store simple student skill information
- create and track help requests
- match students using a simple skill comparison
- keep a history of completed help sessions
- use Python course concepts in one practical project

## Target users

College students who want to give or receive academic help.

## Scope

The first version is offline and local. It does not use a website, mobile app, login system, or online messaging service.

## Main functional modules

1. Student Management
2. Skill Management
3. Help Request Management
4. Skill Matching
5. Help Exchange Management
6. Array / Activity Analysis
7. Study Math Tools and Reporting

## Non-functional requirements

### Usability
The application uses a numbered menu and simple questions so a beginner can operate it.

### Reliability
Student, request and history data are saved in JSON files.

### Maintainability
Different tasks are separated into Python modules.

### Error handling
The program checks empty input, invalid numbers, invalid year, duplicate skills, and invalid request states.

### Resource efficiency
The project uses small local JSON files and simple loops. NumPy is used only for the small analysis part.
