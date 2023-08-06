# David THERINCOURT - 2022
#
# The MIT License (MIT)
#
# Copyright (c) 2014-2019 Damien P. George
# Copyright (c) 2017 Paul Sokolovsky
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
Module pour le traitement des signaux.

Example
-------

from physique.signal import load_oscillo_csv, periode
t, u = load_oscillo_csv('scope.csv')
T = periode(t, u)
        
@author: David Thérincourt - 2022
"""

import numpy as np
from scipy.integrate import trapz
from numpy.fft import fft


def _autocorrelation(y, N, i, M):
    """
    Fonction d'autocorrélation d'un signal y.
    
    Parameters
    ----------
    y : numpy.ndarray
        Signal
    N : int
        Nombre de point de la fonction d'autocorrélation
    i : int
        Indice départ (i>N)
    M : int
        Nombre de points de la fonction d'autocorrélation
        
    Returns
    -------
    c : numpy.ndarray
        Fonction d'autocorrélation
    """
    C = np.zeros(N)
    for k in range(i,i+M):
        for n in range(N):
            C[n] += y[k]*y[k-n]
    return C


def periode(t, y, draw_period_ax=None, draw_period_start=None, draw_period_color="linen"):
    """ Renvoie le période T du signal périodique y(t) par une méthode d'autocorrélation.
    Le signal y(t) doit comporter au moins deux motifs.
    Un nombre important de motifs peut donner des erreurs !
    
    Parameters
    ----------
    t : numpy.ndarray
        Tableau des temps.

    y : numpy.ndarray
        Tableau des valeurs du signal.

    draw_period_ax  : matplotlib.axes, optionnel (None par défaut)
        Repère (axes) pour dessiner la période.

    draw_period_start : float, optionnel (None par défaut)
        Abscisse de début pour dessiner la période.

    draw_period_color : matplotlib color, optionnel ("linen" par défaut)
        Couleur pour dessiner la période.
        
    Return
    -------
    T : float
        Valeur de la période calculée.
    """

    Te = t[1]-t[0]             # Période d'échantillonnage
    Ns = len(t)                # Nb points total
    N = Ns//2                  # Nb points pour autocorrélation = moitié
    tau = t[0:N]               # Retard de la fonction d'autocorrélation
    
    c = _autocorrelation(y, N, N, Ns-N)
    
    na = N//100                              # On saute les premiers indices (10%) pour la recherche du prochain maximum !
    c_max = np.max(c[na:])                   # Maximum de c
    Np = na + np.where(c[na:]==c_max)[0][0]  # Recherche indice (premier) maximum
    T = Np*Te                                # Calcul de la période
    
    if draw_period_start == None:
        draw_period_start = t[0]
        
    if draw_period_ax != None:
        draw_period_ax.axvspan(draw_period_start, draw_period_start+T , color=draw_period_color)
        
    return T



def integre(x, y, xmin, xmax, plot_ax=None):
    """ Calcule numériquement l'intégrale de la fonction y=f(x) entre
    les bornes xmin et xmax avec la méthode des trapèzes.
    
    Parameters
    ----------
    x : numpy.ndarray
        Tableau Numpy des x.

    y : numpy.ndarray
        Tableau Numpy des y.
    xmin : float
        Borne inférieure pour l'intégration.

    xmax : float
        Borne supérieure pour l'intégration.

    plot_ax : matplotlib.axes, optionnel (None par défaut)
        Repère (axes) sur lequel tracé l'aire de l'intégration.
        
    Return
    ------
    aire : float
        Résultat de l'intégration.
    """

    if (xmin<x[0]) or (xmin>x[-2]):
        raise ValueError("Valeur de xmin en dehors de l'intervalle de x")
    if (xmax<x[1]) or (xmax>x[-1]):
        raise ValueError("Valeur de xmax en dehors de l'intervalle de x")
    if xmin>=xmax:
        raise ValueError("Valeur de xmin supérieure à la valeur de xmax")
    
    y = y[(x >= xmin) & (x < xmax)]  # Sélection sur une période
    x = x[(x >= xmin) & (x < xmax)]  # Sélection sur une période
    
    if plot_ax != None:
        plot_ax.fill_between(x,y,hatch='\\',facecolor='linen',  edgecolor='gray')
        
    return trapz(y)*(x[-1]-x[0])/len(x)




def spectre_amplitude(t, y, T, tmin=0, plot_period_ax=None):
    ''' Retourne le spectre d'amplitude d'un signal y(t).
    
    Parameters
    ----------
    t : numpy.ndarray
        Tableau des temps.

    y : numpy.ndarray
        Tableau des valeurs du signal.

    T : float
        Période du signal.

    tmin : float, optionnel (0 par défaut)
        Borne inférieure le calcul du spectre.

    plot_period_ax : matplotlib.axes, optionnel (None par défaut)
        Repère (axes) sur lequel tracer la sélection de la période.
        
    Return
    ------
    (f, A) : (numpy.ndarray, numpy.ndarray)
        Tableaux des fréquences et des amplitudes.
    '''
    
    if T>(t[-1]-t[0]):
        raise ValueError("Période T trop grande")
    
    if (tmin<t[0]) or (tmin>t[-2]):
        raise ValueError("Valeur de tmin en dehors de l'intervalle de t")
    
    tmax = tmin + T
    if tmax>t[-1]:
        raise ValueError("Valeur de tmin trop grande")
    
    if plot_period_ax != None:
        plot_period_ax.axvspan(tmin, tmax , color='linen')
    
    y = y[(t >= tmin) & (t < tmax)]  # Sélection sur une période
    t = t[(t >= tmin) & (t < tmax)]  # Sélection sur une période
    T = t[-1]-t[0]                   # Durée totale
    N = len(t)                       # Nb points
    freq = np.arange(N)*1.0/T        # Tableau des fréquences
    ampl = np.absolute(fft(y))/N     # Tableau des amplitudes
    ampl[1:-1] = ampl[1:-1]*2        #
    
    return freq, ampl                # Retourne fréquences et amplitudes



def spectre_RMS(t, y, T, tmin=0, plot_period_ax=None):
    ''' Retourne le spectre RMS d'un signal y(t).
    
    Parameters
    ----------
    t : numpy.ndarray
        Tableau Numpy des t.

    y : numpy.ndarray
        Tableau Numpy des y.

    T : float
        Période du signal y.

    tmin : float, optionnel (0 par défaut)
        Borne inférieure le calcul du spectre.

    plot_period_ax : matplotlib.axes, optionnel (None par défaut)
        Repère (axes) sur lequel tracer la sélection de la période.
        
    Return
    ------
    (f, U) : (numpy.ndarray, numpy.ndarray)
        Tableaux des fréquences et des valeurs efficaces.
    '''
    
    if T>(t[-1]-t[0]):
        raise ValueError("Période T trop grande")
    
    if (tmin<t[0]) or (tmin>t[-2]):
        raise ValueError("Valeur de tmin en dehors de l'intervalle de t")
    
    tmax = tmin + T
    if tmax>t[-1]:
        raise ValueError("Valeur de tmin trop grande")
    
    if plot_period_ax != None:
        plot_period_ax.axvspan(tmin, tmax , color='linen')
    
    y = y[(t >= tmin) & (t < tmax)]  # Sélection sur une période
    t = t[(t >= tmin) & (t < tmax)]  # Sélection sur une période
    T = t[-1]-t[0]                   # Durée totale
    N = len(t)                       # Nb points
    freq = np.arange(N)*1.0/T        # Tableau des fréquences
    ampl = np.absolute(fft(y))/N     # Tableau des amplitudes
    ampl[1:-1] = ampl[1:-1]*2        #
    
    return freq, ampl/np.sqrt(2)     # Retourne fréquences et valeurs RMS




def spectre_RMS_dBV(t, y, T, tmin=0, plot_period_ax=None):
    ''' Retourne le spectre RMS en dBV d'un signal y(t).
    
    Parameters
    ----------
    t : numpy.ndarray
        Tableau Numpy de t.

    y : numpy.ndarray
        Tableau Numpy de y.

    T : float
        Période du signal y.

    tmin : float, optionnel (0 par défaut)
        Borne inférieure le calcul du spectre.

    plot_period_ax : matplotlib.axes, optionnel (None par défaut)
        Repère (axes) sur lequel tracer la sélection de la période.
        
    Return
    ------
    (f, U_dBV) : (numpy.ndarray, numpy.ndarray)
        Tableaux des fréquences et des valeurs efficaces en dBV.
    '''
    
    if T>(t[-1]-t[0]):
        raise ValueError("Période T trop grande")
    if (tmin<t[0]) or (tmin>t[-2]):
        raise ValueError("Valeur de tmin en dehors de l'intervalle de t")
    
    tmax = tmin + T
    if tmax>t[-1]:
        raise ValueError("Valeur de tmin trop grande")
    
    if plot_period_ax != None:
        plot_period_ax.axvspan(tmin, tmax , color='linen')
    
    y = y[(t >= tmin) & (t < tmax)]  # Sélection sur une période
    t = t[(t >= tmin) & (t < tmax)]  # Sélection sur une période
    T = t[-1]-t[0]                   # Durée totale
    N = len(t)                       # Nb points
    freq = np.arange(N)*1.0/T        # Tableau des fréquences
    ampl = np.absolute(fft(y))/N     # Tableau des amplitudes
    ampl[1:-1] = ampl[1:-1]*2        #Tableau des amplitudes
    ampl[1:-1] = ampl[1:-1]*2        #
    
    return freq, 20*np.log10(ampl/np.sqrt(2))     # Retourne fréquences et valeurs RMS dBV
