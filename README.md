# 💊 Smart Medicine Reminder

## Overview

Smart Medicine Reminder is a healthcare-focused web application developed using Python and Streamlit. The application helps users manage their medicines by storing medicine names, dosage information, and medication timings in a simple and user-friendly interface.

The project was developed as part of Hackathon 1 and focuses on improving medication adherence while supporting multilingual accessibility through Internationalization (i18n) and Localization (l10n).

---

## Problem Statement

Many people, especially elderly patients and individuals with chronic illnesses, forget to take medicines on time. Missing doses can lead to health complications and poor treatment outcomes.

There is a need for a simple and accessible medicine management solution that helps users organize and track their medication schedules.

---

## Solution

Smart Medicine Reminder provides:

* Medicine management dashboard
* Medicine name, dosage, and time tracking
* Multilingual user interface
* Local data storage
* Easy-to-use healthcare assistant interface

The application is designed to be lightweight, simple, and accessible for users of all age groups.

---

## Features

### ✅ Medicine Management

* Add medicine details
* Store dosage information
* Save medicine timings
* View saved medicines

### ✅ Data Management

* Display all medicines in a table
* Count total medicines
* Clear all medicines when required

### ✅ Multilingual Support (i18n & l10n)

Supported Languages:

* English
* Telugu (తెలుగు)
* Hindi (हिन्दी)

Users can dynamically switch languages using the language selector.

### ✅ Accessibility

* Simple user interface
* Large readable components
* Minimal navigation complexity
* Multi-language support

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### Data Storage

* CSV Files
* Pandas

### Deployment

* Streamlit Community Cloud

### Version Control

* GitHub
* code.swecha.org (GitLab)

---

## Internationalization (i18n) & Localization (l10n)

The application was designed using i18n principles by separating user interface text from application logic.

Localization has been implemented for:

1. English
2. Telugu
3. Hindi

This enables users to interact with the application in their preferred language without affecting functionality.

---

## Project Architecture

User Interface (Streamlit)

↓

Medicine Entry Form

↓

CSV Data Storage

↓

Medicine Dashboard

↓

Language Translation Layer

---

## Installation

### Clone Repository

```bash
git clone https://code.swecha.org/ali_peerulla/smart-medicine-reminder-project.git
```

### Navigate to Project

```bash
cd smart-medicine-reminder-project
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## Project Demo

### GitHub Repository

https://github.com/alipeerulla04/smart-medicine-reminder

### Live Application

https://smart-medicine-reminder-geq8sjmhhwlmhv2eeckndq.streamlit.app

---

## Target Users

* Elderly patients
* Chronic disease patients
* Caregivers
* Family members
* Healthcare volunteers

---

## Future Enhancements

* SMS reminders
* Email notifications
* Mobile application
* Doctor integration
* AI-powered medicine recommendations
* Offline medicine reminder alerts
* Cloud database integration

---

## Learnings

During the development of this project we learned:

* Streamlit application development
* GitHub deployment workflow
* Cloud deployment using Streamlit Community Cloud
* Internationalization (i18n)
* Localization (l10n)
* Healthcare-focused application design
* Version control using Git and GitLab

---



### College

GITAM University Hyderabad

### Developer

Shaik Mohammad Ali Peerulla,
Nikhil Goud 
---

## License

This project was developed for educational and hackathon purposes.
