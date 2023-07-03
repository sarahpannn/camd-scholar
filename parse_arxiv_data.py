import csv

in_path = "results.csv"

author_dict = {}

with open(in_path, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        author = row[0]
        if author not in author_dict: 
            author_dict[author] = 0
        author_dict[author] += 1
        
sorted_author_dict = sorted(author_dict.items(), key=lambda x: x[1], reverse=True)
        
out_path = "author_counts.csv"

with open(out_path, 'w') as f:
    writer = csv.writer(f)
    for key in sorted_author_dict:
        writer.writerow([key])
