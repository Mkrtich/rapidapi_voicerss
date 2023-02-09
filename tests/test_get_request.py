import pytest
import os
import json
from src.tts_get_request import TextToSpeechGetRequest


# create an instance of class using the main configs
@pytest.fixture
def get_req_class_obj(get_main_cfgs):
    # initialize an object with general configs and run the request
    get_req_class_obj = TextToSpeechGetRequest(get_main_cfgs)
    return get_req_class_obj


# check with default options using valid api key
def test_positive_default(get_test_cases, get_req_class_obj):
    # get the command arguments of current test
    current_test_case = get_test_cases["test_positive_default"]
    input_fields = current_test_case["input_fields"]
    output_expectations = current_test_case["output_expectations"]

    # run the request
    response = get_req_class_obj.send_request(api_key=input_fields["api_key"], src_text=input_fields["src_text"], content_language=input_fields["content_language"], speech_voice=input_fields["speech_voice"], speech_rate=input_fields["speech_rate"], audio_codec=input_fields["audio_codec"], audio_format= input_fields["audio_format"], ssml= input_fields["ssml"], out_str_format= input_fields["out_str_format"])
    
    # check the status code, content type and content length
    assert response.status_code == output_expectations["status_code"]
    assert response.headers["Content-Type"] == output_expectations["Content-Type"]
    assert response.headers["Content-Length"] == output_expectations["Content-Length"]

# check the en-in language
def test_positive_language_en_in(get_test_cases, get_req_class_obj):
    # get the command arguments of current test
    current_test_case = get_test_cases["test_positive_language_en_in"]
    input_fields = current_test_case["input_fields"]
    output_expectations = current_test_case["output_expectations"]

    # run the request
    response = get_req_class_obj.send_request(api_key=input_fields["api_key"], src_text=input_fields["src_text"], content_language=input_fields["content_language"], speech_voice=input_fields["speech_voice"], speech_rate=input_fields["speech_rate"], audio_codec=input_fields["audio_codec"], audio_format= input_fields["audio_format"], ssml= input_fields["ssml"], out_str_format= input_fields["out_str_format"])
    
    # check the status code, content type and content length
    assert response.status_code == output_expectations["status_code"]
    assert response.headers["Content-Type"] == output_expectations["Content-Type"]
    assert response.headers["Content-Length"] == output_expectations["Content-Length"]

# check the Mike voice
def test_positive_speech_voice_mike(get_test_cases, get_req_class_obj):
    # get the command arguments of current test
    current_test_case = get_test_cases["test_positive_speech_voice_mike"]
    input_fields = current_test_case["input_fields"]
    output_expectations = current_test_case["output_expectations"]

    # run the request
    response = get_req_class_obj.send_request(api_key=input_fields["api_key"], src_text=input_fields["src_text"], content_language=input_fields["content_language"], speech_voice=input_fields["speech_voice"], speech_rate=input_fields["speech_rate"], audio_codec=input_fields["audio_codec"], audio_format= input_fields["audio_format"], ssml= input_fields["ssml"], out_str_format= input_fields["out_str_format"])
    
    # check the status code, content type and content length
    assert response.status_code == output_expectations["status_code"]
    assert response.headers["Content-Type"] == output_expectations["Content-Type"]
    assert response.headers["Content-Length"] == output_expectations["Content-Length"]


# check the speech rate 10
def test_positive_speech_rate_10(get_test_cases, get_req_class_obj):
    # get the command arguments of current test
    current_test_case = get_test_cases["test_positive_speech_rate_10"]
    input_fields = current_test_case["input_fields"]
    output_expectations = current_test_case["output_expectations"]

    # run the request
    response = get_req_class_obj.send_request(api_key=input_fields["api_key"], src_text=input_fields["src_text"], content_language=input_fields["content_language"], speech_voice=input_fields["speech_voice"], speech_rate=input_fields["speech_rate"], audio_codec=input_fields["audio_codec"], audio_format= input_fields["audio_format"], ssml= input_fields["ssml"], out_str_format= input_fields["out_str_format"])
    
    # check the status code, content type and content length
    assert response.status_code == output_expectations["status_code"]
    assert response.headers["Content-Type"] == output_expectations["Content-Type"]
    assert response.headers["Content-Length"] == output_expectations["Content-Length"]


