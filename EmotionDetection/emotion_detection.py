from flask import Flask, request
import requests

def emotion_detector(text_to_analyze):
    if type(text_to_analyze) is not str or text_to_analyze.strip() == '':
        return {
        "anger": None, 
        "disgust": None, 
        "fear": None, 
        "joy": None, 
        "sadness": None, 
        "dominant_emotion": None,
        "status_code": 400
        }

    try: 

        url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        input_json= { "raw_document": { "text": text_to_analyze } }
        response = requests.post(
        url, 
        json=input_json, 
        headers=headers
        )

        # return response.json()

        response_json = response.json()

        final_response = response_json["emotionPredictions"][0]["emotion"]
        domain = max(
            final_response['anger'],
            final_response['disgust'],
            final_response['fear'],
            final_response['joy'],
            final_response['sadness']
            )
        domain_emotion = [key for key, value in final_response.items() if value == domain]
        final_response['dominant_emotion'] = domain_emotion[0]
        final_response["status_code"] = 200

        return final_response
    except KeyError:
        return {
        "status_code": 400
        }
    except:
       return {
        "status_code": 500
        } 


print(emotion_detector("I love this new technology."))