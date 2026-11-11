# Encrypt the input, run the model in an enclave nobody can peek into

Conf42 Blog, 2023-03-09. https://www.conf42.com/blog/python2023/confidential-computing-nitro-enclaves-onnx

In short: Justin Patriquin (Cape Privacy) at Conf42 Python 2023 on confidential computing with AWS Nitro Enclaves, demoed with an ONNX image classifier and PyCape

Encryption at rest and in transit are table stakes; the moment your data is actually being processed, it usually sits in memory in plain text. At Conf42 Python 2023, [Justin Patriquin](https://www.conf42.com/Python_2023_Justin_Patriquin_sensitive_data_machine_learning_models), Software Engineer at Cape Privacy, explains how confidential computing closes that gap with AWS Nitro Enclaves, then deploys a ResNet image classifier into one and sends it an encrypted photo of a golden retriever.

It is a product talk with the theory up front: the first half explains enclaves and attestation in general, the second half demos Cape's Python SDK, PyCape.

## What is confidential computing?

His favourite analogy is to compare it with how ubiquitous encryption at rest and in transit have become. "Confidential computing is a broad set of technologies that allows data to be protected while in use," Justin Patriquin said at Conf42 Python 2023. The party doing the processing, such as a cloud provider, never sees the data. The family includes multiparty computation, fully homomorphic encryption and trusted execution environments, or enclaves, which can complement each other. Cape's focus is enclaves.

## Why not just roll your own encryption?

Because the choices are a minefield. AES or RSA. If AES, GCM or CBC mode. How each choice changes security and efficiency. How to pack the tag and nonce before sending the payload. He shows a short RSA function from Cape's own code base, with OAEP padding, MGF1 and SHA-256, and asks whether the label parameter should be set. You can look up good defaults, he says, but you still won't fully understand what you chose. A library that makes those decisions, documents them and lets you override them is the better deal. Key management has the same problem: on AWS alone you pick between KMS, Secrets Manager and more.

## How do Nitro Enclaves and attestation work?

A Nitro Enclave runs code in a locked-down container that nobody can see into: not AWS, and on Cape's platform not Cape either. You can turn nearly any Docker container into an Enclave Image File (EIF), which holds the container's OS file system plus metadata: a signature from the private key of whoever built it, creation details, and Platform Configuration Registers (PCRs) holding hashes of what is inside.

Attestation is how a caller proves it is talking to the enclave it expects. During the connection the enclave sends an attestation document containing the PCRs, signed by a root AWS certificate that the client must verify. If the hashes match, you know exactly what code will see your data.

## What did the demo show?

Cape's model has three verbs: encrypt, deploy a Python function, run it on your encrypted data. SDKs exist for Python, JavaScript (browser and Node.js) and Java, plus a Go CLI, and the team plans to move shared SDK logic into Rust to cut the surface area for bugs. A Cape function is a Python script with a handler that takes bytes and returns a string or bytes.

The demo uses an ONNX ResNet model pre-trained on ImageNet:

- The handler loads the model with ONNX Runtime, turns the input bytes into a NumPy buffer, runs inference and returns the top five classes as JSON.
- Dependencies are installed into the deployment folder through a Python 3.9 slim Docker image, so they match the enclave's environment. He admits this step is clunky and hopes to add helpers for it.
- PyCape's experimental CLI module (a wrapper around the Go CLI) deploys the folder. Under the hood it opens a websocket to the enclave, runs attestation, encrypts the function and sends it over. Large models make that upload slow.
- A function-scoped token is created, the client preprocesses a dog photo with PyTorch, and the enclave answers golden retriever at 39.7%.

Then he encrypts the input first. The ciphertext is a base64 string with a cape prefix, which the enclave detects and decrypts automatically, so the function itself needs no changes and returns the same golden retriever. The last example encrypts a message for another Cape user, for when you trust a specific service to decrypt your data.

## Who should watch

ML engineers who need to run a proprietary model on someone else's sensitive data, or vice versa, and backend developers curious what attestation looks like from the client side. The code and instructions are in Cape's image-classification-onnx repository on GitHub.

Related Conf42 talks:

- Moritz Eckert on [confidential computing with Intel SGX](https://www.conf42.com/Golang_2021_Moritz_Eckert_confidential_computing_Intel_SGX_security_cloud_native), Conf42 Golang 2021.
- Srinivas Vallabhaneni on [enclaves and confidential security](https://www.conf42.com/Golang_2025_Srinivas_Vallabhaneni_enclaves_security_confidential), Conf42 Golang 2025.
- Ron Lyle Dagdag on [the power of ONNX](https://www.conf42.com/Machine_Learning_2021_Ron_Lyle_Dagdag_Leverage_Power_ONNX), Conf42 Machine Learning 2021.

## From Cape Privacy

Cape Privacy builds a confidential computing platform on AWS Nitro Enclaves, with SDKs including PyCape for encrypting data and deploying and running functions.

- [Cape Privacy](https://capeprivacy.com/)
- [Getting started docs](https://docs.capeprivacy.com/getting-started/)
- [Demo code: image-classification-onnx](https://github.com/capeprivacy/image-classification-onnx)

[Watch the talk on YouTube](https://youtu.be/q4sLggLcytc).

## Watch the talk

[Protecting Sensitive Data and Machine Learning Models](https://www.conf42.com/Python_2023_Justin_Patriquin_sensitive_data_machine_learning_models) at Conf42 Python 2023.
