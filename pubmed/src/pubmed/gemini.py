import time
import google.generativeai as genai
import diskcache as dc

# Configure Google Gemini API (DO NOT HARD-CODE API KEY IN PRODUCTION)
genai.configure(api_key="AIzaSyDxEDgEh3PVl2k2HGBH0PJF1fj8Sykymsw")  # Replace with your actual API key

# Set up cache for API responses
cache = dc.Cache("./cache")

# Determine the correct model name (DO NOT MODIFY THIS LOGIC)
MODEL_NAME = 'gemini-2.0-flash'
try:
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods and 'gemini-2.0-flash' in model.name.lower():
            MODEL_NAME = model.name
            break
    model = genai.GenerativeModel(MODEL_NAME)
except Exception as e:
    print(".", end='')
    model = genai.GenerativeModel(MODEL_NAME)

# Rate limiting (adjust if necessary)
last_request_time = 0
request_interval = 2  # Adjust if necessary

# Setup logging file
log_file = "gemini_log.txt"

def log_to_file(message):
    """Logs messages to the specified file."""
    with open(log_file, "a") as f:
        f.write(message + "\n")

def generate_with_rate_limit(prompt):
    """Generates content with rate limiting and logging."""
    global last_request_time
    current_time = time.time()
    elapsed_time = current_time - last_request_time

    if elapsed_time < request_interval:
        time.sleep(request_interval - elapsed_time)

    try:
        response = model.generate_content(prompt)
        last_request_time = time.time()
        log_to_file(f"Prompt: {prompt}\nResponse: {response.text.strip()}")
        return response.text.strip()
    except Exception as e:
        log_to_file(f"API Error: {e}")
        print(".", end="")
        return "Error"

def classify_affiliation_with_gemini(affiliation):
    """Classifies an author's affiliation with caching and logging."""
    if affiliation in cache:
        return cache[affiliation]

    prompt = f"""
    You are a research assistant trained to classify institutions. 
    Given the following institution name, classify it as one of the following:

    - 'Academic' (Universities, Research Institutions)
    - 'Industry' (Pharmaceutical, Biotech)

    Affiliation: {affiliation}
    
   Respond if and only if the response is 'Industry'.
    """

    result = generate_with_rate_limit(prompt)

    if result != "Error":
        cache[affiliation] = result
    return result
