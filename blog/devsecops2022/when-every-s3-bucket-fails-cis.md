# When every S3 bucket fails the CIS benchmark, the benchmark tells you nothing

Conf42 Blog, 2022-11-30. https://www.conf42.com/blog/devsecops2022/when-every-s3-bucket-fails-cis

In short: Chris Webber (Open Raven) at Conf42 DevSecOps 2022 on prioritising S3 risk by what data is inside, who can write to it, and what you can delete

Turn on a CSPM tool, apply the AWS CIS benchmark, come back the next morning, and nearly every S3 bucket is red. Chris Webber, Engineering Director for IT and Operations at Open Raven, used his Conf42 DevSecOps 2022 talk to explain why that happens and what to look at instead: what kind of data sits in a bucket, who can write to it, and whether it needs to exist at all.

It's a short, practical talk from someone who remembers when data lived on NetApp filers and protected itself by being expensive and hard to reach. That is no longer true, and his small organisation alone has more than 30 AWS accounts, each with a bucket per region for AWS Config before any application data shows up.

## Why do the CIS S3 checks stop helping?

He walks through the automated S3 controls in the benchmark. Encryption at rest sounds obvious until you meet intentionally public assets, or read-heavy workloads where KMS calls from Athena get expensive (he got to know the CFO well after one of those). Denying plain HTTP is right in principle but breaks legitimate public serving. MFA delete means using the root account to delete anything, which is a worse security habit than the one it prevents. And AWS doesn't tick block public access on the buckets it creates for you.

Result: 95% to 100% of buckets get flagged. Chris Webber said at Conf42 DevSecOps 2022: "And when you get to a point where 95% to 100% of a given asset fails by default, those checks are kind of useless." When everything is critical, nothing is prioritised.

## What should you ask about a bucket instead?

His list of questions:

- **Where did the data come from?** AWS once capped accounts at around 100 buckets, so teams packed unrelated data under prefixes in one bucket: static assets next to customer data. The limit is gone; those buckets are not.
- **What region is it in?** Data can be perfectly protected and still break compliance by sitting in the wrong region. The Open Raven map often shows customers buckets in a region they never meant to use, sometimes just AWS Config, sometimes not.
- **Is it written by automation or uploaded by hand?** Many breaches are a backup uploaded manually to the wrong place, outside the controls an application would have.
- **What kind of data is in it?** PHI and PII you need to know about. In a big organisation, asking every owner won't scale, so classify with a scanner such as Open Raven or Amazon Macie.

## Who can write beats who owns it

Ownership is the question everyone asks first and almost nobody can answer; even a named owner may not know what lands in the bucket. He argues the more useful starting point is who can write to it. If applications owned by other teams, or humans uploading by hand, can put data in a bucket, that is where exposure comes from. Most reviews focus on who can read. He would start with write.

## Delete what you don't need

The most quotable advice is also the cheapest: don't protect data that doesn't need protecting. Pair S3 lifecycle rules (the technical part) with data retention rules (the business part): if healthcare data must be kept five years, it can go on five years and one day, and then you no longer have to secure it.

He also suggests Intelligent-Tiering for a reason you might not expect. It saves money, but it also makes access anomalies show up in cost, and far more people watch the bill than watch the security tools.

## Manage the riskiest buckets first

Public buckets are the obvious start, but don't stop there. Look for broad write permissions, and for large numbers of small files, which his team found to be the strongest sign of real customer data (uploaded images, JSON) rather than a dump of some archive. Then scan regularly (Open Raven skips objects whose ETag hasn't changed) and alert on combinations that matter: European data in a US region, or PII in an open bucket. Neither fact alone is the alarm; the pair is.

## Who should watch

Cloud security and platform engineers drowning in CSPM findings, and anyone who has to explain to an auditor why the encryption alert on the public assets bucket is fine. Related talks: [Mor Manor on data security posture in cloud databases](https://www.conf42.com/Cloud_Native_2022_Mor_Manor_inside_cloud_databases_data_security_posture), [Ben Rockwood on posture management](https://www.conf42.com/Cloud_Native_2023_Ben_Rockwood_posture_management) and [Josh Stella on minimising the blast radius of a cloud breach](https://www.conf42.com/DevSecOps_2021_Josh_Stella_Minimizing_the_Blast_Radius_of_a_Cloud_Breach).

[Watch Chris Webber's talk](https://www.conf42.com/DevSecOps_2022_Chris_Webber_data_abyss_cloud_security)

## From Open Raven

- [Open Raven](https://www.openraven.com/): data classification and cloud data security, including the S3 and RDS scanning shown in the talk.

[Watch the talk on YouTube](https://youtu.be/b3QhdUJWQX0).

## Watch the talk

[Staring into the data abyss: Achieving a higher level of cloud security so you can sleep better](https://www.conf42.com/DevSecOps_2022_Chris_Webber_data_abyss_cloud_security) at Conf42 DevSecOps 2022.
