import argparse
from pubmed.pubmed_main import fetch_and_filter_papers
from pubmed.utils import save_to_csv

def main():
    """Command-line interface for fetching PubMed papers."""
    parser = argparse.ArgumentParser(description="Fetch and filter PubMed research papers.")
    
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("-f", "--file", type=str, help="Output file name (default: print to console)")

    args = parser.parse_args()

    print(f"Fetching papers for query: {args.query}")

    # ✅ Enable Debug Mode (If Selected)
    if args.debug:
        print("🔍 Debug Mode: Enabled")

    papers = fetch_and_filter_papers(args.query)

    if not papers:
        print("No relevant papers found.")
        return

    if args.file:
        save_to_csv(papers, args.file)
        print(f"✅ Results saved to {args.file}")
    else:
        print("📄 Results:")
        for paper in papers:
            print(paper)

if __name__ == "__main__":
    main()
