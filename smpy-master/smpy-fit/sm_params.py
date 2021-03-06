"""
SSP Paramaters
make.py

"""
import numpy as np

ssp_input = '../ssp/bc03/chab/lr/'               # Input SSP folder
ssp_output = 'temp_fitting.npz' # Output filename

# Star formation timescales (Gyr)
#tau = [-10.,-5.,-2.5,-1.0,-0.5,-0.25,0.05,0.25,0.5,1.0,2.5,5.,10.]

tau = np.logspace(-3,1,50)
#tau=[0.1,0.2,0.5,1,10]

#Model ages (Gyr)
#tg = [0.005,0.0100,0.0158,0.0251,0.0398,0.0631,0.1000,0.1585,
      #0.2512,0.3,0.4,0.5,0.6310,0.7,0.8,1.0,1.13,1.28,1.43,1.6,
      #2.,2.5,3.,4.,5.,6.5,8.,10.,13.5]   
      
#tg = np.linspace(1,13,5)
#tg=np.linspace(1,5,50)
tg=[1,3,5,7,9,11,13]

# Dust Total Attenuation Values
tauv = [0,1]

dust_model = 'calzetti'                # 'charlot' - Charlot & Fall or 'calzetti' - Calzetti 2000
mu = 0.3                              # Fraction of tauv from ISM
epsilon = 0.                     # Gas recycling parameter
metallicities = [5]       # Metallicities to use

csf = False                           # Set to constant SFR (overrides, tau values)

#Nebular emission
add_nebular = True                    # Include nebular emission
neb_file = 'nebular_emission.dat'     # Nebular emission path
fesc = 0.2                            # Lyman continuum escape fraction

"""
Synthetic Magnitudes Parameters
process.py

"""

synmag_output = 'temp_fitting_neb.npz'

# Filter Directory and Naming Convention - Assumes Ordered Numerically
filt_dir = '../../../SDSS_filters/'
filt_names = '*1.txt'


# Redshift Grid 

zspacing = 'log' # or 'log'
zmin = 0.05 # log(zmin) if using log spacing
zmax = 0.05 # log(zmax) if using log spacing
zstep = 0.005
n_zsteps = 1 #Number of steps for log spacing +1 additional z = 0 step

madau = True                           # Include HI absorption (Madau 1995)


"""
Template matching parameters
match.py

"""
#Observed magnitudes and redshifts to fit
#'input_catalog = '/data/candels/catalogs/mocks/gs_newmocks_full.fits'
#input_catalog = '/data/candels/catalogs/GOODS-S/gs_all_tf_h_120919a_multi.mag.highz.noAGN.fits'
#input_catalog = '/data/candels/photz/GOODS-S/130213/gs_all_tf_h_130213a_multi.sample.phot.fits'
#input_catalog = '/data/MRC0406_irac.mag.fits'
#input_catalog = '/data/candels/catalogs/mocks/regions/mockset1_wide.sample.fits'
input_catalog = '../../../Zoo_catalogues/Week_9/FITS/Volume_limited_sample_Baldry_KD.fits'
input_format = 'fits'


ID_col = 'id'
z_col = 'REDSHIFT_1'

flux_col_end = 'flux'                 # Naming convention for input catalog
fluxerr_col_end ='fluxerr'            # E.g. ACS_F606W_*flux_col_end* = F606W Flux
mag_col_end = 'mag'                   # ACS_F606W_*fluxerr_col_end* = F606W Flux Error
magerr_col_end ='magerr'

filts_used = [0,1,2,3,4,5]#,6] #[2,3,5,8,9,10,11] #[0,1,2,3,4,5,6,7,        # Filter columns from input used
              #8,9,10,11,12,13,14,15]              # (If not all)

flux_corr = 1.0                       # Flux correction to convert to Total Mags

fit_mode = 'flux'                     # Fit to Mag Colours - 'colours' or 'flux'

calc_pdf = False
calc_mode = False                     # Calculate Mode Mass

include_rest = True

mode_mass_percentage = 10.            # Top percentage of fits to use in mode
                                      # mass calculations

muv_max, muv_min, muv_bins = -23., -16., 100 # PDF bins
mass_max, mass_min, mass_bins = 12., 7., 100
beta_max, beta_min, beta_bins = 3., -3., 50 

#Output table parameters:
output_name = 'results'
#output_name = 'results/200912/gs_all_tf_h_130213a_multi.chab.MC.results'
#output_name = '/data/MRC0406_inc.SED.fits'
table_format = 'fits'                 # Available formats:'fits'/'ascii'/'IPAC'
                                      # (those available to local installation
                                      #  of AtPY)
ncpus = 2
