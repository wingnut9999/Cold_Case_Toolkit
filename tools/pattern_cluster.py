from collections import defaultdict

def pattern_cluster(dates):
    clusters = defaultdict(list)
    for date in dates:
        parts = date.split('-')
        if len(parts) == 3:
            month_day = f"{parts[1]}-{parts[2]}"
            clusters[month_day].append(date)
    return dict(clusters)
