# Standard Python libraries
from pathlib import Path

# http://www.numpy.org/
import numpy as np

# https://github.com/usnistgov/DataModelDict
from DataModelDict import DataModelDict as DM

from yabadaba import query

# https://github.com/usnistgov/atomman
import atomman as am
import atomman.unitconvert as uc

from . import CalculationSubset
from ..tools import dict_insert, aslist

class AtommanSystemManipulate(CalculationSubset):
    """Handles calculation terms for modifying the loaded atomic systems"""
    
############################# Core properties #################################

    def __init__(self, parent, prefix='', templateheader=None,
                 templatedescription=None):
        """
        Initializes a calculation record subset object.

        Parameters
        ----------
        parent : iprPy.calculation.Calculation
            The parent calculation object that the subset object is part of.
            This allows for the subset methods to access parameters set to the
            calculation itself or other subsets.
        prefix : str, optional
            An optional prefix to add to metadata field names to allow for
            differentiating between multiple subsets of the same style within
            a single record
        templateheader : str, optional
            An alternate header to use in the template file for the subset.
        templatedescription : str, optional
            An alternate description of the subset for the templatedoc.
        """
        super().__init__(parent, prefix=prefix, templateheader=templateheader,
                         templatedescription=templatedescription)

        self.a_uvw = [1, 0, 0]
        self.b_uvw = [0, 1, 0]
        self.c_uvw = [0, 0, 1]
        self.atomshift = [0.0, 0.0, 0.0]
        self.a_mults = 1
        self.b_mults = 1
        self.c_mults = 1
        self.__transform = None
        self.__rcell = None
        self.__system = None
        

