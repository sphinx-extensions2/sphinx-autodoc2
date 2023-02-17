:py:mod:`aiida.tools`
=====================

.. py:module:: aiida.tools


Description
-----------

Tools to operate on AiiDA ORM class instances

What functionality should go directly in the ORM class in `aiida.orm` and what in `aiida.tools`?

    - The ORM class should define basic functions to set and get data from the object
    - More advanced functionality to operate on the ORM class instances can be placed in `aiida.tools`
        to prevent the ORM namespace from getting too cluttered.

.. note:: Modules in this sub package may require the database environment to be loaded


Package Contents
----------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`CalculationTools <aiida.tools.calculations.base.CalculationTools>`
     - Base class for CalculationTools.
   * - :py:obj:`Graph <aiida.tools.visualization.graph.Graph>`
     - a class to create graphviz graphs of the AiiDA node provenance
   * - :py:obj:`GroupPath <aiida.tools.groups.paths.GroupPath>`
     - A class to provide label delimited access to groups.
   * - :py:obj:`Orbital <aiida.tools.data.orbital.orbital.Orbital>`
     - Base class for Orbitals. Can handle certain basic fields, their setting and validation. More complex Orbital objects should then inherit from this class
   * - :py:obj:`RealhydrogenOrbital <aiida.tools.data.orbital.realhydrogen.RealhydrogenOrbital>`
     - Orbitals for hydrogen, largely follows the conventions used by wannier90 Object to handle the generation of real hydrogen orbitals and their hybrids, has methods for producing s, p, d, f, and sp, sp2, sp3, sp3d, sp3d2 hybrids. This method does not deal with the cannonical hydrogen orbitals which contain imaginary components.

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`default_link_styles <aiida.tools.visualization.graph.default_link_styles>`
     - map link_pair to a graphviz edge style
   * - :py:obj:`default_node_styles <aiida.tools.visualization.graph.default_node_styles>`
     - map a node to a graphviz node style
   * - :py:obj:`default_node_sublabels <aiida.tools.visualization.graph.default_node_sublabels>`
     - function mapping nodes to a sublabel (e.g. specifying some attribute values)
   * - :py:obj:`delete_group_nodes <aiida.tools.graph.deletions.delete_group_nodes>`
     - Delete nodes contained in a list of groups (not the groups themselves!).
   * - :py:obj:`delete_nodes <aiida.tools.graph.deletions.delete_nodes>`
     - Delete nodes given a list of "starting" PKs.
   * - :py:obj:`get_explicit_kpoints_path <aiida.tools.data.array.kpoints.main.get_explicit_kpoints_path>`
     - Returns a dictionary whose contents depend on the method but includes at least the following keys
   * - :py:obj:`get_kpoints_path <aiida.tools.data.array.kpoints.main.get_kpoints_path>`
     - Returns a dictionary whose contents depend on the method but includes at least the following keys
   * - :py:obj:`pstate_node_styles <aiida.tools.visualization.graph.pstate_node_styles>`
     - map a process node to a graphviz node style
   * - :py:obj:`spglib_tuple_to_structure <aiida.tools.data.structure.spglib_tuple_to_structure>`
     - Convert a tuple of the format (cell, scaled_positions, element_numbers) to an AiiDA structure.
   * - :py:obj:`structure_to_spglib_tuple <aiida.tools.data.structure.structure_to_spglib_tuple>`
     - Convert an AiiDA structure to a tuple of the format (cell, scaled_positions, element_numbers).

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`DELETE_LOGGER <aiida.tools.graph.deletions.DELETE_LOGGER>`
     - 

API
~~~

.. py:class:: CalculationTools(node)
   :canonical: aiida.tools.calculations.base.CalculationTools

   Base class for CalculationTools.

   .. py:method:: __init__(node)
      :canonical: aiida.tools.calculations.base.CalculationTools.__init__

.. py:data:: DELETE_LOGGER
   :canonical: aiida.tools.graph.deletions.DELETE_LOGGER
   :value: None

