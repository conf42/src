# Conf42 Python 2025 roundup: dunders, concurrency, data and agents

Conf42 Blog, 2025-02-07. https://www.conf42.com/blog/python2025/python-2025-roundup-dunders-concurrency-data

In short: Conf42 Python 2025 in review, from dunder methods, asyncio vs threads and FireDucks to fsspec, FastAPI fraud systems, agentic Django and WebAuthn.

Iyanuoluwa Ajao introduced a talk at [Conf42 Python 2025](https://www.conf42.com/python2025) by calling Python "the 2nd best language for everything", which is about as honest a summary of the ecosystem as you'll get. The event, streamed online on February 6, 2025, had 51 talks covering both halves of that joke: the language features and libraries that make Python good at so many jobs, and the tricks people use when it isn't fast enough. Speakers came from IBM, Meta, Microsoft, Walmart, Snowflake, Mastercard, Wells Fargo, Qualcomm, NEC and Treeverse.

## The language, used properly

[Eti Ijeoma](https://www.conf42.com/Python_2025_Eti_Ijeoma_python_dunder_methods) (Manufactured Networks) went past `__str__` and `__repr__` to show how dunder methods make APIs feel native and can carry small domain-specific languages. [Iyanuoluwa Ajao](https://www.conf42.com/Python_2025_Iyanuoluwa_Ajao_python_concurrency_patterns) (Fyyne) compared threading, asyncio and multiprocessing, with a practical rule for I/O-bound work: if the libraries you need support async/await, start with asyncio, because threads cost memory and need protecting when they share data; otherwise use threads, and save processes for real parallelism.

[Dmitriy Volkov](https://www.conf42.com/Python_2025_Dmitriy_Volkov_packaging_busy_people) (Palisade Research) covered Python's packaging oddities for people with no time for them, plus the move towards a GIL-free CPython. When Python itself is the bottleneck, [Hariharan Ragothaman](https://www.conf42.com/Python_2025_Hariharan_Ragothaman_cpp_python_workloads) (athenahealth) offloaded compute-heavy work to C++, and [Sourav Saha](https://www.conf42.com/Python_2025_Sourav_Saha_firedricks_dataframe_jit) (NEC Corporation) introduced FireDucks, a multithreaded DataFrame library with JIT compilation that detects and optimises common pandas performance problems without code changes.

## Data tooling that hides the plumbing

[Guy Hardonag](https://www.conf42.com/Python_2025_Guy_Hardonag_file_systems_python) (Treeverse) gave hands-on examples of fsspec, the library that lets Pandas, TensorFlow and PyArrow treat local and cloud storage the same way. Anyone who has written `if path.startswith("s3://")` will appreciate it. [Daniel Emakporuena](https://www.conf42.com/Python_2025_Daniel_Emakporuena_data_analysis_streamlit) built an analysis and dashboard tool on Streamlit for people who outgrew Power BI and Tableau, and [Tim Spann](https://www.conf42.com/Python_2025_Tim_Spann_vector_databases_python) (Snowflake) combined structured, semi-structured and unstructured sources with Python.

At larger scale, [Dileesh Chandra Bikkasani](https://www.conf42.com/Python_2025_Dileesh_Chandra_Bikkasani_network_performance_automation) (AT&T Labs) used Apache Airflow for network performance automation, [Amarnath Immadisetty](https://www.conf42.com/Python_2025_Amarnath_Immadisetty_python_analytics_realtime) (Lowe's) built real-time customer analytics engines, and [Shashank Reddy Beeravelly](https://www.conf42.com/Python_2025_Shashank_Reddy_Beeravelly_data_quality_management) (Walmart) covered AI-assisted data quality checks.

## AI and agents, in plain Python

[Anna Gutowska](https://www.conf42.com/Python_2025_Anna_Gutowska_ai_agents_customizing) (IBM) introduced AI agents that combine LLM reasoning with planning, current information and external tools. [Craig West](https://www.conf42.com/Python_2025_Craig_West_agentic_ai_django) treated agents in Django as "AI as API", building agentic endpoints from scratch, and [Sourabh Gawande](https://www.conf42.com/Python_2025_Sourabh_Gawande_ai_applications_practical) (Kusho) shared the practical side of building LLM applications. [Shannon Lal](https://www.conf42.com/Python_2025_Shannon_Lal_image_search_python) (Designstripe) combined text search with semantic search for images using Motor, MongoDB and OpenAI. The most fun entry was [Jan Van Wassenhove](https://www.conf42.com/Python_2025_Jan_Van_Wassenhove_code_music_electronic) (Sopra Steria), whose MusicAgent uses generative AI, Python and Sonic Pi to compose and produce electronic music live, album art included.

Search and ranking had a strong showing too: neural ranking for real-time personalisation from [Vedant Agarwal](https://www.conf42.com/Python_2025_Vedant_Agarwal_personalization_neural_ranking) (Walmart Global Tech), vector-based semantic search from [Siddharth Pratap Singh](https://www.conf42.com/Python_2025_Siddharth_Pratap_Singh_search_vector_semantic) (Walmart Labs), and context-aware evaluation metrics for search from [Aditya Singh](https://www.conf42.com/Python_2025_Aditya_Singh_precision_metrics_framework). [Parul Gupta](https://www.conf42.com/Python_2025_Parul_Gupta_ai_ml_prototyping) (Meta) described the tooling behind fast ML prototyping, and [Shubham Singh](https://www.conf42.com/Python_2025_Shubham_Singh_ai_code_review) took AI code review beyond syntax checks.

## Services at scale, and catching fraud

[Aby M Joseph and Jayalekshmi K S](https://www.conf42.com/Python_2025_Aby_M_Joseph_Jayalekshmi_K_S_graphql_microservices_fastapi) (UST) built GraphQL microservices on FastAPI, and [Sushil Prabhu Prabhakaran](https://www.conf42.com/Python_2025_Sushil_Prabhu_Prabhakaran_python_cloud_scaling) (TCS) orchestrated async workflows with asyncio and FastAPI. Fraud detection got two architecture talks with the same toolbox: [Narendra Bhargav Boggarapu](https://www.conf42.com/Python_2025_Narendra_Bhargav_Boggarapu_fraud_python_transactions) (Wells Fargo) with FastAPI, Ray and MLflow, and [Vinod Upputuri](https://www.conf42.com/Python_2025_Vinod_Upputuri_fraud_ml_numpy) (Mastercard) with PyTorch, Ray and asyncio. [Ajay Krishnan Prabhakaran](https://www.conf42.com/Python_2025_Ajay_Krishnan_Prabhakaran_sms_spam_python) (Meta) covered SMS spam detection with NLP.

## Security and operations

[Sairam Durgaraju](https://www.conf42.com/Python_2025_Sairam_Durgaraju_fido2_webauthn) (Evernorth Health Services) implemented passwordless, phishing-resistant login in Python with FIDO2, WebAuthn and hardware security keys. [Sandeep Batchu](https://www.conf42.com/Python_2025_Sandeep_Batchu_secure_cloud_applications) (Microsoft) covered secure-by-design cloud applications, and [Mounika Ponugoti](https://www.conf42.com/Python_2025_Mounika_Ponugoti_device_security_attack) (Qualcomm) cost-effective embedded device security, from secure boot to control-flow integrity. On the ops side, [Justin Dearing](https://www.conf42.com/Python_2025_Justin_Dearing_docker_windows_devcontainers) (Neudesic) showed several free ways to run Windows and Linux containers and devcontainers on Windows without Docker Desktop, built on WSL, and [Lurduma Reddy Thirumala Reddy](https://www.conf42.com/Python_2025_Lurduma_Reddy_Thirumala_Reddy_hana_availability_pacemaker) (Intone Networks) automated SAP HANA high availability with Pacemaker clusters.

## Python outside engineering

[Liv McFarlin](https://www.conf42.com/Python_2025_Liv_McFarlin_python_ux_innovation) (Wheels) showed a UX team using Python for research, prototyping and collaboration, [Vamsi Upputuri](https://www.conf42.com/Python_2025_Vamsi_Upputuri_drug_development_python) (Gilead Sciences) Python in clinical drug development under compliance constraints, and [Rao Marapatla](https://www.conf42.com/Python_2025_Rao_Marapatla_data_warehouses_nonprofits) (BreakthroughT1D) data warehouses for nonprofits.

## Sponsors and where to watch

Thanks to [Arato AI](https://arato.ai/?utm_source=conf42&utm_medium=email&utm_campaign=Conf42_mail) and [Rapydo](https://www.rapydo.io/), the gold sponsors, to [StarterAI](https://www.starterai.dev/) as newsletter partner, [HockeyStick](https://www.hockeystick.show/) as podcast partner, and the media partners. Every talk is on the [Conf42 Python 2025 playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrBo176Is4wP2F6UCB0yEkWO) and the [event page](https://www.conf42.com/python2025).

Python stayed the common language across the rest of the year's Conf42 events; [Conf42 MLOps 2025](https://www.conf42.com/mlops2025) is a good next stop.
