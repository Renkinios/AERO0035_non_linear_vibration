# AERO0035: Nonlinear Vibration of Aerospace Structures

## Measure, Identify, Simulate, and Understand the Nonlinear Vibration of a 2-Degree-of-Freedom System
### Academic Year 2024 – 2025

#### Authors:
- Victor Renkin (s2306326)
- Felix Weis (S201629)

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [AI](#ai)

## Introduction
The purpose of this project is to identify and simulate the nonlinear vibrations of a 2-degree-of-freedom system. The identification process involves three key steps: detection, characterization, and parameter estimation. The simulation is conducted using Nonlinear Frequency Responses (NLFRs) and Nonlinear Normal Modes (NNMs). Comprehensive details are provided in the accompanying report.


## Requirements
This project requires the installation of the packages listed in the `requirements.txt` file. To install these dependencies, ensure that [Python](https://www.python.org/) and [pip](https://pip.pypa.io/en/stable/) are installed, then execute the following command:

```bash
pip install -r requirements.txt
```
## Usage
This script allows running simulations and identifications. You can execute all tasks by default or specify which task to run using command-line arguments. To run by default the project the user can run the following command:

```bash
python src/main.py
```
Is important to note that the user need to be in the folder where the `main.py` file is located. The code will generate the figures and the results of the project. The figures will be saved in the `figures` folder. The user can also change the parameters of the system in the `main.py` file.

If the user just one two run the identification part of the project, the user can run the following command:

```bash
python src/main.py --identification
```
if he only wants to run the simulation part of the project, the user can run the following command:

```bash
python src/main.py --simulation
```
If the user need to have some help concerning the runing it can run the following command:

```bash
python src/main.py -h
```


## Project Structure

- **`data/`**: Contains the data used in the project.  
- **`figures/`**: Stores the figures related to the project. Subfolders `identification` and `simulation` contain figures corresponding to their respective sections.  
- **`src/`**: Includes the project's source code, organized into two main parts: `identification` and `simulation`. Several key files are present:
  - **`VizTool.py`**: Used for generating all graphical representations.  
  - **`DataPull.py`**: Handles data extraction.  
  - **`main.py`**: Compiles and executes the project.  


## AI

The AI is used to occasionally correct the code and to reformulate sentences from the report.
