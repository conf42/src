# Sort every file into binary, configuration or data, then containerise the VM

Conf42 Blog, 2023-03-29. https://www.conf42.com/cloud2023/evolute-bcd-vm-to-container-framework

In short: Kristopher Francisco (Evolute) at Conf42 Cloud Native 2023 on the BCD framework and ML-driven VM-to-container migration with Evolute Migrate

Every legacy app you are told to move to Kubernetes is some mix of things that run, things that make this instance unique, and things the business would miss. At Conf42 Cloud Native 2023, Kristopher Francisco, co-founder of Evolute, called that split BCD (binary, configuration, data) and showed how Evolute Migrate uses it, plus k-means clustering and decision trees, to turn a running VM into a container image, with a live GlassFish demo and a 20-year-old Windows service as the hard case.

This is a product talk: the framework is presented as reusable, but the demo, the algorithms and the success claims are Evolute's.

## What is the BCD framework?

The input is a breadcrumb: an application binary, a package or a file, anything that uniquely references the software (his examples range from mysqld to an FTP RPM to vendor binaries). From there, every component of the software in its source environment goes into one of three buckets:

- **Binary**: the software runtime.
- **Configuration**: the unique variables that make an instance distinct.
- **Data**: customer-specific information, which may move somewhere else entirely.

Once every piece is classified, he argues, the artifact becomes portable: VM to VM, VM to container, and from containers on to serverless and any Kubernetes platform on AWS, Azure or Google Cloud. You can apply the same sorting by hand in your own modernisation work, which is the reusable bit for people who never touch the product.

## Where does the machine learning come in?

Two steps. Classification uses unsupervised k-means clustering to work out where the software begins and ends: which components belong inside the application, which run outside it, and how they depend on each other. Containerisation uses supervised decision trees. It starts from seven or eight base paths, but across operating systems, frameworks, dependencies, sources and destinations there are about 3,100 deterministic paths. The tool has to be deterministic, he stresses, because a migration that works sometimes is not a migration.

The claim attached: by his account, about 99% of the software they have tried has worked. "We saved the 1% for what we may not have experienced yet," Kristopher Francisco said at Conf42 Cloud Native 2023. There is no independent methodology behind the figure in the talk, so read it as a vendor's number.

At runtime, build is kept separate from run, services start in the right order, and components that need to scale apart are split apart.

## What does the demo show?

The CLI is called Chrysalis (the pupa-to-butterfly stage). Pointed at a source VM with a root user and keys, a staging area and a target application, it connects, compares source and destination, classifies the software into BCD and produces a base container image. He then runs it with Docker, starts the database and the GlassFish domain, and queries the Pet Clinic demo app inside the container. The generated Dockerfile targets Amazon Linux and lists the packages and dependencies it found.

The harder example is an in-house broker application written 20 years ago, which, he says, its operating system vendor and everyone else had called impossible to containerise. The output manifest is a Windows Server Core image that installs the Visual C++ runtimes, creates the Windows services and sets up MSMQ queues. Configuration is pulled out so each environment can have its own values, and the data moves to Azure SQL with the connection string pointing there.

## How should migrated apps scale?

He gives three deterministic patterns that he says cover 80 to 90% of software:

- **By application function** (say, the shopping cart of an e-commerce app): an m x n pattern built from Deployments and Services, scaling app and web tiers more than the database.
- **By resource demand** (CPU, memory, disk, network): n+1 with a pod autoscaler.
- **By component** (an nginx package on the OS): n+1 by deployment count, or an odd member count for a scale-out database that needs quorum.

## What usually blocks a migration?

Networking and security, in his experience. His three computational truths for getting past them: everyone respects the OSI model, so map how each layer works in the source and in the destination (Evolute Migrate builds translation maps across the layers); communication expresses relationships, so trace inter-process and network calls; and operating systems are abstractions, a set of interfaces and packages rather than a black box. Then the line that sums up the pitch: "Our input is software, but our output is software as well."

## Who should watch

Teams staring at a backlog of VMs to move into containers, and anyone wanting a vocabulary for classifying what a legacy app is made of. Expect a vendor walkthrough with a short demo, not a neutral comparison of migration tools, although the timeline section does name the alternatives (Google's migration tooling, AWS App2Container, Azure Migrate, Konveyor). Pair it with [Sindhuja Nagarajan on migration pipelines](https://www.conf42.com/Cloud_Native_2023_Sindhuja_Nagarajan_solving_migration_pipelines), [JJ Asghar on the stumbling blocks of moving a monolith to cloud native](https://www.conf42.com/Site_Reliability_Engineering_2021_JJ_Asghar_migrating_monolith_cloudnative_stumbling_blocks) and [Hareesh Iyer on modernising monoliths into microservices](https://www.conf42.com/Cloud_Native_2024_Hareesh_Iyer_modernize_monoliths_microservices).

[Watch Kristopher Francisco's talk](https://www.conf42.com/Cloud_Native_2023_Kristopher_Francisco_auto_containerization_cloud_portability)

## From Evolute

- [Evolute](https://www.evolute.io/): makers of Evolute Migrate, the containerisation and migration software shown in this talk.

[Watch the talk on YouTube](https://youtu.be/7Mqs9Jin4TA).

## Watch the talk

[AI-Based Containerization: A Framework For Cloud Portability](https://www.conf42.com/Cloud_Native_2023_Kristopher_Francisco_auto_containerization_cloud_portability) at Conf42 Cloud Native 2023.
