:py:mod:`aiida.parsers`
=======================

.. py:module:: aiida.parsers

.. autodoc2-docstring:: aiida.parsers
   :allowtitles:

Package Contents
----------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`Parser <aiida.parsers.parser.Parser>`
     - .. autodoc2-docstring:: aiida.parsers.parser.Parser
          :summary:

API
~~~

.. py:class:: Parser(node: aiida.orm.CalcJobNode)
   :canonical: aiida.parsers.parser.Parser

   Bases: :py:obj:`abc.ABC`

   .. autodoc2-docstring:: aiida.parsers.parser.Parser

   .. rubric:: Initialization

   .. autodoc2-docstring:: aiida.parsers.parser.Parser.__init__

   .. py:property:: logger
      :canonical: aiida.parsers.parser.Parser.logger

      .. autodoc2-docstring:: aiida.parsers.parser.Parser.logger

   .. py:property:: node
      :canonical: aiida.parsers.parser.Parser.node
      :type: aiida.orm.CalcJobNode

      .. autodoc2-docstring:: aiida.parsers.parser.Parser.node

   .. py:property:: exit_codes
      :canonical: aiida.parsers.parser.Parser.exit_codes
      :type: aiida.engine.ExitCodesNamespace

      .. autodoc2-docstring:: aiida.parsers.parser.Parser.exit_codes

   .. py:property:: retrieved
      :canonical: aiida.parsers.parser.Parser.retrieved
      :type: aiida.orm.FolderData

      .. autodoc2-docstring:: aiida.parsers.parser.Parser.retrieved

   .. py:property:: outputs
      :canonical: aiida.parsers.parser.Parser.outputs

      .. autodoc2-docstring:: aiida.parsers.parser.Parser.outputs

   .. py:method:: out(link_label: str, node: aiida.orm.Data) -> None
      :canonical: aiida.parsers.parser.Parser.out

      .. autodoc2-docstring:: aiida.parsers.parser.Parser.out

   .. py:method:: get_outputs_for_parsing()
      :canonical: aiida.parsers.parser.Parser.get_outputs_for_parsing

      .. autodoc2-docstring:: aiida.parsers.parser.Parser.get_outputs_for_parsing

   .. py:method:: parse_from_node(node: aiida.orm.CalcJobNode, store_provenance=True, retrieved_temporary_folder=None) -> typing.Tuple[typing.Optional[typing.Dict[str, typing.Any]], aiida.orm.CalcFunctionNode]
      :canonical: aiida.parsers.parser.Parser.parse_from_node
      :classmethod:

      .. autodoc2-docstring:: aiida.parsers.parser.Parser.parse_from_node

   .. py:method:: parse(**kwargs) -> typing.Optional[aiida.engine.ExitCode]
      :canonical: aiida.parsers.parser.Parser.parse
      :abstractmethod:

      .. autodoc2-docstring:: aiida.parsers.parser.Parser.parse
