from uiframe import *
import toexcel
import preprocess
import fselector
import classifier

def main():
    model = Model()
    root = Tk()
    root.geometry("800x550+100+100")
    app = MyFrame(root, model)
    app.mainloop()
   
    
if __name__ == '__main__':
    main()