############################## Class attributes ################################

    @property
    def a_uvw(self):
        """numpy.NDArray: Crystal vector of ucell to align with the a box vector"""
        return self.__a_uvw
    
    @a_uvw.setter
    def a_uvw(self, value):
        value = np.asarray(value, dtype=int)
        assert value.shape == (3,) or value.shape == (4,)
        self.__a_uvw = value
            
    @property
    def b_uvw(self):
        """numpy.NDArray: Crystal vector of ucell to align with the b box vector"""
        return self.__b_uvw
    
    @b_uvw.setter
    def b_uvw(self, value):
        value = np.asarray(value, dtype=int)
        assert value.shape == (3,) or value.shape == (4,)
        self.__b_uvw = value
            
    @property
    def c_uvw(self):
        """numpy.NDArray: Crystal vector of ucell to align with the c box vector"""
        return self.__c_uvw
    
    @c_uvw.setter
    def c_uvw(self, value):
        value = np.asarray(value, dtype=int)
        assert value.shape == (3,) or value.shape == (4,)
        self.__c_uvw = value

    @property
    def uvws(self):
        """numpy.NDArray: Array of the three crystal vectors to align with the box vectors"""
        return np.vstack([self.a_uvw, self.b_uvw, self.c_uvw])
    
    @uvws.setter
    def uvws(self, value):
        value = np.asarray(value, dtype=int)
        assert value.shape == (3,3) or value.shape == (3,4)
        self.__a_uvw = value[0]
        self.__b_uvw = value[1]
        self.__c_uvw = value[2]

    @property
    def atomshift(self):
        """numpy.NDArray: Rigid shift to apply to all atoms after rotating to uvws orientation"""
        return self.__atomshift
    
    @atomshift.setter
    def atomshift(self, value):
        value = np.asarray(value, dtype=float)
        assert value.shape == (3,)
        self.__atomshift = value
            
    @property
    def a_mults(self):
        """tuple: Size multipliers for the rotated a box vector"""
        return self.__a_mults

    @a_mults.setter
    def a_mults(self, value):
        value = aslist(value)
        
        if len(value) == 1:
            value[0] = int(value[0])
            if value[0] > 0:
                value = [0, value[0]]
            
            # Add 0 after if value is negative
            elif value[0] < 0:
                value = [value[0], 0]
            
            else:
                raise ValueError('a_mults values cannot both be 0')
        
        elif len(value) == 2:
            value[0] = int(value[0])
            value[1] = int(value[1])
            if value[0] > 0:
                raise ValueError('First a_mults value must be <= 0')
            if value[1] < 0:
                raise ValueError('Second a_mults value must be >= 0')
            if value[0] == value[1]:
                raise ValueError('a_mults values cannot both be 0')
        
        self.__a_mults = tuple(value)

    @property
    def b_mults(self):
        """tuple: Size multipliers for the rotated b box vector"""
        return self.__b_mults

    @b_mults.setter
    def b_mults(self, value):
        value = aslist(value)
        
        if len(value) == 1:
            value[0] = int(value[0])
            if value[0] > 0:
                value = [0, value[0]]
            
            # Add 0 after if value is negative
            elif value[0] < 0:
                value = [value[0], 0]
            
            else:
                raise ValueError('b_mults values cannot both be 0')
        
        elif len(value) == 2:
            value[0] = int(value[0])
            value[1] = int(value[1])
            if value[0] > 0:
                raise ValueError('First b_mults value must be <= 0')
            if value[1] < 0:
                raise ValueError('Second b_mults value must be >= 0')
            if value[0] == value[1]:
                raise ValueError('b_mults values cannot both be 0')
        
        self.__b_mults = tuple(value)
    
    @property
    def c_mults(self):
        """tuple: Size multipliers for the rotated c box vector"""
        return self.__c_mults

    @c_mults.setter
    def c_mults(self, value):
        value = aslist(value)
        
        if len(value) == 1:
            value[0] = int(value[0])
            if value[0] > 0:
                value = [0, value[0]]
            
            # Add 0 after if value is negative
            elif value[0] < 0:
                value = [value[0], 0]
            
            else:
                raise ValueError('c_mults values cannot both be 0')
        
        elif len(value) == 2:
            value[0] = int(value[0])
            value[1] = int(value[1])
            if value[0] > 0:
                raise ValueError('First c_mults value must be <= 0')
            if value[1] < 0:
                raise ValueError('Second c_mults value must be >= 0')
            if value[0] == value[1]:
                raise ValueError('c_mults values cannot both be 0')
        
        self.__c_mults = tuple(value)

    @property
    def sizemults(self):
        """tuple: All three sets of size multipliers"""
        return (self.a_mults, self.b_mults, self.c_mults)

    @sizemults.setter
    def sizemults(self, value):
        if len(value) == 3:
            self.a_mults = value[0]
            self.b_mults = value[1]
            self.c_mults = value[2]
        elif len(value) == 6:
            self.a_mults = value[0:2]
            self.b_mults = value[2:4]
            self.c_mults = value[4:6]
        else:
            raise ValueError('len of sizemults must be 3 or 6')
    
    @property
    def transform(self):
        """numpy.NDArray: The Cartesian transformation matrix between ucell and rcell"""
        if self.__transform is None:
            self.__manipulatesystem()
        return self.__transform

    @property
    def rcell(self):
        """atomman.System: The rotated and shifted cell"""
        if self.__rcell is None:
            self.__manipulatesystem()
        return self.__rcell

    @property
    def system(self):
        """atomman.System: The rotated and shifted supercell"""
        if self.__system is None:
            self.__manipulatesystem()
        return self.__system

    def __manipulatesystem(self):
        """
        Creates the atomic system by manipulating the loaded ucell according
        to the set attribute values.
        """
        # Get ucell
        ucell = self.parent.system.ucell
        
        # Rotate to specified uvws
        rcell, transform = ucell.rotate(self.uvws, return_transform=True)
        
        # Scale atomshift by rcell vectors
        shift = np.dot(self.atomshift, rcell.box.vects)
        
        # Shift atoms
        rcell.atoms.pos += shift
        
        # Apply sizemults
        system = rcell.supersize(self.a_mults, self.b_mults, self.c_mults)
        system.wrap()

        # Update class attributes
        self.__transform = transform
        self.__system = system
        self.__rcell = rcell

    def set_values(self, **kwargs):
        """
        Allows for multiple class attribute values to be updated at once.

        Parameters
        ----------
        uvws : array-like object, optional
            All three crystal vectors to align the rotated cell's box vectors
            with. Cannot be given with a_uvw, b_uvw or c_uvw.
        a_uvw : array-like object, optional
            The crystal vector to align with the rotated cell's a box vector.
            Cannot be given with uvws.
        b_uvw : array-like object, optional
            The crystal vector to align with the rotated cell's b box vector.
            Cannot be given with uvws.
        c_uvw : array-like object, optional
            The crystal vector to align with the rotated cell's c box vector.
            Cannot be given with uvws.
        
        """
        if 'uvws' in kwargs:
            if 'a_uvw' in kwargs or 'b_uvw' in kwargs or 'c_uvw' in kwargs:
                raise ValueError('uvws cannot be given with the individual uvw terms')
            self.uvws = kwargs['uvws']
        if 'a_uvw' in kwargs:
            self.a_uvw = kwargs['a_uvw']
        if 'b_uvw' in kwargs:
            self.b_uvw = kwargs['b_uvw']
        if 'c_uvw' in kwargs:
            self.c_uvw = kwargs['c_uvw']
        if 'atomshift' in kwargs:
            self.atomshift = kwargs['atomshift']
        if 'sizemults' in kwargs:
            if 'a_mults' in kwargs or 'b_mults' in kwargs or 'c_mults' in kwargs:
                raise ValueError('sizemults cannot be given with the individual mults terms')
            self.sizemults = kwargs['sizemults']
        if 'a_mults' in kwargs:
            self.a_mults = kwargs['a_mults']
        if 'b_mults' in kwargs:
            self.b_mults = kwargs['b_mults']
        if 'c_mults' in kwargs:
            self.c_mults = kwargs['c_mults']


