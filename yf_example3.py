#Week 4 quiz
import os
import toolkit_config as cfg
import yf_example2
def qan_prc_to_csv(year):
    pth = os.path.join(cfg.DATADIR, 'qan_prc_2020.csv')
    yf_example2.yf_prc_to_csv(tic, pth, "2020-01-01", "2020-12-31")



if __name__ == "__main__":
    tic = 'QAN.AX'
    qan_prc_to_csv(2020)