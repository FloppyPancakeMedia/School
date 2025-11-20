"""
Small wrapper for Gemini. Reads `GEMINI_API_KEY` from the environment for real client.
Provides `assess(prompt, player_text)` which returns 'pass' or 'fail'.
If real client fails or key not present, falls back to MockGeminiClient.
"""

import os
import time
from enum import StrEnum
import requests
import random
from google import genai
from google.genai import types
import traceback, logging

logging.basicConfig(filename="gemini_errors.log", level=logging.INFO)


def _log_exc(e):
    logging.info("Gemini call failed: %s", repr(e))
    logging.info(traceback.format_exc())


GEMINI_ENDPOINT = (
    "https://generative.googleapis.com/v1beta2/models/text-bison-001:generateText"
)
GEMINI_API_KEY = "" # Paste API key here because I don't know how to get it from sys env yet


class GeminiModels(StrEnum):
    PRO25 = "gemini-2.5-pro"
    FLASH25 = "gemini-2.5-flash"
    FLASH25LITE = "gemini-2.5-flash-lite"
    FLASH20 = "gemini-2.0-flash"


GEMINI_MODEL = GeminiModels.FLASH20

HARDCODE_SCENARIOS = {
    "philosophy": "You enter philosophy class and the teacher begins lecturing. You slept like hell the last 2 days and are having trouble staying awake. What do you do?",
    "audio_tech": "You're in audio lab and the speaker is squealing. You need to fix the mix quickly. What do you do?",
    "culinary": "The instructor asks you to plate a dessert using only three ingredients. How do you proceed?",
    "network_ops": "The network goes down before an important demo. What quick steps do you take?",
    "nursing": "A patient is calling for help and you're the only one in the room. What's your immediate action?",
    "admin": "The registrar asks why you want to register for classes — sell yourself in one sentence.",
    "bathroom": "You are at the bathroom. Take a second to relieve yourself.",
}

SCENARIO_PROMPTS = {
    "philosophy": {
        "sys_instruct": "You are a pretentious philosophy professor who thinks all his students are dumb. You are talking directly to a student to determine whether they pass or fail the class",
        "prompt": "Generate a funny scenario where a philosophy student is attending class and meets a challenge they must respond to. Limit your response to 50 words.",
    },
    "audio_tech": {
        "sys_instruct": "You are an audio technology teacher who did a little too much acid in the 70's. You are talking directly to a student to determine whether they pass or fail the class",
        "prompt": "Present a funny challenge where an audio technology student is attending class and is presented with a situation they must respond to. Limit your response to 50 words.",
    },
    "culinary": {
        "sys_instruct": "You are a goofy, rotund culinary instructor. You are talking directly to a student to determine whether they pass or fail the class",
        "prompt": "Present a funny challenge where a culinary student is attending class and meets a challenge they must respond to. Limit your response to 50 words.",
    },
    "network_ops": {
        "sys_instruct": "You are a libertarian, nihilistic network operations professor. You are talking directly to a student to determine whether they pass or fail the class",
        "prompt": "Generate a funny scenario where a network operations student is attending class and meets a challenge they must respond to. Limit your response to 50 words.",
    },
    "nursing": {
        "sys_instruct": "You are an existential comedy writer. You are talking directly to a student to determine whether they pass or fail the class",
        "prompt": "Generate a funny scenario where a nursing student is attending class and meets a challenge they must respond to. Limit your response to 50 words.",
    },
    "admin": {
        "sys_instruct": "You are a dull and bored admin assistant being approached by a prospective, over-ambitious student. You are talking directly to the student",
        "prompt": "Generate a funny scenario where a college student is at the admin building and has to sign up for school. There are 5 degrees the student must earn at this school - audio tech, philosophy, network operations, nursing, and culinary - and you are to ask the student why they should be accepted. The student is to give a response to which either a pass or fail will be determined. Limit your response to 50 words.",
    },
    "bathroom": {
        "sys_instruct": "You are a comedy writer who's actually really shy and a bit prude but has to write a bathroom scenario. This is a scenario that a game's protaganist encounters, and either will pass or fail",
        "prompt": "Generate a funny scenario where a student (who is the player character of an RPG) walks into a bathroom but encounters a challenge. You are presenting the challenge to the player. The player is to respond how they would react in the scenario and they either pass or fail. Limit your response to 50 words.",
    },
}


