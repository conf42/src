# Stitch your REST APIs into one graph and write queries, not more APIs

Conf42 Blog, 2022-06-09. https://www.conf42.com/blog/sre2022/graphql-write-queries-not-more-apis

In short: Priya Singh (MuleSoft) at Conf42 Site Reliability Engineering 2022 on federating REST APIs behind one GraphQL endpoint, with a demo in Anypoint DataGraph

Most organisations have already made their APIs reusable, one API at a time, and then write yet another API to glue three of them together for a new screen. At Conf42 Site Reliability Engineering 2022, Priya Singh, Senior Solutions Engineer at [MuleSoft](https://www.mulesoft.com/), argued that the next step is to treat those REST APIs as one graph behind a single GraphQL endpoint, so a new feature becomes a query instead of a project. The second half is a demo in MuleSoft's Anypoint DataGraph.

It's a vendor talk and an introductory one on GraphQL itself; the useful bits for engineers are the framing of APIs as a graph and the per-field tracing at the end.

## From custom code to reuse to one graph

Priya lays out three stages. In the past, every data-combining job was custom code that started from scratch and was stuck inside one project. Today most teams build REST APIs and reuse them, but only one at a time, so combining data still means multiple requests plus new APIs on top to massage and orchestrate the results. The aspiration is to pull from many APIs at once, in one request, with no extra glue code.

GraphQL is the tool for that: a query language for APIs that, as Priya puts it, works much like an SQL join across tables, except the tables are APIs. It also fixes over- and under-fetching, since the client names the fields it wants and nobody writes filter logic to throw the rest away.

## Your APIs already have foreign keys

The conceptual point that carries the talk: the APIs in a typical enterprise already relate to each other. Customer data lives in the ERP or CRM, shipments in a database, products in SQL Server. An order API relates to the customer API through a customer ID; an invoice relates to a product through a product ID. Stitch those relationships together and you have a graph with a unified schema covering every field of every connected API.

"To give that view, we will actually write queries instead of APIs," Priya Singh said at Conf42 Site Reliability Engineering 2022.

## The demo: a mobile developer named Sana

The demo follows Sana, a mobile developer at a retailer who has to show order status and expected delivery date in the app. The traditional route is to identify the order and shipment APIs, request access, check they work, then write logic to pick two fields out of payloads full of carrier details, customer data and tax amounts. Priya, who comes from a development background, estimates that takes months.

In the DataGraph version the back-end team has already combined the order, sales and shipment APIs into a unified schema served at one endpoint. Priya shows the schema's query operations, level-one and nested types, and two ideas worth knowing whatever tool you use: a merged type, where one Order object takes some fields from the sales API and some from the order API, and a linked type, where Order connects to the customer API through the customer ID. Then Sana writes the query, with autocomplete across every connected API, so she never needs to know which API a field comes from. The endpoint also works from Postman or any other API client, and it can be managed and secured like any other API.

## Tracing which field is slow

The SRE-relevant part comes last. For a business-critical flow such as order confirmations, Priya runs a traced query that reports response time per field, not just per call, because each field may come from a different back-end API. In the demo the tax amount field is the slow one, which tells you which API to optimise.

## Who should watch

Teams whose front-end developers spend weeks finding and combining back-end APIs, and anyone evaluating GraphQL federation over existing REST services. If you already run GraphQL in production, the first half will be familiar.

Other Conf42 talks on the topic: Phillip Kruger on [queryable APIs with MicroProfile GraphQL](https://www.conf42.com/Enterprise_Software_2021_Phillip_Krger_queryable_apis_microprofile_graphql), Roy Derks on [TypeScript and GraphQL for web apps](https://www.conf42.com/JavaScript_2022_Roy_Derks_web_apps_future_typescript_graphql), and Navendu Pottekkat on [SRE best practices for API design](https://www.conf42.com/Site_Reliability_Engineering_2022_Navendu_Pottekkat_sre_best_practices_api_design) from the same event.

[Watch Priya Singh's talk](https://www.conf42.com/Site_Reliability_Engineering_2022_Priya_Singh_evolution_of_composable_architecture_graphql) from [Conf42 Site Reliability Engineering 2022](https://www.conf42.com/sre2022).

## From MuleSoft

Anypoint DataGraph, shown in the talk, is part of MuleSoft's Anypoint Platform. Priya's closing resources point to a DataGraph tutorial for a first project and to the GraphQL documentation.

- MuleSoft: [mulesoft.com](https://www.mulesoft.com/)
- [Discover Anypoint Platform](https://videos.mulesoft.com/watch/bakFGgwqNDJzoJFNydiMiH)
- [Try Anypoint Platform](https://anypoint.mulesoft.com/login)
- [Join the MuleSoft Community](https://www.mulesoft.com/community)

[Watch the talk on YouTube](https://youtu.be/ALFcjl1xcyo).

## Watch the talk

[Build the next evolution of composable architecture using GraphQL](https://www.conf42.com/Site_Reliability_Engineering_2022_Priya_Singh_evolution_of_composable_architecture_graphql) at Conf42 Site Reliability Engineering 2022.
