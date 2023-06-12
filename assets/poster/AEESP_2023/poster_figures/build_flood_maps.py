import numpy as np
import contextily as cx
import rasterio
from rasterio.plot import show
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os
from matplotlib.colors import ListedColormap

def main():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    gpkg = "../data/analysis_data.gpkg"

    regions = {
        1: {"name": "burlington_davenport",
            "label": "Burlington, IA - Davenport, IA",
            "bbox": (-92, -89.5, 40, 42)
        },
        2: {"name": "paducah_cairo",
            "label": "Paducah, KY - Cairo, IL",
            "bbox": (-90, -87.5, 36, 38)
        }
    }

    for r in regions:
        # must import flood raster tifs before running.
        fl_path = f"../poster_data/d{r}_MEAN_past_100/FloodSpreader_DEP_d{r}_MEAN_past_100.tif"
        flood = rasterio.open(fl_path)

        w, e, s, n = regions[r]["bbox"]

        img, ext = cx.bounds2img(
            w, s, e, n, 
            ll = True, 
            source=cx.providers.CartoDB.Positron
        )
        img, ext = cx.warp_tiles(img, ext, "EPSG:4269")

        regions[r]["flood"] = flood
        regions[r]["img"] = img
        regions[r]["ext"] = ext

    cbar = mpl.colormaps["Blues"].resampled(256)
    cbar = ListedColormap(cbar(np.linspace(0.25, 0.95, 128)))
    cbar.set_under("#00000000")


    fig, (ax1, ax2) = plt.subplots(figsize=(10, 4), ncols = 2)

    ax1.imshow(regions[1]["img"], extent = regions[1]["ext"])
    show(regions[1]["flood"], ax = ax1, transform = regions[1]["flood"].transform, cmap = cbar, vmin = 0.1, vmax = 15)
    ax1.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax1.yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax1.xaxis.set_major_formatter("{x}\u00B0")
    ax1.yaxis.set_major_formatter("{x}\u00B0")
    ax1.set_xlim(regions[1]["bbox"][0], regions[1]["bbox"][1])
    ax1.set_ylim(regions[1]["bbox"][2], regions[1]["bbox"][3])
    ax1.set_title(f"{regions[1]['label']}", loc='left')

    ax2.imshow(regions[2]["img"], extent = regions[2]["ext"])
    show(regions[2]["flood"], ax = ax2, transform = regions[2]["flood"].transform, cmap = cbar, vmin = 0.1, vmax = 15)
    ax2.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax2.yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax2.xaxis.set_major_formatter("{x}\u00B0")
    ax2.yaxis.set_major_formatter("{x}\u00B0")
    ax2.set_xlim(regions[2]["bbox"][0], regions[2]["bbox"][1])
    ax2.set_ylim(regions[2]["bbox"][2], regions[2]["bbox"][3])
    ax2.set_title(f"{regions[2]['label']}", loc='left')

    fig.suptitle(
        f"100-year Flood Depth Maps",
        x = 0.123,
        y = .95,
        horizontalalignment="left",
        verticalalignment="top",
        fontweight='bold',
        color = "#003591"
    )

    

    fig.savefig(
        f"floods.png",
        bbox_inches = "tight"
    )

    print("Done")

if __name__ == "__main__":
    main()