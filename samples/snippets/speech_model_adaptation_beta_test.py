# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import google.auth

from google.cloud import speech_v1p1beta1 as speech

import speech_model_adaptation_beta


STORAGE_URI = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"
_, PROJECT_ID = google.auth.default()
LOCATION = "us-west1"
PHRASE_ID = "restaurantphrasesets"
CUSTOM_CLASS_ID = "seattlerestaurants"
PHRASE_PARENT = f"projects/{PROJECT_ID}/locations/{LOCATION}/phraseSets/{PHRASE_ID}"
CLASS_PARENT = (
    f"projects/{PROJECT_ID}/locations/{LOCATION}/customClasses/{CUSTOM_CLASS_ID}"
)


def test_model_adaptation_beta(capsys):
    transcript = speech_model_adaptation_beta.transcribe_with_model_adaptation(
        PROJECT_ID, LOCATION, STORAGE_URI
    )
    assert "how long is the Brooklyn Bridge" in transcript
    client = speech.AdaptationClient()
    client.delete_phrase_set(name=PHRASE_PARENT)
    client.delete_custom_class(name=CLASS_PARENT)
