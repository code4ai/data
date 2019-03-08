## Data Collection (Anonymized)

- As English Gigaword v5 requires copyright, we detail data processing procedure step by step. 
- Please download the raw data first from [here](https://catalog.ldc.upenn.edu/LDC2011T07) and follow our instruction to reproduce the data.

The seven distinct international sources of English newswire included in fifth edition are the following:

- Agence France-Presse, English Service (afp_eng)
- Associated Press Worldstream, English Service (apw_eng)
- Central News Agency of Taiwan, English Service (cna_eng)
- Los Angeles Times/Washington Post Newswire Service (ltw_eng)
- Washington Post/Bloomberg Newswire Service (wpb_eng)
- New York Times Newswire Service (nyt_eng)
- Xinhua News Agency, English Service (xin_eng) raw data should be like this:

After downloading, your raw data should be like this:

<img src="https://github.com/code4ai/data/blob/master/raw_data_folder.png" width="15%" height="15%">

In each folder, for example, in folder of New York Times Newswire Service (nyt_eng), the raw data should be like this:

<img src="https://github.com/code4ai/data/blob/master/nyt_raw_data.png" width="20%" height="20%">

Then, run the following (step 1):

`python 1_data_construction.py`

where it took seven folders as inputs, and output seven .txt documents (e.g., 2_raw_afp.txt, 2_raw_nyt.txt...).
Run the following (step 2):

`python 2_data_processing_server.py`

The output is seven .txt documents (e.g., 3_raw_afp.txt, 3_raw_nyt.txt...).

Finally, run the following (step 3):

`python 3_data_filter.py`

The output *final_data_14w.txt* contains 140,000 sentence groups as mentioned in paper. 
