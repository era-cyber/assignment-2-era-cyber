from dip import *
import math

class CellCounting:
    def __init__(self):
        pass

    def blob_coloring(self, image):
        """Label connected components in the binary image."""
        labels = {}
        height, width = image.shape
        label_map = [[0]*width for _ in range(height)]
        next_label = 1
        parent = {}

        # First pass
        for r in range(height):
            for c in range(width):
                if image[r, c] == 255:
                    neighbors = []
                    if r > 0 and c > 0 and label_map[r-1][c-1] > 0:
                        neighbors.append(label_map[r-1][c-1])
                    if r > 0 and label_map[r-1][c] > 0:
                        neighbors.append(label_map[r-1][c])
                    if r > 0 and c < width-1 and label_map[r-1][c+1] > 0:
                        neighbors.append(label_map[r-1][c+1])
                    if c > 0 and label_map[r][c-1] > 0:
                        neighbors.append(label_map[r][c-1])

                    if not neighbors:
                        label_map[r][c] = next_label
                        parent[next_label] = next_label
                        next_label += 1
                    else:
                        min_label = min(neighbors)
                        label_map[r][c] = min_label
                        for lb in neighbors:
                            root_min = parent[min_label]
                            parent[lb] = root_min

        # Flatten parent links
        for lb in list(parent.keys()):
            while parent[lb] != parent[parent[lb]]:
                parent[lb] = parent[parent[lb]]

        # Build region pixel lists
        for r in range(height):
            for c in range(width):
                lb = label_map[r][c]
                if lb > 0:
                    root = parent[lb]
                    label_map[r][c] = root
                    labels.setdefault(root, []).append((r, c))

        return labels

    def compute_statistics(self, regions):
        """
        regions: dict {label: [(r,c), ...]}
        Returns stats dict {label: (area, (cx, cy))}
        """
        stats = {}
        for label, pixels in regions.items():
            area = len(pixels)
            if area < 15:
                continue
            sum_r = sum(p[0] for p in pixels)
            sum_c = sum(p[1] for p in pixels)
            cx = int(sum_c / area)
            cy = int(sum_r / area)
            print(f"Region: {label}, Area: {area}, Centroid: ({cy},{cx})")
            stats[label] = (area, (cx, cy))
        return stats

    def mark_image_regions(self, image, stats):
        """
        Annotate the binary image with labels and centroids.
        stats: dict {label: (area, (cx, cy))}
        """
        out_img = image.copy()
        for label, (area, (cx, cy)) in stats.items():
            putText(out_img, str(label), (cx, cy - 10), FONT_HERSHEY_SIMPLEX, 0.5, (255), 1)
            putText(out_img, str(area), (cx, cy + 10), FONT_HERSHEY_SIMPLEX, 0.5, (255), 1)
            putText(out_img, "*", (cx, cy), FONT_HERSHEY_SIMPLEX, 1, (255), 2)
        return out_img
