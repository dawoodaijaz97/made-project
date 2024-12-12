# **MADE WS2024/25 \- Homeworks**

## Methods of Advanced Data Engineering

Please see slide deck A01 on the handling and grading of homework.

# **Course Organization** {#course-organization}

[https://made.uni1.de](https://made.uni1.de/)

**Table of Contents**

[Course Organization](#course-organization)

[Project Work](#project-work)

[Project Work 1 \- Set Up Project](#project-work-1---set-up-project)

[Project Work 2 \- Project Plan](#project-work-2---project-plan)

[Project Work 3 \- Data Pipeline](#project-work-3---data-pipeline)

[Project Work 4 \- Data Report](#project-work-4---data-report)

[Project Work 5 \- Automated Testing](#project-work-5---automated-testing)

[Project Work 6 \- CI](#project-work-6---ci)

[Project Work 7 \- Final Report](#project-work-7---final-report)

[Exercises](#exercises)

[Exercise 1](#exercise-1)

[Exercise 2](#exercise-2)

[Exercise 3](#exercise-3)

[Exercise 4](#exercise-4)

[Exercise 5](#exercise-5)

# **Project Work** {#project-work}

You will develop an **individual** data science project over the course of the semester. 

* The project work is conducted self-organized by the student  
  * **This semester’s topic: “The Americas” (Projects with relation to North-, Middle- or South-America)**  
* The project has to be based on at least two different open data sources/set  
  * Open data sources to consider (feel free to go beyond):  
    * [Mobilithek](https://mobilithek.info/)  
    * [European Data Portal](https://data.europa.eu/)  
    * [GovData](https://www.govdata.de/)  
    * [GitHub \- awesomedata/awesome-public-datasets: A topic-centric list of HQ open datasets.](https://github.com/awesomedata/awesome-public-datasets)  
  * Do not use APIs you will need to continuously crawl, only static data sets you can download once  
  * Make sure you are allowed to use the data license-wise  (e.g., it is licensed under an open data license) and read up on your obligations\!  
  * Tell your fellow students about interesting data sources in the course forum: [​​https://www.studon.fau.de/frm5003028.html](https://www.studon.fau.de/frm5003028.html)  
* Use Python LTS or Jayvee to implement your project work  
* The goal of the project is to create a report that answers an interesting question based on at least two data sources  
  * [Example projects](https://oss.cs.fau.de/tag/made-projects/)

## **Project Work 1 \- Set Up Project** {#project-work-1---set-up-project}

* Create a public GitHub repository for the module by forking [**https://github.com/jvalue/made-template**](https://github.com/jvalue/made-template)  
* (optional) Rename your repository as you see fit  
* Answer Google Form with a link to your repository  
  * [https://forms.gle/N8ev7giukG86EtZd8](https://forms.gle/N8ev7giukG86EtZd8)  
  * **Do not rename your forked GitHub repository after submitting the form\!**  
* (optional) Set up Python / Jayvee / Jupyter Notebook environment  
  * [https://jvalue.github.io/jayvee/](https://jvalue.github.io/jayvee/)  
    * Consider giving Jayvee a star at [https://github.com/jvalue/jayvee](https://github.com/jvalue/jayvee) to be kept in the loop about new releases  
* (Optional) Watch and get familiar with Jayvee basics using the following resources:  
  * Core concepts video: 	[https://www.youtube.com/watch?v=X8fOK8JIBZA](https://www.youtube.com/watch?v=X8fOK8JIBZA)  
  * Core concept docs: 	[https://jvalue.github.io/jayvee/docs/user/core-concepts](https://jvalue.github.io/jayvee/docs/user/core-concepts)  
  * Tutorial examples: 	[https://jvalue.github.io/jayvee/docs/category/jayvee-examples](https://jvalue.github.io/jayvee/docs/category/jayvee-examples)

## **Project Work 2 \- Project Plan** {#project-work-2---project-plan}

* **Submit** project plan  
  * As markdown file ***project-plan.md*** in the **/project** directory of your repository  
  * Follow the [example](https://github.com/jvalue/made-template/blob/main/examples/project-plan-example.md) to do so   
  * Create coarse-grained issues that layout the working packages you will work on during the semester and link them in section “Work Packages” in the project plan. This plan is allowed to be enhanced and changed over the course of the semester. Please keep it up-to-date.  
* (Optional) Prepare for Project Work 3 \- Data Pipeline  
  * Explore your chosen datasets  
    * What data is available? What errors are there?  
    * What limitations present themselves, is data missing and representative?  
    * What data types are relevant, do you need to research anything?  
  * You can use a Python notebook to load and explore your data (see the [example](https://github.com/jvalue/made-template/blob/main/examples/data-exploration-example.ipynb) in your repository)  
  * You **do not need to make a submission** for this part of the Project Work, it is just for you to get more familiar with your data

## **Project Work 3 \- Data Pipeline** {#project-work-3---data-pipeline}

* Follow your project plan to build an automated data pipeline for your project  
  * Write a script (for example in Python or Jayvee) that pulls the data sets you chose from the internet, transforms it and fixes errors, and finally stores your data in the /data directory  
    * Place the script in the **/project** directory (any file name is fine)  
    * Add a **/project/pipeline.sh** that starts your pipeline as you would do from the command line as entry point:  
      * E.g. if you run your script on your command line using \`python3 /project/pipeline.py\`, create a /project/pipeline.sh with the content: 

        \#\!/bin/bash  
        python3 /project/pipeline.py

  * The output of the script should be: datasets in your **/data** directory (e.g., as SQLite databases)   
    * Do **NOT** check in your data sets, just your script  
    * You can use [.gitignore](https://git-scm.com/docs/gitignore) to avoid checking in files on git  
    * This data set will be the base for your data report in future project work  
* Update the issues and project plan if necessary

## **Project Work 4 \- Data Report** {#project-work-4---data-report}

* **Remember: This is a required submission to pass the course, not submitting it by the deadline will result in you failing the course**  
* Submit a report about your choice of data and how you improved it using an automated data pipeline  
  * Must be:  
    * In your **/project** folder  
    * Called **data-report.pdf**  
    * **Maximum length: 3 A4 pages**  
  * Can  
    * Be produced using a Jupyter Notebook, Markdown, LateX… as long as the final output is the pdf file  
    * Include figures and tables to give an overview of data pipeline structure or data sources  
  * Audience  
    * An interested reader with software engineering and data engineering skills who knows nothing about your project  
  * Content / Structure  
    * Question  
      * Your question for your whole project  
    * Data Sources  
      * Describe your data sources: Why you have chosen them, where they are from, and what data they contain  
        * What is the structure and quality of your data? (Compare lecture D01)  
      * Describe the licenses of your data sources, why you are allowed to use the data and how you are planning to follow their obligations  
        * If your source data is under a standard open-data license just pointing out where to find that is enough information for being allowed to use it, please still describe how you plan to fulfill their obligations  
        * Add a direct link to the source of your claim that the data set is under the license you specify  
    * Data Pipeline  
      * Describe your data pipeline on a high level, which technology did you use to implement it  
      * Which transformation or cleaning steps did you do and why?  
      * What problems did you encounter and how did you solve them?  
      * Describe what meta-quality measures you implemented, how does your pipeline deal with errors or changing input data?  
    * Result and Limitations  
      * Describe the output data of your data pipeline  
        * What is the data structure and quality of your result? (Compare lecture D01)  
      * What data format did you choose as the output of your pipeline and why  
      * Critically reflect on your data and any potential issues you anticipate for your final report

## **Project Work 5 \- Automated Testing** {#project-work-5---automated-testing}

* Add automated tests for your project  
  * Add a **/project/tests.sh** file that executes your tests  
    * Same approach as for Project Work 4  
  * There should be at least one test case on the system-test level   
    * Executes your data pipeline  
    * Validates that the output file(s) exist (but make sure the data pipeline creates them and you do not check them in)  
* (optional) Continue working on your project  
  * If you are not finished, complete the exploratory data analysis  
  * Start planning what you want to write about in your final report (for an example, see /examples in your template repository or [https://oss.cs.fau.de/tag/made-projects/](https://oss.cs.fau.de/tag/made-projects/))  
    * Careful: Look at the report examples as inspiration for ideas but not structure, previous semesters might have had other requirements  
* Update your issues if necessary

## **Project Work 6 \- CI** {#project-work-6---ci}

* Add CI for your project  
  * Use [GitHub Actions](https://docs.github.com/en/actions/quickstart) with a **new file** (not in *exercise-feedback.yml*)  
  * On every push to the main branch, execute your tests  
    * Using the tests.sh (from project work 5\)  
  * If your tests download external data or are too expensive to run using GitHub actions  
    * Consider using mocks for data as discussed in the testing lecture  
  * If all else fails, comment out the actual test invocation in your test.sh (with an explanation why) but still set up a GitHub action  
* (optional) Continue working on your project  
  * Start working on your final report (upcoming project work)  
* Update the issues if necessary

## **Project Work 7 \- Final Report** {#project-work-7---final-report}

* **Remember: The final report is a required submission to pass the course, not submitting it by the deadline will result in you failing the course**  
* Final report about your data analysis  
  * Must be  
    * In your **/project** folder  
    * Called **analysis-report.pdf**  
    * Length: **max. 4 pages** in A4 format  
      * In case your report is longer: Focus on the story you want to tell and prefer high-quality figures with a higher depth of information and **shorten the report to the max length**.  
  * Can  
    * Be produced using a Jupyter Notebook, Markdown, LateX… as long as the final output is the **pdf** file  
    * Include figures and tables to explain your findings  
  * Audience  
    * An interested reader with software engineering and data engineering skills who knows nothing about your project  
  * Content/Structure  
    * **Introduction**: Introduces and motivates the question you answer in the report  
    * **Used Data**: Describe the used data you used for the analysis (the output of your data pipeline). Briefly discuss the structure and meaning of the data (such as domain-specific value types), and implement the obligations to comply with the data licenses of your data sources if necessary.  
    * **Analysis**: Present the executed analysis: method, result, and interpretation. This section doesn’t need to show code, but the reader should understand what you did and why it is appropriate what you’ve done to answer the question. Focus on the results (positive and/or negative) but leave out any failed attempts.  
    * **Conclusions:** Explicitly answer the question you posed to yourself. Critically reflect whether the question could be answered completely and if there are any remaining uncertainties or limitations.

# **Exercises** {#exercises}

* Place all exercise submissions into the folder named “**exercises**” in your GitHub repository  
  * Name exercise submissions “exercise\<number\>.jv”  
    * For example, for exercise 1, you must submit the following file: **/exercises/exercise1.jv**  
* We will grade the version of the exercise that is in your public GitHub repository at the **deadline** (\!)

## **Exercise 1** {#exercise-1}

* Build an automated data pipeline for the following source:  
  * [https://opendata.rhein-kreis-neuss.de/api/explore/v2.1/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv?lang=en\&timezone=Europe%2FBerlin\&use\_labels=true\&delimiter=%3B](https://opendata.rhein-kreis-neuss.de/api/explore/v2.1/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv?lang=en&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B)  
  * Do NOT use a local file, always take the data from the link above  
* Goal  
  * Write data into a SQLite database called “**airports.sqlite**”, in the table “**airports**”  
  * Do **not** save the following columns: Zeitzone, DST, Zeitzonen-Datenbank, geo\_punkt  
  * Assign fitting built-in SQLite types (e.g., BIGINT, TEXT or FLOAT) to all other columns  
  * Do not rename column names  
  * No further data validation is required, do not drop any rows or change any data points  
* Use **Jayvee version 0.6.3**  
* Submit as  **/exercises/exercise1.jv**

## **Exercise 2** {#exercise-2}

* Build an automated data pipeline for the following source:  
  * [https://www.govdata.de/web/guest/suchen/-/details/stadt-neuss-baumpflanzungen-2023](https://www.govdata.de/web/guest/suchen/-/details/stadt-neuss-baumpflanzungen-2023)  
  * direct link to CSV: [https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/stadt-neuss-herbstpflanzung-2023/exports/csv](https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/stadt-neuss-herbstpflanzung-2023/exports/csv)  
  * Do NOT use a local file, always take the data from the link above  
* Goal  
  * Keep only valid data we are interested in  
    * Define types of values and constraints for them  
    * We are only interested in “Vogelsang”, valid stadtteil start with "Vogelsang"  
    * "id" contains geopoints with the following pattern:  
      * {geo-coordinate 1}, {geo-coordinate 2}  
      * a geo-coordinate is defined as {1-3 numbers}.{numbers}  
    * Drop "baumart\_deutsch" column  
    * Drop all rows with invalid values  
  * Assign fitting built-in SQLite types (e.g., BIGINT, TEXT or FLOAT) to all columns  
  * Write data into a SQLite database called “**trees.sqlite**”, in the table “**trees**”  
* Use **Jayvee version 0.6.3**  
* Submit as  **/exercises/exercise2.jv**

## **Exercise 3** {#exercise-3}

* Update Jayvee to version 0.6.4  
  * [Update instructions](https://jvalue.github.io/jayvee/docs/user/intro/update)  
* Build an automated data pipeline for the following source:  
  * Meta data: [https://datacatalog.worldbank.org/search/dataset/0061114/World-Development-Report-2022---Chapter-5-Figures](https://datacatalog.worldbank.org/search/dataset/0061114/World-Development-Report-2022---Chapter-5-Figures)  
  * direct link to data: [https://thedocs.worldbank.org/en/doc/7d852628d96b9411d43e5d36d5dff941-0050062022/original/Graphs-Chapter-5-02082022.xlsx](https://thedocs.worldbank.org/en/doc/7d852628d96b9411d43e5d36d5dff941-0050062022/original/Graphs-Chapter-5-02082022.xlsx)  
  * Do NOT use a local file, always take the data from the link above  
* Goal  
  * Extract the data we are interested in  
    * Extract the sheet called “Figure S5.1.2” from the Excel file  
    * Ignore the figure itself and only keep the table with actual data (from cell P2 to S45)  
  * Rename header columns: “ISO3” to "Country Code", “GDP per capita (US$, thousands)” to "GDP per Capita", “Share of government sustainable bonds" to "Bond Issuance Share"  
    * “Economy” does not have to be renamed  
  * Validate data, drop all invalid rows  
    * "Country Code" must be a valid ISO 3166-1 alpha-3 country code (must not be empty)  
    * "GDP per Capita" must be a positive decimal or 0 (must not be empty)  
    * "Bond Issuance Share" must be a decimal between 0 and 1 (both values included, must not be empty)  
  * Assign fitting built-in SQLite types (e.g., BIGINT, TEXT or FLOAT) to all columns  
  * Write data into a SQLite database called “**country-stats.sqlite**”  
    * One table “**bondIssuance**”, containing the data about bond issuance share (columns "Country Code" and "Bond Issuance Share")  
    * One table “**gdpPerCapita**”, containing the data about GDP per capita (columns "Country Code" and "GDP per Capita")  
* Use **Jayvee version 0.6.4 (new release\!)**  
  * Jayvee 0.6.4 has a *CountryCodeAlpha3 value type* in its standard library that you might find useful  
* Submit as  **/exercises/exercise3.jv**

## **Exercise 4** {#exercise-4}

* Build an automated data pipeline for the following source:  
  * [https://mobilithek.info/offers/526718847762190336](https://mobilithek.info/offers/526718847762190336)  
  * Direct download link: [https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip](https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip)  
* Goal  
  * Download and unzip data  
    * Use the “data.csv” in the zip file  
  * Reshape data  
    * Only use the columns "Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C"  
    * There can be multiple temperature measurements per row  
      * You can ignore all columns to the right of the first “​​Geraet aktiv”  
    * Translate/rename column headers from German to English:  
      * “Geraet” to “id”  
      * “Hersteller” to “producer”  
      * “Model” to “model”  
      * “Monat” to “month”  
      * “Temperatur in °C (DWD)” to “temperature”  
      * “Batterietemperatur in °C” to “battery\_temperature”  
  * Transform data  
    * Transform temperatures in Celsius to Fahrenheit (formula is (TemperatureInCelsius \* 9/5) \+ 32\) in place (keep the same column names)  
      * For the columns temperature and battery\_temperature  
  * Validate data  
    * Use validations as you see fit, e.g., for “Geraet” to be an id over 0  
  * Use fitting SQLite types (e.g., BIGINT, TEXT or FLOAT) for all columns  
  * Write data into a SQLite database called “**temperatures.sqlite**”, in the table “**temperatures**”  
* Use **Jayvee version 0.6.4**  
* Submit as  **/exercises/exercise4.jv**

## **Exercise 5** {#exercise-5}

* Build an automated data pipeline for the following source:  
  * Direct download link: [https://gtfs.rhoenenergie-bus.de/GTFS.zip](https://gtfs.rhoenenergie-bus.de/GTFS.zip)  
* Goal  
  * Work with domain-specific GTFS data  
  * Pick out only stops (from stops.txt)  
    * Only the columns stop\_id, stop\_name, stop\_lat, stop\_lon, zone\_id with fitting data types  
  * Filter data  
    * Only keep stops from zone 1925  
  * Validate data  
    * stop\_name must be a text but must maintain german umlauts  
    * stop\_lat/stop\_lon must be a geographic coordinates between \-90 and 90, including upper/lower bounds  
    * Drop rows containing invalid data  
  * Use fitting SQLite types (e.g., BIGINT, TEXT or FLOAT) for all columns  
  * Write data into a SQLite database called “**gtfs.sqlite**”, in the table “**stops**”  
* Use **Jayvee version 0.6.4**  
* Submit as  **/exercises/exercise5.jv**