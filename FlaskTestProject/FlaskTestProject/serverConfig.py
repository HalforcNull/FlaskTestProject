
class Config(object):
    DEBUG = True
    DB_HOSTNAME = 'localhost'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_DATABASE = 'dbo'
    ENV_RSCRIPT_RUNNING_ENV_PATH = 'C:/Program Files/R/R-3.4.1/bin/RScript.exe'
    ENV_REXE_ENV_PATH = 'C:/Program Files/R/R-3.4.1/bin/R.exe'
    ENV_SCRIPTFOLDER = 'C:/DemoScriptFolder/'
    ENV_INPUT_FILE_PATH = 'C:/DemoWorkingFolder/Inputs/'
    ENV_OUTPUT_FILE_PATH = 'C:/DemoWorkingFolder/Outputs/'
    CONFIG_ALLOWED_EXTENSIONS = set(['csv'])
    ENV_FILE_UPLOAD_FOLDER = 'C:/DemoWorkingFolder/Inputs/'
    ENV_FILE_PICKLE_FOLDER = 'C:/WebsiteData/Pickle/'
    ENV_FILE_BIOMODULE_FOLDER = 'C:/WebsiteData/Pickle/BioModule/'
    ENV_FILE_GTEX_GENE = 'C:/WebsiteData/Gene/GtexGene.txt'
