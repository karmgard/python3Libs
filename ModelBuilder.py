from pywavefront import Wavefront
###############################################################################
class ModelBuilder:
    def __init__(self, f, v=False):
        self.x, self.y, self.z = 0.0,0.0,0.0
        self.phi, self.theta, self.alpha = 0.0,0.0,1.0
        self.verbose = v
        self.scene = None

        self.fileName = f
        self.name = f.split('/')[f.count('/')].rstrip(".obj")
        try:
            self.scene = Wavefront(self.fileName)

            if ( self.verbose ):
                print("%s loaded" % self.name)

        except FileNotFoundError:
            print ("No such file %s" % self.fileName)
        pass

    def dump_values(self):
        print("%s (x,y,z) = (%.1f, %.1f, %.1f)" % (self.name,self.x,self.y,self.z))
        print("(\u03C6,\u03B8,\u03B1) = (%.1f, %.1f, %.1f)" % 
              (self.phi,self.theta,self.alpha))

        # Iterate vertex data collected in each material
        for name, material in self.scene.materials.items():
            # Contains the vertex format (string) such as "T2F_N3F_V3F"
            # T2F, C3F, N3F and V3F may appear in this string
            #print(material.vertex_format)
            # Contains the vertex list of floats in the format described above
            #print(material.vertices)
            # Material properties
            #print(material.diffuse)
            #print(material.ambient)
            #print(material.texture)
            print("%s.alpha = %f" % (name,material.transparency))

        print()
        pass

    def get_filename(self):
        return self.fileName
        pass

    def get_scene(self):
        return self.scene
        pass

    def setAlpha(self, alpha):
        if ( alpha < 0 ):
            alpha = self.alpha

        for name,material in self.scene.materials.items():
            material.set_alpha(alpha)
            self.alpha = alpha
            pass
        
    def set_initial_values( self, values ):
        try:
            self.x     = float(values[0])
            self.y     = float(values[1])
            self.z     = float(values[2])
            self.phi   = float(values[3])
            self.theta = float(values[4])
            self.alpha = float(values[5])

            for name,material in self.scene.materials.items():
                material.set_alpha(self.alpha)
                pass
        except:
            print("Unable to set values for %s" % self.name)

        if ( self.verbose ):
            self.dump_values()
        pass
    pass
############################ End Class ModelBuilder ###########################
