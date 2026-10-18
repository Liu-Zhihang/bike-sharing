# Efficiency and Equity of Multimodal Travel Between Public Transit and Bike-sharing

## Introduction:
This repository contains the code and intermediary data related to our paper titled **"Efficiency and equity of the multimodal travel between public transit and bike-sharing accounting for multiscale"**. You can access the paper [here](Manuscript/Manuscript.pdf).

## Abstract:
As a supplement to the existing public transit system, bike-sharing is considered an effective solution to the "first mile" and "last mile" of travel. While many stakeholders believe that multimodal travel between public transit and bike-sharing can improve urban accessibility and sustainability, few studies have assessed the impact of bike-sharing on existing public transportation systems in terms of efficiency and equality. This research uses three months of mobile phone location data and about 140 million bike-sharing trips (origin-destination, OD) data from Shenzhen, China, to analyze first mile and last mile bike-sharing multimodal travel and measure the impact of bike-sharing on the existing public transportation system in terms of efficiency and equality at different scales. The research finds that bike-sharing is less effective in improving the operational efficiency of urban public transport and creates new inequalities at both global and local scales of the urban public transport system. Bike-sharing is only effective in tiny areas of the city and specific modes (subway-bike-sharing) and does not benefit groups with low socioeconomic levels and those living in edge areas of the city. Improving the equity and accessibility of public transportation is a key factor towards promoting sustainable urban development, and the analysis of this study on multimodal travel efficiency and inequality of bike-sharing can provide helpful insights for future sustainable urban planning.

![Research Framework](Figures/Fig1_Research_framework.jpg)

## Visualization:
The interactive map is published at [zhihangliu.cn](https://zhihangliu.cn/projects/Sharingbike/Morning_bike_sharing.html). The same pages are in [`visualization/`](visualization/).

The original Kepler export was about 100MB per peak and often failed to open in a browser. `visualization/assets/data/features_data_morning.lite.json` (about 6MB) and `features_data_evening.lite.json` (about 4MB) keep the first-mile and last-mile OD flows, plus simplified metro and bus lines. Bus-stop points are omitted. The basemap is CARTO Dark Matter, so the page does not need a Mapbox token.

Preview locally from the repository root:

```bash
python -m http.server 8080
```

Then open `http://127.0.0.1:8080/visualization/Morning_bike_sharing.html`.

![Website Preview](website.gif)

## Data Source:
The shared bike data was collected from Shenzhen Open Data Platform, available [here](https://opendata.sz.gov.cn/). The data collection script can be found in [shared_bike_data_downloader.py](shared_bike_data_downloader.py).

## Note:
Additional analysis codes and intermediary process data will be made public upon the publication of the paper.