# check the mp3 output
def test_positive_mpeg_codec(get_test_cases, get_req_class_obj):
    # get the command arguments of current test
    current_test_case = get_test_cases["test_positive_mpeg_codec"]
    input_fields = current_test_case["input_fields"]
    output_expectations = current_test_case["output_expectations"]

    # run the request
    response = get_req_class_obj.send_request(api_key=input_fields["api_key"], src_text=input_fields["src_text"], content_language=input_fields["content_language"], speech_voice=input_fields["speech_voice"], speech_rate=input_fields["speech_rate"], audio_codec=input_fields["audio_codec"], audio_format= input_fields["audio_format"], ssml= input_fields["ssml"], out_str_format= input_fields["out_str_format"])
    
    # check the status code, content type and content length
    assert response.status_code == output_expectations["status_code"]
    assert response.headers["Content-Type"] == output_expectations["Content-Type"]
    assert response.headers["Content-Length"] == output_expectations["Content-Length"]


# check the audio format 48khz_8bit_mono
def test_positive_audio_format_48khz_8bit_mono(get_test_cases, get_req_class_obj):
    # get the command arguments of current test
    current_test_case = get_test_cases["test_positive_audio_format_48khz_8bit_mono"]
    input_fields = current_test_case["input_fields"]
    output_expectations = current_test_case["output_expectations"]

    # run the request
    response = get_req_class_obj.send_request(api_key=input_fields["api_key"], src_text=input_fields["src_text"], content_language=input_fields["content_language"], speech_voice=input_fields["speech_voice"], speech_rate=input_fields["speech_rate"], audio_codec=input_fields["audio_codec"], audio_format= input_fields["audio_format"], ssml= input_fields["ssml"], out_str_format= input_fields["out_str_format"])
    
    # check the status code, content type and content length
    assert response.status_code == output_expectations["status_code"]
    assert response.headers["Content-Type"] == output_expectations["Content-Type"]
    assert response.headers["Content-Length"] == output_expectations["Content-Length"]


# check the combination of several options, france, sr=-5, stereo, mpeg
def test_positive_fr_logan_10_mpeg_stereo(get_test_cases, get_req_class_obj):
    # get the command arguments of current test
    current_test_case = get_test_cases["test_positive_fr_logan_10_mpeg_stereo"]
    input_fields = current_test_case["input_fields"]
    output_expectations = current_test_case["output_expectations"]

    # run the request
    response = get_req_class_obj.send_request(api_key=input_fields["api_key"], src_text=input_fields["src_text"], content_language=input_fields["content_language"], speech_voice=input_fields["speech_voice"], speech_rate=input_fields["speech_rate"], audio_codec=input_fields["audio_codec"], audio_format= input_fields["audio_format"], ssml= input_fields["ssml"], out_str_format= input_fields["out_str_format"])
    
    # check the status code, content type and content length
    assert response.status_code == output_expectations["status_code"]
    assert response.headers["Content-Type"] == output_expectations["Content-Type"]
    assert response.headers["Content-Length"] == output_expectations["Content-Length"]


# check the b64 true option
def test_positive_b64_true(get_test_cases, get_req_class_obj):
    # get the command arguments of current test
    current_test_case = get_test_cases["test_positive_b64_true"]
    input_fields = current_test_case["input_fields"]
    output_expectations = current_test_case["output_expectations"]

    # run the request
    response = get_req_class_obj.send_request(api_key=input_fields["api_key"], src_text=input_fields["src_text"], content_language=input_fields["content_language"], speech_voice=input_fields["speech_voice"], speech_rate=input_fields["speech_rate"], audio_codec=input_fields["audio_codec"], audio_format= input_fields["audio_format"], ssml= input_fields["ssml"], out_str_format= input_fields["out_str_format"])
    
    # check the status code, content type and content length
    assert response.status_code == output_expectations["status_code"]
    assert response.headers["Content-Type"] == output_expectations["Content-Type"]
    assert response.headers["Content-Length"] == output_expectations["Content-Length"]


