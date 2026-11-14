# Put your cloud's API output in a database and ask it questions

Conf42 Blog, 2026-05-12, updated 2026-11-09. https://www.conf42.com/blog/dbd2026/cloud-api-metadata-into-a-database

In short: Jason Lester of Capgemini at Conf42 Database DevOps 2026 on loading cloud CLI and API output into tables for permission audits, history and start-stop tooling.

Your cloud console can tell you which groups a user belongs to; it usually can't tell you what that user could do last month. At Conf42 Database DevOps 2026, Jason Lester, Managing Architect at Capgemini UK, showed the low-tech fix: pull the metadata out through the provider's CLI or API, load it into database tables, and let SQL answer the questions the console was never built for.

It is a short, practical talk with examples from Oracle Cloud Infrastructure, which is what Jason works with, though he is clear that the idea carries over to AWS, Azure and GCP. A good one for anyone who has clicked through forty console pages to build an inventory spreadsheet.

## The console is a friendly layer over a bigger API

Hyperscaler consoles are designed for getting started fast: drop-downs, calendars, sensible defaults. Underneath, APIs do the actual work, and not every API feature makes it into the console. The upside of the API is composition: Jason compares it to Lego, chaining one call that reads a database's details into another that builds a new one.

The downside gets equal billing. Without the visual feedback of the console, it is easy to get lost in the data and break something, so he recommends experimenting in an environment where you cannot delete production.

REST APIs are the common form, callable from tools like Postman, and authentication is the usual pain: on Oracle Cloud you call an authentication API for a token before every other call. The vendors' CLIs wrap that up. Run `oci compute instance list` with a compartment and you get every instance back as JSON, with far more metadata than the console shows, using a config you generated once.

## Once it's in tables, joins do the auditing

Jason's team created an `OCI instances` table and loaded the tenancy's instance metadata into it: inventory, build dates, status, CPU and memory, plus performance and cost statistics that are hard to find in the console. With the data in a database you can point other tools, AI included, at it to look for trends and changes.

The permissions example is the strongest. In Oracle Cloud, access comes from policy statements granted to groups, and users join groups. The console shows a user's groups but not the privileges those groups inherit without reading every policy. Extract users, groups and policies into tables and a few joins tell you exactly what a user can do in a given compartment Scrape it regularly and you get history, so the forensic question of who had access to a system a month ago becomes a query rather than an afternoon of backtracking through audit logs.

## A small app beats a big console for one job

On top of that metadata the team built applications in Oracle APEX. The common customer request is shutting down non-production environments outside working hours, say dev off at 6pm on weekdays and all weekend, which saves real money. When a developer needs it on a Saturday, the APEX app lets them start it without knowing the technical steps, optionally routing an approval email to a manager with the cost of running it that day.

Hierarchical groups, stored as metadata, encode start and stop order: the database comes up before the application server, and the app server goes down before the database.

## Who should watch

Cloud and database admins who keep answering inventory, cost and access questions by hand, especially on Oracle Cloud. It is an idea talk with concrete examples rather than a tool release; Jason's blog at jasonlesterdba.wordpress.com has the how-to. If you already run a cloud asset inventory product, you will recognise the pattern.

## Related Conf42 talks

- [Ahmed Tariq on identity and permissions in the cloud](https://www.conf42.com/AI_Agents_2026_Ahmed_Tariq_identity_permissions_cloud) at Conf42 AI Agents 2026.
- [Pradeep Gaddamidi on cloud cost monitoring](https://www.conf42.com/DevOps_2025_Pradeep_Gaddamidi_cloud_cost_monitoring) at Conf42 DevOps 2025.
- [Maksymilian Kalek on AWS cost efficiency](https://www.conf42.com/Cloud_Native_2025_Maksymilian_Kalek_aws_cost_efficiency) at Conf42 Cloud Native 2025.

[Watch Jason Lester's talk](https://www.conf42.com/Database_DevOps_2026_Jason_Lester_productivity_teams_efficiency)

[Watch the talk on YouTube](https://youtu.be/fWx5r87dHcA).

## Watch the talk

[Doing more with Cloud API's](https://www.conf42.com/Database_DevOps_2026_Jason_Lester_productivity_teams_efficiency) at Conf42 Database DevOps 2026.
