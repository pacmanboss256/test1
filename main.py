from src.data import saveData, loadData, makeData
from figures.viz import makeFigure

def main():
    data = makeData()
    saveData(data,'test1.npy')
    makeFigure(data, 'testfig.svg')

if __name__ == "__main__":
    main()