# check the behaviour on language and voice disagreement 
def test_specific_speech_voice_olga_en(get_test_cases, get_req_class_obj):
    # get the command arguments of current test
    current_test_case = get_test_cases["test_specific_speech_voice_olga_en"]
    input_fields = current_test_case["input_fields"]
    output_expectations = current_test_case["output_expectations"]

    # run the request
    response = get_req_class_obj.send_request(api_key=input_fields["api_key"], src_text=input_fields["src_text"], content_language=input_fields["content_language"], speech_voice=input_fields["speech_voice"], speech_rate=input_fields["speech_rate"], audio_codec=input_fields["audio_codec"], audio_format= input_fields["audio_format"], ssml= input_fields["ssml"], out_str_format= input_fields["out_str_format"])
    
    # check the status code, content type and content length
    assert response.status_code == output_expectations["status_code"]
    assert response.headers["Content-Type"] == output_expectations["Content-Type"]
    assert response.headers["Content-Length"] == output_expectations["Content-Length"]


# check the behaviour during not existing voice value, here should be used the default one for that language
def test_specific_nonexisting_voice(get_test_cases, get_req_class_obj):
    # get the command arguments of current test
    current_test_case = get_test_cases["test_specific_nonexisting_voice"]
    input_fields = current_test_case["input_fields"]
    output_expectations = current_test_case["output_expectations"]

    # run the request
    response = get_req_class_obj.send_request(api_key=input_fields["api_key"], src_text=input_fields["src_text"], content_language=input_fields["content_language"], speech_voice=input_fields["speech_voice"], speech_rate=input_fields["speech_rate"], audio_codec=input_fields["audio_codec"], audio_format= input_fields["audio_format"], ssml= input_fields["ssml"], out_str_format= input_fields["out_str_format"])
    
    # check the status code, content type and content length
    assert response.status_code == output_expectations["status_code"]
    assert response.headers["Content-Type"] == output_expectations["Content-Type"]
    assert response.headers["Content-Length"] == output_expectations["Content-Length"]


# check the behaviour during not existing codec value
def test_specific_nonexisting_codec(get_test_cases, get_req_class_obj):
    # get the command arguments of current test
    current_test_case = get_test_cases["test_specific_nonexisting_codec"]
    input_fields = current_test_case["input_fields"]
    output_expectations = current_test_case["output_expectations"]

    # run the request
    response = get_req_class_obj.send_request(api_key=input_fields["api_key"], src_text=input_fields["src_text"], content_language=input_fields["content_language"], speech_voice=input_fields["speech_voice"], speech_rate=input_fields["speech_rate"], audio_codec=input_fields["audio_codec"], audio_format= input_fields["audio_format"], ssml= input_fields["ssml"], out_str_format= input_fields["out_str_format"])
    
    # check the status code, content type and content length
    assert response.status_code == output_expectations["status_code"]
    assert response.headers["Content-Type"] == output_expectations["Content-Type"]
    assert response.headers["Content-Length"] == output_expectations["Content-Length"]


# check the behaviour during wrong speech rate, positive, out of range.. the behaviour - no error message, but output length is 1
def test_specific_speech_rate_50(get_test_cases, get_req_class_obj):
    # get the command arguments of current test
    current_test_case = get_test_cases["test_specific_speech_rate_50"]
    input_fields = current_test_case["input_fields"]
    output_expectations = current_test_case["output_expectations"]

    # run the request
    response = get_req_class_obj.send_request(api_key=input_fields["api_key"], src_text=input_fields["src_text"], content_language=input_fields["content_language"], speech_voice=input_fields["speech_voice"], speech_rate=input_fields["speech_rate"], audio_codec=input_fields["audio_codec"], audio_format= input_fields["audio_format"], ssml= input_fields["ssml"], out_str_format= input_fields["out_str_format"])
    
    # check the status code, content type and content length
    assert response.status_code == output_expectations["status_code"]
    assert response.headers["Content-Type"] == output_expectations["Content-Type"]
    assert response.headers["Content-Length"] == output_expectations["Content-Length"]


