from gpt4all import GPT4All
import json

llm = GPT4All("mistral-7b-instruct-v0.1.Q4_0.gguf")

FINANCIAL_METRICS_PROMPT = """
You are a senior financial analyst.
Your task: extract **all possible financial metrics** from the text below.
Be exhaustive — if a metric is mentioned anywhere, capture it, even if approximate.
Do not summarize; capture raw values.

Text:
{context}

Extract the following categories (add others if found):
- Revenue (total, per product, per region, YoY, QoQ)
- Profit (gross, operating, net)
- Expenses (cost of goods sold, operating expenses, R&D, marketing, interest)
- Margins (gross margin %, operating margin %, net margin %)
- Assets & liabilities (total, current, non-current)
- Cash flow (operating, investing, financing)
- Debt (short-term, long-term)
- Risks (financial, operational, market)
- Forecasts (next quarter, year, multi-year, guidance changes)
- Valuation metrics (P/E ratio, EPS, EBITDA, book value, market cap)
- Any other numeric or percentage KPI relevant to finance

Output JSON with this structure:
{{
  "revenue": [],
  "profit": [],
  "expenses": [],
  "margins": [],
  "assets_liabilities": [],
  "cash_flow": [],
  "debt": [],
  "risks": [],
  "forecasts": [],
  "valuation_metrics": [],
  "other": []
}}

Answer:
"""

def ask_local_llm(context: str) -> str:
    prompt = FINANCIAL_METRICS_PROMPT.format(context=context)
    output = llm.generate(prompt, max_tokens=1000)
    print("LLM raw output:", output)
    return output.strip()

def merge_metrics(metrics_list):
    merged = []
    seen = set()
    for m in metrics_list:
        key = (m.get('metric_name'), m.get('period'))
        if key not in seen:
            seen.add(key)
            merged.append(m)
    return merged