####################### Parameter file interactions ###########################

    def _template_init(self, templateheader=None, templatedescription=None):
        """
        Sets the template header and description values.

        Parameters
        ----------
        templateheader : str, optional
            An alternate header to use in the template file for the subset.
        templatedescription : str, optional
            An alternate description of the subset for the templatedoc.
        """
        # Set default template header
        if templateheader is None:
            templateheader = 'System Manipulations'

        # Set default template description
        if templatedescription is None:
            templatedescription = 'Performs simple manipulations on the loaded initial system.'
        
        super()._template_init(templateheader, templatedescription)

    @property
    def templatekeys(self):
        """dict : The subset-specific input keys and their descriptions."""
        
        return  {
            'a_uvw': ' '.join([
                "The Miller(-Bravais) crystal vector relative to the loaded system",
                "to orient with the a box vector of a resulting rotated system.",
                "Specified as three or four space-delimited numbers.",
                "Either all or none of the uvw parameters must be given."]),
            'b_uvw': ' '.join([
                "The Miller(-Bravais) crystal vector relative to the loaded system",
                "to orient with the b box vector of a resulting rotated system.",
                "Specified as three or four space-delimited numbers.",
                "Either all or none of the uvw parameters must be given."]),
            'c_uvw': ' '.join([
                "The Miller(-Bravais) crystal vector relative to the loaded system",
                "to orient with the c box vector of a resulting rotated system.",
                "Specified as three or four space-delimited numbers.",
                "Either all or none of the uvw parameters must be given."]),
            'atomshift': ' '.join([
                "A rigid-body shift vector to apply to all atoms in the rotated",
                "configuration.  Specified as three space-delimited numbers that",
                "are relative to the size of the system after rotating, but before",
                "sizemults have been applied. This allows for the same relative",
                "shift of similar systems regardless of box_parameters and sizemults.",
                "Default value is '0.0 0.0 0.0' (i.e. no shift)."]),
            'sizemults': ' '.join([
                "Multiplication parameters to construct a supercell from the rotated",
                "system.  Given as either three or six space-delimited integers.",
                "For three integers, each value indicates the number of replicas",
                "to make along the corresponding a, b, c box vector with negative",
                "values replicating in the negative Cartesian space.",
                "For six integers, the values are divided into three pairs with",
                "each pair indicating the number of 'negative' and 'positive'",
                "replications to make for a given a, b, c box vector."])
        }
    
    @property
    def preparekeys(self):
        """
        list : The input keys (without prefix) used when preparing a calculation.
        Typically, this is templatekeys plus *_content keys so prepare can access
        content before it exists in the calc folders being prepared.
        """
        return list(self.templatekeys.keys()) + []

    @property
    def interpretkeys(self):
        """
        list : The input keys (without prefix) accessed when interpreting the 
        calculation input file.  Typically, this is preparekeys plus any extra
        keys used or generated when processing the inputs.
        """
        return self.preparekeys + [
            'ucell',
            'uvws',
            'transformationmatrix',
            'initialsystem',
        ]

    def load_parameters(self, input_dict):
        """
        Interprets calculation parameters.
        
        Parameters
        ----------
        input_dict : dict
            Dictionary containing input parameter key-value pairs.
        """

        # Set default keynames
        keymap = self.keymap
        
        # Extract input values and assign default values
        a_uvw = input_dict.get(keymap['a_uvw'], None)
        b_uvw = input_dict.get(keymap['b_uvw'], None)
        c_uvw = input_dict.get(keymap['c_uvw'], None)
        atomshift = input_dict.get(keymap['atomshift'], '0 0 0')
        sizemults = input_dict.get(keymap['sizemults'], '1 1 1')
        
        # Assign default uvws only if all are None
        if a_uvw is None and b_uvw is None and c_uvw is None:
            a_uvw = '1 0 0'
            b_uvw = '0 1 0'
            c_uvw = '0 0 1'
        
        # Issue error for incomplete uvws set
        elif a_uvw is None or b_uvw is None or c_uvw is None:
            raise TypeError('incomplete set of uvws terms')
        
        # Process uvws
        self.a_uvw = np.array(a_uvw.strip().split(), dtype=float)
        self.b_uvw = np.array(b_uvw.strip().split(), dtype=float)
        self.c_uvw = np.array(c_uvw.strip().split(), dtype=float)
        
        # Process sizemults
        self.sizemults = np.array(sizemults.strip().split(), dtype=int)

        # Process atomshift
        self.atomshift = np.array(atomshift.strip().split(), dtype=float)