# check the behaviour during wrong speech rate, negative, out of range.. the behaviour - no error message, but output length is 1
def test_specific_speech_rate_minus_100(get_test_cases, get_req_class_obj):
    # get the command arguments of current test
    current_test_case = get_test_cases["test_specific_speech_rate_minus_100"]
    input_fields = current_test_case["input_fields"]
    output_expectations = current_test_case["output_expectations"]

    # run the request
    response = get_req_class_obj.send_request(api_key=input_fields["api_key"], src_text=input_fields["src_text"], content_language=input_fields["content_language"], speech_voice=input_fields["speech_voice"], speech_rate=input_fields["speech_rate"], audio_codec=input_fields["audio_codec"], audio_format= input_fields["audio_format"], ssml= input_fields["ssml"], out_str_format= input_fields["out_str_format"])
    
    # check the status code, content type and content length
    assert response.status_code == output_expectations["status_code"]
    assert response.headers["Content-Type"] == output_expectations["Content-Type"]
    assert response.headers["Content-Length"] == output_expectations["Content-Length"]

    
# check the behaviour on big text, during the get request - behaviour is different by comparison wtih post, error 414 is returned
def test_specific_long_txt(get_test_cases, get_req_class_obj):
    # get the command arguments of current test
    current_test_case = get_test_cases["test_specific_long_txt"]
    input_fields = current_test_case["input_fields"]
    output_expectations = current_test_case["output_expectations"]

    # run the request
    response = get_req_class_obj.send_request(api_key=input_fields["api_key"], src_text=input_fields["src_text"]*1000, content_language=input_fields["content_language"], speech_voice=input_fields["speech_voice"], speech_rate=input_fields["speech_rate"], audio_codec=input_fields["audio_codec"], audio_format= input_fields["audio_format"], ssml= input_fields["ssml"], out_str_format= input_fields["out_str_format"])
    
    # check the status code, content type and content length
    assert response.status_code == output_expectations["status_code"]
    assert response.headers["Content-Type"] == output_expectations["Content-Type"]
    assert response.headers["Content-Length"] == output_expectations["Content-Length"]


# check with default options and validate the output mp3
def test_specific_check_en_us_mpeg_content(get_test_cases, get_req_class_obj):
    # get the command arguments of current test
    current_test_case = get_test_cases["test_specific_check_en_us_mpeg_content"]
    input_fields = current_test_case["input_fields"]
    output_expectations = current_test_case["output_expectations"]

    # run the request
    response = get_req_class_obj.send_request(api_key=input_fields["api_key"], src_text=input_fields["src_text"], content_language=input_fields["content_language"], speech_voice=input_fields["speech_voice"], speech_rate=input_fields["speech_rate"], audio_codec=input_fields["audio_codec"], audio_format= input_fields["audio_format"], ssml= input_fields["ssml"], out_str_format= input_fields["out_str_format"])
    
    # check the status code, content type and content length
    assert response.status_code == output_expectations["status_code"]
    assert response.headers["Content-Type"] == output_expectations["Content-Type"]
    assert response.headers["Content-Length"] == output_expectations["Content-Length"]

    # audio comparison part
    with open(os.path.join("golden_audios", "test_specific_check_en_us_mpeg_content.mp3"), "rb") as f_golden:
        golden_content = f_golden.read()
    assert golden_content == response.content


