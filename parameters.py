#################################################################################
class parameters:
    def __init__(self, f, v=False):
        self.verbose = v
        self.fileName = f
        self.values = {}
        self.types  = {}

        try:
            self.file = open(self.fileName, "r")
            if ( self.verbose ):
                print("%s loaded" % self.fileName)

        except FileNotFoundError:
            print ("No such file %s" % self.fileName)
        pass

        for l in self.file:
            # Clean up the line, removing any extraneous characters
            line = l.rstrip()

            if len(line) <= 0:
                continue

            if line[0] == '#':
                continue

            try:
                index = line.index('#')
                line = line[:index]
            except ValueError:
                pass

            line = line.strip()
            if ( len(line) <= 0 ):
                continue

            line = line.replace("\t"," ")
            line = line.replace("  ","")
            line = line.replace("=","")

            # Split the line into its components
            p     = line.split(" ")
            type  = p[0].strip().lower()
            index = p[1].strip().upper()
            value = p[len(p)-1].strip()

            # Handle empty values
            if ( index == value ) :
                if ( type == "int" or type == "long" ) :
                    value = 0
                elif ( type == "float" or type == "double" ) :
                    value = 0.0
                elif ( type == "string" ) :
                    value = ''
                elif ( type == "bool" ) :
                    value = 0
                    
            # Store the values (appropriately typed) in the dictionary by index keyword
            if ( type == "int" or type == "long" ) :
                self.values[index] = int(value)
            elif ( type == "float" or type == "double" ) :
                self.values[index] = float(value)
            elif ( type == "string" ) :
                self.values[index] = value
            elif ( type == "bool" ) :
                if ( value.lower == "true" or value == 1 ) :
                    self.values[index] = True
                else :
                    self.values[index] = False

            self.types[index]  = type

        self.file.close()
        pass

    def set_value_by_index(self, index, value):
        type = self.types[index]
        # Store the values (appropriately typed) in the dictionary by index keyword
        if ( type == "int" or type == "long" ) :
            self.values[index] = int(value)
        elif ( type == "float" or type == "double" ) :
            self.values[index] = float(value)
        elif ( type == "string" ) :
            self.values[index] = value
        elif ( type == "bool" ) :
            if ( value.lower == "true" or value == 1 ) :
                self.values[index] = True
            else :
                self.values[index] = False
        pass

    def set_value(self, type, index, value):
        # Store the values (appropriately typed) in the dictionary by index keyword
        if ( type == "int" or type == "long" ) :
            self.values[index] = int(value)
        elif ( type == "float" or type == "double" ) :
            self.values[index] = float(value)
        elif ( type == "string" ) :
            self.values[index] = value
        elif ( type == "bool" ) :
            if ( value.lower == "true" or value == 1 ) :
                self.values[index] = True
            else :
                self.values[index] = False
                
        self.types[index]  = type
        pass    

    def check_index(self, index):
        try:
            value = self.values[index.upper()]
            return True
        except KeyError:
            return False
        pass

    def get_value_by_index(self,index):
        try:
            return self.values[index.upper()]
        except KeyError:
            print ("Uknown index %s" %index.upper())
            return None
        pass

    def dump_values(self):
        print(self.values)
        print(self.types)
        pass
    pass
############################ End Class parameters #############################