.. py:class:: Graph(engine=None, graph_attr=None, global_node_style=None, global_edge_style=None, include_sublabels=True, link_style_fn=None, node_style_fn=None, node_sublabel_fn=None, node_id_type='pk', backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None)
   :canonical: aiida.tools.visualization.graph.Graph

   a class to create graphviz graphs of the AiiDA node provenance

   .. py:method:: __init__(engine=None, graph_attr=None, global_node_style=None, global_edge_style=None, include_sublabels=True, link_style_fn=None, node_style_fn=None, node_sublabel_fn=None, node_id_type='pk', backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None)
      :canonical: aiida.tools.visualization.graph.Graph.__init__

      a class to create graphviz graphs of the AiiDA node provenance

      Nodes and edges, are cached, so that they are only created once

      :param engine: the graphviz engine, e.g. dot, circo (Default value = None)
      :type engine: str or None
      :param graph_attr: attributes for the graphviz graph (Default value = None)
      :type graph_attr: dict or None
      :param global_node_style: styles which will be added to all nodes.
          Note this will override any builtin attributes (Default value = None)
      :type global_node_style: dict or None
      :param global_edge_style: styles which will be added to all edges.
          Note this will override any builtin attributes (Default value = None)
      :type global_edge_style: dict or None
      :param include_sublabels: if True, the note text will include node dependant sub-labels (Default value = True)
      :type include_sublabels: bool
      :param link_style_fn: callable mapping LinkType to graphviz style dict;
          link_style_fn(link_type) -> dict (Default value = None)
      :param node_sublabel_fn: callable mapping nodes to a graphviz style dict;
          node_sublabel_fn(node) -> dict (Default value = None)
      :param node_sublabel_fn: callable mapping data node to a sublabel (e.g. specifying some attribute values)
          node_sublabel_fn(node) -> str (Default value = None)
      :param node_id_type: the type of identifier to within the node text ('pk', 'uuid' or 'label')
      :type node_id_type: str


   .. py:property:: backend
      :canonical: aiida.tools.visualization.graph.Graph.backend
      :type: aiida.orm.implementation.StorageBackend

      The backend used to create the graph

   .. py:property:: graphviz
      :canonical: aiida.tools.visualization.graph.Graph.graphviz

      return a copy of the graphviz.Digraph

   .. py:property:: nodes
      :canonical: aiida.tools.visualization.graph.Graph.nodes

      return a copy of the nodes

   .. py:property:: edges
      :canonical: aiida.tools.visualization.graph.Graph.edges

      return a copy of the edges

   .. py:method:: _load_node(node)
      :canonical: aiida.tools.visualization.graph.Graph._load_node

      load a node (if not already loaded)

      :param node: node or node pk/uuid
      :type node: int or str or aiida.orm.nodes.node.Node
      :returns: aiida.orm.nodes.node.Node


   .. py:method:: _default_link_types(link_types)
      :canonical: aiida.tools.visualization.graph.Graph._default_link_types
      :staticmethod:

      If link_types is empty, it will return all the links_types

      :param links: iterable with the link_types ()
      :returns: list of :py:class:`aiida.common.links.LinkType`


   .. py:method:: add_node(node, style_override=None, overwrite=False)
      :canonical: aiida.tools.visualization.graph.Graph.add_node

      add single node to the graph

      :param node: node or node pk/uuid
      :type node: int or str or aiida.orm.nodes.node.Node
      :param style_override: graphviz style parameters that will override default values
      :type style_override: dict or None
      :param overwrite: whether to overrite an existing node (Default value = False)
      :type overwrite: bool


   .. py:method:: add_edge(in_node, out_node, link_pair=None, style=None, overwrite=False)
      :canonical: aiida.tools.visualization.graph.Graph.add_edge

      add single node to the graph

      :param in_node: node or node pk/uuid
      :type in_node: int or aiida.orm.nodes.node.Node
      :param out_node: node or node pk/uuid
      :type out_node: int or str or aiida.orm.nodes.node.Node
      :param link_pair: defining the relationship between the nodes
      :type link_pair: None or aiida.orm.utils.links.LinkPair
      :param style: graphviz style parameters (Default value = None)
      :type style: dict or None
      :param overwrite: whether to overrite existing edge (Default value = False)
      :type overwrite: bool


   .. py:method:: _convert_link_types(link_types)
      :canonical: aiida.tools.visualization.graph.Graph._convert_link_types
      :staticmethod:

      convert link types, which may be strings, to a member of LinkType

   .. py:method:: add_incoming(node, link_types=(), annotate_links=None, return_pks=True)
      :canonical: aiida.tools.visualization.graph.Graph.add_incoming

      add nodes and edges for incoming links to a node

      :param node: node or node pk/uuid
      :type node: aiida.orm.nodes.node.Node or int
      :param link_types: filter by link types (Default value = ())
      :type link_types: str or tuple[str] or aiida.common.links.LinkType or tuple[aiida.common.links.LinkType]
      :param annotate_links: label edges with the link 'label', 'type' or 'both' (Default value = None)
      :type annotate_links: bool or str
      :param return_pks: whether to return a list of nodes, or list of node pks (Default value = True)
      :type return_pks: bool
      :returns: list of nodes or node pks


   .. py:method:: add_outgoing(node, link_types=(), annotate_links=None, return_pks=True)
      :canonical: aiida.tools.visualization.graph.Graph.add_outgoing

      add nodes and edges for outgoing links to a node

      :param node: node or node pk
      :type node: aiida.orm.nodes.node.Node or int
      :param link_types: filter by link types (Default value = ())
      :type link_types: str or tuple[str] or aiida.common.links.LinkType or tuple[aiida.common.links.LinkType]
      :param annotate_links: label edges with the link 'label', 'type' or 'both' (Default value = None)
      :type annotate_links: bool or str
      :param return_pks: whether to return a list of nodes, or list of node pks (Default value = True)
      :type return_pks: bool
      :returns: list of nodes or node pks


   .. py:method:: recurse_descendants(origin, depth=None, link_types=(), annotate_links=False, origin_style=MappingProxyType(_OVERRIDE_STYLES_DICT['origin_node']), include_process_inputs=False, highlight_classes=None)
      :canonical: aiida.tools.visualization.graph.Graph.recurse_descendants

      add nodes and edges from an origin recursively,
      following outgoing links

      :param origin: node or node pk/uuid
      :type origin: aiida.orm.nodes.node.Node or int
      :param depth: if not None, stop after travelling a certain depth into the graph (Default value = None)
      :type depth: None or int
      :param link_types: filter by subset of link types (Default value = ())
      :type link_types: tuple or str
      :param annotate_links: label edges with the link 'label', 'type' or 'both' (Default value = False)
      :type annotate_links: bool or str
      :param origin_style: node style map for origin node (Default value = None)
      :type origin_style: None or dict
      :param include_calculation_inputs: include incoming links for all processes (Default value = False)
      :type include_calculation_inputs: bool
      :param highlight_classes: target class in exported graph expected to be highlight and
          other nodes are decolorized (Default value = None)
      :typle highlight_classes: tuple of class or class


   .. py:method:: recurse_ancestors(origin, depth=None, link_types=(), annotate_links=False, origin_style=MappingProxyType(_OVERRIDE_STYLES_DICT['origin_node']), include_process_outputs=False, highlight_classes=None)
      :canonical: aiida.tools.visualization.graph.Graph.recurse_ancestors

      add nodes and edges from an origin recursively,
      following incoming links

      :param origin: node or node pk/uuid
      :type origin: aiida.orm.nodes.node.Node or int
      :param depth: if not None, stop after travelling a certain depth into the graph (Default value = None)
      :type depth: None or int
      :param link_types: filter by subset of link types (Default value = ())
      :type link_types: tuple or str
      :param annotate_links: label edges with the link 'label', 'type' or 'both' (Default value = False)
      :type annotate_links: bool
      :param origin_style: node style map for origin node (Default value = None)
      :type origin_style: None or dict
      :param include_process_outputs:  include outgoing links for all processes (Default value = False)
      :type include_process_outputs: bool
      :param highlight_classes:  class label (as displayed in the graph, e.g. 'StructureData', 'FolderData', etc.)
          to be highlight and other nodes are decolorized (Default value = None)
      :typle highlight_classes: list or tuple of str


   .. py:method:: add_origin_to_targets(origin, target_cls, target_filters=None, include_target_inputs=False, include_target_outputs=False, origin_style=(), annotate_links=False)
      :canonical: aiida.tools.visualization.graph.Graph.add_origin_to_targets

      Add nodes and edges from an origin node to all nodes of a target node class.

      :param origin: node or node pk/uuid
      :type origin: aiida.orm.nodes.node.Node or int
      :param target_cls: target node class
      :param target_filters:  (Default value = None)
      :type target_filters: dict or None
      :param include_target_inputs:  (Default value = False)
      :type include_target_inputs: bool
      :param include_target_outputs:  (Default value = False)
      :type include_target_outputs: bool
      :param origin_style: node style map for origin node (Default value = ())
      :type origin_style: dict or tuple
      :param annotate_links: label edges with the link 'label', 'type' or 'both' (Default value = False)
      :type annotate_links: bool


   .. py:method:: add_origins_to_targets(origin_cls, target_cls, origin_filters=None, target_filters=None, include_target_inputs=False, include_target_outputs=False, origin_style=(), annotate_links=False)
      :canonical: aiida.tools.visualization.graph.Graph.add_origins_to_targets

      Add nodes and edges from all nodes of an origin class to all node of a target node class.

      :param origin_cls: origin node class
      :param target_cls: target node class
      :param origin_filters:  (Default value = None)
      :type origin_filters: dict or None
      :param target_filters:  (Default value = None)
      :type target_filters: dict or None
      :param include_target_inputs:  (Default value = False)
      :type include_target_inputs: bool
      :param include_target_outputs:  (Default value = False)
      :type include_target_outputs: bool
      :param origin_style: node style map for origin node (Default value = ())
      :type origin_style: dict or tuple
      :param annotate_links: label edges with the link 'label', 'type' or 'both' (Default value = False)
      :type annotate_links: bool


