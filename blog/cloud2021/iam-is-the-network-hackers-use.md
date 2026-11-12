# In AWS, IAM is the network attackers actually move through

Conf42 Blog, 2021-04-29. https://www.conf42.com/blog/cloud2021/iam-is-the-network-hackers-use

In short: Josh Stella (Fugue) at Conf42 Cloud Native 2021 on a mental model for AWS IAM, why wildcards age badly, and where tags and bucket policies help

Most cloud breaches don't break in through a server's operating system; they walk through permissions. At Conf42 Cloud Native 2021, Josh Stella, co-founder and CTO of Fugue and formerly a principal solutions architect at AWS focused on national security, argues that IAM forms a network of its own in AWS, and spends most of the session at a whiteboard and the AWS console building a mental model for it.

There are five slides, then the hands-on part. If you're new to IAM it works as an introduction; if you aren't, the bits about wildcard inheritance and tag-based access are the reason to watch.

## Why is cloud security different?

The old picture of hacking (pick a target, find a way in) still happens; his example is the North Korean breach of Sony Pictures. Far more common now is what he calls the cloud exploit strategy: automation scans every object reachable from the internet for misconfigurations and hands the attacker a shopping list. The Capital One breach worked that way, he says; the attacker's automation found Capital One, not the other way round.

A quoted estimate that new assets get scanned within a few hours of deployment is, in his view, rosy. "It is more like five to seven minutes," Josh Stella said at Conf42 Cloud Native 2021.

He adds two uncomfortable points. Compliance frameworks (ISO, NIST, HIPAA, GDPR, CIS), even read as paranoidly as Fugue reads them, miss many of these techniques. And you can't judge IAM from an infrastructure-as-code file alone: the danger is in the combination of resources once they land in the account.

## Principals, actions, resources and two walls of denial

The whiteboard model is three columns. Principals are actors, the only things that send requests: a human, an application, or a resource such as an EC2 instance, container or Lambda function. Actions are the API verbs, thousands of them, such as GetObject, ListBucket (one bucket's contents) and ListBuckets (all your buckets). Resources are named things: a bucket called baz, a database, a container.

By default everything is denied, and there are two walls: between principals and actions, and between actions and resources. An IAM policy's allowances poke holes in those walls, and any deny along the way kills the request. When a resource such as an EC2 instance is the principal, those holes connect resources to each other, which is how IAM becomes a network.

Practical advice from this part: a business function usually needs actions from several services, so think of actions as one long list to pick the minimum from. Attach policies to roles (a developer role, a team role) rather than inline to users, and don't let policies proliferate; AWS already puts hundreds of managed ones in your account.

## Why a star in a policy ages badly

In the console he builds an EC2 policy and ticks all of Write. That's 289 write actions in EC2 alone, against 124 describe and 23 read actions, and the reason people reach for a wildcard is that enumerating them is real work. His argument for doing it anyway is time.

A star inherits every action AWS adds later. His example is an EC2 action that lets an instance switch which IAM instance profile it has, a route to privilege escalation and lateral movement. It didn't exist when he worked at AWS, so a write-star policy written back then might have been safe and now isn't, on every instance that carries it. He also warns that an instance with an S3 read-write role that can list buckets is exactly what an attacker hopes to find, and that the right fix is sometimes architectural: if an instance needs a list of buckets, put it in a database.

## Tags, bucket policies and no single right answer

Listing every resource ARN in policies breaks down at scale; Fugue's customers often have hundreds of thousands of cloud resources. Attribute-based access control scopes access by tags instead, and he likes it, with a catch: tags are now part of your security boundary, so writing (and maybe reading) tags must be tightly restricted, or an attacker with tag permissions can retag resources into reach.

IAM is also only one policy citizen among several. He recommends a bucket policy on every S3 bucket; one that allows requests only from a given VPC endpoint adds another wall of denial, even if two EC2 instances both think they can read every bucket.

His closing point is about method. The most common failure he sees is teams that copy examples without ever building a mental model. Architecture choices change the IAM work too: Fugue's second version moved computation almost entirely to Lambda, which meant automating role creation per function to keep the blast radius small.

## Who should watch

AWS engineers and security folks who write IAM policies by hand or review them, especially if a policy still has a star that nobody remembers adding.

## Related Conf42 talks

- Yoav Yanilov and Itamar Bareket on [AWS tags and advanced IAM](https://www.conf42.com/DevSecOps_2022_Yoav_Yanilov_Itamar_Bareket_aws_tags_advanced_iam) at Conf42 DevSecOps 2022.
- Ashish Rajan on [cloud security assessments](https://www.conf42.com/Cloud_Native_2021_Ashish_Rajan_Cloud_Security_Assessments_in_2021), from the same event.
- Josh Stella on [cloud security and Open Policy Agent](https://www.conf42.com/Open_Source_Showcase_2020_Josh_Stella_cloud_security__open_policy_agent_opa) at Conf42 Open Source Showcase 2020.

[Watch Josh Stella's talk](https://www.conf42.com/Cloud_Native_2021_Josh_Stella_security_iam) from [Conf42 Cloud Native 2021](https://www.conf42.com/cloud2021).

## From Fugue

Fugue secures cloud infrastructure and checks it for compliance; the talk shows its automatic infrastructure diagrams for exploring how resources and IAM profiles connect.

- Fugue: [fugue.co/conf42](https://www.fugue.co/conf42)

[Watch the talk on YouTube](https://youtu.be/fBI8nWRuPkg).

## Watch the talk

[Locking Down the Security of IAM](https://www.conf42.com/Cloud_Native_2021_Josh_Stella_security_iam) at Conf42 Cloud Native 2021.
