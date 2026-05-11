import os
import json
import re
import subprocess
import shutil
import ollama

MAX_RETRIES = 5
MODEL_NAME = 'gemma4:e4b'

# Target JSON to test on
TEST_JSON_FILE = "scraped_json/cmc-index.json"
TEMP_SCRIPT_FILE = "temp_generated_script.py"
OUTPUT_DIR = "generated_endpoints"
SUCCESS_DIR = "llm_successful_scripts"

def get_json_sample(filepath, max_chars=4000):
    with open(filepath, 'r') as f:
        content = f.read()
    return content[:max_chars]

def get_reference_code():
    with open("fast_json_splitter.py", "r") as f:
        return f.read()

def call_llm(prompt):
    print(f"\n[Auto-Coder] Sending prompt to {MODEL_NAME}...")
    try:
        response = ollama.generate(
            model=MODEL_NAME, 
            prompt=prompt
        )
        return response['response']
    except Exception as e:
        print(f"[Auto-Coder] Error calling LLM: {e}")
        return None

def extract_python_code(text):
    # Regex to find python code blocks
    pattern = r"```python\n(.*?)\n```"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1)
    
    # Fallback to any code block
    pattern_fallback = r"```\n(.*?)\n```"
    match_fallback = re.search(pattern_fallback, text, re.DOTALL)
    if match_fallback:
        return match_fallback.group(1)
        
    return text # If no blocks, assume raw text

def execute_script(script_path):
    print(f"[Auto-Coder] Executing {script_path}...")
    result = subprocess.run(
        ["python3", script_path], 
        capture_output=True, 
        text=True
    )
    return result

def main():
    if not os.path.exists(SUCCESS_DIR):
        os.makedirs(SUCCESS_DIR)
        
    json_sample = get_json_sample(TEST_JSON_FILE)
    reference_code = get_reference_code()
    
    # We enforce that the generated script only looks at ONE file and outputs to generated_endpoints
    initial_prompt = f"""You are an expert Python developer. 
Your goal is to write a Python script that parses a specific JSON file, recursively extracts API endpoints (which are dictionaries containing 'method' and 'path'), and saves them as individual Markdown files.

The target JSON file is `{TEST_JSON_FILE}`. The output directory should be `{OUTPUT_DIR}`.

Here is an example of what the script should look like and the logic you should follow:
```python
{reference_code}
```

However, you must adapt it so it ONLY parses `{TEST_JSON_FILE}` (do not loop over an entire directory).
Make sure to create the `{OUTPUT_DIR}` directory if it doesn't exist.

Here is a sample of the JSON you will be parsing:
```json
{json_sample}
```

Write the COMPLETE, fully working Python script. Only output the python code inside a ```python ``` markdown block.
"""

    current_prompt = initial_prompt
    
    for attempt in range(1, MAX_RETRIES + 1):
        print(f"\n================ Attempt {attempt} / {MAX_RETRIES} ================")
        
        # 1. Clean output dir
        if os.path.exists(OUTPUT_DIR):
            shutil.rmtree(OUTPUT_DIR)
            
        # 2. Get code from LLM
        llm_response = call_llm(current_prompt)
        if not llm_response:
            print("[Auto-Coder] Failed to get response from LLM.")
            break
            
        code = extract_python_code(llm_response)
        
        # 3. Save to temp script
        with open(TEMP_SCRIPT_FILE, 'w') as f:
            f.write(code.strip())
            
        # 4. Execute
        result = execute_script(TEMP_SCRIPT_FILE)
        
        # 5. Check results
        print(f"[Auto-Coder] Execution Return Code: {result.returncode}")
        if result.stdout:
            print(f"[Auto-Coder] stdout: \n{result.stdout.strip()}")
            
        success = False
        error_msg = ""
        
        if result.returncode != 0:
            error_msg = result.stderr.strip()
            print(f"[Auto-Coder] Script Error: \n{error_msg}")
        else:
            # Check if files were created
            if os.path.exists(OUTPUT_DIR) and len(os.listdir(OUTPUT_DIR)) > 0:
                files_created = os.listdir(OUTPUT_DIR)
                print(f"[Auto-Coder] Success! Created {len(files_created)} markdown files: {files_created}")
                success = True
            else:
                error_msg = f"The script ran without throwing a Python error, but no files were created in the `{OUTPUT_DIR}` directory."
                print(f"[Auto-Coder] Semantic Error: {error_msg}")
                
        # 6. Loop or Exit
        if success:
            final_path = os.path.join(SUCCESS_DIR, "final_generated_parser.py")
            shutil.copy(TEMP_SCRIPT_FILE, final_path)
            print(f"\n[Auto-Coder] Mission Accomplished! Final script saved to {final_path}")
            break
        else:
            if attempt == MAX_RETRIES:
                print(f"\n[Auto-Coder] Max retries reached. The model failed to generate a working script.")
                break
                
            print(f"\n[Auto-Coder] Requesting fix from LLM...")
            # Formulate the feedback prompt
            current_prompt = f"""You previously wrote a Python script, but it failed to run correctly.
Here is the code you wrote:
```python
{code}
```

Here is the error or issue that occurred when I executed it:
{error_msg}

Please fix the code and return the entire corrected Python script. Remember to ONLY output the python code inside a ```python ``` markdown block.
"""

if __name__ == "__main__":
    main()
