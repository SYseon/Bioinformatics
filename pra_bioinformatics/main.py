from uiframe import *
import toexcel
import preprocess
import fselector
import classifier

def main():
    toexcel.excel_init()
    model = Model()
    root = Tk()
    root.geometry("800x550+100+100")
    app = MyFrame(root, model)
    app.mainloop()
    toexcel.set_value(preprocess.Preprocessor.alg_list, fselector.FSelector.alg_list, classifier.Classifier.alg_list, classifier.Classifier.accuracy)
    
    
if __name__ == '__main__':
    main()