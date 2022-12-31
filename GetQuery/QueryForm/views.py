from .forms import QueryFormInputs
from django.shortcuts import render
import openai
import os

# TODO: Paste your API key form open ai below
API_KEY = os.getenv("API_KEY")


def _talk_to_ai(query):
    openai.api_key = API_KEY

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=query,
        temperature=0.7,
        max_tokens=1447,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0]['text'].strip()


def _validate_if_programming(query, language, api_key):
    sentence = F"is \"syntax for {query}\" related to programming, Yes or No?"
    if api_key == "":
        return "API KEY not received"
    if "yes" in _talk_to_ai(sentence).lower():
        get_answer = F"syntax for {query} in {language} with example"
        final_answer = _talk_to_ai(get_answer)
        return final_answer


def get_query_view(request):
    query_form = QueryFormInputs()
    op_value = "No Query input or Query not understandable."
    query_language = "python"
    if request.method == 'POST':
        query_form = QueryFormInputs(request.POST)
        op_value = "changed"

        if query_form.is_valid():
            inp_query = query_form.cleaned_data['syntax_for']
            lang = query_form.cleaned_data['in_language']
            op_value = _validate_if_programming(inp_query, lang, API_KEY)
            if op_value:
                op_value = op_value.strip()
            else:
                op_value = "Could not understand"

            query_language = lang

    context = {"form": query_form,
               "output_value": op_value,
               "query_language": query_language
               }

    return render(request, 'home.html', context)
