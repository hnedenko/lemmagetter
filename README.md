# lemmagetter

An endpoint that receives an array of words (string) as input, turns the key-value dictionary, where the key is the word from the passed array, the value is the lemma of the word.

Accepts POST request link "host/lemmas/api/v1/getalllemmas"
Example:  
Request: {"words": ["best", "running"]}  
Response: {"lemmas": {"best": "good", "running": "run" }}

Implementing building with Docker: 
"docker-compose build"  
"docker run -it --rm -p 7666:8000 lemmagetter-web-app"

- English only
- If a specific word cannot be processed, it will simply pass it off as a lemma
- Error handling and cases of incorrect login are not performed in the current version