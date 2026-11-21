# Containers, Terraform and GitOps turn AI deploys into a non-event

Conf42 Blog, 2025-08-12, updated 2026-11-09. https://www.conf42.com/blog/platform2025/containers-iac-gitops-for-ai-platforms

In short: Google's Bhaskar Goyal at Conf42 Platform Engineering 2025 on AI-aware Docker builds, Kubernetes GPU pools, Terraform modules and GitOps for model deploys.

"It works on my machine" is funnier when the machine has a GPU and the model is several gigabytes. At Conf42 Platform Engineering 2025, Bhaskar Goyal, a software engineer at Google, laid out a four-part path from chaotic AI deployments to boring, reliable ones: AI-aware containers, Kubernetes, Terraform and GitOps, with a 30-day and 90-day plan to get there.

None of the pieces are new. The value is in how each one is tuned for AI workloads, and in the order he suggests adopting them.

## Three ways AI deploys go wrong

Bhaskar groups the pain into environment inconsistency (libraries, dependencies and hardware differ between a data scientist's laptop and production), manual deployment that depends on one person who might be on holiday, and the production fires that follow. The cost is deployment cycles stretching from days into weeks or months, and teams losing faith in AI projects.

## Docker patterns built for models

Containerisation fixes the laptop problem, but AI adds GPUs, huge artifacts and unusual scaling. His three Docker patterns:

- **Multi-stage builds** for smaller, more secure production images with faster pulls.
- **Hardware-aware base images**: CUDA-enabled for GPU workloads, CPU-optimised for CPU inference, instead of one generic base for everything.
- **Layer caching by change frequency**: stable system packages first, frequently changing code and model artifacts last.

He quotes a principal engineer at a Fortune 500 financial services company crediting containerisation with a 65% cut in model deployment failures.

## Kubernetes for expensive hardware

On Kubernetes, the AI-specific bits are horizontal pod autoscaling on custom metrics such as prediction requests per second, GPU node pools with resource quotas so costly GPUs are shared fairly across teams, and canary deployments that roll a new model version to a small slice of users before going wide.

## Terraform and GitOps keep it reproducible

For infrastructure as code he recommends Terraform modules for common AI components (model registries, inference clusters, feature stores), separate directories or workspaces per environment so promotion through CI/CD stays consistent, and remote state in S3 or Google Cloud Storage with locking, encryption and versioning turned on. The disaster recovery payoff: rebuild the platform in hours instead of days.

GitOps ties it together. Git is the single source of truth for infrastructure and application config, a pull-based operator such as Argo CD or Flux syncs the cluster, drift is detected and corrected, and a rollback is a git revert.

## The numbers and the plan

The results he cites from organisations adopting these patterns: 85% less deployment time for complex AI workloads, 73% fewer production incidents, 40% infrastructure savings and three times more models in production.

The plan is the most useful slide. In 30 days, containerise one high-value AI workload with multi-stage builds, write basic Terraform modules for the key components, and set up a GitOps repository. In 90 days, run Kubernetes with GPU support, add canary releases for model updates, and build monitoring tailored to AI workloads.

## Who should watch

Platform engineers who just inherited the ML team's deployments, and ML engineers who want production to stop being a surprise. If you already run Argo CD with GPU node pools, it is a confirmation, not a revelation.

## Related Conf42 talks

- [Graziano Casto on managing AI workloads in cloud environments](https://www.conf42.com/Large_Language_Models_LLMs_2025_Graziano_Casto_workloads_cloud_environments) covers the operational challenges from another angle.
- [Kosseila Haddalene on running vLLM inference on Kubernetes across clouds](https://www.conf42.com/MLOps_2026_Kosseila_Haddalene_vllm_kubernetes_gpu) is a production GPU blueprint.
- [Eti Ijeoma on optimizing cache usage in Docker builds](https://www.conf42.com/Cloud_Native_2025_Eti_Ijeoma_docker_cache_efficiency) expands the layer caching advice.

[Watch Bhaskar Goyal's talk](https://www.conf42.com/Platform_Engineering_2025_Bhaskar_Goyal_container_paradise_chaos)

[Watch the talk on YouTube](https://youtu.be/1zzXcJciecU).

## Watch the talk

[Building Bulletproof AI Platforms: From Container Chaos to Production Paradise](https://www.conf42.com/Platform_Engineering_2025_Bhaskar_Goyal_container_paradise_chaos) at Conf42 Platform Engineering 2025.
