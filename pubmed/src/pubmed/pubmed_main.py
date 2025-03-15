from Bio import Entrez
import re
from pubmed.gemini import classify_affiliation_with_gemini

# 🔹 Replace with your valid email (required for PubMed API requests)
Entrez.email = "kskapil287@gmail.com"

def fetch_and_filter_papers(query):
    """Fetches PubMed papers using Entrez, filters non-academic affiliations, and summarizes papers."""

    # 🔹 Step 1: Search PubMed for papers matching the query
    handle = Entrez.esearch(db="pubmed", term=query, retmax=20)
    record = Entrez.read(handle)
    handle.close()
    
    pubmed_ids = record.get("IdList", [])

    if not pubmed_ids:
        print("No papers found.")
        return []

    papers = []

    # 🔹 Step 2: Fetching details of each paper
    handle = Entrez.efetch(db="pubmed", id=pubmed_ids, rettype="medline", retmode="text")
    records = handle.read().split("\n\n")  # Split based on PubMed format
    handle.close()

    for record in records:
        lines = record.split("\n")
        pmid = title  = publication_date = "N/A"
        authors = []
        affiliations = []

        for line in lines:
            if line.startswith("PMID- "):
                pmid = line.replace("PMID- ", "").strip()
            elif line.startswith("TI  - "):
                title = line.replace("TI  - ", "").strip()
            elif line.startswith("DP  - "):
                publication_date = line.replace("DP  - ", "").strip()
            elif line.startswith("AU  - "):
                authors.append(line.replace("AU  - ", "").strip())
            elif line.startswith("AD  - "):
                affiliations.append(line.replace("AD  - ", "").strip())
        
        non_academic_authors = []
        company_affiliations = []
        corresponding_email = None

        # 🔹 Step 3: Use Gemini API to classify affiliations
        for author, affil in zip(authors, affiliations):
            classification = classify_affiliation_with_gemini(affil)
            if classification == "Industry":
                non_academic_authors.append(author)
                company_affiliations.append(affil)

            # 🔹 Extract email addresses from affiliations
            
            if "@" in affil:
                match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', affil)
                if match and not corresponding_email:
                    corresponding_email = match.group(0)
                    print(corresponding_email)
                
     

        # 🔹 Step 4: Store results
        papers.append({
            "PubmedID": pmid,
            "Title": title,
            "Publication Date": publication_date,
            "Non-academic Author(s)": ", ".join(non_academic_authors) or "N/A",
            "Company Affiliation(s)": ", ".join(company_affiliations) or "N/A",
            "Corresponding Author Email": corresponding_email or "N/A"
        })

    return papers
