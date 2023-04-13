import json

from utils import http
from django.conf import settings
from decorators import access_required
import openai
openai.api_key = settings.OPENAI_API_KEY


# API functions
def api_ping(request, version):
    return http.JsonSuccessResponse()


@access_required
def api_login(request, version):
    return http.JsonSuccessResponse()


def completions(request, version):
    prompt = request.POST['prompt']
    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=2048, stream=False)
    result = {
        "data": response['choices'][0]['text']
    }
    return http.JsonSuccessResponse(result)


def chat(request, version):
    prompt = request.POST['prompt']
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    result = {
        "data": completion.choices[0].message
    }
    return http.JsonSuccessResponse(result)


def images(request, version):
    prompt = request.POST['prompt']
    completion = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256"
    )
    result = {
        "data": completion.data[0]['url']
    }
    return http.JsonSuccessResponse(result)
