# DevGenAIWithJamOct2026

## Labs, courseware, survey, completion certificate
- [Labs and courseware](https://us-east-1.student.classrooms.aws.training/class/ilt%23nqD37DQnCgx2v4wWx97DVs)
- [MyClass](https://myclass.skillbuilder.aws), here you can get the certificate and fill the survey when attendance is marked complete

## Day 1 links
- [Built-in algorithms and pretrained models in Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html)
- [The Neural Network Zoo](https://www.asimovinstitute.org/neural-network-zoo/)
- [Attention is all you need](https://arxiv.org/pdf/1706.03762)
- [How Sequence-to-Sequence Works](https://docs.aws.amazon.com/sagemaker/latest/dg/seq-2-seq-howitworks.html), its implementation highlights the limitations it had, and how attention networks solved the issue.
- [What are Embeddings in Machine Learning?](https://aws.amazon.com/what-is/embeddings-in-machine-learning/)
- [What are Transformers in Artificial Intelligence?](https://aws.amazon.com/what-is/transformers-in-artificial-intelligence/)
- Some vector playgrounds
    - [Embedding Playground](https://www.adityabawankule.io/tools/embedding-playground)
    - [Embedding Projector](https://projector.tensorflow.org/)
- [Classifier Context Rot: Monitor Performance Degrades with Context Length](https://arxiv.org/html/2605.12366v1)
- High-level AI services tend to have a very simple and specialized API. Take [Polly](https://docs.aws.amazon.com/polly/latest/APIReference/API_Operations.html), a text-to-speech service, as an example.
- Prompt engineering
    - Costar framework
        - [Implementing advanced prompt engineering with Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/implementing-advanced-prompt-engineering-with-amazon-bedrock/), AWS blog discussing it
        - [Developing an Interactive OpenMP Programming Book with Large Language Models](https://arxiv.org/pdf/2409.09296), article mentioning the costar all along their methodology
        - [COSTAR Prompt Engineering: What It Is and Why It Matters](https://aws.amazon.com/what-is/prompt-engineering/)
        - ... there are way more references on this
    - (What is Prompt Engineering?)[https://aws.amazon.com/what-is/prompt-engineering/]
    - [Prompt engineering concepts](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-engineering-guidelines.html), notice that there are links for each model provider's best practices
    - [Design a prompt](https://docs.aws.amazon.com/bedrock/latest/userguide/design-a-prompt.html), this comes from Bedrock's docs
- Evaluating prompts and responses
    - [Built-in prompts for metrics when using Model-as-a-judge](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-judge-prompt.html)
    - [Evaluate models or RAG systems using Amazon Bedrock Evaluations – Now generally available](https://aws.amazon.com/blogs/machine-learning/evaluate-models-or-rag-systems-using-amazon-bedrock-evaluations-now-generally-available/)
    - [Evaluate, compare, and select the best foundation models for your use case in Amazon Bedrock (preview)](https://aws.amazon.com/blogs/aws/evaluate-compare-and-select-the-best-foundation-models-for-your-use-case-in-amazon-bedrock-preview/) - announcement, when LLM-as-a-judge was still not available
    - [Creating a model evaluation job that use human workers in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-human.html)
    - [Model evaluation task types in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-tasks.html), uses publicly available prompt datasets and metrics used as benchmarks
- [ReAct: SYNERGIZING REASONING AND ACTING IN LANGUAGE MODELS](https://arxiv.org/pdf/2210.03629), one could say this is the article that "gave birth" to agents
- [Amazon Bedrock Prompt Management is now available in GA](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-prompt-management-is-now-available-in-ga/)
- [Amazon Bedrock introduces new advanced prompt optimization and migration tool](https://aws.amazon.com/blogs/aws/amazon-bedrock-introduces-new-advanced-prompt-optimization-and-migration-tool/)
- Inference profiles
    - [Cross-region](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html), they are us, apac, eu, ... and global
    - [Application inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html), don't forget you need to use the ARN of the inference profile in place of the model id whenever submitting a request to Bedrock
- [Create a batch inference job](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html)
- [Increase model invocation capacity with Provisioned Throughput in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html)
- [Prompt caching for faster model inference](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html)
- [Memory concepts in Langchain](https://docs.langchain.com/oss/python/concepts/memory). Keep in mind that langchain is just **one** example framework that exposes Memory as a high-level resource, and you are able to define the backing store wherever you would like. 
- Vector stores on AWS
    - [Amazon DynamoDB now supports real-time vector search at any scale](https://aws.amazon.com/blogs/aws/amazon-dynamodb-now-supports-real-time-vector-search-at-any-scale/)
    - [Amazon S3 Vectors now generally available with increased scale and performance](https://aws.amazon.com/blogs/aws/amazon-s3-vectors-now-generally-available-with-increased-scale-and-performance/)
    - [Introducing Amazon Kendra GenAI Index – Enhanced semantic search and retrieval capabilities](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-kendra-genai-index-enhanced-semantic-search-and-retrieval-capabilities/)
    - [Vector database options](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-an-aws-vector-database-for-rag-use-cases/vector-db-options.html), from the prescriptive guidance on options for vector store in RAG scenarios
- [What is RAG?](https://aws.amazon.com/what-is/retrieval-augmented-generation/)

## Day 2 links
- Knowledge bases-related operations:
    - [Generate a query for structured data](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-generate-query.html) - GenerateQuery API
    - [Improve the relevance of query responses with a reranker model in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/rerank.html) - Rerank API
    - [RetrieveAndGenerate](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html) - full RAG-workflow in a call
    - [Retrieve](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html), does only the R(etrieve) part of RAG 
    - The knowledge bases seen in the lab and course are now called "self-managed KBs". There is a new, preferred way, called "Managed knowledge bases". More about it here:
        - [Introducing Amazon Bedrock Managed Knowledge Base for faster, more accurate enterprise AI applications](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-managed-knowledge-base-for-faster-more-accurate-enterprise-ai-applications/)
    - [Amazon Bedrock Knowledge Bases now supports hybrid search](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-knowledge-bases-now-supports-hybrid-search/)
    - [Build and deploy an automatic sync solution for Amazon Bedrock Knowledge Bases](https://aws.amazon.com/blogs/machine-learning/build-and-deploy-an-automatic-sync-solution-for-amazon-bedrock-knowledge-bases/)
    - [Amazon EventBridge – Event-Driven AWS Integration for your SaaS Applications](https://aws.amazon.com/blogs/aws/amazon-eventbridge-event-driven-aws-integration-for-your-saas-applications/)
    - [Try the new console experience in Amazon Bedrock, optimized for Anthropic- and OpenAI-compatible APIs](https://aws.amazon.com/blogs/aws/try-the-new-console-experience-in-amazon-bedrock-optimized-for-anthropic-and-openai-compatible-apis/)
    - [APIs supported by Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/apis.html)
    - [List of available RAGAS metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/)

- [Multi-Cloud is the Worst Practice](https://www.lastweekinaws.com/blog/multi-cloud-is-the-worst-practice/), just food for thought.

- [Optimize model inference for latency](https://docs.aws.amazon.com/bedrock/latest/userguide/latency-optimized-inference.html)
- [Understanding intelligent prompt routing in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html)
- [Binary Model Insights](https://docs.aws.amazon.com/machine-learning/latest/dg/binary-model-insights.html) - this documentation sits on a product that is gone for more than ten years. But the concpets are not dependent on the service.
- [Built-in evaluation prompts for RAG workflows](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-eval-prompt.html)
- [Ragas built-in metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/)