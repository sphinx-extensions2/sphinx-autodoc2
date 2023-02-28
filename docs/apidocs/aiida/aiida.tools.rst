:py:mod:`aiida.tools`
=====================

.. py:module:: aiida.tools

.. autodoc2-docstring:: aiida.tools
   :allowtitles:

Package Contents
----------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`CalculationTools <aiida.tools.calculations.base.CalculationTools>`
     - .. autodoc2-docstring:: aiida.tools.calculations.base.CalculationTools
          :summary:
   * - :py:obj:`Graph <aiida.tools.visualization.graph.Graph>`
     - .. autodoc2-docstring:: aiida.tools.visualization.graph.Graph
          :summary:
   * - :py:obj:`GroupPath <aiida.tools.groups.paths.GroupPath>`
     - .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath
          :summary:
   * - :py:obj:`Orbital <aiida.tools.data.orbital.orbital.Orbital>`
     - .. autodoc2-docstring:: aiida.tools.data.orbital.orbital.Orbital
          :summary:
   * - :py:obj:`RealhydrogenOrbital <aiida.tools.data.orbital.realhydrogen.RealhydrogenOrbital>`
     - .. autodoc2-docstring:: aiida.tools.data.orbital.realhydrogen.RealhydrogenOrbital
          :summary:

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`default_link_styles <aiida.tools.visualization.graph.default_link_styles>`
     - .. autodoc2-docstring:: aiida.tools.visualization.graph.default_link_styles
          :summary:
   * - :py:obj:`default_node_styles <aiida.tools.visualization.graph.default_node_styles>`
     - .. autodoc2-docstring:: aiida.tools.visualization.graph.default_node_styles
          :summary:
   * - :py:obj:`default_node_sublabels <aiida.tools.visualization.graph.default_node_sublabels>`
     - .. autodoc2-docstring:: aiida.tools.visualization.graph.default_node_sublabels
          :summary:
   * - :py:obj:`delete_group_nodes <aiida.tools.graph.deletions.delete_group_nodes>`
     - .. autodoc2-docstring:: aiida.tools.graph.deletions.delete_group_nodes
          :summary:
   * - :py:obj:`delete_nodes <aiida.tools.graph.deletions.delete_nodes>`
     - .. autodoc2-docstring:: aiida.tools.graph.deletions.delete_nodes
          :summary:
   * - :py:obj:`get_explicit_kpoints_path <aiida.tools.data.array.kpoints.main.get_explicit_kpoints_path>`
     - .. autodoc2-docstring:: aiida.tools.data.array.kpoints.main.get_explicit_kpoints_path
          :summary:
   * - :py:obj:`get_kpoints_path <aiida.tools.data.array.kpoints.main.get_kpoints_path>`
     - .. autodoc2-docstring:: aiida.tools.data.array.kpoints.main.get_kpoints_path
          :summary:
   * - :py:obj:`pstate_node_styles <aiida.tools.visualization.graph.pstate_node_styles>`
     - .. autodoc2-docstring:: aiida.tools.visualization.graph.pstate_node_styles
          :summary:
   * - :py:obj:`spglib_tuple_to_structure <aiida.tools.data.structure.spglib_tuple_to_structure>`
     - .. autodoc2-docstring:: aiida.tools.data.structure.spglib_tuple_to_structure
          :summary:
   * - :py:obj:`structure_to_spglib_tuple <aiida.tools.data.structure.structure_to_spglib_tuple>`
     - .. autodoc2-docstring:: aiida.tools.data.structure.structure_to_spglib_tuple
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`DELETE_LOGGER <aiida.tools.graph.deletions.DELETE_LOGGER>`
     - .. autodoc2-docstring:: aiida.tools.graph.deletions.DELETE_LOGGER
          :summary:

API
~~~

.. py:class:: CalculationTools(node)
   :canonical: aiida.tools.calculations.base.CalculationTools

   .. autodoc2-docstring:: aiida.tools.calculations.base.CalculationTools

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.tools.calculations.base.CalculationTools.__init__

.. py:data:: DELETE_LOGGER
   :canonical: aiida.tools.graph.deletions.DELETE_LOGGER
   :value: None

   .. autodoc2-docstring:: aiida.tools.graph.deletions.DELETE_LOGGER

