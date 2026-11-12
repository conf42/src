# A pay-per-mile fintech with no servers, not even a jump box

Conf42 Blog, 2021-04-30. https://www.conf42.com/blog/cloud2021/serverless-fintech-under-100-pounds

In short: Daniel Bass (Zeti) at Conf42 Cloud Native 2021 on building a fintech startup entirely on Azure serverless services, from vehicle telemetry to investor dashboards

Daniel Bass, CTO of Zeti, built a fintech startup without a single server, virtual or physical, and at Conf42 Cloud Native 2021 he showed how. Zeti finances zero emission vehicles on a pay-per-mile basis, and its platform tracks thousands of vehicles in real time on Azure Functions, Cosmos DB, Event Grid, SignalR and Azure Static Web Apps. His takeaway: for a startup, paying only for what you use maps your bills to your revenue.

Bass came from fintech, as lead engineer on a private assets and alternatives team at a major investment manager, and has written two books on serverless architectures on Microsoft Azure. This talk is the field report from putting that into a company.

## Why does pay-per-mile need real-time data?

Zeti's model replaces a fixed monthly payment with a per-mile one. Drive zero miles, pay zero pounds; drive more and you pay by the mile, 30 pence in his example. That suits operators who already think in revenue per mile, such as taxi and delivery fleets, and battery electric vehicles, which cost more up front but need very little maintenance.

The platform has to know where each vehicle is, whether it has crashed, and what its odometer says, so operators can be billed. It also tells investors how their money is performing in real time. Bass points at the Hertz default early in the pandemic: nobody was renting cars, and lenders only found out much later. Seeing usage as it happens is rare in vehicle finance.

## What counts as serverless here?

Bass is clear it is more than functions as a service. His definition is anything utility-like: you pay for what you use, it's on tap, it scales and you don't manage it. CDNs and pay-per-transaction databases such as Google Spanner count. The mindset is to strip out undifferentiated heavy lifting. If your business is running Kubernetes clusters, get very good at it; if you sell insurance, running clusters is not where your value is.

"So the only real security you need to worry about is your own code, which is a massive benefit," Daniel Bass said at Conf42 Cloud Native 2021. For a financial company the comparison is stark: a server in the corner of the office needs a burglar alarm, failsafe power and fast patching for the next decade-old Linux exploit.

He is also upfront about the environmental argument. Serverless systems scale to zero, so idle capacity should mean less waste, but cloud providers don't break down energy use per service, so he admits he has no hard data.

## How does the architecture fit together?

Two flows run through it. Users, investors and fleet operators, load a React and TypeScript static web app, which calls an Azure Function that wakes up, reads account details from Cosmos DB in its serverless mode, and returns them.

The other flow is the vehicles. Events only arrive while vehicles move, so traffic swings from very busy to almost nothing. An Azure Function ingests events from many providers, since a Renault's tracker speaks differently from a Tesla's, normalises them into Zeti's own model and pushes them onto Event Grid. SignalR carries them into the browser, handling the websocket negotiation that browsers support unevenly.

## Why is the static web app the key piece?

Bass calls servers bucketed usage: you buy a whole core even if you use 5% of it. The static web app removes the last bucket, the MVC server, so the whole architecture bills per use. Think of it as an app on your phone that talks to a secure back end. Identity is Azure AD for staff and Azure AD B2C for customers, which he calls the world's worst named cloud service, so Zeti stores no usernames, passwords or even email addresses.

Separating front end from back end also keeps options open. If the API layer later has to be permanently hosted, to avoid cold starts or sit in a locked-down virtual network, the front end doesn't care.

## Did it work?

So far, yes. Zeti tracks its whole deployed fleet through the system without it choking, though Bass notes load tests with tools such as Serverless Artillery don't replace real production traffic. The bill, he said, is less than 100 pounds.

## Who should watch?

Founders and early engineers choosing a stack, and anyone curious how far Azure's managed services go before you need a VM. It is a practical architecture talk, light on code.

## Related Conf42 talks

- Jorge Fonseca on [global active-active serverless](https://www.conf42.com/Cloud_Native_2021_Jorge_Fonseca_global_activeactive_serverless) at Conf42 Cloud Native 2021.
- Aviad Mor on [observability for serverless and managed services](https://www.conf42.com/Cloud_Native_2021_Aviad_Mor_observability_serverless_asynchronous_managed_services) at Conf42 Cloud Native 2021.
- Tal Melamed on [serverless security](https://www.conf42.com/Cloud_Native_2022_Tal_Melamed_serverless_security) at Conf42 Cloud Native 2022.

[Watch Daniel Bass's talk](https://www.conf42.com/Cloud_Native_2021_Daniel_Bass_serverless_fintech_startup_azure), part of [Conf42 Cloud Native 2021](https://www.conf42.com/cloud2021).

## From Zeti

Zeti is the pay-per-mile financing platform for zero emission vehicles where Daniel Bass is CTO.

- [Zeti website](https://zeti.co.uk/)

[Watch the talk on YouTube](https://youtu.be/QtNAl56HXdI).

## Watch the talk

[Building a Serverless FinTech Startup on Azure](https://www.conf42.com/Cloud_Native_2021_Daniel_Bass_serverless_fintech_startup_azure) at Conf42 Cloud Native 2021.
