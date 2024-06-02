# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 19:37:23 2016

@author: marckelson
"""

import numpy as np



def stats_spec(wa, fl, er, wa1, wa2, show=False):
        """Calculates statistics (mean, standard deviation (i.e. RMS), mean
        error, etc) of the flux between two wavelength points.

        Returns
        -------
        mean flux, RMS of flux, mean error, SNR:
           SNR = (mean flux / RMS)
        
        >>> wa = np.linspace(10,20,10)
        >>> np.random.seed(77)
        >>> fl = np.random.randn(len(wa)) + 10
        >>> er = np.ones(len(wa))
        >>> sp = Spectrum(wa=wa, fl=fl, er=er)
        >>> data = sp.stats(11, 18)
        >>> np.allclose(data, [9.66873, 0.98909, 1.0, 9.77542])
        True
        """
        # Search for the indices where the wavelength range wa1 to wa2 starts and ends in the array wa
        i,j = wa.searchsorted([wa1, wa2])
        # Extract the flux and error values within the specified wavelength range
        fl = fl[i:j]
        er = er[i:j]
    
        # Create a mask to select only the good data points (i.e., those with non-zero error and non-NaN flux)
        good = (er > 0) & ~np.isnan(fl)
    
        # If there are no good data points, print a message and return NaN values
        if len(good.nonzero()[0]) == 0:
            print('No good data in this range!')
            return np.nan, np.nan, np.nan, np.nan
    
        # Extract the good flux and error values
        fl = fl[good]
        er = er[good]
    
        # Calculate the mean flux
        mfl = fl.mean()
    
        # Calculate the standard deviation of the flux
        std = fl.std()
    
        # Calculate the mean error
        mer = er.mean()
    
        # Calculate the signal-to-noise ratio (SNR)
        snr = mfl / std
    
        # If show is True, print the calculated statistics with 2 digits after the decimal point.
        if show:
            print('mean {:.2f}, std {:.2f}, er {:.2f}, snr {:.2f}'.format(mfl, std, mer, snr))
    
        # Return the calculated statistics
        return mfl, std, mer, snr