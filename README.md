
---

```markdown
# 📄 PubMed Paper Fetcher 📄🔬  
A Python tool to **fetch research papers from PubMed**, classify author affiliations, and summarize papers using **Google Gemini API**.  

## 🚀 Features  
✅ Fetches **PubMed research papers** using `Biopython` (Entrez API).  
✅ Uses **Google Gemini AI** to classify **Academic vs. Industry** affiliations.  
✅ Summarizes papers in **simple terms**.  
✅ Saves results to a **CSV file**.  
✅ CLI with **debug mode, file output, and rate-limiting**.  

## 📌 Installation  
```bash
pip install poetry  
git clone https://github.com/YOUR_GITHUB_USERNAME/Pubmed.git  
cd pubmed  
poetry install  
```

## 📌 Configuration  
1. **Get API Key** → [Google AI Studio](https://aistudio.google.com/).  
2. **Set API Key:**  
   - **Windows:** `set GEMINI_API_KEY=your_api_key`  
   - **macOS/Lin** `export GEMINI_API_KEY="your_api_key"ux:`  

## 📌 Usage  
🔹 **Fetch papers & save to CSV:**  
```bash
poetry run get-papers-list "brain tumor" -f results.csv
```
🔹 **Run without saving (print to terminal):**  
```bash
poetry run get-papers-list "COVID-19 vaccine"
```
🔹 **Enable Debug Mode:**  
```bash
poetry run get-papers-list "Alzheimer's treatment" -d
```

## 📌 CLI Options  
| Option | Description |  
|--------|------------|  
| `-h, --help` | Show usage instructions |  
| `-d, --debug` | Enable debug mode |  
| `-f, --file` | Save output to a CSV file |  

## 📌 Project Structure  
```
📂 PubMed-Paper-Fetcher/
│── 📂 pubmed/                # Main application folder
│   ├── cli.py               # Command-line interface
│   ├── pubmed_main.py       # Fetch & process PubMed papers
│   ├── gemini.py            # Google Gemini API integration
│   ├── utils.py             # CSV file handling
│── .gitignore               # Ignore unnecessary files
│── pyproject.toml           # Poetry dependencies
│── README.md                # Project documentation
```

## 📌 Example Output (`results.csv`)  
| PubmedID | Title | Publication Date | Non-Academic Author(s) | Company Affiliation(s) | Corresponding Author Email |  
|----------|-------|------------------|------------------------|------------------------|--------------------------|  
| 39512184 | Bridging the gap: unlocking the potential of emerging drug therapies for brain | 2025 Mar 6 | John Doe | Pfizer Inc. | johndoe@pfizer.com |  


This project is **MIT Licensed**. See [LICENSE](LICENSE) for details.  
```

---

### **📌 How to Use This**
✅ Copy and **paste this directly into `README.md`** in your project folder.  
✅ Commit and **push it to GitHub**:  
```bash
git add README.md  
git commit -m "Added README file"  
git push origin main  
```
