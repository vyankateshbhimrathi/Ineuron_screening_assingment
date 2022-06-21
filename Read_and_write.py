import os
import logging as lg
lg.basicConfig(filename='logfiles', filemode='w', level=lg.INFO, format="%(asctime)s %(levelname)s %(message)s")


class File_operation():

    def __init__(self, filename, file_path):
        self.file_path = file_path
        self.file = filename


    def read_replace_content(self):
        """
        This function is for replacing the given text with another text.
        """

        try:
            lg.info('checking file exists in given path or not')
            if os.path.exists(self.file_path + self.file + '.txt'):
                with open(self.file + '.txt', 'r') as f:
                    lg.info('file opened successfully')
                    # reading the content from file
                    file_read = f.read()
                    # replacing the text
                    data = file_read.replace('placement', 'screening')
                    lg.info('again opening file in write mode to replace the content')
                with open(self.file + '.txt', 'w') as f:
                    # writing the date into the file
                    f.write(data)
                    lg.info('replacement of given text is completed')
                    f.close()
                    lg.info('file closed successfully')

        except Exception as e:
            lg.info('this error occurred : {}'.format(e))
            







file_object = File_operation('example', "C:/Users/admin/Documents/")
file_object.read_replace_content()

