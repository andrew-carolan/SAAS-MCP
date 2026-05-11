import os
import json
from typing import Any, List, Dict

# --- Configuration ---
INPUT_FILE_PATH = "scraped_json/cmc-index.json"
OUTPUT_DIR = "generated_endpoints"
# -----------------------

def find_endpoints(data: Any, endpoints_found: List[Dict]):
    """
    Recursively searches the JSON data for objects that look like API endpoints.
    Endpoints are identified by having 'method' and 'path' keys,
    and the method being a standard HTTP verb.
    """
    if isinstance(data, dict):
        # 1. Check if this dict represents an endpoint
        # We must ensure the method is a string to check validity
        method = data.get("method")
        if isinstance(method, str):
            # Check if method is an allowed HTTP verb
            upper_method = method.upper()
            if upper_method in ["GET", "POST", "PUT", "DELETE", "PATCH"]:
                # We found a valid endpoint structure
                endpoints_found.append(data)
                
        # 2. Continue searching recursively through all values
        for value in data.values():
            find_endpoints(value, endpoints_found)
            
    elif isinstance(data, list):
        # Process lists by calling recursively on each item
        for item in data:
            find_endpoints(item, endpoints_found)

def format_endpoint_to_markdown(endpoint: Dict) -> tuple[str, str, str]:
    """Formats the extracted JSON endpoint data into a readable Markdown string."""
    method = endpoint.get("method", "UNKNOWN").upper()
    path = endpoint.get("path", "Unknown Path")
    summary = endpoint.get("summary", "")
    description = endpoint.get("description", "")
    
    md = f"# {method} {path}\n\n"
    if summary:
        md += f"**Summary:** {summary}\n\n"
    if description:
        md += f"**Description:** {description}\n\n"
        
    # Add parameters if they exist
    parameters = endpoint.get("parameters")
    if parameters and isinstance(parameters, list) and len(parameters) > 0:
        md += "### Parameters\n\n"
        for param in parameters:
            p_name = param.get("name", "Unknown")
            p_in = param.get("in", "")
            # Handle required status gracefully
            p_required = "Required" if param.get("required") else "Optional"
            p_desc = param.get("description", "")
            md += f"- **{p_name}** ({p_in}) - *{p_required}*: {p_desc}\n"
        md += "\n"
        
    # Dump the raw JSON for the rest of the details so nothing is lost
    md += "### Raw Data\n\n```json\n"
    md += json.dumps(endpoint, indent=2)
    md += "\n```\n"
    
    return method, path, md

def main():
    """
    Main execution function: loads the specified JSON file, extracts endpoints,
    and saves them as individual Markdown files.
    """
    
    # Check if the input file exists
    if not os.path.exists(INPUT_FILE_PATH):
        print(f"Error: Input file not found at {INPUT_FILE_PATH}")
        print("Please ensure 'scraped_json/cmc-index.json' exists.")
        return

    # Ensure the output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created output directory: {OUTPUT_DIR}")

    print(f"Loading data from {INPUT_FILE_PATH}...")

    try:
        with open(INPUT_FILE_PATH, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"Fatal Error: Could not decode JSON from {INPUT_FILE_PATH}. Check file integrity.")
        return
    except Exception as e:
        print(f"An unexpected error occurred reading the file: {e}")
        return
        
    
    total_endpoints = 0
    endpoints = []
    
    # 1. Find all endpoints recursively
    find_endpoints(data, endpoints)
    
    if not endpoints:
        print("Warning: No endpoints found matching the defined criteria (must have method/path).")
        return
    
    print(f"\n[INFO] Found {len(endpoints)} endpoints. Starting file generation...")
    
    # 2. Process and save each endpoint
    for i, ep in enumerate(endpoints):
        method, path, content = format_endpoint_to_markdown(ep)
        
        # Create a safe filename: remove leading/trailing slashes, replace slashes, braces, etc.
        # Example: /v1/users/{id} -> v1_users_id
        safe_path = path.strip("/").replace("/", "_").replace("{", "").replace("}", "")
        
        # Handle case where path might be empty or invalid
        if not safe_path:
            safe_path = "root"
        
        out_filename = f"{method}_{safe_path}.md"
        out_filepath = os.path.join(OUTPUT_DIR, out_filename)
        
        with open(out_filepath, 'w', encoding='utf-8') as out_f:
            out_f.write(content)
            
        total_endpoints += 1
        print(f"   - Successfully saved endpoint {i+1}/{len(endpoints)}: {out_filename}")
                    
    print("\n=========================================================")
    print(f"SUCCESS! Processed {len(endpoints)} endpoints.")
    print(f"All Markdown files saved to the '{OUTPUT_DIR}/' directory.")
    print("=========================================================")

if __name__ == "__main__":
    main()