import pyautogui
import pandas as pd
import time

pyautogui.PAUSE = 0.5 
tabela = pd.read_csv("produtos.csv") 

for linha in tabela.index:
    pyautogui.click(x=1723, y=418) 
    pyautogui.write(str(tabela.loc[linha, "codigo"])) 
    pyautogui.press("tab")
