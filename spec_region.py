# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 19:21:35 2016

@author: marckelsonsilva

Given a wavelength range as a list or tuple, clip the spectra to this range

Example: wave, flux = spec_region(wavelength, flux, (5500, 6500))

It will provide the spectrum for the specific region desired.
"""

import numpy as np

# Function to extract a specific region of a spectrum
def spec_region01(wave, flux, error, wl_range):
    # Unpack the wavelength range into lower and upper bounds
    lower, upper = wl_range
    
    # Iterate over the wavelength array
    for i in range(len(wave)):
        # Find the indices where the wavelength is within the specified range
        inds = np.where((wave > lower) & (wave < upper))
        
        # Extract the wavelengths, fluxes, and errors within the specified range
        wlv = wave[inds]
        fl = flux[inds]
        err = error[inds]
    
    # Return the extracted wavelengths, fluxes, and errors
    return wlv, fl, err

# Function to extract a specific region of a spectrum (similar to spec_region01 but without error)
def spec_region02(wave, flux, wl_range):
    # Unpack the wavelength range into lower and upper bounds
    lower, upper = wl_range
    
    # Iterate over the wavelength array
    for i in range(len(wave)):
        # Find the indices where the wavelength is within the specified range
        inds = np.where((wave > lower) & (wave < upper))
        
        # Extract the wavelengths and fluxes within the specified range
        wlv = wave[inds]
        fl = flux[inds]
    
    # Return the extracted wavelengths and fluxes
    return wlv, fl