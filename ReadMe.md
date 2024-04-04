# LLM Testing with Trulens
This repository contains an example of using Trulens to asses the quality of an LLMs output. It is built around using the Ollama API to interact with and test the Meta Llama2 LLM. You can read the associated blog post on [The Quality Duck](https://insertlinkhere.com) website.

This example is a single file python script and should be considered as a proof of concept (POC), rather than an example of good practice for framework development using this tool.

## Assertions
The framework includes assertions that rely on calling the LLM a second time to assess the quality of the output. As this is a POC being run locally it uses the same LLM for assertions as we are testing. 