.. py:class:: Graph(engine=None, graph_attr=None, global_node_style=None, global_edge_style=None, include_sublabels=True, link_style_fn=None, node_style_fn=None, node_sublabel_fn=None, node_id_type='pk', backend: typing.Optional[aiida.orm.implementation.StorageBackend] = None)
   :canonical: aiida.tools.visualization.graph.Graph

   .. autodoc2-docstring:: aiida.tools.visualization.graph.Graph

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.tools.visualization.graph.Graph.__init__

   .. py:property:: backend
      :canonical: aiida.tools.visualization.graph.Graph.backend
      :type: aiida.orm.implementation.StorageBackend

      .. autodoc2-docstring:: aiida.tools.visualization.graph.Graph.backend

   .. py:property:: graphviz
      :canonical: aiida.tools.visualization.graph.Graph.graphviz

      .. autodoc2-docstring:: aiida.tools.visualization.graph.Graph.graphviz

   .. py:property:: nodes
      :canonical: aiida.tools.visualization.graph.Graph.nodes

      .. autodoc2-docstring:: aiida.tools.visualization.graph.Graph.nodes

   .. py:property:: edges
      :canonical: aiida.tools.visualization.graph.Graph.edges

      .. autodoc2-docstring:: aiida.tools.visualization.graph.Graph.edges

   .. py:method:: _load_node(node)
      :canonical: aiida.tools.visualization.graph.Graph._load_node

      .. autodoc2-docstring:: aiida.tools.visualization.graph.Graph._load_node

   .. py:method:: _default_link_types(link_types)
      :canonical: aiida.tools.visualization.graph.Graph._default_link_types
      :staticmethod:

      .. autodoc2-docstring:: aiida.tools.visualization.graph.Graph._default_link_types

   .. py:method:: add_node(node, style_override=None, overwrite=False)
      :canonical: aiida.tools.visualization.graph.Graph.add_node

      .. autodoc2-docstring:: aiida.tools.visualization.graph.Graph.add_node

   .. py:method:: add_edge(in_node, out_node, link_pair=None, style=None, overwrite=False)
      :canonical: aiida.tools.visualization.graph.Graph.add_edge

      .. autodoc2-docstring:: aiida.tools.visualization.graph.Graph.add_edge

   .. py:method:: _convert_link_types(link_types)
      :canonical: aiida.tools.visualization.graph.Graph._convert_link_types
      :staticmethod:

      .. autodoc2-docstring:: aiida.tools.visualization.graph.Graph._convert_link_types

   .. py:method:: add_incoming(node, link_types=(), annotate_links=None, return_pks=True)
      :canonical: aiida.tools.visualization.graph.Graph.add_incoming

      .. autodoc2-docstring:: aiida.tools.visualization.graph.Graph.add_incoming

   .. py:method:: add_outgoing(node, link_types=(), annotate_links=None, return_pks=True)
      :canonical: aiida.tools.visualization.graph.Graph.add_outgoing

      .. autodoc2-docstring:: aiida.tools.visualization.graph.Graph.add_outgoing

   .. py:method:: recurse_descendants(origin, depth=None, link_types=(), annotate_links=False, origin_style=MappingProxyType(_OVERRIDE_STYLES_DICT['origin_node']), include_process_inputs=False, highlight_classes=None)
      :canonical: aiida.tools.visualization.graph.Graph.recurse_descendants

      .. autodoc2-docstring:: aiida.tools.visualization.graph.Graph.recurse_descendants

   .. py:method:: recurse_ancestors(origin, depth=None, link_types=(), annotate_links=False, origin_style=MappingProxyType(_OVERRIDE_STYLES_DICT['origin_node']), include_process_outputs=False, highlight_classes=None)
      :canonical: aiida.tools.visualization.graph.Graph.recurse_ancestors

      .. autodoc2-docstring:: aiida.tools.visualization.graph.Graph.recurse_ancestors

   .. py:method:: add_origin_to_targets(origin, target_cls, target_filters=None, include_target_inputs=False, include_target_outputs=False, origin_style=(), annotate_links=False)
      :canonical: aiida.tools.visualization.graph.Graph.add_origin_to_targets

      .. autodoc2-docstring:: aiida.tools.visualization.graph.Graph.add_origin_to_targets

   .. py:method:: add_origins_to_targets(origin_cls, target_cls, origin_filters=None, target_filters=None, include_target_inputs=False, include_target_outputs=False, origin_style=(), annotate_links=False)
      :canonical: aiida.tools.visualization.graph.Graph.add_origins_to_targets

      .. autodoc2-docstring:: aiida.tools.visualization.graph.Graph.add_origins_to_targets

