let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {

            responseJson = JSON.parse(xhttp.responseText);

            document.getElementById("system_response").innerHTML = 
            "Anger: " + responseJson["anger"] + " <br>" +
            "Disgust: " + responseJson.disgust + " <br>" +
            "Fear: " + responseJson.fear + " <br>" +
            "Joy: " + responseJson.joy + " <br>" +
            "Sadness: " + responseJson.sadness + " <br>" +
            "Dominant emotion: " + responseJson.dominant_emotion + " <br>";
            //{'anger': 0.03176603, 'disgust': 0.023066374, 'fear': 0.33919972, 'joy': 0.23857419, 'sadness': 0.2719701, 'dominant_emotion': ['fear'], 'status_code': 200}
        } else if (this.status == 400) {
            document.getElementById("system_response").innerHTML = "¡Texto inválido! ¡Por favor, inténtalo de nuevo!";
        } else {
            document.getElementById("system_response").innerHTML = "Error interno";
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze"+"="+textToAnalyze, true);
    xhttp.send();
}
