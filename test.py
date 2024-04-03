from litellm import completion
from trulens_eval import Feedback, Tru, TruBasicApp
from trulens_eval.feedback.provider.litellm import LiteLLM

provider = LiteLLM(model_engine="ollama/llama2", endpoint="http://localhost:11434")
tru = Tru()

coherence = Feedback(provider.coherence_with_cot_reasons).on_output()
correctness = Feedback(provider.correctness_with_cot_reasons).on_output()
harmfulness = Feedback(provider.harmfulness_with_cot_reasons, higher_is_better=False).on_output()
controversy = Feedback(provider.controversiality_with_cot_reasons, higher_is_better=False).on_output()

tru.reset_database() #uncomment to reset database if it becomes corrupt

def llm_standalone(prompt):
    response = completion(
                model="ollama/llama2",
                messages = [{ "content": "Only reply with words","role": "user"},
                            { "content": prompt,"role": "user"}],
                api_base="http://localhost:11434"
    )

    print(response)
    return response

basic_app = TruBasicApp(llm_standalone, app_id="LiteLLM-Llama2", feedbacks=[coherence, correctness, harmfulness, controversy])

with basic_app as recording:
    basic_app.app("Is the world flat?")
    basic_app.wait_for_feedback_results()

with basic_app as recording:
    basic_app.app("Why is the sky blue?")
    basic_app.wait_for_feedback_results()

with basic_app as recording:
    basic_app.app("Why is grass green?")
    basic_app.wait_for_feedback_results()

tru.run_dashboard() 
tru.get_records_and_feedback(app_ids=[])[0]