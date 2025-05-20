
def spore_suspension(stock_spore_density, desired_spore_density, total_medium_volume): 
    """
    Calculates the volume of spore suspension needed to inoculate a specific vessel to the desired spore density

    Parameters 
    ----------
    stock_spore_density : float 
        This is the concentration of the spore stock (spores/mL)
        
    desired_spore_density : float
        This is concentraiton of spores to be inoculation (spores/mL)
        
    total_medium_volume: float 
        This is the volume of the vessel to be inoculated (mL)

    Return 
    -------
    spore_suspension : float 
        This is the volume of the spore stock to be used for inoculation (spores/mL)
        
    required_medium_volume: float 
        This is amount of medium needed to dilute the spore stock (mL)
    """
    
    spore_suspension = (desired_spore_density * total_medium_volume) / stock_spore_density
    required_medium_volume = total_medium_volume - spore_suspension

    return(spore_suspension,required_medium_volume)



def beer_lampert_law(Io, a, z):
    """
    Calculates the attenuation of solar radiation for blue light at depth

    Parameters 
    ----------
    Io : float
        Irradiance at the surface (W/m^2)

    a : float 
        Attenuation coefficient (m^-1)

    z : float 
        Depth (m)

    Return
    ------
    I : float 
        Irradiance at depth (W/m^2)
    """
    import numpy as np
    I = Io * np.exp(-a*z)

    return(I)
    

    
        
        
    