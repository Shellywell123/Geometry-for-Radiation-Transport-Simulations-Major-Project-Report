from string import Template
import Target_Sphere as t
import numpy as np
import pybdsim

################################################################################

def run_gdml_spheres_same_slice_and_stack(min,max):
    
    """
        generate a .txt wth four lists of data, number of slices & runtimes,
        from a minimum and maxiumum number of slices and stacks
        """
    
    Meshing_ver = "New"
    
    for val in range(min,max+1):
        
        # create gdml
        t.Test(False,False,n_slice = val,n_stack = val)
        
        #make gmad
        f = open('Template.gmad','r')
        contents = f.read()
        f.close()
        template = Template(contents)
        d = {'value': str("gdml:../../GDMLs/"+Meshing_ver+"/Target_Sphere_"+str(val)+"_"+str(val)+".gdml")}
        rendered = template.substitute(d)
        gmadfilename = "GMADs/"+Meshing_ver+"/slice_"+str(val)+"_stack_"+str(val)+".gmad"
        f = open(gmadfilename, 'w')
        f.write(rendered)
        f.close()
        
        # use gmad and gdml to get root output
        pybdsim.Run.RunBdsim(gmadfilename,"root_outputs/"+Meshing_ver+"/"+str(val)+"_"+str(val))
        
        #load in root file to do analysis ...
        
        print "{}%".format(val-min+1//(max-min))

#################################################################################

run_gdml_spheres_same_slice_and_stack(10,100)