.. py:exception:: GroupNotFoundError(grouppath)
   :canonical: aiida.tools.groups.paths.GroupNotFoundError

   Bases: :py:obj:`Exception`

   .. autodoc2-docstring:: aiida.tools.groups.paths.GroupNotFoundError

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.tools.groups.paths.GroupNotFoundError.__init__

.. py:exception:: GroupNotUniqueError(grouppath)
   :canonical: aiida.tools.groups.paths.GroupNotUniqueError

   Bases: :py:obj:`Exception`

   .. autodoc2-docstring:: aiida.tools.groups.paths.GroupNotUniqueError

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.tools.groups.paths.GroupNotUniqueError.__init__

.. py:class:: GroupPath(path: str = '', cls: aiida.orm.groups.GroupMeta = orm.Group, warn_invalid_child: bool = True)
   :canonical: aiida.tools.groups.paths.GroupPath

   .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath.__init__

   .. py:method:: _validate_path(path)
      :canonical: aiida.tools.groups.paths.GroupPath._validate_path

      .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath._validate_path

   .. py:method:: __repr__() -> str
      :canonical: aiida.tools.groups.paths.GroupPath.__repr__

      .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath.__repr__

   .. py:method:: __eq__(other: typing.Any) -> bool
      :canonical: aiida.tools.groups.paths.GroupPath.__eq__

      .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath.__eq__

   .. py:method:: __lt__(other: typing.Any) -> bool
      :canonical: aiida.tools.groups.paths.GroupPath.__lt__

      .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath.__lt__

   .. py:property:: path
      :canonical: aiida.tools.groups.paths.GroupPath.path
      :type: str

      .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath.path

   .. py:property:: path_list
      :canonical: aiida.tools.groups.paths.GroupPath.path_list
      :type: typing.List[str]

      .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath.path_list

   .. py:property:: key
      :canonical: aiida.tools.groups.paths.GroupPath.key
      :type: typing.Optional[str]

      .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath.key

   .. py:property:: delimiter
      :canonical: aiida.tools.groups.paths.GroupPath.delimiter
      :type: str

      .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath.delimiter

   .. py:property:: cls
      :canonical: aiida.tools.groups.paths.GroupPath.cls
      :type: aiida.orm.groups.GroupMeta

      .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath.cls

   .. py:property:: parent
      :canonical: aiida.tools.groups.paths.GroupPath.parent
      :type: typing.Optional[aiida.tools.groups.paths.GroupPath]

      .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath.parent

   .. py:method:: __truediv__(path: str) -> aiida.tools.groups.paths.GroupPath
      :canonical: aiida.tools.groups.paths.GroupPath.__truediv__

      .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath.__truediv__

   .. py:method:: __getitem__(path: str) -> aiida.tools.groups.paths.GroupPath
      :canonical: aiida.tools.groups.paths.GroupPath.__getitem__

      .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath.__getitem__

   .. py:method:: get_group() -> typing.Optional[aiida.tools.groups.paths.GroupPath]
      :canonical: aiida.tools.groups.paths.GroupPath.get_group

      .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath.get_group

   .. py:property:: group_ids
      :canonical: aiida.tools.groups.paths.GroupPath.group_ids
      :type: typing.List[int]

      .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath.group_ids

   .. py:property:: is_virtual
      :canonical: aiida.tools.groups.paths.GroupPath.is_virtual
      :type: bool

      .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath.is_virtual

   .. py:method:: get_or_create_group() -> typing.Tuple[aiida.orm.Group, bool]
      :canonical: aiida.tools.groups.paths.GroupPath.get_or_create_group

      .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath.get_or_create_group

   .. py:method:: delete_group()
      :canonical: aiida.tools.groups.paths.GroupPath.delete_group

      .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath.delete_group

   .. py:property:: children
      :canonical: aiida.tools.groups.paths.GroupPath.children
      :type: typing.Iterator[aiida.tools.groups.paths.GroupPath]

      .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath.children

   .. py:method:: __iter__() -> typing.Iterator[aiida.tools.groups.paths.GroupPath]
      :canonical: aiida.tools.groups.paths.GroupPath.__iter__

      .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath.__iter__

   .. py:method:: __len__() -> int
      :canonical: aiida.tools.groups.paths.GroupPath.__len__

      .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath.__len__

   .. py:method:: __contains__(key: str) -> bool
      :canonical: aiida.tools.groups.paths.GroupPath.__contains__

      .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath.__contains__

   .. py:method:: walk(return_virtual: bool = True) -> typing.Iterator[aiida.tools.groups.paths.GroupPath]
      :canonical: aiida.tools.groups.paths.GroupPath.walk

      .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath.walk

   .. py:method:: walk_nodes(filters: typing.Optional[dict] = None, node_class: typing.Optional[aiida.orm.Node] = None, query_batch: typing.Optional[int] = None) -> typing.Iterator[aiida.tools.groups.paths.WalkNodeResult]
      :canonical: aiida.tools.groups.paths.GroupPath.walk_nodes

      .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath.walk_nodes

   .. py:property:: browse
      :canonical: aiida.tools.groups.paths.GroupPath.browse

      .. autodoc2-docstring:: aiida.tools.groups.paths.GroupPath.browse

