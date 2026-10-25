# Acknowledgements

The questions are thinkingtext's, exported from the cell registry of its news indexes. The per-read baselines shipped in each pack
(the mean and standard deviation of every read) are computed on public news; nothing is fitted on labels, on prices or on the
indexes' own article data, which is not part of this repository.

| data | use | terms |
|---|---|---|
| Wikinews articles (categories Economy and business, Energy, OPEC and the company categories, plus searches), `sources/calibration/wikinews_business.json.gz` | the calibration sample; the shipped `samples/inputs.json` of each pack, each article attributed with its title, URL and revision | CC BY 2.5 |

The illustrative articles in `sources/calibration/synthetic_samples.json` were written by thinkingtext for the companies Wikinews
rarely covers; they are marked as invented wherever they are used.
