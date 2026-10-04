from fastmcp import FastMCP
from tools.diagnosis_tools import get_diagnosis
from tools.symptom_extractor import extract_symptoms
from tools.pubmed_fetcher import fetch_pubmed_articles_with_metadata
from tools.summarizer import summarize_text
mcp = FastMCP("medical disgnosis custom mcp")

@mcp.tool()
def full_medical_analysis(symptom_text):
        symptoms = extract_symptoms(symptom_text)
        diagnosis = get_diagnosis(symptoms)
        pwbmed_raw = fetch_pubmed_articles_with_metadata(" ".join(symptoms))
        summary = summarize_text(pwbmed_raw[:3000])
        return {
        "symptom":symptoms,
        "diabnosis":diagnosis,
        "pubmed_summary" :summary
        }
        
if __name__ == "__main__":
    # Run MCP server with stdio transport (required for Claude Desktop)
    mcp.run()

### Please create venv first and then excecute below steps
# 1) python -m venv mcp
# 2) .\mcp\Scripts\activate
# 3) pip install FastMCP==2.1.2
# 4) pip freeze > filename.txt
# 5) pip list
# 6) uv init .
# 7) uv add "mcp[cli]"
# 8) mcp install mcp_tools.py
# 9) to run Fast API for testing purpose uvicorn fastapi_app:app --reload --port 8080