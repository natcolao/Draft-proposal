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