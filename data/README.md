# Data Dictionary: Synthetic SaaS Behavior

This dataset contains synthetic user behavior metrics designed to simulate a B2B SaaS platform. It is used to train and benchmark classification models (Predicting Pro conversion).

## Features

| Feature | Type | Description |
| :--- | :--- | :--- |
| `user_id` | Integer | Unique identifier for the user. |
| `days_since_signup` | Integer | Number of days since the user registered (1 - 364). |
| `sessions_last_7_days` | Integer | Total login sessions in the past week (0 - 49). |
| `avg_session_duration` | Float | Average session time in minutes (0.5 - 30.0). |
| `budgets_created` | Integer | Lifetime number of budgets created (0 - 99). |
| `pdfs_downloaded` | Integer | Lifetime number of PDFs exported (0 - 39). |
| `clients_added` | Integer | Number of clients stored in the CRM (0 - 19). |
| `sector` | String | Industry category (construction, consulting, retail, education). |
| `converted_to_pro` | Integer | **Target Variable**. 1 if the user upgraded to a paid plan, 0 otherwise. |

## Target Distribution Logic
The `converted_to_pro` label is not purely random. It is heavily weighted by high-intent actions (`pdfs_downloaded` and `budgets_created`), offset by inactivity (`days_since_signup`), and includes Gaussian noise to simulate real-world unpredictability. The top 15% scoring users are flagged as converted (1).