########################### Data model interactions ###########################

    def load_model(self, model):
        """Loads subset attributes from an existing model."""
        run_params = model['calculation']['run-parameter']
        self.a_mults = run_params[f'{self.modelprefix}size-multipliers']['a']
        self.b_mults = run_params[f'{self.modelprefix}size-multipliers']['b']
        self.c_mults = run_params[f'{self.modelprefix}size-multipliers']['c']
        #self.atomshift = run_params[f'{self.modelprefix}atom-shift']
        #self.a_uvw = run_params[f'{self.modelprefix}rotation-vector']['a']
        #self.b_uvw = run_params[f'{self.modelprefix}rotation-vector']['b']
        #self.c_uvw = run_params[f'{self.modelprefix}rotation-vector']['c']

    def build_model(self, model, **kwargs):
        """
        Adds the subset model to the parent model.
        
        Parameters
        ----------
        model : DataModelDict.DataModelDict
            The record content (after root element) to add content to.
        kwargs : any
            Any options to pass on to dict_insert that specify where the subset
            content gets added to in the parent model.
        """

        # Build paths if needed
        if 'calculation' not in model:
            model['calculation'] = DM()
        if 'run-parameter' not in model['calculation']:
            model['calculation']['run-parameter'] = DM()

        run_params = model['calculation']['run-parameter']
        
        run_params[f'{self.modelprefix}size-multipliers'] = DM()
        run_params[f'{self.modelprefix}size-multipliers']['a'] = list(self.a_mults)
        run_params[f'{self.modelprefix}size-multipliers']['b'] = list(self.b_mults)
        run_params[f'{self.modelprefix}size-multipliers']['c'] = list(self.c_mults)
        #run_params[f'{self.modelprefix}atom-shift'] = self.atomshift.tolist()
        #run_params[f'{self.modelprefix}rotation-vector'] = DM()
        #run_params[f'{self.modelprefix}rotation-vector']['a'] = self.a_uvw.tolist()
        #run_params[f'{self.modelprefix}rotation-vector']['b'] = self.b_uvw.tolist()
        #run_params[f'{self.modelprefix}rotation-vector']['c'] = self.c_uvw.tolist()
        
    def mongoquery(self, a_mult1=None, a_mult2=None, b_mult1=None,
                       b_mult2=None, c_mult1=None, c_mult2=None, **kwargs):
        """
        Generate a query to parse records with the subset from a Mongo-style
        database.
        
        Parameters
        ----------
        a_mult1 : int
            The lower size multiplier for the a box direction.
        a_mult2 : int
            The upper size multiplier for the a box direction.
        b_mult1 : int
            The lower size multiplier for the b box direction.
        b_mult2 : int
            The upper size multiplier for the b box direction.
        c_mult1 : int
            The lower size multiplier for the c box direction.
        c_mult2 : int
            The upper size multiplier for the c box direction.
        kwargs : any
            The parent query terms and values ignored by the subset.

        Returns
        -------
        dict
            The Mongo-style find query terms.
        """
        # Init query and set root paths
        mquery = {}
        parentroot = f'content.{self.parent.modelroot}'
        root = f'{parentroot}.{self.modelroot}'
        runparam_prefix = f'{parentroot}.calculation.run-parameter.{self.modelprefix}'

        # Build query terms
        query.int_match.mongo(mquery, f'{runparam_prefix}size-multipliers.a.0', a_mult1)
        query.int_match.mongo(mquery, f'{runparam_prefix}size-multipliers.a.1', a_mult2)
        query.int_match.mongo(mquery, f'{runparam_prefix}size-multipliers.b.0', b_mult1)
        query.int_match.mongo(mquery, f'{runparam_prefix}size-multipliers.b.1', b_mult2)
        query.int_match.mongo(mquery, f'{runparam_prefix}size-multipliers.c.0', c_mult1)
        query.int_match.mongo(mquery, f'{runparam_prefix}size-multipliers.c.1', c_mult2)
        
        # Return query dict
        return mquery

    def cdcsquery(self, a_mult1=None, a_mult2=None, b_mult1=None,
                       b_mult2=None, c_mult1=None, c_mult2=None, **kwargs):
        """
        Generate a query to parse records with the subset from a CDCS-style
        database.
        
        Parameters
        ----------
        a_mult1 : int
            The lower size multiplier for the a box direction.
        a_mult2 : int
            The upper size multiplier for the a box direction.
        b_mult1 : int
            The lower size multiplier for the b box direction.
        b_mult2 : int
            The upper size multiplier for the b box direction.
        c_mult1 : int
            The lower size multiplier for the c box direction.
        c_mult2 : int
            The upper size multiplier for the c box direction.
        kwargs : any
            The parent query terms and values ignored by the subset.

        Returns
        -------
        dict
            The CDCS-style find query terms.
        """
        # Init query and set root paths
        mquery = {}
        parentroot = self.parent.modelroot
        root = f'{parentroot}.{self.modelroot}'
        runparam_prefix = f'{parentroot}.calculation.run-parameter.{self.modelprefix}'

        # Build query terms
        query.int_match.mongo(mquery, f'{runparam_prefix}size-multipliers.a.0', a_mult1)
        query.int_match.mongo(mquery, f'{runparam_prefix}size-multipliers.a.1', a_mult2)
        query.int_match.mongo(mquery, f'{runparam_prefix}size-multipliers.b.0', b_mult1)
        query.int_match.mongo(mquery, f'{runparam_prefix}size-multipliers.b.1', b_mult2)
        query.int_match.mongo(mquery, f'{runparam_prefix}size-multipliers.c.0', c_mult1)
        query.int_match.mongo(mquery, f'{runparam_prefix}size-multipliers.c.1', c_mult2)
        
        # Return query dict
        return mquery

    def metadata(self, meta):
        """
        Converts the structured content to a simpler dictionary.
        
        Parameters
        ----------
        meta : dict
            The dictionary to add the subset content to
        """
        prefix = self.prefix

        meta[f'{prefix}a_mult1'] = self.a_mults[0]
        meta[f'{prefix}a_mult2'] = self.a_mults[1]
        meta[f'{prefix}b_mult1'] = self.b_mults[0]
        meta[f'{prefix}b_mult2'] = self.b_mults[1]
        meta[f'{prefix}c_mult1'] = self.c_mults[0]
        meta[f'{prefix}c_mult2'] = self.c_mults[1]

        meta[f'{prefix}atomshift'] = self.atomshift.tolist()

        meta[f'{prefix}a_uvw'] = self.a_uvw.tolist()
        meta[f'{prefix}b_uvw'] = self.b_uvw.tolist()
        meta[f'{prefix}c_uvw'] = self.c_uvw.tolist()

    def pandasfilter(self, dataframe, a_mult1=None, a_mult2=None,
                     b_mult1=None, b_mult2=None, c_mult1=None, c_mult2=None,
                     **kwargs):
        """
        Parses a pandas dataframe containing the subset's metadata to find 
        entries matching the terms and values given. Ideally, this should find
        the same matches as the mongoquery and cdcsquery methods for the same
        search parameters.

        Parameters
        ----------
        dataframe : pandas.DataFrame
            The metadata dataframe to filter.
        a_mult1 : int
            The lower size multiplier for the a box direction.
        a_mult2 : int
            The upper size multiplier for the a box direction.
        b_mult1 : int
            The lower size multiplier for the b box direction.
        b_mult2 : int
            The upper size multiplier for the b box direction.
        c_mult1 : int
            The lower size multiplier for the c box direction.
        c_mult2 : int
            The upper size multiplier for the c box direction.
        kwargs : any
            The parent query terms and values ignored by the subset.

        Returns
        -------
        pandas.Series of bool
            True for each entry where all filter terms+values match, False for
            all other entries.
        """
        prefix = self.prefix
        matches = (
            query.int_match.pandas(dataframe,  f'{prefix}a_mult1', a_mult1)
            &query.int_match.pandas(dataframe, f'{prefix}a_mult2', a_mult2)
            &query.int_match.pandas(dataframe, f'{prefix}b_mult1', b_mult1)
            &query.int_match.pandas(dataframe, f'{prefix}b_mult2', b_mult2)
            &query.int_match.pandas(dataframe, f'{prefix}c_mult1', c_mult1)
            &query.int_match.pandas(dataframe, f'{prefix}c_mult2', c_mult2)
        )
        return matches

########################### Calculation interactions ##########################

    def calc_inputs(self, input_dict):
        """
        Generates calculation function input parameters based on the values
        assigned to attributes of the subset.

        Parameters
        ----------
        input_dict : dict
            The dictionary of input parameters to add subset terms to.
        """
        input_dict['transform'] = self.transform
        input_dict['system'] = self.system