.. py:exception:: GroupNotFoundError(grouppath)
   :canonical: aiida.tools.groups.paths.GroupNotFoundError

   Bases: :py:obj:`Exception`

   An exception raised when a path does not have an associated group.

   .. py:method:: __init__(grouppath)
      :canonical: aiida.tools.groups.paths.GroupNotFoundError.__init__

      Initialize self.  See help(type(self)) for accurate signature.

.. py:exception:: GroupNotUniqueError(grouppath)
   :canonical: aiida.tools.groups.paths.GroupNotUniqueError

   Bases: :py:obj:`Exception`

   An exception raised when a path has multiple associated groups.

   .. py:method:: __init__(grouppath)
      :canonical: aiida.tools.groups.paths.GroupNotUniqueError.__init__

      Initialize self.  See help(type(self)) for accurate signature.

.. py:class:: GroupPath(path: str = '', cls: aiida.orm.groups.GroupMeta = orm.Group, warn_invalid_child: bool = True)
   :canonical: aiida.tools.groups.paths.GroupPath

   A class to provide label delimited access to groups.

   See tests for usage examples.


   .. py:method:: __init__(path: str = '', cls: aiida.orm.groups.GroupMeta = orm.Group, warn_invalid_child: bool = True) -> None
      :canonical: aiida.tools.groups.paths.GroupPath.__init__

      Instantiate the class.

      :param path: The initial path of the group.
      :param cls: The subclass of `Group` to operate on.
      :param warn_invalid_child: Issue a warning, when iterating children, if a child path is invalid.



   .. py:method:: _validate_path(path)
      :canonical: aiida.tools.groups.paths.GroupPath._validate_path

      Validate the supplied path.

   .. py:method:: __repr__() -> str
      :canonical: aiida.tools.groups.paths.GroupPath.__repr__

      Represent the instantiated class.

   .. py:method:: __eq__(other: typing.Any) -> bool
      :canonical: aiida.tools.groups.paths.GroupPath.__eq__

      Compare equality of path and ``Group`` subclass to another ``GroupPath`` object.

   .. py:method:: __lt__(other: typing.Any) -> bool
      :canonical: aiida.tools.groups.paths.GroupPath.__lt__

      Compare less-than operator of path and ``Group`` subclass to another ``GroupPath`` object.

   .. py:property:: path
      :canonical: aiida.tools.groups.paths.GroupPath.path
      :type: str

      Return the path string.

   .. py:property:: path_list
      :canonical: aiida.tools.groups.paths.GroupPath.path_list
      :type: typing.List[str]

      Return a list of the path components.

   .. py:property:: key
      :canonical: aiida.tools.groups.paths.GroupPath.key
      :type: typing.Optional[str]

      Return the final component of the the path.

   .. py:property:: delimiter
      :canonical: aiida.tools.groups.paths.GroupPath.delimiter
      :type: str

      Return the delimiter used to split path into components.

   .. py:property:: cls
      :canonical: aiida.tools.groups.paths.GroupPath.cls
      :type: aiida.orm.groups.GroupMeta

      Return the cls used to query for and instantiate a ``Group`` with.

   .. py:property:: parent
      :canonical: aiida.tools.groups.paths.GroupPath.parent
      :type: typing.Optional[aiida.tools.groups.paths.GroupPath]

      Return the parent path.

   .. py:method:: __truediv__(path: str) -> aiida.tools.groups.paths.GroupPath
      :canonical: aiida.tools.groups.paths.GroupPath.__truediv__

      Return a child ``GroupPath``, with a new path formed by appending ``path`` to the current path.

   .. py:method:: __getitem__(path: str) -> aiida.tools.groups.paths.GroupPath
      :canonical: aiida.tools.groups.paths.GroupPath.__getitem__

      Return a child ``GroupPath``, with a new path formed by appending ``path`` to the current path.

   .. py:method:: get_group() -> typing.Optional[aiida.tools.groups.paths.GroupPath]
      :canonical: aiida.tools.groups.paths.GroupPath.get_group

      Return the concrete group associated with this path.

   .. py:property:: group_ids
      :canonical: aiida.tools.groups.paths.GroupPath.group_ids
      :type: typing.List[int]

      Return all the UUID associated with this GroupPath.

      :returns: and empty list, if no group associated with this label,
          or can be multiple if cls was None

      This is an efficient method for checking existence,
      which does not require the (slow) loading of the ORM entity.


   .. py:property:: is_virtual
      :canonical: aiida.tools.groups.paths.GroupPath.is_virtual
      :type: bool

      Return whether there is one or more concrete groups associated with this path.

   .. py:method:: get_or_create_group() -> typing.Tuple[aiida.orm.Group, bool]
      :canonical: aiida.tools.groups.paths.GroupPath.get_or_create_group

      Return the concrete group associated with this path or, create it, if it does not already exist.

   .. py:method:: delete_group()
      :canonical: aiida.tools.groups.paths.GroupPath.delete_group

      Delete the concrete group associated with this path.

      :raises: GroupNotFoundError, GroupNotUniqueError


   .. py:property:: children
      :canonical: aiida.tools.groups.paths.GroupPath.children
      :type: typing.Iterator[aiida.tools.groups.paths.GroupPath]

      Iterate through all (direct) children of this path.

   .. py:method:: __iter__() -> typing.Iterator[aiida.tools.groups.paths.GroupPath]
      :canonical: aiida.tools.groups.paths.GroupPath.__iter__

      Iterate through all (direct) children of this path.

   .. py:method:: __len__() -> int
      :canonical: aiida.tools.groups.paths.GroupPath.__len__

      Return the number of children for this path.

   .. py:method:: __contains__(key: str) -> bool
      :canonical: aiida.tools.groups.paths.GroupPath.__contains__

      Return whether a child exists for this key.

   .. py:method:: walk(return_virtual: bool = True) -> typing.Iterator[aiida.tools.groups.paths.GroupPath]
      :canonical: aiida.tools.groups.paths.GroupPath.walk

      Recursively iterate through all children of this path.

   .. py:method:: walk_nodes(filters: typing.Optional[dict] = None, node_class: typing.Optional[aiida.orm.Node] = None, query_batch: typing.Optional[int] = None) -> typing.Iterator[aiida.tools.groups.paths.WalkNodeResult]
      :canonical: aiida.tools.groups.paths.GroupPath.walk_nodes

      Recursively iterate through all nodes of this path and its children.

      :param filters: filters to apply to the node query
      :param node_class: return only nodes of a certain class (or list of classes)
      :param query_batch: The size of the batches to ask the backend to batch results in subcollections.
          You can optimize the speed of the query by tuning this parameter.
          Be aware though that is only safe if no commit will take place during this transaction.


   .. py:property:: browse
      :canonical: aiida.tools.groups.paths.GroupPath.browse

      Return a ``GroupAttr`` instance, for attribute access to children.

