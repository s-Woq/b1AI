from py_files.stabledif import CelebAPreprocessing 
from py_files.iter_img import processImages


def run():
    preprocessor=CelebAPreprocessing()
    processImages("./")
    






if __name__== "__main__":
    run()