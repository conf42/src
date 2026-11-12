# A motion sensor says more than on or off, if you engineer the features

Conf42 Blog, 2021-07-29. https://www.conf42.com/blog/ml2021/binary-iot-sensors-more-than-on-off

In short: Nidal Albeiruti (AWS) at Conf42 Machine Learning 2021 on time windows, elapsed times and region features from binary IoT sensors, plus SageMaker Data Wrangler

A PIR motion sensor gives you one bit. A house full of them, read over time, tells you who is moving between which rooms, how long they stayed and when nobody is home at all. [Nidal Albeiruti](https://www.conf42.com/Machine_Learning_2021_Nidal_Albeiruti_Feature_Engineering_Techniques_Binary_IoT_Sensors), Solutions Architect at AWS, spent his Conf42 Machine Learning 2021 talk on that gap: the feature engineering that turns binary IoT readings into inputs a model can learn from, and Amazon SageMaker Data Wrangler as the tool to make that preparation repeatable.

The talk runs from general to specific: IoT solutions, sensors, binary sensors, features, feature engineering, then the binary-specific techniques, which are the reason to watch.

## What counts as a binary sensor?

Any sensor whose reading is one of two mutually exclusive values. His examples: passive infrared (PIR) motion detectors (movement or none), pressure sensors, connectivity sensors, vibration sensors and smoke detectors. They are everywhere in IoT and industrial IoT, from worker safety and warehouse tracking to remote patient monitoring and ambient intelligence in the home.

For sourcing hardware he points to the AWS Device Qualification Program and the AWS Partner Device Catalog, which lists devices tested with AWS IoT services.

## What makes a feature good?

He leans on Pedro Domingos: what separates ML projects that succeed from those that fail is, more than anything, the features used. A good feature is informative (it means something to a human), available (enough instances, or a plan for missing data), discriminant (it separates the target classes or correlates with the target value), as independent of other features as possible, and simple. Better features usually mean simpler models, and good features let a simple model beat a complex one. He also separates features from hyperparameters, which are inputs to the learning algorithm rather than something it learns.

The general toolbox gets a quick tour: feature creation, importance (random forests give you a score for free), transformation, extraction to fight the curse of dimensionality, and selection by variance or correlation thresholds. The standard techniques follow: imputation, outlier handling, binning, log transform, one-hot encoding, grouping, feature split, scaling and date extraction. One reminder worth keeping: feature engineering is sensitive to the algorithm, since categorical features suit decision trees better than SVMs.

## So what do you do with a stream of zeros and ones?

For sensor data in general, a Fourier transform moves readings from the time domain to the frequency domain. For binary sensors specifically, he proposes:

- **Bag of features.** Cut the observations into time windows and ignore the order inside each window, mixing sensors of the same or different types in one bag.
- **Windowed segmentation.** Choose a window length, abstract each window to a single value (the median, or minimum or maximum when the presence of one value should represent the whole window).
- **Localisation by region.** Several binary sensors watching an area partition it into subregions, each defined by which sensors detect a target there.

On window length, Nidal Albeiruti said at Conf42 Machine Learning 2021: "Please note that you should do some exploratory data analysis to find the typical sensor activity durations, and then you can select the time window length." Five seconds, ten or more, depending on what the data shows.

From there the new features include the location area tied to a sensor's ID, the total elapsed time a sensor stays on, aggregations that compare similar periods of the day, and merges with other sensors for context, such as a light sensor that tells a daytime event from one at night.

## What can PIR sensors alone tell a model?

The PIR section is the most concrete. Activity level in a region is the number of events firing there. Two consecutive same-value events from the same sensor mean the person is still active in that region, and the time between them is a feature, as is inactivity time. Two consecutive events from different sensors mean the person moved between regions, which gives you movement and transition times. The frequency of movement within one region is another.

His favourite is the absence of signal. When no sensor in the whole ensemble fires, that silence is a feature in its own right: the monitored person is not there, which he found very helpful for behavioural modelling in ambient intelligence work. It is the IoT version of the dog that did not bark.

## Where does Data Wrangler fit?

In SageMaker's four stages (prepare, build, train and tune, deploy and manage), Data Wrangler sits in prepare next to Feature Store, inside SageMaker Studio. He lists over 300 built-in transforms, custom transforms in Python, PySpark or Spark SQL, built-in charts, and model analysis such as feature importance, target leakage and explainability. Sources include Amazon S3, Athena, Redshift, Lake Formation, Feature Store and, recently at the time, Snowflake. A flow can be exported to a SageMaker pipeline, a Data Wrangler job, a Python script or a feature group, and the flow file can be versioned and shared for reproducibility. That last part answers his earlier point that data preparation built in a notebook still has to run in production on a schedule.

His summary, in his words: "So binary sensors are not about zeros or ones, only much more can be extrapolated and extracted to help your machine learning models."

## Who should watch?

Data scientists handed IoT or smart-home data for the first time, and engineers building activity or presence detection who suspect their model is starving on raw on/off events. The first half is a solid refresher on feature engineering; the binary sensor and PIR sections are the original part.

## Related Conf42 talks

- Pawel Skrzypek and Anna Warno on [time series forecasting methods](https://www.conf42.com/Machine_Learning_2021_Pawel_Skrzypek_Anna_Warno_Time_Series_Forecasting_Methods) at Conf42 Machine Learning 2021.
- Ron Lyle Dagdag on [anomaly detection for JavaScript apps](https://www.conf42.com/JavaScript_2021_Ron_Lyle_Dagdag_Spidey_Senses_Anomaly_detection) at Conf42 JavaScript 2021.
- Marie Cruz on [monitoring plants with IoT sensors and Grafana Cloud](https://www.conf42.com/Internet_of_Things_IoT_2025_Marie_Cruz_sensors_gardening_analytics) at Conf42 IoT 2025.

[Watch the talk on YouTube](https://youtu.be/1ovwCFKuEs8).

## From AWS

- Amazon Web Services: [aws.amazon.com](https://aws.amazon.com/)
- Amazon SageMaker Data Wrangler: [aws.amazon.com/sagemaker/data-wrangler](https://aws.amazon.com/sagemaker/data-wrangler/)
- AWS Partner Device Catalog: [devices.amazonaws.com](https://devices.amazonaws.com/)

## Watch the talk

[Feature Engineering Techniques for Binary IoT Sensors](https://www.conf42.com/Machine_Learning_2021_Nidal_Albeiruti_Feature_Engineering_Techniques_Binary_IoT_Sensors) at Conf42 Machine Learning 2021.