.. py:exception:: InvalidPath()
   :canonical: aiida.tools.groups.paths.InvalidPath

   Bases: :py:obj:`Exception`

   An exception to indicate that a path is not valid.

.. py:exception:: NoGroupsInPathError(grouppath)
   :canonical: aiida.tools.groups.paths.NoGroupsInPathError

   Bases: :py:obj:`Exception`

   An exception raised when a path has multiple associated groups.

   .. py:method:: __init__(grouppath)
      :canonical: aiida.tools.groups.paths.NoGroupsInPathError.__init__

      Initialize self.  See help(type(self)) for accurate signature.

.. py:class:: Orbital(**kwargs)
   :canonical: aiida.tools.data.orbital.orbital.Orbital

   Base class for Orbitals. Can handle certain basic fields, their setting
   and validation. More complex Orbital objects should then inherit from
   this class

   :param position: the absolute position (three floats) units in angstrom
   :param x_orientation: x,y,z unit vector defining polar angle theta
                         in spherical coordinates unitless
   :param z_orientation: x,y,z unit vector defining azimuthal angle phi
                         in spherical coordinates unitless
   :param orientation_spin: x,y,z unit vector defining the spin orientation
                            unitless
   :param diffusivity: Float controls the radial term in orbital equation
                       units are reciprocal Angstrom.


   .. py:attribute:: _base_fields_required
      :canonical: aiida.tools.data.orbital.orbital.Orbital._base_fields_required
      :value: (('position',),)

   .. py:attribute:: _base_fields_optional
      :canonical: aiida.tools.data.orbital.orbital.Orbital._base_fields_optional
      :value: None

   .. py:method:: __init__(**kwargs)
      :canonical: aiida.tools.data.orbital.orbital.Orbital.__init__

   .. py:method:: __repr__()
      :canonical: aiida.tools.data.orbital.orbital.Orbital.__repr__

      Return repr(self).

   .. py:method:: __str__() -> str
      :canonical: aiida.tools.data.orbital.orbital.Orbital.__str__

      Return str(self).

   .. py:method:: _validate_keys(input_dict)
      :canonical: aiida.tools.data.orbital.orbital.Orbital._validate_keys

      Checks all the input_dict and tries to validate them, to ensure
      that they have been properly set raises Exceptions indicating any
      problems that should arise during the validation

      :param input_dict: a dictionary of inputs
      :return: input_dict: the original dictionary with all validated kyes
               now removed
      :return: validated_dict: a dictionary containing all the input keys
               which have now been validated.


   .. py:method:: set_orbital_dict(init_dict)
      :canonical: aiida.tools.data.orbital.orbital.Orbital.set_orbital_dict

      Sets the orbital_dict, which can vary depending on the particular
      implementation of this base class.

      :param init_dict: the initialization dictionary


   .. py:method:: get_orbital_dict()
      :canonical: aiida.tools.data.orbital.orbital.Orbital.get_orbital_dict

      returns the internal keys as a dictionary