# check the output wav file of russian male speaker
def test_specific_check_russian_wav_content(get_test_cases, get_req_class_obj):
    # get the command arguments of current test
    current_test_case = get_test_cases["test_specific_check_russian_wav_content"]
    input_fields = current_test_case["input_fields"]
    output_expectations = current_test_case["output_expectations"]

    # run the request
    response = get_req_class_obj.send_request(api_key=input_fields["api_key"], src_text=input_fields["src_text"], content_language=input_fields["content_language"], speech_voice=input_fields["speech_voice"], speech_rate=input_fields["speech_rate"], audio_codec=input_fields["audio_codec"], audio_format= input_fields["audio_format"], ssml= input_fields["ssml"], out_str_format= input_fields["out_str_format"])
    
    # check the status code, content type and content length
    assert response.status_code == output_expectations["status_code"]
    assert response.headers["Content-Type"] == output_expectations["Content-Type"]
    assert response.headers["Content-Length"] == output_expectations["Content-Length"]

    # audio comparison part
    with open(os.path.join("golden_audios", "test_specific_check_russian_wav_content.wav"), "rb") as f_golden:
        golden_content = f_golden.read()
    assert golden_content == response.content


# check the missing api key errors
def test_negative_missing_api_key(get_test_cases, get_req_class_obj):
    # get the command arguments of current test
    current_test_case = get_test_cases["test_negative_missing_api_key"]
    input_fields = current_test_case["input_fields"]
    output_expectations = current_test_case["output_expectations"]

    # run the request
    response = get_req_class_obj.send_request(api_key=input_fields["api_key"], src_text=input_fields["src_text"], content_language=input_fields["content_language"], speech_voice=input_fields["speech_voice"], speech_rate=input_fields["speech_rate"], audio_codec=input_fields["audio_codec"], audio_format= input_fields["audio_format"], ssml= input_fields["ssml"], out_str_format= input_fields["out_str_format"])

    # check the status code, content type and error message
    assert response.status_code == output_expectations["status_code"]
    assert response.headers["Content-Type"] == output_expectations["Content-Type"]
    assert response.text == output_expectations["error_text"]


# check the invalid api key errors
def test_negative_invalid_api_key(get_test_cases, get_req_class_obj):
    # get the command arguments of current test
    current_test_case = get_test_cases["test_negative_invalid_api_key"]
    input_fields = current_test_case["input_fields"]
    output_expectations = current_test_case["output_expectations"]

    # run the request
    response = get_req_class_obj.send_request(api_key=input_fields["api_key"], src_text=input_fields["src_text"], content_language=input_fields["content_language"], speech_voice=input_fields["speech_voice"], speech_rate=input_fields["speech_rate"], audio_codec=input_fields["audio_codec"], audio_format= input_fields["audio_format"], ssml= input_fields["ssml"], out_str_format= input_fields["out_str_format"])

    # check the status code, content type and error message
    assert response.status_code == output_expectations["status_code"]
    assert response.headers["Content-Type"] == output_expectations["Content-Type"]
    assert response.text == output_expectations["error_text"]


# check the inactive account error, here is used key of non-active account
def test_negative_inactive_account(get_test_cases, get_req_class_obj):
    # get the command arguments of current test
    current_test_case = get_test_cases["test_negative_inactive_account"]
    input_fields = current_test_case["input_fields"]
    output_expectations = current_test_case["output_expectations"]

    # run the request
    response = get_req_class_obj.send_request(api_key=input_fields["api_key"], src_text=input_fields["src_text"], content_language=input_fields["content_language"], speech_voice=input_fields["speech_voice"], speech_rate=input_fields["speech_rate"], audio_codec=input_fields["audio_codec"], audio_format= input_fields["audio_format"], ssml= input_fields["ssml"], out_str_format= input_fields["out_str_format"])

    # check the status code, content type and error message
    assert response.status_code == output_expectations["status_code"]
    assert response.headers["Content-Type"] == output_expectations["Content-Type"]
    assert response.text == output_expectations["error_text"]


# check the subscription expired error
def test_negative_subcription_expired(get_test_cases, get_req_class_obj):
    # get the command arguments of current test
    current_test_case = get_test_cases["test_negative_subcription_expired"]
    input_fields = current_test_case["input_fields"]
    output_expectations = current_test_case["output_expectations"]

    # run the request
    response = get_req_class_obj.send_request(api_key=input_fields["api_key"], src_text=input_fields["src_text"], content_language=input_fields["content_language"], speech_voice=input_fields["speech_voice"], speech_rate=input_fields["speech_rate"], audio_codec=input_fields["audio_codec"], audio_format= input_fields["audio_format"], ssml= input_fields["ssml"], out_str_format= input_fields["out_str_format"])
    
    # check the status code, content type and error message
    assert response.status_code == output_expectations["status_code"]
    assert response.headers["Content-Type"] == output_expectations["Content-Type"]
    assert response.text == output_expectations["error_text"]


