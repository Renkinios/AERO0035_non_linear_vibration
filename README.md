# AERO0035: Nonlinear Vibration of Aerospace Structures

## Identifying and Simulating Nonlinearities in a 2-DoF Mechanical System
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
The overleaf link to the report is [here](https://www.overleaf.com/read/vpkzxfvyhgvq#7ad03e).
The link for the slides is [here](https://www.overleaf.com/read/tctrtqygsxnv#d2b162).


## Requirements
This project requires the installation of the packages listed in the `requirements.txt` file. To install these dependencies, ensure that [Python](https://www.python.org/) and [pip](https://pip.pypa.io/en/stable/) are installed, then execute the following command:

```bash
pip install -r requirements.txt
```
## Usage
This script enables simulations and identifications. By default, all tasks can be executed, or specific tasks can be selected using command-line arguments. It is **important** to note that the data is too large to include here and must be added manually. To run the project with default settings, use the following command:

```bash
python src/main.py
```
The code will generate the figures and the results of the project. The figures will be saved in the `figures` folder. The user can also change the parameters of the system in the `main.py` file.

To run specific parts of the project, the following commands can be used:
- Identification :

```bash
python src/main.py --identification
```
- Simulation :

```bash
python src/main.py --simulation
```
For help on the command-line arguments, use the following command:

```bash
python src/main.py -h
```


## Project Structure

- **`data/`**: Contains the data used in the project, which must be imported manually. Each test is categorized into different folders: `first_lab`, `second_lab`, `third_lab`, and `fourth_lab`.

- **`figures/`**: Stores the figures related to the project. Subfolders `identification` and `simulation` contain figures corresponding to their respective sections.  

- **`src/`**: Includes the project's source code, organized into two main parts: `identification` and `simulation`. Several key files are present:
  - **`VizTool.py`**: Used for generating all graphical representations.  
  - **`DataPull.py`**: Handles data extraction.  
  - **`main.py`**: Compiles and executes the project.  


## AI

The AI is used to occasionally correct the code and to reformulate sentences from the report.
