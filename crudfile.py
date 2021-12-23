import json

# debut programme
class Crud:

    def __init__(self, namefile):
        self.namefile = namefile

    def lire(self):
        fichier = open(self.namefile, 'r')
        return fichier.read()

def convertJsonToDict(dataJson, cle):
    json_convert_dict = json.loads(dataJson)
    print(json_convert_dict[cle])
    
def main():
    crud = Crud('file_json.json')
    print(crud.lire())
    data_a_convert = crud.lire()
    convertJsonToDict(data_a_convert, 'glossary')


if __name__ == "__main__":
    main()
