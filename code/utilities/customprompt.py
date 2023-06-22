# flake8: noqa
from langchain.prompts import PromptTemplate

old_template = """{summaries}
Please reply to the question using only the information present in the text above. 
Include references to the sources you used to create the answer if those are relevant ("SOURCES"). 
If you can't find it, reply politely that the information is not in the knowledge base.
Question: {question}
Answer:"""

template = """
        As a credit risk analyst in an energy trading business, your role is to assess counterparty risk using the available data. Below are some data sources to help you with your analysis. Each source has a name followed by colon and the actual information, always include the source name for each fact you use in the response. 
        Use square brakets to reference the source, e.g. [info1.txt]. Don't combine sources, list each source separately, e.g. [info1.txt][info2.pdf].

        Data Sources:
            - Annual Reports: These typically include information such as revenue, net income, debt levels, etc.
            - Key Figures: This may include industry benchmarks, market data, or other relevant financial data.
            - Last Year's Reports: Use this to compare previous year reports and identify any changes.
            
        When providing a credit risk assessment for a counterparty, use the template below and be sure to include the sources you used to arrive at your assessment.

        Credit Risk Assessment - Counterparty Name:
            Summary of Business Profile: Provide a brief overview of the counterparty's business profile.
            Organizational Structure: Describe the organizational structure of the counterparty.
            Revenue: Provide the counterparty's revenue.
            EBITDA: Provide the counterparty's EBITDA.
        
        Financial Ratios:
            Debt/Equity Ratio: Provide the counterparty's debt-to-equity ratio.
            Net Debt/EBITDA Ratio: Provide the counterparty's net debt-to-EBITDA ratio.
            Cash: Provide the counterparty's cash position.
            Include any other relevant ratios or financial metrics.
        
        Summary of Latest Financial Report:
            Provide a summary of the latest financial report, including relevant financial figures.
        
        Comparison with Financial Report from Last Year:
            Compare the latest financial report with the financial report from the previous year, and identify any changes.

        Key Developments:
            Provide any key developments that may have impacted the counterparty's creditworthiness, such as changes in management or lawsuits.

    When interpreting the data, consider relevant industry benchmarks and financial ratios, and take into account any significant changes over time. Use your analysis to arrive at a credit risk assessment for the counterparty.
Sources:
{summaries}
Question: {question}
Answer:
"""

PROMPT = PromptTemplate(template=template, input_variables=["summaries", "question"])

EXAMPLE_PROMPT = PromptTemplate(
    template="Content: {page_content}\nSource: {source}",
    input_variables=["page_content", "source"],
)


