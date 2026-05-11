import os
import json

def find_endpoints(data, endpoints_found):
    """
    Recursively searches the JSON data for objects that look like API endpoints.
    Usually they have 'method' and 'path' keys.
    """
    if isinstance(data, dict):
        # Check if this dict represents an endpoint
        if "method" in data and "path" in data and isinstance(data["method"], str):
            method = data["method"].upper()
            if method in ["GET", "POST", "PUT", "DELETE", "PATCH"]:
                endpoints_found.append(data)
                
        # Continue searching recursively
        for key, value in data.items():
            find_endpoints(value, endpoints_found)
            
    elif isinstance(data, list):
        for item in data:
            find_endpoints(item, endpoints_found)

def format_endpoint_to_markdown(endpoint):
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
    parameters = endpoint.get("parameters", [])
    if parameters and isinstance(parameters, list) and len(parameters) > 0:
        md += "### Parameters\n\n"
        for param in parameters:
            p_name = param.get("name", "Unknown")
            p_in = param.get("in", "")
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
    input_dir = "scraped_json"
    output_dir = "extracted_endpoints"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    files = sorted([f for f in os.listdir(input_dir) if f.endswith(".json")])
    print(f"Starting JSON parsing for {len(files)} files...")

    total_endpoints = 0

    for filename in files:
        filepath = os.path.join(input_dir, filename)
        with open(filepath, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print(f"Skipping {filename}: Invalid JSON")
                continue
                
        endpoints = []
        find_endpoints(data, endpoints)
        
        if endpoints:
            print(f"Found {len(endpoints)} endpoints in {filename}")
            total_endpoints += len(endpoints)
            
            for ep in endpoints:
                method, path, content = format_endpoint_to_markdown(ep)
                
                # Create a safe filename like GET_v1_cryptocurrency_info.md
                safe_path = path.strip("/").replace("/", "_").replace("{", "").replace("}", "")
                if not safe_path:
                    safe_path = "root"
                
                out_filename = f"{method}_{safe_path}.md"
                out_filepath = os.path.join(output_dir, out_filename)
                
                with open(out_filepath, 'w') as out_f:
                    out_f.write(content)
                    
    print(f"\nDone! Extracted a total of {total_endpoints} endpoints into '{output_dir}/'")

if __name__ == "__main__":
    main()
