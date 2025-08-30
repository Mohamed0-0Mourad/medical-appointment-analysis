# Medical Appointment No-Shows Analysis Dashboard
> Data Resource: https://www.kaggle.com/datasets/joniarroba/noshowappointments

## Tools & Technologies:
Python, Pandas, Plotly, Dash, Flask, HTML, CSS.

---

## **Key Questions Explored**

1. What is the delay between appointment request and actual appointment, and how does it contribute to no-shows?
2. Which age segments have the highest no-shows, and what are the gender dynamics within these groups?
3. What percentage does each age segment contribute to overall no-shows?
4. Which neighborhoods have the highest no-show rates
5. How scholarship affect no-shows? 
6. What is the contribution of different medical conditions to no-show behavior? 
7. What percentage of patients fail to attend despite receiving SMS reminders? and what percentage could have been rescued by an SMS?
8. Are no-shows more common among first-time patients or follow-up appointments?

---

## **Insights**

* **Communication (SMS):**

  * Less than 50% of no-shows reported receiving an SMS reminder, suggesting a major gap in outreach.
* **Neighborhoods:**

  * The highest absence rates are concentrated in *ITARARÉ* and *SANTA CECÍLIA*.

[//]: # (  * Other neighborhoods with notable no-shows include *ENSIADA DE SUA, SANTA HELENA, ARIOVALDO, VILAROBIM, and ILHA DE SANTA MARIA*.)

[//]: # (  * Patients with disabilities are disproportionately absent in *SÃO BENEDITO, SANTA LUCIA, and JUCUTIQUARA*.)
* **Age & Demographics:**

  * Young adults and middle-aged patients account for **55%+ of all no-shows**.
  * Around **60% of patients in these groups face delays of 10+ days** between booking and appointment, contributing significantly to absences.
* **Hypertension:**

  * **Hypertension** is strongly correlated with absences, responsible for an average of **60% of no-shows**, particularly among patients older than teenagers.
  * Around **70% of no-shows are from follow-up patients**, suggesting dissatisfaction or scheduling fatigue rather than first-time disengagement.
  * Highest percentages (**+75%**) of absent and hypertensive customers are in *ENSIADA DE SUA, SANTA HELENA, ARIOVALDO, VILAROBIM, and ILHA DE SANTA MARIA* 
* **Accessibility:**

  * More than **40% of handicapped patients are lost** in certain neighborhoods due to accessibility issues. 
  * These certain neighbourhoods include: *SÃO BENEDITO, SANTA LUCIA, and JUCUTIQUARA*
---

## **Recommendations**

* **For SMS Communication:**

  * Increase SMS coverage and reminders, as improved outreach could reduce absences by up to **50%**.
  * Explore alternative reminders (e.g., WhatsApp, automated calls) for segments with low SMS response rates.

* **For Young & Middle-Aged Patients:**

  * Offer appointment slots outside of traditional work hours.
  * Reduce delays between booking and appointment to under 10 days wherever possible.

* **For Hypertensive Patients:**

  * Prioritize hypertensive patients in scheduling to reduce delays.
  * Reduce wait time.
  * Simplify appointment registration and minimize unnecessary tests.
  * Ensure effective and empathetic patient-provider communication.

* **For Handicapped Patients:**

  * Invest in accessible, handicap-friendly facilities, especially in high-risk neighborhoods (e.g., *SÃO BENEDITO, SANTA LUCIA, JUCUTIQUARA*).

---

## **Conclusion**

No-shows are concentrated among **young and middle-aged hypertensive patients in specific neighborhoods** and are strongly influenced by **appointment delays and communication gaps**. By addressing **scheduling delays, enhancing accessibility, and improving reminder systems**, the organization can significantly reduce no-show rates, improve patient care, optimize resource utilization, and ensure effective patient-provider communication.

> # Live Dashboard link:
> https://momourad.pythonanywhere.com/ 