.. py:class:: RealhydrogenOrbital
   :canonical: aiida.tools.data.orbital.realhydrogen.RealhydrogenOrbital

   Bases: :py:obj:`aiida.tools.data.orbital.orbital.Orbital`

   Orbitals for hydrogen, largely follows the conventions used by wannier90
   Object to handle the generation of real hydrogen orbitals and their
   hybrids, has methods for producing s, p, d, f, and sp, sp2, sp3, sp3d,
   sp3d2 hybrids. This method does not deal with the cannonical hydrogen
   orbitals which contain imaginary components.

   The orbitals described here are chiefly concerned with the symmetric
   aspects of the oribitals without the context of space. Therefore
   diffusitivity, position and atomic labels should be handled in the
   OrbitalData class.

   Following the notation of table 3.1, 3.2 of Wannier90 user guide
   (which can be downloaded from http://www.wannier.org/support/)
   A brief description of what is meant by each of these labels:

   :param radial_nodes: the number of radial nodes (or inflections) if no
                        radial nodes are supplied, defaults to 0
   :param angular_momentum: Angular quantum number, using real orbitals
   :param magnetic_number: Magnetic quantum number, using real orbitals
   :param spin: spin, up (1) down (-1) or unspecified (0)

   The conventions regarding L and M correpsond to those used in
   wannier90 for all L greater than 0 the orbital is not hyrbridized
   see table 3.1 and for L less than 0 the orbital is hybridized see
   table 3.2. M then indexes all the possible orbitals from 0 to 2L for
   L > 0 and from 0 to (-L) for L < 0.


   .. py:attribute:: _base_fields_required
      :canonical: aiida.tools.data.orbital.realhydrogen.RealhydrogenOrbital._base_fields_required
      :value: None

   .. py:attribute:: _base_fields_optional
      :canonical: aiida.tools.data.orbital.realhydrogen.RealhydrogenOrbital._base_fields_optional
      :value: None

   .. py:method:: __str__()
      :canonical: aiida.tools.data.orbital.realhydrogen.RealhydrogenOrbital.__str__

   .. py:method:: _validate_keys(input_dict)
      :canonical: aiida.tools.data.orbital.realhydrogen.RealhydrogenOrbital._validate_keys

      Validates the keys otherwise raise ValidationError. Does basic
      validation from the parent followed by validations for the
      quantum numbers. Raises exceptions should the input_dict fail the
      valiation or if it contains any unsupported keywords.

      :param input_dict: the dictionary of keys to be validated
      :return validated_dict: a validated dictionary


   .. py:method:: get_name_from_quantum_numbers(angular_momentum, magnetic_number=None)
      :canonical: aiida.tools.data.orbital.realhydrogen.RealhydrogenOrbital.get_name_from_quantum_numbers
      :classmethod:

      Returns the orbital_name correponding to the angular_momentum alone,
      or to both angular_number with magnetic_number. For example using
      angular_momentum=1 and magnetic_number=1 will return "Px"


   .. py:method:: get_quantum_numbers_from_name(name)
      :canonical: aiida.tools.data.orbital.realhydrogen.RealhydrogenOrbital.get_quantum_numbers_from_name
      :classmethod:

      Returns all the angular and magnetic numbers corresponding to name.
      For example, using "P" as name will return all quantum numbers
      associated with a "P" orbital, while "Px" will return only one set
      of quantum numbers, the ones associated with "Px"


.. py:function:: default_link_styles(link_pair: aiida.orm.utils.links.LinkPair, add_label: bool, add_type: bool) -> dict
   :canonical: aiida.tools.visualization.graph.default_link_styles

   map link_pair to a graphviz edge style

   :param link_type: a LinkPair attribute
   :type link_type: aiida.orm.utils.links.LinkPair
   :param add_label: include link label
   :type add_label: bool
   :param add_type: include link type
   :type add_type: bool
   :rtype: dict


.. py:function:: default_node_styles(node)
   :canonical: aiida.tools.visualization.graph.default_node_styles

   map a node to a graphviz node style

   :param node: the node to map
   :type node: aiida.orm.nodes.node.Node
   :rtype: dict


.. py:function:: default_node_sublabels(node)
   :canonical: aiida.tools.visualization.graph.default_node_sublabels

   function mapping nodes to a sublabel
   (e.g. specifying some attribute values)

   :param node: the node to map
   :type node: aiida.orm.nodes.node.Node
   :rtype: str


.. py:function:: delete_group_nodes(pks: typing.Iterable[int], dry_run: typing.Union[bool, typing.Callable[[typing.Set[int]], bool]] = True, backend=None, **traversal_rules: bool) -> typing.Tuple[typing.Set[int], bool]
   :canonical: aiida.tools.graph.deletions.delete_group_nodes

   Delete nodes contained in a list of groups (not the groups themselves!).

   This command will delete not only the nodes, but also the ones that are
   linked to these and should be also deleted in order to keep a consistent provenance
   according to the rules explained in the concepts section of the documentation.
   In summary:

   1. If a DATA node is deleted, any process nodes linked to it will also be deleted.

   2. If a CALC node is deleted, any incoming WORK node (callers) will be deleted as
   well whereas any incoming DATA node (inputs) will be kept. Outgoing DATA nodes
   (outputs) will be deleted by default but this can be disabled.

   3. If a WORK node is deleted, any incoming WORK node (callers) will be deleted as
   well, but all DATA nodes will be kept. Outgoing WORK or CALC nodes will be kept by
   default, but deletion of either of both kind of connected nodes can be enabled.

   These rules are 'recursive', so if a CALC node is deleted, then its output DATA
   nodes will be deleted as well, and then any CALC node that may have those as
   inputs, and so on.

   :param pks: a list of the groups

   :param dry_run:
       If True, return the pks to delete without deleting anything.
       If False, delete the pks without confirmation
       If callable, a function that return True/False, based on the pks, e.g. ``dry_run=lambda pks: True``

   :param traversal_rules: graph traversal rules. See :const:`aiida.common.links.GraphTraversalRules` what rule names
       are toggleable and what the defaults are.

   :returns: (node pks to delete, whether they were deleted)



.. py:function:: delete_nodes(pks: typing.Iterable[int], dry_run: typing.Union[bool, typing.Callable[[typing.Set[int]], bool]] = True, backend=None, **traversal_rules: bool) -> typing.Tuple[typing.Set[int], bool]
   :canonical: aiida.tools.graph.deletions.delete_nodes

   Delete nodes given a list of "starting" PKs.

   This command will delete not only the specified nodes, but also the ones that are
   linked to these and should be also deleted in order to keep a consistent provenance
   according to the rules explained in the Topics - Provenance section of the documentation.
   In summary:

   1. If a DATA node is deleted, any process nodes linked to it will also be deleted.

   2. If a CALC node is deleted, any incoming WORK node (callers) will be deleted as
   well whereas any incoming DATA node (inputs) will be kept. Outgoing DATA nodes
   (outputs) will be deleted by default but this can be disabled.

   3. If a WORK node is deleted, any incoming WORK node (callers) will be deleted as
   well, but all DATA nodes will be kept. Outgoing WORK or CALC nodes will be kept by
   default, but deletion of either of both kind of connected nodes can be enabled.

   These rules are 'recursive', so if a CALC node is deleted, then its output DATA
   nodes will be deleted as well, and then any CALC node that may have those as
   inputs, and so on.

   :param pks: a list of starting PKs of the nodes to delete
       (the full set will be based on the traversal rules)

   :param dry_run:
       If True, return the pks to delete without deleting anything.
       If False, delete the pks without confirmation
       If callable, a function that return True/False, based on the pks, e.g. ``dry_run=lambda pks: True``

   :param traversal_rules: graph traversal rules.
       See :const:`aiida.common.links.GraphTraversalRules` for what rule names
       are toggleable and what the defaults are.

   :returns: (pks to delete, whether they were deleted)



.. py:function:: get_explicit_kpoints_path(structure, method='seekpath', **kwargs)
   :canonical: aiida.tools.data.array.kpoints.main.get_explicit_kpoints_path

   Returns a dictionary whose contents depend on the method but includes at least the following keys

       * parameters: Dict node
       * explicit_kpoints: KpointsData node with explicit kpoints path

   The contents of the parameters depends on the method but contains at least the keys

       * 'point_coords': a dictionary with 'kpoints-label': [float coordinates]
       * 'path': a list of length-2 tuples, with the labels of the starting
           and ending point of each label section

   The 'seekpath' method which is the default also returns the following additional nodes

       * primitive_structure: StructureData with the primitive cell
       * conv_structure: StructureData with the conventional cell

   Note that the generated kpoints for the seekpath method only apply on the returned primitive_structure
   and not on the input structure that was provided

   :param structure: a StructureData node
   :param method: the method to use for kpoint generation, options are 'seekpath' and 'legacy'.
       It is strongly advised to use the default 'seekpath' as the 'legacy' implementation is known to have
       bugs for certain structure cells
   :param kwargs: optional keyword arguments that depend on the selected method
   :returns: dictionary as described above in the docstring


.. py:function:: get_kpoints_path(structure, method='seekpath', **kwargs)
   :canonical: aiida.tools.data.array.kpoints.main.get_kpoints_path

   Returns a dictionary whose contents depend on the method but includes at least the following keys

       * parameters: Dict node

   The contents of the parameters depends on the method but contains at least the keys

       * 'point_coords': a dictionary with 'kpoints-label': [float coordinates]
       * 'path': a list of length-2 tuples, with the labels of the starting
           and ending point of each label section

   The 'seekpath' method which is the default also returns the following additional nodes

       * primitive_structure: StructureData with the primitive cell
       * conv_structure: StructureData with the conventional cell

   Note that the generated kpoints for the seekpath method only apply on the returned primitive_structure
   and not on the input structure that was provided

   :param structure: a StructureData node
   :param method: the method to use for kpoint generation, options are 'seekpath' and 'legacy'.
       It is strongly advised to use the default 'seekpath' as the 'legacy' implementation is known to have
       bugs for certain structure cells
   :param kwargs: optional keyword arguments that depend on the selected method
   :returns: dictionary as described above in the docstring


.. py:function:: pstate_node_styles(node)
   :canonical: aiida.tools.visualization.graph.pstate_node_styles

   map a process node to a graphviz node style

   :param node: the node to map
   :type node: aiida.orm.nodes.node.Node
   :rtype: dict


.. py:function:: spglib_tuple_to_structure(structure_tuple, kind_info=None, kinds=None)
   :canonical: aiida.tools.data.structure.spglib_tuple_to_structure

   Convert a tuple of the format (cell, scaled_positions, element_numbers) to an AiiDA structure.

   Unless the element_numbers are identical to the Z number of the atoms,
   you should pass both kind_info and kinds, with the same format as returned
   by get_tuple_from_aiida_structure.

   :param structure_tuple: the structure in format (structure_tuple, kind_info)
   :param kind_info: a dictionary mapping the kind_names to
      the numbers used in element_numbers. If not provided, assumes {element_name: element_Z}
   :param kinds: a list of the kinds of the structure.


.. py:function:: structure_to_spglib_tuple(structure)
   :canonical: aiida.tools.data.structure.structure_to_spglib_tuple

   Convert an AiiDA structure to a tuple of the format (cell, scaled_positions, element_numbers).

   :param structure: the AiiDA structure
   :return: (structure_tuple, kind_info, kinds) where structure_tuple
       is a tuple of format (cell, scaled_positions, element_numbers);
       kind_info is a dictionary mapping the kind_names to
       the numbers used in element_numbers. When possible, it uses
       the Z number of the element, otherwise it uses numbers > 1000;
       kinds is a list of the kinds of the structure.

