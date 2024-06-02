# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 18:18:26 2015

@author: marckelson

Spectrum function aims to get the wavelength and flux from 2-dimensional/1-dimensional fits file or 
.csv, .txt or .dat data files.
To perform it one needs to set wave, flux = Spectrum("/path/specfilename"). If the fits file is a 2-dimensional spectrum 
one will need to provide the range of lines that must be summed. 
"""

import numpy as np
from astropy.io import fits
import getWave


def Spectrum(specfilename):
    """
    This function reads a spectrum from a FITS or ASCII file and returns the wavelength and flux.

    Parameters:
    specfilename (str): The path to the spectrum file. The file can be a FITS file or a.csv,.txt, or.dat file.

    Returns:
    tuple: A tuple containing two numpy arrays, wave and flux. wave represents the wavelength, and flux represents the corresponding flux values.

    Raises:
    FileNotFoundError: If the specified file does not exist.
    ValueError: If the file format is not supported.
    """

    # Check if the file is a FITS file
    if ".fits" in specfilename:      
        naxis_key = "NAXIS"
        naxis1_key = "NAXIS1"
        object_key = "OBJECT"
        arm_key = "HIERARCH ESO SEQ ARM"
        
        # Open the FITS file
        specfile = fits.open(specfilename)
        head = specfile[0].header
        
        # Get the dimensions of the data
        naxis1 = int(head[naxis1_key])
        naxis = int(head[naxis_key])
        
        # If the data is a 2-dimensional spectrum
        if naxis == 2:
            arm = head[arm_key]
            
            # If the spectrum is from the UVB or VIS arm
            if arm == 'UVB' or arm == 'VIS':
                num_spec = int(head[naxis1_key])
                
                # Get the wavelength using the getWave function
                global wave
                wave = getWave.pix2wave(specfilename) 
                
                # Get the flux by summing the specified lines
                spec = specfile[0].data
                global flux
                flux = spec[45:49,:].sum(axis=0)
                
            # If the spectrum is from the NIR arm
            else:
                num_spec = int(head[naxis1_key])
                
                # Get the wavelength using the getWave function
                wave = getWave.pix2wave(specfilename) 
                
                # Get the flux by summing the specified lines
                spec = specfile[0].data
                flux = spec[13:17,:].sum(axis=0)
                
            # Return the wavelength and flux
            return wave, flux
        
        # If the data is a 1-dimensional spectrum
        else:
            num_spec = 1 
            
            # Get the wavelength using the getWave function
            wave = getWave.pix2wave(specfilename)
            
            # Get the flux
            flux = specfile[0].data
            
            # Return the wavelength and flux
            return wave, flux
            
        # Print the object name if available
        if (object_key in head):
            print("Working with the object ",head[object_key])
            
    # Check if the file is an ASCII file
    if (".csv" in specfilename) or (".txt" in specfilename) or (".dat" in specfilename):
        
        # Load the ASCII data
        dataSpec = np.loadtxt(specfilename)
        
        # Get the wavelength and flux
        wave = dataSpec[:,0]
        flux = dataSpec[:,1]  
        
        # Return the wavelength and flux
        return wave, flux