.. py:exception:: InvalidPath()
   :canonical: aiida.tools.groups.paths.InvalidPath

   Bases: :py:obj:`Exception`

   .. autodoc2-docstring:: aiida.tools.groups.paths.InvalidPath

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.tools.groups.paths.InvalidPath.__init__

.. py:exception:: NoGroupsInPathError(grouppath)
   :canonical: aiida.tools.groups.paths.NoGroupsInPathError

   Bases: :py:obj:`Exception`

   .. autodoc2-docstring:: aiida.tools.groups.paths.NoGroupsInPathError

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.tools.groups.paths.NoGroupsInPathError.__init__

.. py:class:: Orbital(**kwargs)
   :canonical: aiida.tools.data.orbital.orbital.Orbital

   .. autodoc2-docstring:: aiida.tools.data.orbital.orbital.Orbital

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.tools.data.orbital.orbital.Orbital.__init__

   .. py:attribute:: _base_fields_required
      :canonical: aiida.tools.data.orbital.orbital.Orbital._base_fields_required
      :value: (('position',),)

      .. autodoc2-docstring:: aiida.tools.data.orbital.orbital.Orbital._base_fields_required

   .. py:attribute:: _base_fields_optional
      :canonical: aiida.tools.data.orbital.orbital.Orbital._base_fields_optional
      :value: None

      .. autodoc2-docstring:: aiida.tools.data.orbital.orbital.Orbital._base_fields_optional

   .. py:method:: __repr__()
      :canonical: aiida.tools.data.orbital.orbital.Orbital.__repr__

   .. py:method:: __str__() -> str
      :canonical: aiida.tools.data.orbital.orbital.Orbital.__str__

   .. py:method:: _validate_keys(input_dict)
      :canonical: aiida.tools.data.orbital.orbital.Orbital._validate_keys

      .. autodoc2-docstring:: aiida.tools.data.orbital.orbital.Orbital._validate_keys

   .. py:method:: set_orbital_dict(init_dict)
      :canonical: aiida.tools.data.orbital.orbital.Orbital.set_orbital_dict

      .. autodoc2-docstring:: aiida.tools.data.orbital.orbital.Orbital.set_orbital_dict

   .. py:method:: get_orbital_dict()
      :canonical: aiida.tools.data.orbital.orbital.Orbital.get_orbital_dict

      .. autodoc2-docstring:: aiida.tools.data.orbital.orbital.Orbital.get_orbital_dict

