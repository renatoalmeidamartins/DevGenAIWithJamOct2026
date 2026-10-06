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