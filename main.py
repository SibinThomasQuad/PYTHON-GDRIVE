from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth                                     = GoogleAuth()
drive                                     = GoogleDrive(gauth)
def upload()                              : 
    upload_file_list                      = ['a.png', 'b.png']
    for upload_file in upload_file_list   : 
        gfile                             = drive.CreateFile({'parents': [{'id': '1LlPvGOzoGW8vyO4EQc3z1dbhL6QzOAT4'}]})
        # Read file and set it as the content of this instance.
        gfile.SetContentFile(upload_file)
        gfile.Upload() # Upload the file.
def list()                                : 
    file_list                             = drive.ListFile({'q': "'{}' in parents and trashed=false".format('1LlPvGOzoGW8vyO4EQc3z1dbhL6QzOAT4')}).GetList()
    for file in file_list                 : 
	    print('title: %s, id: %s' % (file['title'], file['id']))
def download()                            : 
    file_list                             = drive.ListFile({'q': "'{}' in parents and trashed=false".format('1LlPvGOzoGW8vyO4EQc3z1dbhL6QzOAT4')}).GetList()
    for file in file_list                 : 
        file.GetContentFile(file['title'])
