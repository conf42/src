# Move cold MongoDB data to S3 and keep querying it with MQL

Conf42 Blog, 2021-04-28. https://www.conf42.com/blog/cloud2021/cold-iot-data-to-s3-still-queryable

In short: Joe Karlsson (MongoDB) at Conf42 Cloud Native 2021 on archiving cold IoT data to S3 and querying it in place with MongoDB Atlas Data Lake

Joe Karlsson, Software Engineer and Developer Advocate at MongoDB, showed at Conf42 Cloud Native 2021 how to stop paying hot-storage prices for data nobody reads. His demo archives old IoT readings from a MongoDB Atlas cluster to an S3 bucket as JSON, then queries them through MongoDB Atlas Data Lake with ordinary MongoDB queries. The pitch is two wins at once: a smaller bill and less electricity burned keeping stale data hot.

It is a short, upbeat product demo, prerecorded rather than live ("I'm not really ready to live this dangerously yet"), and it shows exactly the MongoDB features it names.

## Why does cold data cost so much?

Data keeps growing with every feature and every user, and scaling makes it worse. Shard a MongoDB database horizontally and each shard is usually backed by two replicas, so every gigabyte you keep is stored several times over and has to be powered. The abstract adds a sustainability figure: by 2040, storing digital data is set to create 14% of the world's greenhouse emissions.

His model is hot versus cold data. Time series IoT readings feed dashboards while they're fresh, then go stale: still worth keeping for historical analysis, rarely touched, like your tweets from four years ago. Storage closer to the CPU costs more, as anyone who has priced RAM against hard drives knows, so cold data belongs on the cheapest tier you can still query.

## What does Atlas Data Lake do?

Atlas Data Lake queries data in S3 and in Atlas in place, in its native format, using the MongoDB Query Language. You use the same drivers, and a control plane works out where each part of a query has to go and consolidates the results. Queries against archived data may be slower, which is the trade you accept for data that doesn't need to be hot. Karlsson's point is that many teams were building their own MongoDB data lake plumbing, which is hard to get right.

## What did the demo show?

A Python generator inserts fake IoT data: 24,000 documents, about 52 MB, into a world.iot collection. He configures the data lake in the Atlas UI and connects AWS S3 by granting an IAM role, then adds an S3 service to a MongoDB Realm application.

The archiving itself comes in two flavours. A Realm serverless function finds the oldest reading, takes one day's worth of documents, writes them to the cold-data bucket as Extended JSON with PutObject, then deletes them from the cluster. The alternative is a pymongo aggregation that matches a date range and uses the $out stage to write straight to S3 as JSON, with a maximum file size of 200 MiB per file.

Running the script moves 240 documents. The collection drops from 24,000 to 23,520, the files show up in S3 as plain JSON you can open in an editor, and they stay reachable through the data lake. "We can still query it like it was a normal MongoDB database," Joe Karlsson said at Conf42 Cloud Native 2021. He closes by pointing to Online Archive, which does the same tiering from rules configured in the Atlas GUI, no function to write.

## Who should watch?

Teams on MongoDB Atlas with time series or event data piling up in their clusters, who want to see the moving parts of tiering before switching on Online Archive. The demo code and the IoT data generator are on GitHub.

## Related Conf42 talks

- Joe Karlsson on [MongoDB schema design](https://www.conf42.com/JavaScript_2020_Joe_Karlsson_mongodb_schema_design) at Conf42 JavaScript 2020.
- Satish Mane and Rajeev Jaiiswal on [building an open format data lakehouse](https://www.conf42.com/Cloud_Native_2023_Satish_Mane_Rajeev_Jaiiswal_build_open_format_data_lakehouse) at Conf42 Cloud Native 2023.
- Neel Shah on [green and sustainable software](https://www.conf42.com/DevOps_2024_Neel_Shah_green_sustainable_software) at Conf42 DevOps 2024.

[Watch Joe Karlsson's talk](https://www.conf42.com/Cloud_Native_2021_Joe_Karlsson_save_the_world_data_lakes), part of [Conf42 Cloud Native 2021](https://www.conf42.com/cloud2021).

## From MongoDB

MongoDB makes the MongoDB Atlas cloud database, whose Data Lake and Online Archive features this talk demonstrates.

- [MongoDB Atlas](https://www.mongodb.com/atlas)
- [Demo code on GitHub](https://github.com/JoeKarlsson/mongodb-datalake-save-the-world)

[Watch the talk on YouTube](https://youtu.be/fAvVxQknDL0).

## Watch the talk

[Save The World And Money with MongoDB Data Lakes](https://www.conf42.com/Cloud_Native_2021_Joe_Karlsson_save_the_world_data_lakes) at Conf42 Cloud Native 2021.
