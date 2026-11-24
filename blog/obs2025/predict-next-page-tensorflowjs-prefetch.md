# Teach the browser to guess your next click, then prefetch it

Conf42 Blog, 2025-05-25, updated 2026-11-09. https://www.conf42.com/blog/obs2025/predict-next-page-tensorflowjs-prefetch

In short: Alexandru Hang of ING Tech Romania at Conf42 Observability 2025 on training a TensorFlow.js model on activity logs to predict and prefetch the next page.

Your activity logs already know where most users go after the home page. At Conf42 Observability 2025, Alexandru Hang, a software engineer at ING Tech Romania, showed how to turn that history into a small neural network that predicts a user's next page and lets the app fetch its data before the click lands.

It is an observability talk with an unusual angle: the logs are not there to explain an outage after the fact, they are training data for making the app feel faster in the moment.

## The problem: pages that load a lot of stuff

Web apps keep getting heavier, and each page pulls in more assets and API calls. Alexandru's goal is twofold: give the user an instant page, and give the server a heads-up about the load that is coming. If you know the user is about to open messages, you can request that data while the app is idle, and the click finds everything already in memory.

He considers the boring option first, and it is a fair one. A statistical approach would tell you that a large share of users go from home to the newsfeed and then to messages. That works, but it is the same guess for everyone. He wants a per-user prediction, which is where the neural network comes in.

## A machine learning primer for software engineers

The first half is a gentle tour aimed at people who are "not AI engineers", in his words. He walks through linear regression (good for extrapolating a trend, wrong for picking a next action), decision trees and random forests (classification), and then neural networks, which he picks because they adapt to patterns and can even mimic the simpler models. He demonstrates that last point by having a small network approximate a linear function from a handful of points.

The cats-versus-dogs example carries the explanation of training and testing: feed labelled data, hold some back, and measure accuracy. If 80 of 100 test images come back right, the accuracy is 80%, and you either ship or go back to training. Senior ML folks can skip ahead; everyone else gets a clear mental model in a few minutes.

## TensorFlow.js moves the guessing to the client

The tool choice is the interesting design call. Alexandru uses TensorFlow, and specifically TensorFlow.js, so the model can run in the browser. Since the prediction is per user anyway, running it on the user's own device keeps that work off the server. He also notes you can start from a pre-trained model (for example from Hugging Face), retrain one for a more specific case, or build your own when neither fits.

## The model is small and readable

The code walkthrough is short:

- **Encode the pages.** Neural networks do not take strings, so each page (home, newsfeed, messages, shop) gets a number and becomes a one-hot vector, the shape TensorFlow expects.
- **Define a sequential model.** Two dense layers: a ReLU hidden layer and a softmax output layer that turns the result into a choice of next page.
- **Train with `model.fit`.** The activity log is the input, the following page is the label, with 100 epochs and a chosen batch size.
- **Predict with `model.predict`.** Pass the current history, get the likely next page, and prefetch its assets.

For the demo the activity log is an in-memory array, which keeps the network out of the picture. He points to the full source on GitHub for the whole loop. The same predictions, he adds, can feed anomaly detection on user flows or forecasts of server workload.

## Who should watch

Frontend and full-stack engineers who have never trained a model and want a first, concrete use for one in their own app. It is an intro, and it says so. If you already run recommendation models in production, the primer will feel slow, but the prefetch framing might still give you an idea for your access logs.

## Related Conf42 talks

- [Aleksandr Guzenko on code splitting techniques](https://www.conf42.com/JavaScript_2023_Aleksandr_Guzenko_breaking_monolith_code_splitting_techniques) (JavaScript 2023), the other half of loading less at the right moment.
- [Vedant Agarwal on real-time personalization with neural ranking](https://www.conf42.com/Python_2025_Vedant_Agarwal_personalization_neural_ranking) (Python 2025), for what this idea looks like at production scale.
- [Anton Kalik on AI meeting Node.js](https://www.conf42.com/JavaScript_2023_Anton_Kalik_ai_nodejs_custom_sports_activity) (JavaScript 2023), another JavaScript-first take on putting a model in your app.

[Watch Alexandru Hang's talk](https://www.conf42.com/Observability_2025_Alexandru_Hang_logs_behaviour_experience)

[Watch the talk on YouTube](https://youtu.be/PqyERbLOWWs).

## Watch the talk

[Using the activity logs to predict user behaviour and improve experience](https://www.conf42.com/Observability_2025_Alexandru_Hang_logs_behaviour_experience) at Conf42 Observability 2025.