class RealGeminiClient:
    def __init__(self, api_key: str | None = None, timeout: int = 5):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        self.timeout = timeout
        log_file = open("log.txt", "w")
        log_file.write("Attempting to use RealGeminiClient")
        log_file.close()

    def generate_scenario(self, b: str) -> str:
        try:
            client = genai.Client(api_key=GEMINI_API_KEY)
            response = client.models.generate_content(
                model=GEMINI_MODEL,
                config=types.GenerateContentConfig(
                    system_instruction=SCENARIO_PROMPTS[b]["sys_instruct"]),
                contents=SCENARIO_PROMPTS[b]["prompt"],
            )
            return response.text
        except Exception as e:
            _log_exc(e)
            return "Could not contact Gemini in generate_scenario. Consider complaining to Google."

    def assess(self, prompt: str, player_text: str) -> str:
        if not self.api_key:
            raise RuntimeError("No GEMINI_API_KEY available")
        try:
            client = genai.Client(api_key=GEMINI_API_KEY)
            prompt += "The player has responded with: " + player_text
            prompt += "Now your response should be a pass or fail and a humerous reason for your decision. There should be a default 75 percent chance of passing. Pass or fail should be the first word of your response, followed by the reason. Do not begin your response with anything except 'pass' or 'fail'"
            response = client.models.generate_content(model=GEMINI_MODEL, 
                                                      config=types.GenerateContentConfig(
                                                          system_instruction="You are now the ultimate judge of fate in this totally insignificant scenario."
                                                      ),
                                                      contents=prompt)
            return response.text
        except Exception as e:
            _log_exc(e)
            return "Could not contact Gemini in assess. Consider throwing your computer out the window."
        
        # headers = {
        #     'Authorization': f'Bearer {self.api_key}',
        #     'Content-Type': 'application/json',
        # }
        # payload = {
        #     'prompt': f"PROMPT: {prompt}\nPLAYER: {player_text}\nReturn only the single word 'pass' or 'fail'.",
        #     'temperature': 0.3,
        #     'maxOutputTokens': 32,
        # }
        # try:
        #     r = requests.post(GEMINI_ENDPOINT, headers=headers, json=payload, timeout=self.timeout)
        #     r.raise_for_status()
        #     data = r.text
        #     # crude parsing: look for pass/fail word
        #     low = data.lower()
        #     if 'pass' in low:
        #         return 'pass'
        #     if 'fail' in low:
        #         return 'fail'
        #     return 'fail'
        # except Exception:
        #     raise


class MockGeminiClient:

    def __init__(self, seed: int | None = None):
        if seed is not None:
            random.seed(seed)

    def generate_scenario(self, b: str):
        return HARDCODE_SCENARIOS[b]

    def assess(self, prompt: str, player_text: str) -> str:
        # simple heuristic: if player_text mentions certain helpful words, lean to pass
        helpful = [
            "study",
            "listen",
            "coffee",
            "ask",
            "participate",
            "practice",
            "help",
        ]
        low = player_text.lower()
        score = 0
        for w in helpful:
            if w in low:
                score += 1
        # if any helpful words, high chance to pass
        if score >= 1:
            return "pass" if random.random() < 0.9 else "fail"
        # otherwise random
        return "pass" if random.random() < 0.4 else "fail"


def get_client(using_gemini: bool):
    if using_gemini:
        try:
            key = GEMINI_API_KEY
            client = RealGeminiClient(api_key=key)
            # quick test to ensure key plausibly works is skipped; we'll prefer it but allow runtime fallback
            return client
        except Exception:
            log_file = open("log.txt", "w")
            log_file.write(f"API key access failed {time.time}")
            log_file.close()
    else:
        return MockGeminiClient()