.. py:class:: RealhydrogenOrbital
   :canonical: aiida.tools.data.orbital.realhydrogen.RealhydrogenOrbital

   Bases: :py:obj:`aiida.tools.data.orbital.orbital.Orbital`

   .. autodoc2-docstring:: aiida.tools.data.orbital.realhydrogen.RealhydrogenOrbital

   .. py:attribute:: _base_fields_required
      :canonical: aiida.tools.data.orbital.realhydrogen.RealhydrogenOrbital._base_fields_required
      :value: None

      .. autodoc2-docstring:: aiida.tools.data.orbital.realhydrogen.RealhydrogenOrbital._base_fields_required

   .. py:attribute:: _base_fields_optional
      :canonical: aiida.tools.data.orbital.realhydrogen.RealhydrogenOrbital._base_fields_optional
      :value: None

      .. autodoc2-docstring:: aiida.tools.data.orbital.realhydrogen.RealhydrogenOrbital._base_fields_optional

   .. py:method:: __str__()
      :canonical: aiida.tools.data.orbital.realhydrogen.RealhydrogenOrbital.__str__

      .. autodoc2-docstring:: aiida.tools.data.orbital.realhydrogen.RealhydrogenOrbital.__str__

   .. py:method:: _validate_keys(input_dict)
      :canonical: aiida.tools.data.orbital.realhydrogen.RealhydrogenOrbital._validate_keys

      .. autodoc2-docstring:: aiida.tools.data.orbital.realhydrogen.RealhydrogenOrbital._validate_keys

   .. py:method:: get_name_from_quantum_numbers(angular_momentum, magnetic_number=None)
      :canonical: aiida.tools.data.orbital.realhydrogen.RealhydrogenOrbital.get_name_from_quantum_numbers
      :classmethod:

      .. autodoc2-docstring:: aiida.tools.data.orbital.realhydrogen.RealhydrogenOrbital.get_name_from_quantum_numbers

   .. py:method:: get_quantum_numbers_from_name(name)
      :canonical: aiida.tools.data.orbital.realhydrogen.RealhydrogenOrbital.get_quantum_numbers_from_name
      :classmethod:

      .. autodoc2-docstring:: aiida.tools.data.orbital.realhydrogen.RealhydrogenOrbital.get_quantum_numbers_from_name

.. py:function:: default_link_styles(link_pair: aiida.orm.utils.links.LinkPair, add_label: bool, add_type: bool) -> dict
   :canonical: aiida.tools.visualization.graph.default_link_styles

   .. autodoc2-docstring:: aiida.tools.visualization.graph.default_link_styles

.. py:function:: default_node_styles(node)
   :canonical: aiida.tools.visualization.graph.default_node_styles

   .. autodoc2-docstring:: aiida.tools.visualization.graph.default_node_styles

.. py:function:: default_node_sublabels(node)
   :canonical: aiida.tools.visualization.graph.default_node_sublabels

   .. autodoc2-docstring:: aiida.tools.visualization.graph.default_node_sublabels

.. py:function:: delete_group_nodes(pks: typing.Iterable[int], dry_run: typing.Union[bool, typing.Callable[[typing.Set[int]], bool]] = True, backend=None, **traversal_rules: bool) -> typing.Tuple[typing.Set[int], bool]
   :canonical: aiida.tools.graph.deletions.delete_group_nodes

   .. autodoc2-docstring:: aiida.tools.graph.deletions.delete_group_nodes

.. py:function:: delete_nodes(pks: typing.Iterable[int], dry_run: typing.Union[bool, typing.Callable[[typing.Set[int]], bool]] = True, backend=None, **traversal_rules: bool) -> typing.Tuple[typing.Set[int], bool]
   :canonical: aiida.tools.graph.deletions.delete_nodes

   .. autodoc2-docstring:: aiida.tools.graph.deletions.delete_nodes

.. py:function:: get_explicit_kpoints_path(structure, method='seekpath', **kwargs)
   :canonical: aiida.tools.data.array.kpoints.main.get_explicit_kpoints_path

   .. autodoc2-docstring:: aiida.tools.data.array.kpoints.main.get_explicit_kpoints_path

.. py:function:: get_kpoints_path(structure, method='seekpath', **kwargs)
   :canonical: aiida.tools.data.array.kpoints.main.get_kpoints_path

   .. autodoc2-docstring:: aiida.tools.data.array.kpoints.main.get_kpoints_path

.. py:function:: pstate_node_styles(node)
   :canonical: aiida.tools.visualization.graph.pstate_node_styles

   .. autodoc2-docstring:: aiida.tools.visualization.graph.pstate_node_styles

.. py:function:: spglib_tuple_to_structure(structure_tuple, kind_info=None, kinds=None)
   :canonical: aiida.tools.data.structure.spglib_tuple_to_structure

   .. autodoc2-docstring:: aiida.tools.data.structure.spglib_tuple_to_structure

.. py:function:: structure_to_spglib_tuple(structure)
   :canonical: aiida.tools.data.structure.structure_to_spglib_tuple

   .. autodoc2-docstring:: aiida.tools.data.structure.structure_to_spglib_tuple
