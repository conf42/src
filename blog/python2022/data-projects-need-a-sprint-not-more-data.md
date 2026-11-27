# Your data project needs a five-person sprint, not more data

Conf42 Blog, 2022-01-26. https://www.conf42.com/blog/python2022/data-projects-need-a-sprint-not-more-data

In short: Aman Sharma (Twimbit) at Conf42 Python 2022 on why data projects stall and a four-step sprint, plus diagrams, no-code tools and dashboards, to get insights out

Most data projects do not die from a lack of data. They die in the meeting where someone asks why the team is here again. At Conf42 Python 2022, Aman Sharma, co-founder and CTO of Twimbit, a platform for creating and discovering research insights, laid out the six ways data projects stall and a sprint-based process, borrowed from Jake Knapp's *Sprint* book, for getting from a pile of data to a decision.

Fair warning, which he gives himself at the end: this is not a code walkthrough. It is a process talk for the people who plan, staff and present data work.

## Data is the ocean, insights are the lighthouse

Aman opens with the difference between data and insights. "Being inside data is like sailing a boat in a deep ocean, right?" Aman Sharma said at Conf42 Python 2022. You are surrounded by streams of options and cannot tell what you are looking for until something points the way. The whole talk is about building that lighthouse on purpose.

## Six ways a data project stalls

Each problem comes with symptoms and a fix:

- **Goal clarity.** Everyone has a different perception of the goal, so the outcomes differ and ROI is poor. Fix: identify one goal and communicate it.
- **Poor planning.** Missed deadlines, low-yield results and a recurring complaint that the resources are wrong. Often the project just gets abandoned. Fix: tighter structure, fewer deliverables, strict timelines.
- **Dirty data.** Too much time on preprocessing, and a poor ratio of insights to data. Fix: better preprocessing tools and better ingestion at the source, such as how your analytics or survey tools capture data in the first place.
- **Technical challenges.** Small teams are short on tools, people and talent; big ones also wrestle with GDPR and privacy. Fix: no-code tools and documentation.
- **Complexity.** Insights presented in a way the decision maker cannot read lead to bad decisions, and eventually to stakeholders deciding data science is too complicated to bother with. Fix: better visualisation, no-code and a feedback round at the end of each project.
- **Silos.** Invisible walls between the data team and everyone else. Fix: all of the above, plus dashboards that are available around the clock.

## The four-step data sprint

His answer is a sprint with four stages: clear goal, plan well, execute, and test and improvise. The clear-goal stage sets a long-term aspirational goal, a short list of sprint questions (keep it short, he warns, or the timeline grows with it) and a rough map of how data will flow. "The whole target of doing a sprint is to achieve a limited scope in a limited timeline," he said.

Planning means talking to experts without handing them the decision, picking a small target, and collecting approaches without debating them first: everyone writes a sticky note, then the team votes. His ideal team is about five people: two hands-on coders, two on data and visualisation, and a manager. Execution freezes the deliverables and sets a timeline of one to two weeks, three if the scope is big. The last stage builds a small MVP or test report, checks the hypothesis with the stakeholder, and only then goes to a live dashboard. Learnings feed the next sprint's kickoff.

## Draw the pipeline before you build it

Aman calls diagrams underrated and demos one: web analytics as the ingestion source, a database, a Python preprocessing script on a 24-hour schedule, BigQuery for the queries, and Google Data Studio for the view a non-technical decision maker reads. His tip is to place all the components first and draw the connectors last. The diagram is where the team discovers the conditional paths, like a query failing and sending you back to preprocessing.

## Code or no-code?

Code wins on flexibility and scalability and loses on talent and silos. No-code wins on speed, learning curve and openness, and loses on flexibility and dependency: if the vendor shuts down, so does your project. He sorts the code tools into languages (Python, R, Scala), querying and analysis (SQL, MATLAB, BigQuery) and application suites (Spark, BigML, Hadoop), and the no-code side into dashboarding (Data Studio, Tableau, Power BI), flow automation and end-to-end platforms. His rule of thumb: low functional requirements point to no-code; high ones point to code.

## Dashboards and documents close the loop

Dashboarding is four steps: collect the visualisations, put the most important question on top with related charts side by side, schedule automatic refreshes (he names Apache Superset and Airflow), and share access with non-technical people. Then document everything from day one in a shared document. His own preference is a plain spreadsheet.

## Who should watch

Team leads and analysts at small and mid-sized companies whose data projects keep running long, and engineers who build pipelines for stakeholders who never open the dashboard. Python developers looking for code should pick another talk.

## Related Conf42 talks

- Jesse Anderson on [why data projects fail](https://www.conf42.com/Machine_Learning_2024_Jesse_Anderson_data_projects_failure) at Conf42 Machine Learning 2024.
- Mark Needham on [a real-time analytics dashboard with Streamlit, Apache Pinot and Kafka](https://www.conf42.com/Python_2022_Mark_Needham_realtime_analytics_dashboard_streamlit_apache_pinot_apache_kafka) at Conf42 Python 2022.
- Siddhartha Parimi on [unifying data silos](https://www.conf42.com/Cloud_Native_2025_Siddhartha_Parimi_data_silos_unification) at Conf42 Cloud Native 2025.

[Watch Aman Sharma's talk](https://www.conf42.com/Python_2022_Aman_Sharma_data_everywhere) from [Conf42 Python 2022](https://www.conf42.com/python2022).

## From Twimbit

Twimbit, where Aman Sharma is co-founder and CTO, is a platform for creating and discovering research insights.

- Twimbit: [twimbit.com](https://twimbit.com/)

[Watch the talk on YouTube](https://youtu.be/o5R1TNhgkIs).

## Watch the talk

[Data data everywhere, No time to think 🤔](https://www.conf42.com/Python_2022_Aman_Sharma_data_everywhere) at Conf42 Python 2022.
