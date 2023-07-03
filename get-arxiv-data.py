import arxiv
import csv

search = arxiv.Search(
  query = "AGI",
  max_results = 100,
  sort_by = arxiv.SortCriterion.Relevance,
  sort_order = arxiv.arxiv.SortOrder.Descending
)

out_path = 'results.csv'

with open(out_path, 'a') as f:
  writer = csv.writer(f)
  for result in search.results():
    for author in result.authors:
      writer.writerow([author.name])

# for result in search.results():
#   print(result.title)