# check the missing text
def test_negative_missing_text(get_test_cases, get_req_class_obj):
    # get the command arguments of current test
    current_test_case = get_test_cases["test_negative_missing_text"]
    input_fields = current_test_case["input_fields"]
    output_expectations = current_test_case["output_expectations"]

    # run the request
    response = get_req_class_obj.send_request(api_key=input_fields["api_key"], src_text=input_fields["src_text"], content_language=input_fields["content_language"], speech_voice=input_fields["speech_voice"], speech_rate=input_fields["speech_rate"], audio_codec=input_fields["audio_codec"], audio_format= input_fields["audio_format"], ssml= input_fields["ssml"], out_str_format= input_fields["out_str_format"])
    
    # check the status code, content type and error message
    assert response.status_code == output_expectations["status_code"]
    assert response.headers["Content-Type"] == output_expectations["Content-Type"]
    assert response.text == output_expectations["error_text"]


# check a not supported language
def test_negative_not_supported_language(get_test_cases, get_req_class_obj):
    # get the command arguments of current test
    current_test_case = get_test_cases["test_negative_not_supported_language"]
    input_fields = current_test_case["input_fields"]
    output_expectations = current_test_case["output_expectations"]

    # run the request
    response = get_req_class_obj.send_request(api_key=input_fields["api_key"], src_text=input_fields["src_text"], content_language=input_fields["content_language"], speech_voice=input_fields["speech_voice"], speech_rate=input_fields["speech_rate"], audio_codec=input_fields["audio_codec"], audio_format= input_fields["audio_format"], ssml= input_fields["ssml"], out_str_format= input_fields["out_str_format"])
   
    # check the status code, content type and error message
    assert response.status_code == output_expectations["status_code"]
    assert response.headers["Content-Type"] == output_expectations["Content-Type"]
    assert response.text == output_expectations["error_text"]


# check the missing language
def test_negative_missing_language(get_test_cases, get_req_class_obj):
    # get the command arguments of current test
    current_test_case = get_test_cases["test_negative_missing_language"]
    input_fields = current_test_case["input_fields"]
    output_expectations = current_test_case["output_expectations"]

    # run the request
    response = get_req_class_obj.send_request(api_key=input_fields["api_key"], src_text=input_fields["src_text"], content_language=input_fields["content_language"], speech_voice=input_fields["speech_voice"], speech_rate=input_fields["speech_rate"], audio_codec=input_fields["audio_codec"], audio_format= input_fields["audio_format"], ssml= input_fields["ssml"], out_str_format= input_fields["out_str_format"])
    
    # check the status code, content type and error message
    assert response.status_code == output_expectations["status_code"]
    assert response.headers["Content-Type"] == output_expectations["Content-Type"]
    assert response.text == output_expectations["error_text"]


# check the ssml true option
def test_negative_ssml_subscription(get_test_cases, get_req_class_obj):
    # get the command arguments of current test
    current_test_case = get_test_cases["test_negative_ssml_subscription"]
    input_fields = current_test_case["input_fields"]
    output_expectations = current_test_case["output_expectations"]

    # run the request
    response = get_req_class_obj.send_request(api_key=input_fields["api_key"], src_text=input_fields["src_text"], content_language=input_fields["content_language"], speech_voice=input_fields["speech_voice"], speech_rate=input_fields["speech_rate"], audio_codec=input_fields["audio_codec"], audio_format= input_fields["audio_format"], ssml= input_fields["ssml"], out_str_format= input_fields["out_str_format"])
    
    # check the status code, content type and error message
    assert response.status_code == output_expectations["status_code"]
    assert response.headers["Content-Type"] == output_expectations["Content-Type"]
    assert response.text == output_expectations["error_text"]
