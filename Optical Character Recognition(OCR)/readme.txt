==================================================================================
1. 事件: 改動keras底層。 時間: 2019/11/22。 環境: python36

檔名:
C:\Users\user\Anaconda3\envs\python36\lib\site-packages\keras\engine\saving.py

敘述:
1.def load_weights_from_hdf5_group_by_name(_, _, skip_mismatch = False)
False 是預測值，改為True

2.改為True後，value仍為false，因此在1063行新增 skip_mismatch = True

理由:
1. Fucking foolly.Ku 的OCR遷移學習問題。

結論:
Working

2020/2/24

已修改回來
1.def load_weights_from_hdf5_group_by_name(_, _, skip_mismatch = False)
2.delete "2.改為True後，value仍為false，因此在1063行新增 skip_mismatch = True"
==================================================================================

