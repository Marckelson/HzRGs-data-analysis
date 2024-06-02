# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 13:09:16 2015

@author: marckelsonsilva
"""

#import pylab
from astropy.io import fits
import scipy

# Function to convert pixel values to wavelengths
def pix2wave(specfilename, refpix_key = 'CRPIX1', refwave_key = 'CRVAL1', slope_key = 'CD1_1', Npix_key = 'NAXIS1'):
  # Open the FITS file
  specfile = fits.open(specfilename)
  
  # Get the header of the FITS file
  head = specfile[0].header
  
  # Get the reference pixel, wavelength, slope, and number of pixels from the header
  refpix = head[refpix_key]
  refwave = head[refwave_key]
  slope = head[slope_key]
  Npix = head[Npix_key]
  
  # Close the FITS file
  specfile.close()
  
  # Generate an array of pixel values from 1 to Npix
  t = scipy.arange(1, Npix + 1)
  
  # Calculate the wavelength for each pixel using the formula: wavelength = slope * (pixel - refpix) + refwave
  return slope * (t - refpix) + refwave

# Function to convert wavelengths to pixel values
def wave2pix(specfilename, wave, refpix_key = 'CRPIX1', refwave_key = 'CRVAL1', slope_key = 'CD1_1'):
  """
  Returns the pixel value at which the wavelength equals wave (most likely not an integer)
  """
  # Open the FITS file
  specfile = fits.open(specfilename)
  
  # Get the header of the FITS file
  head = specfile[0].header
  
  # Get the reference pixel, wavelength, and slope from the header
  refpix = head[refpix_key]
  refwave = head[refwave_key]
  slope = head[slope_key]
  
  # Close the FITS file
  specfile.close()
  
  # Calculate the pixel value using the formula: pixel = (wave - refwave) / slope + refpix
  return (wave - refwave) / slope + refpix

# Function to get the wavelength value at a given pixel
def getWaveValue(specfilename, pix, refpix_key = 'CRPIX1', refwave_key = 'CRVAL1', slope_key = 'CD1_1'):
  # Open the FITS file
  specfile = fits.open(specfilename)
  
  # Get the header of the FITS file
  head = specfile[0].header
  
  # Get the reference pixel, wavelength, and slope from the header
  refpix = head[refpix_key]
  refwave = head[refwave_key]
  slope = head[slope_key]
  
  # Close the FITS file
  specfile.close()
  
  # Calculate the wavelength value using the formula: wavelength = slope * (pixel - refpix) + refwave
  return slope * (pix - refpix) + refwave 