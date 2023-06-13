# Contrastive Learning for Practical Synthetic Data Generation Using Seasonal and Trend Representations
## Implementation
1. Download the datasets and place them in `CoST-main/datasets`
2. For training, run `pip install -r requirements.txt` on terminal followed by:
     * mendeley : `python -u train.py mendeley forecast_multivar --alpha 0.0005 --kernels 1 2 4 8 16 32 64 128 --max-train-length 201 --batch-size 128 --archive forecast_csv --repr-dims 320 --max-threads 8 --seed 2 --eval --epochs 400`
     * calce : `python -u train.py dataset4 forecast_dataset4 --alpha 0.0005 --kernels 1 2 4 8 16 32 64 128 --max-train-length 201 --batch-size 128 --archive forecast_csv_univar --repr-dims 320 --max-threads 8 --eval --epochs 400`
     * colab implementation [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HrudayR/CoST/blob/master/cost_contrastive.ipynb)
3. After training is completed, the results are stored in `CoST-main/training`
4. The results can be viwed by running [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HrudayR/CoST/blob/master/results.ipynb)

## Acknowledgments
We would like to thank the contributors of the original [CoST](https://github.com/salesforce/CoST) repository and the authors of the paper titled [CONTRASTIVE LEARNING OF DISENTANGLED SEASONAL-TREND REPRESENTATIONS FOR TIME SERIES FORECASTING](https://openreview.net/pdf?id=PilZY3omXV2)  
  
Additionally we would like to mention that the being used is sourced from:
1. [mendeley](https://data.mendeley.com/datasets/wykht8y7tg/1)
2. [calce](https://web.calce.umd.edu/batteries/data.htm)
  
  
 ## <span id="citelink">Citation</span>

```
@inproceedings{
    woo2022cost,
    title={Co{ST}: Contrastive Learning of Disentangled Seasonal-Trend Representations for Time Series Forecasting},
    author={Gerald Woo and Chenghao Liu and Doyen Sahoo and Akshat Kumar and Steven Hoi},
    booktitle={International Conference on Learning Representations},
    year={2022},
    url={https://openreview.net/forum?id=PilZY3omXV2}
}
```
